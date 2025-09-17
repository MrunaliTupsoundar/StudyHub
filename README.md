StudyHub: Your Personal Study Companion
Overview
This guide will walk you through setting up and running the StudyHub application.

Prerequisites
You need the following installed:

Python

pip (Python package installer)

Setup and Installation
1. Clone the Repository
To get started, clone the project from its GitHub repository.

git clone [https://github.com/MrunaliTupsoundar/StudyHub.git](https://github.com/MrunaliTupsoundar/StudyHub.git)
cd StudyHub

2. Create the .env file
Navigate to your backend folder and create a new file named .env.

FLASK_SECRET=RANDOM_STRING

3. Create and Activate a Virtual Environment
Create a virtual environment to manage dependencies.

Create the virtual environment:

Windows: python -m venv venv

macOS / Linux: python3 -m venv venv

Activate the virtual environment:

Windows: .\venv\Scripts\activate

macOS / Linux: source venv/bin/activate

4. Install Dependencies
Install all required packages.

pip install -r requirements.txt

Running the Application
1. Run the Main Application File
Start the application by executing app.py.

python app.py

2. Access the Web Interface
Once the server is running, go to the following URL:

http://127.0.0.1:5000/studyhub_og/register.html

