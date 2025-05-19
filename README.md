# doc_mgmt
User and document management using Django

## Setup Instructions for Backend - Django

### 1. Make sure docker desktop is running successfully, Docker Compose build and run command
```bash
docker-compose up --build
```

OR

### 1. Create a virtual environment and activate it
```bash
virtualenv venv
venv\Scripts\activate
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the application
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser


