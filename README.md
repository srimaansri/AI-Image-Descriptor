# 🧠 AI-Image-Descriptor

A simple yet powerful web app that uses the BLIP model to generate intelligent captions for images — either uploaded by the user or scraped from any URL. Built with Gradio, Transformers, and Torch.

🧪 Live Demo

👉 Try it here: https://huggingface.co/spaces/layer-rep/Image_Captions

![image](https://github.com/user-attachments/assets/f50c8707-65fd-4be0-9621-873415061356)


> ✅ Works locally with Python 3.12  
> ✅ Compatible with CPU and GPU  
> ✅ Lightweight and fast — uses `Salesforce/blip-image-captioning-base`  
> ✅ Built-in UI using Gradio  

---

## 🚀 Features

- **Upload images** or paste a **webpage URL**
- Generates **descriptive captions** using BLIP
- Captions the **first 3 usable images** on any webpage
- Fast setup with a **single Python file**
- One-click **copy-to-clipboard**
- Clean, responsive **Gradio UI**
- Fully documented, beginner-friendly code

---

## 🖼️ Demo Preview

> 📸 *(Optional: You can add a screenshot here using `![Alt Text](url)`)*  
*Drag and drop images, or caption directly from a URL.*

---

## 🧠 Model Used

- [`Salesforce/blip-image-captioning-base`](https://huggingface.co/Salesforce/blip-image-captioning-base)  
  A lightweight BLIP model optimized for fast, local captioning without tokenizer issues.

---

## 📦 Requirements

All dependencies are listed in `requirements.txt`. Install with:

```bash
pip install -r requirements.txt


🛠️ Setup Instructions
✅ Python 3.12 compatible

1. Clone the repo
git clone https://github.com/srimaansri/AI-Image-Descriptor.git
cd AI-Image-Descriptor

2. (Optional) Create a virtual environment

python -m venv venv
venv\Scripts\activate  # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the app
python gradio_blip2_app.py
