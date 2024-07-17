
# FastAPI Chat Completion API

This is a FastAPI project that provides a simple chat completion API using OpenAI's GPT-4o model. The API supports CORS and has endpoints for basic interactions and chat completion.

## Setup

### Prerequisites

- Python 3.7+
- FastAPI
- OpenAI API key
- Dotenv

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/NoahFD/ComputerModel3DFastAPI.git
   cd ComputerModel3DFastAPI
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install fastapi uvicorn python-dotenv openai
   ```

4. **Create a `.env` file:**

   Create a file named `.env` in the root directory of your project and add your OpenAI API key in the following format:

   ```env
   OPENAI_API_KEY="sk-xxxx"
   ```

### Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### GET /

Returns a simple greeting message.

- **URL:** `/`
- **Method:** `GET`
- **Response:**

  ```json
  {
    "message": "Hello World"
  }
  ```

### POST /

Generates a chat completion based on the provided message prompt.

- **URL:** `/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "prompt": "Your prompt here"
  }
  ```

- **Response:**

  ```json
  {
    "role": "assistant",
    "content": "The generated response from GPT-4 model"
  }
  ```

### GET /hello/{name}

Returns a personalized greeting message.

- **URL:** `/hello/{name}`
- **Method:** `GET`
- **Path Parameter:**
  - `name` (string): The name to greet.

- **Response:**

  ```json
  {
    "message": "Hello {name}"
  }
  ```

## Middleware

The application uses CORS middleware to allow all origins, methods, headers, and credentials.

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Notes

- Make sure to keep your `.env` file secure and do not expose your API key in a public repository.

## License

This project is licensed under the MIT License.
