# Debug Assistant
An AI-powered tool that helps you understand and fix Python errors faster. You can upload `.log`, `.txt`, or `.py` files — it reads them, summarizes the problem, and suggests fixes using OpenAI.

## Why use this?
This project was built to simplify debugging during development. Instead of searching errors manually, it gives you a clean summary, links to useful docs, and makes the process smoother. It’s meant to feel like a smart assistant sitting beside you.

## Features
- Accepts `.log`, `.py`, or plain traceback files
- Summarizes the core issue using OpenAI
- Suggests fix ideas and relevant resources
- Minimal web UI with upload form
- CLI-compatible file parsing logic
- Built with FastAPI, so it’s fast and extendable

## Getting Started
### 1. Clone the repo
```bash
git clone https://github.com/asrithcheepurupalli/debug-assistant.git
cd debug-assistant
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Add your OpenAI API key
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_key_here
```
**Note:** Don’t commit this file to GitHub.

### 4. Run the server locally
```bash
uvicorn main:app --reload
```
Visit `http://localhost:8000` in your browser.

## Project Structure
```
debug-assistant/
├── main.py              # FastAPI backend logic
├── utils.py             # Log parsing and cleanup
├── templates/
│   └── index.html       # Jinja2 template for web UI
├── static/              # Static assets (optional)
├── .env                 # Your OpenAI key (not committed)
├── requirements.txt     # Python dependencies
├── example.log          # Sample input for testing
```

## Built With
- Python 3.12
- FastAPI
- Jinja2
- OpenAI SDK
- python-dotenv

## Author
**Asrith Cheepurupalli**  
[Portfolio](https://asrithcheepurupalli.codes)  
[GitHub](https://github.com/asrithcheepurupalli)

## License
MIT License. Built as a personal dev tool and portfolio project.
