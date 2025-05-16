# FastAPI Project

This is a FastAPI and Celery project skeleton designed to provide a structured approach to building web applications using FastAPI needing Queue functionality.

## Project Structure

```
fastapi_celery
├── src
│   ├── api
│   │   ├── main.py          # Entry point of the FastAPI application
│   │   ├── routes           # Directory for route definitions
│   │   │   └── __init__.py
│   │   └── services         # Directory for service layer logic
│   │       └── __init__.py
│   ├── models               # Directory for data models
│   │   └── __init__.py
│   ├── schemas              # Directory for Pydantic schemas
│   │   └── __init__.py
│   └── utils                # Directory for utility functions
│       └── __init__.py
├── tests                    # Directory for tests
│   ├── __init__.py
│   └── test_main.py         # Tests for the main application logic
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application, execute the following command:

```
uvicorn src.api.main:app --reload
```

Visit `http://127.0.0.1:8000` in your browser to access the application. The interactive API documentation can be found at `http://127.0.0.1:8000/docs`.

