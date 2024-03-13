# First Version Project

This is the first version of a Flask project.

## Installation

To set up the project environment, follow these steps:

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

3. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the FLASK_APP environment variable:

   ```bash
   export FLASK_APP=app.py
   ```

5. Optionally, set the FLASK_ENV environment variable to 'development' for debug mode:

   ```bash
   export FLASK_ENV=development
   ```

## Running the Application

To run the application, use the following command:

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000/`.

## Configuration

Before running the application, ensure you have set the necessary environment variables as specified in `app/config.py`. For example, you may need to set `SECRET_KEY` and `DATABASE_URL`.