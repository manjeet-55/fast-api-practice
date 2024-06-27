# FastAPI Project Instructions

## Project Setup

### 1. Create the Virtual Environment

Use the **python3 -m venv** command to create a new virtual environment, if not created before.

You can name the virtual environment directory whatever you like; here, we'll use **fastapi-env**

```sh
python3 -m venv fastapi-env
```

### 2. Activate the Virtual Environment

To start working on this project, first navigate to the project directory and activate the virtual environment:

```sh
source fastapi-env/bin/activate
```

### 3. Install Packages

install the required packages to run a fastapi application, install only if you have created a new Virtual environment:

```sh
pip install fastapi uvicorn
```

### 4. Run the FastAPI Application

Start the FastAPI server using Uvicorn:

```sh
uvicorn main:app --reload
```

The application will be available at http://127.0.0.1:8000.

## End the Session

### 1 . Stop the FastAPI Server

If the FastAPI server is running, stop it by pressing Ctrl+C in the terminal where it is running.

### 2. Deactivate the Virtual Environment

Deactivate the virtual environment by running:

```sh
deactivate
```

### 3. Delete the Virtual Environment Directory (optional)

Remove the virtual environment directory using the rm -rf command. Make sure you are in the parent directory of the virtual environment:

```sh
rm -rf fastapi-env
```
