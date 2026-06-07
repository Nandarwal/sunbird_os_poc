# Sunbird Assessment POC

A lightweight assessment platform inspired by the Sunbird architecture. Users can register, log in, select a quiz, attempt assessments, and store results in a PostgreSQL database.

The project demonstrates a simple end-to-end assessment workflow using HTML, JavaScript, Flask, PostgreSQL, Docker, and Git.

---

# Features

- User Registration
- User Login
- Multiple Quiz Support
- Dynamic Quiz Loading from JSON Files
- Flask REST API Backend
- PostgreSQL Database Storage
- Docker-Based Database Deployment
- Easily Extensible Assessment Architecture
- Assessment Result Tracking
- Simple Authentication Flow

---

# Architecture

```text
Browser
    ↓
HTML + JavaScript Frontend
    ↓
Flask API Backend
    ↓
PostgreSQL Database
    ↓
Docker Container
```

---

# Project Structure

```text
sunbird_os_poc/
│
├── quizzes/
│   ├── cloud_ops.json
│   ├── linux_basics.json
│   ├── networking.json
│   ├── database_basics.json
│   └── sunbird_intro.json
│
├── app.py
├── index.html
├── docker-compose.yml
├── kong.yml
├── requirements.txt
└── README.md
```

---

# Software Installation Guide

Before running this project, install the following software.

---

## 1. Install Python

### Windows

#### Option 1 (Recommended)

Install Python from the Microsoft Store.

Search for:

```text
Python 3
```

and install the latest version.

#### Option 2

Download and install from:

```text
https://www.python.org/downloads/
```

Verify installation:

```cmd
python --version
```

or

```cmd
py --version
```

Expected output:

```text
Python 3.x.x
```

---

### macOS

Install using Homebrew:

```bash
brew install python
```

Verify:

```bash
python3 --version
```

Expected output:

```text
Python 3.x.x
```

---

## 2. Install Git

### Windows

Download Git:

```text
https://git-scm.com/downloads
```

or install using Winget:

```cmd
winget install --id Git.Git -e --source winget
```

Verify installation:

```cmd
git --version
```

Expected output:

```text
git version 2.x.x
```

---

### macOS

Install using Homebrew:

```bash
brew install git
```

Verify:

```bash
git --version
```

---

## 3. Install Docker Desktop

Download Docker Desktop:

```text
https://www.docker.com/products/docker-desktop/
```

or install through Microsoft Store.

After installation:

1. Launch Docker Desktop
2. Sign in (optional but recommended)
3. Wait until Docker displays:

```text
Docker Engine Running
```

Verify installation:

```bash
docker --version
docker compose version
```

Example:

```text
Docker version 28.x.x
Docker Compose version 2.x.x
```

---

# Verify Docker Is Running

Before running any Docker commands:

1. Open Docker Desktop.
2. Wait until Docker shows:

```text
Docker Engine Running
```

Verify:

```bash
docker ps
```

If you receive:

```text
failed to connect to the docker API
```

Docker Desktop is not running.

---

# Step 1: Clone the Repository

Clone the repository:

```bash
git clone https://github.com/Nandarwal/sunbird_os_poc.git
```

Move into the project directory:

```bash
cd sunbird_os_poc
```

Verify:

```bash
pwd
```

You should now be inside:

```text
sunbird_os_poc
```

---

# Step 2: Create a Virtual Environment

Create a Python virtual environment:

```bash
python3 -m venv venv
```

### Activate Virtual Environment

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```cmd
venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of your terminal prompt.

---

# Step 3: Install Python Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

### Verify Flask Installation

```bash
pip show flask
```

### Verify psycopg2 Installation

```bash
pip show psycopg2-binary
```

---

# Step 4: Start PostgreSQL Using Docker

Start the database container:

```bash
docker compose up -d
```

Verify containers:

```bash
docker ps
```

Expected container:

```text
sb-quiz-db
```

---

# Step 5: Create Database Tables

Connect to PostgreSQL:

```bash
docker exec -it sb-quiz-db psql -U quiz_admin -d intern_assessment
```

Create the quiz results table:

```sql
CREATE TABLE IF NOT EXISTS quiz_results (
    id SERIAL PRIMARY KEY,
    phone_number VARCHAR(20),
    quiz_id VARCHAR(100),
    quiz_name VARCHAR(200),
    score INTEGER,
    total_questions INTEGER,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Verify table creation:

```sql
\dt
```

View schema:

```sql
\d quiz_results
```

Exit PostgreSQL:

```sql
\q
```

---

# Step 6: Start the Flask Backend

Run:

```bash
python app.py
```

Expected output:

```text
* Running on http://127.0.0.1:5000
```

Keep this terminal running.

---

# Step 7: Start the Frontend

Open a second terminal.

Move to the project folder:

```bash
cd sunbird_os_poc
```

Start a local web server:

```bash
python -m http.server 8000
```

Expected output:

```text
Serving HTTP on 0.0.0.0 port 8000
```

---

# Step 8: Open the Application

Open your browser and visit:

```text
http://localhost:8000/index.html
```

---

# Step 9: Use the Application

1. Register a new account
2. Login
3. Select a quiz
4. Click Start Quiz
5. Answer all questions
6. Click Submit Quiz
7. View your score
8. Verify results are saved in PostgreSQL

---

# Step 10: Verify Results in PostgreSQL

Open a new terminal:

```bash
docker exec -it sb-quiz-db psql -U quiz_admin -d intern_assessment
```

View all quiz attempts:

```sql
SELECT * FROM quiz_results;
```

Count records:

```sql
SELECT COUNT(*) FROM quiz_results;
```

View schema:

```sql
\d quiz_results
```

List all tables:

```sql
\dt
```

---

# Quick Start

If all software is already installed:

### Terminal 1

```bash
docker compose up -d

python app.py
```

### Terminal 2

```bash
python -m http.server 8000
```

### Browser

```text
http://localhost:8000/index.html
```

---

# Common Errors and Solutions

## Error: Docker Daemon Not Running

Error:

```text
failed to connect to the docker API
```

Solution:

1. Open Docker Desktop
2. Wait for Docker Engine to start
3. Run:

```bash
docker compose up -d
```

again.

---

## Error: Port 5000 Already In Use

Error:

```text
Address already in use
Port 5000 is in use
```

### macOS

Find process:

```bash
lsof -i :5000
```

Stop process:

```bash
kill -9 PID
```

Replace PID with the actual process ID.

---

## Error: Quiz Not Loading

Verify that the `quizzes/` folder contains:

```text
cloud_ops.json
linux_basics.json
networking.json
database_basics.json
sunbird_intro.json
```

---

## Error: Database Connection Failed

Verify Docker container is running:

```bash
docker ps
```

Verify PostgreSQL credentials in `app.py` match those configured in Docker:

- host
- database
- user
- password

---

# Screenshots

## Login Page

(Add Screenshot)

---

## Quiz Selection

(Add Screenshot)

---

## Quiz Attempt

(Add Screenshot)

---

## Database Results

(Add Screenshot)

---

# Tech Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Flask
- Flask-CORS

### Database

- PostgreSQL

### Infrastructure

- Docker
- Docker Compose

### Optional Components

- Redis
- Kong API Gateway

---

# Future Enhancements

- Password Hashing
- Authentication Tokens
- Assessment Analytics Dashboard
- User Attempt History
- Leaderboards
- Admin Dashboard
- Sunbird Integration
- Kong API Gateway Integration

---

# Contributing

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# License

This project is intended for learning, experimentation, and proof-of-concept purposes.