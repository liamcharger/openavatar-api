# Openavatar API

The **Openavatar API** is an experimental backend for the [Openavatar iOS app](https://github.com/liamcharger/openavatar-ios). It provides user management features powered by PostgreSQL, with more endpoints and features in development.

## Documentation

You can read the complete documentation [here](https://openavatar.apidocumentation.com).

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- [FastAPI](https://fastapi.tiangolo.com/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/liamcharger/openavatar-api.git
   cd openavatar-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables in a `.env` file:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/openavatar
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

The server will start at `http://127.0.0.1:8000`.

## Endpoints

### Root (`/`)
- **GET**: Returns a basic status check.
  ```json
  {
    "status": "ok"
  }
  ```

### Users (`/users`)
- **GET**: Retrieve a list of all users.
- **POST**: Create a new user at `/users/create`.
- **GET**: Retrieve a specific user by ID at `/users/{userId}`.
- **DELETE**: Delete a user by ID at `/users/{userId}`.
