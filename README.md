# ExaSeek

**ExaSeek** is a modern, AI-powered semantic search engine for desktop, built with Python and Tkinter. It integrates with the [Exa API](https://exa.ai) to deliver intelligent, real-time search results from across the web, displayed within a sleek, user-friendly interface.

---

## 🚀 Features

- 🔍 **Real-time Semantic Search** using the Exa AI API
- 🖥️ **Modern Desktop GUI** with Tkinter
- 🎨 **Clean, Professional UI** with:
  - Large, easy-to-use search input field
  - Custom-styled buttons with hover effects
  - Scrollable results display area
  - Smooth fade-in transitions and animations
  - Consistent padding, spacing, and typography
- ⚠️ **Robust Error Handling** and real-time user feedback
- 📦 **Modular, Maintainable Codebase**

---

## 📥 Installation

1. **Clone the repository**

```bash
git clone https://github.com/mahmoud-saed/ExaSeek.git
cd ExaSeek
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your Exa API key**

Create a `.env` file in the project root with the following content:

```env
EXA_API_KEY=your_exa_api_key_here
```

---

## ▶️ How to Use

1. **Run the application**

```bash
python main.py
```

2. **Enter your search query** in the input field

3. **Press the search button** or hit `Enter`

4. **Browse the semantic search results**, styled and displayed in the scrollable results section

5. **Monitor status bar** for API status, errors, or messages

---

## 🧩 Dependencies

- `exa_py` – Python client for Exa API
- `tkinter` – Python standard GUI toolkit
- `dotenv` – For loading environment variables
- `requests` – For API communication

You can install all dependencies using:

```bash
pip install -r requirements.txt
```
---

## 🛠 Technical Requirements

- Python 3.8+
- Internet connection (for API requests)
- Exa API Key (required for search functionality)

---

## 🌱 Future Improvements

- 🔐 OAuth support for secured API access
- 🌐 Multiple language support
- 💾 Local caching for offline viewing of results
- 🎚️ User preferences and themes
- 🔍 Enhanced result filtering and tagging
- 📊 Analytics dashboard for user queries
