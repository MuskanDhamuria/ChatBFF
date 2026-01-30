# ChatBFF - Gemini Powered Chatbot

A modern chatbot application powered by Google's Gemini AI API. Built with Python/Flask backend and HTML/CSS/JS frontend.

## Features

- 💬 Real-time chat interface
- 🧠 Powered by Google Gemini API
- 📱 Responsive design
- 💾 Conversation history per session
- 🚀 Fast and lightweight
- 🐍 Python Flask backend

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Google Gemini API Key (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Setup Instructions

### 1. Get Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your Gemini API key

Start the backend server:

```bash
python app.py
```

### 3. Frontend Setup

Open the frontend in your browser. You can use any local server:

**Option 1: Python SimpleHTTPServer**
```bash
cd frontend
python -m http.server 8000
```

**Option 2: Node.js http-server**
```bash
npm install -g http-server
cd frontend
http-server
```

Then visit `http://localhost:8000` (or the port shown) in your browser.

## Usage

1. Type a message in the chat box
2. Press Enter or click Send
3. The chatbot will respond using Gemini AI
4. Click Clear to start a new conversation

## Technologies Used

- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: Google Gemini API
- **Other**: python-dotenv

## Future Enhancements

- [ ] Add user authentication
- [ ] Store conversation history in database (SQLite/PostgreSQL)
- [ ] Support for multiple AI models
- [ ] Image/file upload support
- [ ] Mobile app version
- [ ] Dark mode toggle
- [ ] Multiple language support
- [ ] Conversation export (PDF/JSON)


## Support

For issues or questions, please email me. 
