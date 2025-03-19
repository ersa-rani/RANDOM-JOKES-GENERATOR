# Random Joke Generator 🎭😂

This is a simple Streamlit web app that fetches random jokes from a custom FastAPI backend.

## Features 🚀
- Fetches random jokes from your FastAPI backend.
- Simple and interactive UI built with Streamlit.
- Click a button to get a new joke instantly.
- Displays jokes in a clean, formatted manner.

## Tech Stack 🛠️
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Hosting:** Vercel (FastAPI), Streamlit Sharing (or other hosting services)

## Installation & Usage 🏗️
### 1. Clone the Repository
```sh
git clone https://github.com/ersa-rani/random-joke-generator.git
cd random-joke-generator
```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```sh
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```sh
streamlit run app.py
```

## FastAPI Backend 🔗
The backend for fetching jokes is built using FastAPI. You can find it here:
[FastAPI Joke API Repository](https://github.com/your-username/fastapi-joke-api)

### Running the Backend Locally
1. Navigate to the FastAPI repo:
```sh
git clone https://github.com/ersa-rani/fastapi-joke-api.git
cd fastapi-joke-api
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Run the FastAPI server:
```sh
uvicorn main:app --reload
```
4. Test the API at `http://127.0.0.1:8000/random_joke`

## API Endpoint 📡
- `GET /random_joke` - Returns a random joke in JSON format.

## Author 👩‍💻
Developed by [Ersa Rani](https://github.com/ersa-rani)

