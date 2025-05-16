# 📝 Text-summarization-through-huggingface-model

This is a simple Streamlit app that uses Hugging Face's `transformers` library to summarize long pieces of text using a pre-trained model.

---

## 🚀 Features

- Summarizes long text using state-of-the-art NLP models
- Easy-to-use web UI built with Streamlit
- Powered by Hugging Face's `pipeline("summarization")`

---

## 📂 Project Structure

```
text-summarization-through-huggingface-model/
├── main_summarizer.py         # Main Streamlit app
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── venv/                      # Virtual environment (not committed to Git)
```

---

## 🧰 Requirements

- Python 3.8–3.12
- Internet connection (for model download)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/text-summarization-through-huggingface-model.git
cd text-summarization-through-huggingface-model
```

### 2. Create and activate a virtual environment

#### On Windows:

```bash
python -m venv venv

# If using Command Prompt
venv\Scripts\activate.bat

# If using PowerShell (run as Admin if needed)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, create one with the following:

```txt
streamlit
transformers
torch
```

### 4. Run the app

```bash
streamlit run main_summarizer.py
```

---

## 🖥️ Example Usage

1. Enter your long-form text into the input box.
2. Click "Generate Summary".
3. View the summarized text below.

---

## ⚠️ Troubleshooting

- **Transformers import error / torchvision circular import**: Make sure your script isn't named `transformers.py`, `torch.py`, or similar. Clean your project by deleting `__pycache__` folders.
- **Virtual environment not activating in PowerShell**: Use `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.

---

## 📜 License

MIT License. Feel free to use and modify this for educational or personal projects.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## ✨ Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io/)
