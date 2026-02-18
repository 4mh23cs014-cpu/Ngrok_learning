
https://ngrok-learning-1.onrender.com# ngrok_learnings

A FastAPI application with User CRUD operations, connected to a Vercel Postgres database.

## Project Structure

```
ngrok_learnings/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app & routes
│   ├── database.py      # SQLAlchemy DB connection
│   ├── models.py        # User model
│   ├── schemas.py       # Pydantic schemas
│   └── crud.py          # CRUD operations
│
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── README.md
```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure `.env`** — update `DATABASE_URL` with your Vercel Postgres connection string.

3. **Run the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Open API docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

| Method | Endpoint            | Description          |
|--------|---------------------|----------------------|
| GET    | `/`                 | Hello World          |
| POST   | `/users`            | Create a new user    |
| GET    | `/users`            | Get all users        |
| GET    | `/users/{user_id}`  | Get user by ID       |
