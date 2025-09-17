StudyHub
Welcome to Your StudyHub! This guide will walk you through setting up and running the application.

Prerequisites:
Python
pip (Python package installer)

Setup and Installation
Clone the Repository
If you haven't already, clone this repository to your local machine.

Bash:

git https://github.com/MrunaliTupsoundar/StudyHub.git
cd [your-project-folder]


Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

Windows:
Bash
python -m venv venv

macOS / Linux:
Bash
python3 -m venv venv

Activate the Virtual Environment

Windows:
Bash
.\venv\Scripts\activate

macOS / Linux:
Bash
source venv/bin/activate


Install Dependencies
Install all the required packages listed in requirements.txt.
Bash:
pip install -r requirements.txt


Running the Application:
Run the Main Application File
Start the application by executing app.py.

Bash
python app.py

Access the Web Interface
Once the server is running, you can access the registration page in your web browser at the following URL:

http://127.0.0.1:5000/studyhub_og/register.html
You should now see the application's registration page. If you encounter any issues, please check that all dependencies were installed correctly and that your virtual environment is active.
