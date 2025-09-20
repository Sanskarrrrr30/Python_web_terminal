# Python-Based Web Terminal

This project is a Python-based web terminal developed for the CodeMate Hackathon as a submission for **Problem Statement 1: Python-Based Command Terminal**. The application mimics the behavior of a real system terminal, allowing users to execute standard commands and interact with the file system through a web interface.

The project was developed with the mandatory use of the **CodeMate Build** and **CodeMate Extension** AI tools.

### Features

The terminal includes the following core functionalities:

* **File and Directory Operations**: Supports standard commands such as `ls`, `cd`, `pwd`, `mkdir`, and `rm`.
* **System Monitoring**: Provides commands to check system resources like CPU usage (`cpu`), memory usage (`mem`), and a list of running processes (`ps`).
* **Web-Based Interface**: The terminal is accessible via a responsive web interface built using the Flask framework.
* **AI-Driven Commands**: Includes a basic natural language parser that translates common English phrases into terminal commands, such as "list files" to `ls` or "create folder" to `mkdir`.

### Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Sanskarrrrr30/Python_web_terminal.git](https://github.com/Sanskarrrrr30/Python_web_terminal.git)
    cd Python_web_terminal
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    The project requires the following dependencies:
    * `Flask`
    * `psutil`

    You can install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Access the terminal:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

3.  **Enter commands:**
    You can use the terminal in two ways:
    * **Standard Commands**: Type commands like `ls`, `pwd`, `cd <directory_name>`, `cpu`, or `mem`.
    * **Natural Language Queries**: Type plain English phrases like "list files" or "make folder my_new_folder" to execute commands.
