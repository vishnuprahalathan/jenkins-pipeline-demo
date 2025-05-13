# 🚀 DevOps Task 2 – Jenkins CI/CD Pipeline with Docker

This repository contains a complete CI/CD pipeline setup for a Python Flask application using **Jenkins** and **Docker**, as part of my DevOps internship assignment.

---

## 🎯 Objective

Automate the build, test, and deployment process using Jenkins, Docker, and GitHub. The pipeline triggers automatically on code commits.

---

## 🧰 Tools & Technologies Used

- 🧪 Jenkins (via Docker)
- 🐳 Docker
- 🐍 Python (Flask)
- 🧪 unittest (Python)
- 🗂 GitHub (for code and webhook)

---

## 📁 Project Structure

jenkins-pipeline-demo/
├── app.py # Flask web application
├── Dockerfile # Container instructions
├── Jenkinsfile # CI/CD pipeline script
├── requirements.txt # Python dependencies
├── tests/
│ └── test_app.py # Unit tests
├── README.md # Project documentation
└── screenshots/ # (Optional) Jenkins screenshots

yaml
Copy
Edit

---

## ⚙️ How It Works

1. **Jenkins** pulls code from GitHub.
2. Builds a **Docker** image using the `Dockerfile`.
3. Runs unit tests with `unittest`.
4. If tests pass, deploys the app in a container.
5. Pipeline runs automatically on every GitHub push (webhook enabled).

---
