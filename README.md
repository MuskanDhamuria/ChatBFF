# ChatBFF - Gemini Powered Chatbot

A modern chatbot application powered by Google's Gemini AI API. Built with Python/Flask backend and HTML/CSS/JS frontend.

## Features

- 💬 Real-time chat interface
- 🧠 Powered by Google Gemini API
- 📱 Responsive design
- 💾 Conversation history per session
- 🚀 Fast and lightweight
- 🐍 Python Flask backend

## Project Structure

```
ChatBFF/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
└── frontend/
    └── index.html
```

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

Edit `.env` and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
PORT=5000
FLASK_ENV=development
```

Start the backend server:

```bash
python app.py
```

The server will run on `http://localhost:5000`

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

## API Endpoints

### Chat Endpoint

**POST** `/api/chat`

Request:
```json
{
  "message": "Your message here",
  "sessionId": "optional_session_id"
}
```

Response:
```json
{
  "success": true,
  "response": "AI response here",
  "sessionId": "session_id"
}
```

### Clear Session

**POST** `/api/clear-session`

Request:
```json
{
  "sessionId": "session_id"
}
```

Response:
```json
{
  "success": true,
  "message": "Session cleared"
}
```

### Health Check

**GET** `/api/health`

Response:
```json
{
  "status": "API is running"
}
```

## Technologies Used

- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: Google Gemini API
- **Other**: python-dotenv

## Troubleshooting

### "GEMINI_API_KEY not found" error
- Make sure your `.env` file exists in the backend directory
- Verify it has the correct `GEMINI_API_KEY` value
- Restart the Flask server after updating `.env`

### CORS errors
- The backend has CORS enabled for development
- Make sure the backend is running on port 5000
- Check that the `API_URL` in `index.html` matches your backend URL

### Virtual environment issues
- Make sure to activate the virtual environment before running the server
- Use `which python` or `where python` to verify which Python is being used

### No response from chatbot
- Check your internet connection
- Verify your API key validity on Google AI Studio
- Check the browser console (F12) and terminal for error messages

## Future Enhancements

- [ ] Add user authentication
- [ ] Store conversation history in database (SQLite/PostgreSQL)
- [ ] Support for multiple AI models
- [ ] Image/file upload support
- [ ] Mobile app version
- [ ] Dark mode toggle
- [ ] Multiple language support
- [ ] Conversation export (PDF/JSON)

## License

MIT

## Support

For issues or questions, please open an issue in the repository.

---

**Made with ❤️ using Gemini API and Flask**