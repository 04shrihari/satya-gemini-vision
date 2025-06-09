# 🧠 Satya Gemini Vision

Satya Gemini Vision is an AI-powered web application that allows users to ask **natural language questions about images**—such as invoices, bills, documents, or photos—and receive intelligent answers powered by **Google Gemini 1.5 Vision**.

This project is ideal for developers exploring multimodal AI, document automation, or custom AI-powered interfaces.

---

## 📌 Project Features

- 📷 Upload any image (document, invoice, ID, etc.)
- ❓ Ask natural language questions about image contents
- 🤖 Gemini AI interprets the image and answers intelligently
- 🎨 User-friendly pastel UI with dark bold fonts
- ⚙️ Built using Python, Streamlit, and Gemini Generative AI

---

## 🔧 Requirements

### 🖥 System Requirements

- Python 3.9+
- Git
- Streamlit-compatible browser (Chrome, Firefox, etc.)
- IDE (VS Code recommended)

### 📦 Python Dependencies

Install all at once using:

```bash
pip install -r requirements.txt
````

Or manually install:

```
streamlit==1.35.0
google-generativeai==0.5.2
python-dotenv==1.0.1
Pillow==10.3.0
```

---

## 🔐 Setting Up Google Generative AI API

Step-by-step:

1. Visit [https://ai.google.dev](https://ai.google.dev)
2. Sign in with your Google account
3. Navigate to **Get API Key**
4. Copy the key
5. Create a `.env` file in the root of your project with the following content:

```env
GOOGLE_API_KEY=your_api_key_here
```

✅ Done! Now your app can access the Gemini model securely.

---

## 🧰 Project Folder Structure

```
satya-gemini-vision/
│
├── app.py               # Main Streamlit app
├── app.ipynb            # Notebook version for exploration
├── vision.ipynb         # Gemini Vision notebook
├── .env                 # Your secret API key (not shared)
├── requirements.txt     # Python dependencies
├── README.md            # This documentation
└── venv/                # Your virtual environment (ignored by Git)
```

---

## 🚀 How to Run This Project

### 1. Clone the Repo

```bash
git clone https://github.com/04shrihari/satya-gemini-vision.git
cd satya-gemini-vision
```

### 2. Create & Activate a Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install All Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your API Key

Create a `.env` file and add:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Start the App

```bash
streamlit run app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## ✨ How to Use the App

1. Click on **"Browse files"** to upload an image
2. Type your question (e.g. “What is the invoice number?”)
3. Click **"Tell me about the image"**
4. The app displays the AI-generated answer instantly

---

## 🧠 Examples of Questions

* "Who is the sender of this invoice?"
* "List all items in the bill"
* "What is the due amount and date?"
* "Is there any tax mentioned?"

---

## 📘 Beginner Tips: How to Build Similar Projects

* Learn Python fundamentals: functions, file I/O, virtual environments
* Use `streamlit` for easy web app interfaces
* Store sensitive data in `.env` files
* Use `google-generativeai` to access Gemini models
* Try projects like:

  * AI-powered document search
  * Chat with PDF/Image/Video
  * Vision-based form extraction

---

## ✅ Version Control With Git

This project uses Git. Follow these commands:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/04shrihari/satya-gemini-vision.git
git push -u origin main
```

---

## 🧑‍💻 Author

**Made by:** [@04shrihari](https://github.com/04shrihari)
📧 **Email:** [shriharik04@gmail.com](mailto:shriharik04@gmail.com)

---

## 💡 License & Usage

* This project is shared for educational and learning purposes.
* Do not expose your API key in public repositories.
* Commercial use is not permitted without permission.

---

## ⭐ Star This Repo

If you found this project helpful, **please give it a ⭐ on GitHub** to support future improvements.

---

## 🙏 Acknowledgements

* Special thanks to [Google AI](https://ai.google.dev) for the Gemini API
* Inspired by real-world image automation challenges
* Built with ❤️ using open-source tools and frameworks

---