# 🧠 AI-Image-Descriptor
![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![HuggingFace-Space](https://img.shields.io/badge/Live-HuggingFace-yellow)
![Gradio](https://img.shields.io/badge/Built%20with-Gradio-orange)

A simple yet powerful web app that uses the BLIP model to generate intelligent captions for images — either uploaded by the user or scraped from any URL. Built with Gradio, Transformers, and Torch.

🧪 Live Demo

👉 Try it here: https://huggingface.co/spaces/layer-rep/Image_Captions

### 🖼️ Screenshot Preview 
![image](https://github.com/user-attachments/assets/6b1087d5-1b4a-4b90-9d7c-4d5c49bb4f97)



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

The app will be live at:
📍 http://127.0.0.1:7860

💡 How It Works
The app uses BLIP to encode images and generate natural-language captions.

In image mode: Upload an image → get caption.

In URL mode:

Extracts <img> tags using BeautifulSoup

Filters and downloads valid images

Runs captioning on the first 3 usable images

All wrapped in a clean, responsive Gradio interface.

📁 File Structure

AI-Image-Descriptor/
├── gradio_blip2_app.py                 # Main app script
├── requirements.txt                    # All dependencies
├── Screenshot 2025-05-07 231113.png    # UI preview image
├── .gitignore                          # Clean repo: ignores venv, __pycache__, etc.

📢 License
This project is licensed under the MIT License.


✨ Author
Made with ❤️ by srimaansri


