"""
BLIP Image Captioning  –  Windows + Python 3.12 friendly
--------------------------------------------------------
• Upload an image   OR   drop a webpage URL → get AI captions.
• Model:  Salesforce/blip-image-captioning-base   (no tokenizer crashes)
• Extras: Hero header, copy‑to‑clipboard button, two‑column layout.
"""

import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import requests, torch, os

# -------------------------  Load model  ---------------------------------
MODEL_ID = "Salesforce/blip-image-captioning-base"

processor = BlipProcessor.from_pretrained(MODEL_ID)
model = BlipForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device).eval()

# -------------------------  Core helpers  -------------------------------
def blip_caption(pil_img: Image.Image) -> str:
    """Return a caption for a single PIL image."""
    inputs = processor(images=pil_img.convert("RGB"), return_tensors="pt").to(device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=50)
    return processor.decode(out[0], skip_special_tokens=True)

def caption_from_url(url: str) -> str:
    """Grab first 3 real images from a webpage and caption them."""
    try:
        soup = BeautifulSoup(requests.get(url, timeout=5).text, "html.parser")
    except Exception as e:
        return f"Failed to fetch page: {e}"

    captions, seen = [], set()
    for img in soup.find_all("img"):
        src = img.get("src") or ""
        # resolve relative URLs
        if src.startswith("//"):
            src = "https:" + src
        if not src.startswith(("http://", "https://")):
            continue
        if any(x in src for x in ("svg", "base64", "blank", "1x1")) or src in seen:
            continue
        seen.add(src)
        try:
            raw = Image.open(BytesIO(requests.get(src, timeout=5).content))
            captions.append(f"{src}\n{blip_caption(raw)}")
            if len(captions) == 3:
                break
        except Exception:
            continue
    return "\n\n".join(captions) if captions else "No suitable images found."

# -------------------------  UI / Gradio  --------------------------------
CSS = """
.gr-box {border-radius:14px !important;}
button {font-weight:600;}
"""

with gr.Blocks(css=CSS, theme=gr.themes.Soft()) as demo:
    # Hero banner
    gr.Markdown("""
    <div style='display:flex;align-items:center;gap:10px;font-size:1.5rem'>
        <span style='font-size:2rem'>🖼️</span><b>BLIP Image Captioning</b>
    </div>
    <p style='margin-top:-8px'>
        Upload an image or paste a webpage URL – I’ll describe what I see.
        <a href='https://huggingface.co/Salesforce/blip-image-captioning-base' target='_blank'>Model card ↗</a>
    </p>
    """)

    with gr.Row():
        # ------------  Image column ------------
        with gr.Column(scale=1):
            img_in   = gr.Image(label="Drop an image", type="pil", height=280)
            cap_out  = gr.Textbox(label="Caption", interactive=False)
            with gr.Row():
                btn_cap   = gr.Button("Generate caption")
                copy_btn  = gr.Button("📋 Copy", size="sm", variant="secondary")
            btn_cap.click(lambda i: blip_caption(i) if i else "No image.",
                          img_in, cap_out)
            copy_btn.click(None,        # no Python fn
                           cap_out, []) # no Python outputs
            # copy to clipboard in the browser
            copy_btn.click(js="navigator.clipboard.writeText(args[0]);",  # <-- param is js
                           inputs=cap_out, outputs=None)

        # ------------  URL column --------------
        with gr.Column(scale=1):
            url_in  = gr.Textbox(label="Webpage URL")
            url_out = gr.Textbox(label="Captions (first 3 images)", lines=8, interactive=False)
            btn_url = gr.Button("Scrape & caption")
            btn_url.click(caption_from_url, url_in, url_out)

demo.launch(share=True)
