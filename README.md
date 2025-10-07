# StudyHub

StudyHub is a simple web-based study companion to help students stay organized and focused.  

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MrunaliTupsoundar/StudyHub.git
cd StudyHub
```

### 2. Create the `.env` File
Inside the `backend` folder, create a file named `.env` and add:
```env
FLASK_SECRET=RANDOM_STRING
```

### 3. Create and Activate a Virtual Environment
**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### 5. Start the Server
```bash
python app.py
```

### 6. Access the Web Interface
Once the server is running, open your browser and go to:
```
http://127.0.0.1:5000/studyhub_og/register.html
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first  
to discuss what you would like to change.  

Please make sure to update tests as appropriate.

