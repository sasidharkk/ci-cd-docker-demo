README.md — CI/CD Pipeline with GitHub Actions & Docker

\\\\\\ Project Title ///////

********* CI/CD Pipeline with GitHub Actions & Docker (No Cloud Needed) *************

>> Objective <<

Set up a complete CI/CD pipeline that:

Builds a Docker image

Runs tests automatically

Pushes the image to Docker Hub

Deploys locally using Docker or Minikube

@@@@@@@@@@@@@@@@@   Tools Used   @@@@@@@@@@@@@@@@@@@@@@@@@@

GitHub Actions – CI/CD automation

Docker & Docker Hub – Containerization and image registry

Python Flask – Simple demo web app

Git – Version control

(Optional) Minikube – Local Kubernetes cluster

<<<< Step-by-Step >>>>

STEP 1 — Prerequisites

Before starting, install:

* Git

* Docker Desktop

* (Optional) Minikube

### Create accounts: ###

* GitHub

* Docker Hub

STEP 2 — Create Project Folder

Open PowerShell or Git Bash and run:

mkdir ci-cd-docker-demo
cd ci-cd-docker-demo

STEP 3 — Create a Simple Flask App

app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from CI/CD Pipeline!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


requirements.txt

flask
pytest


test_app.py

from app import app

def test_home():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"Hello from CI/CD Pipeline!" in resp.data


Your folder should look like:

ci-cd-docker-demo/
├─ app.py
├─ requirements.txt
├─ Dockerfile
├─ tests/
│  └─ test_app.py
├─ .github/
│  └─ workflows/
│     └─ ci-cd.yml
├─ docker-compose.yml
└─ README.md

STEP 4 — Test the App Locally

Create a virtual environment and run:

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py


Open your browser at http://localhost:5000

You should see → Hello from CI/CD Pipeline!

Test code:

pytest -q

STEP 5 — Add Docker Support

Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]


Build and run to test locally:

docker build -t ci-cd-demo:local .
docker run --rm -p 5000:5000 ci-cd-demo:local


Then open: http://localhost:5000

STEP 6 — (Optional) Docker Compose File

docker-compose.yml

version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"


Run:

docker-compose up --build

STEP 7 — Push Project to GitHub

Create a new GitHub repository (e.g., ci-cd-docker-demo).

Then push your project:

git init
git add .
git commit -m "Initial commit - Flask CI/CD demo"
git branch -M main
git remote add origin https://github.com/<your-username>/ci-cd-docker-demo.git
git push -u origin main


STEP 8 — Create Docker Hub Repo & Access Token

Go to Docker Hub

Create a new repo named ci-cd-docker-demo.

Go to Account Settings → Security → New Access Token
Name it github-actions-token and copy the token.


STEP 9 — Set Up GitHub Actions Workflow

Create folders:

.github/workflows/ci-cd.yml


Add this content:

name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest -q

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_HUB_USERNAME }}
          password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKER_HUB_USERNAME }}/ci-cd-docker-demo:latest


Commit and push:

git add .github/workflows/ci-cd.yml
git commit -m "Add GitHub Actions workflow"
git push

 
STEP 10 — Add GitHub Secrets

In your GitHub repo:

Go to Settings → Secrets and variables → Actions → New repository secret

Name: DOCKER_HUB_USERNAME → your Docker Hub username

Name: DOCKER_HUB_ACCESS_TOKEN → your Docker Hub token

STEP 11 — Check GitHub Actions

Go to your repo → Actions tab

You should see:
✅ Checkout
✅ Install dependencies
✅ Run tests
✅ Login to Docker Hub
✅ Build & push Docker image

After success, check your Docker Hub → new image will appear:

docker.io/<your-username>/ci-cd-docker-demo:latest

STEP 12 — Deploy Locally

Option A: Run with Docker
docker pull <your-username>/ci-cd-docker-demo:latest
docker run -d -p 5000:5000 <your-username>/ci-cd-docker-demo:latest


Open: http://localhost:5000

Option B: Deploy with Minikube
minikube start
kubectl create deployment ci-cd-demo --image=<your-username>/ci-cd-docker-demo:latest
kubectl expose deployment ci-cd-demo --type=NodePort --port=5000
minikube service ci-cd-demo

STEP 13 — Screenshots for Submission

Take screenshots of:

<img width="1918" height="1031" alt="Screenshot 2025-11-04 164201" src="https://github.com/user-attachments/assets/f32023ae-774c-4b89-8570-4dab1adb9781" />
<img width="1919" height="1026" alt="Screenshot 2025-11-04 164222" src="https://github.com/user-attachments/assets/ced7a1fc-51a1-4326-8cfd-5ebdeac2823c" />
<img width="1919" height="1026" alt="Screenshot 2025-11-04 164302" src="https://github.com/user-attachments/assets/a9269879-b8b6-440a-b23e-2c725fcaf4e5" />
<img width="1919" height="1035" alt="Screenshot 2025-11-04 165337" src="https://github.com/user-attachments/assets/ae49ee36-9cee-4406-86bc-50e6bdd01c17" />
<img width="1914" height="1032" alt="Screenshot 2025-11-04 165429" src="https://github.com/user-attachments/assets/6f70ce50-185b-460e-a049-f9f2d105eab5" />
<img width="1919" height="1041" alt="Screenshot 2025-11-04 165512" src="https://github.com/user-attachments/assets/6cf4d5c6-2855-4996-a837-ced480b9579f" />
<img width="1919" height="1035" alt="Screenshot 2025-11-04 165444" src="https://github.com/user-attachments/assets/f8211021-3c05-4d1d-8530-90d7e602e723" />
<img width="1910" height="1035" alt="Screenshot 2025-11-04 165659" src="https://github.com/user-attachments/assets/4d67acb6-e403-4951-8c0c-f133e93cdc81" />

✅ GitHub Actions successful run

🐋 Docker Hub image page

🌐 App running in browser (http://localhost:5000)

(Optional) Minikube dashboard or service

Deliverables

Item	Description
GitHub Repo	Contains code and .github/workflows/ci-cd.yml
Docker Hub Image	https://hub.docker.com/r/<your-username>/ci-cd-docker-demo
Workflow Screenshot	Show successful build & push
Deployed App Screenshot	Show running app in browser

Troubleshooting 
Issue	Solution
python.exe not found	Reinstall Python and add to PATH
Docker login failed	Check GitHub Secrets values
Port already in use	Run container on another port (-p 5001:5000)
pytest not found	Add pytest to requirements.txt
GitHub Actions stuck	Retry workflow or check syntax in YAML
✅ Example Output

App URL: http://localhost:5000

Message: Hello from CI/CD Pipeline!

Docker Hub Image: https://hub.docker.com/r/yourusername/ci-cd-docker-demo

GitHub Actions: All steps green ✅

Author

Kondapaneni Sasidhar
Project: CI/CD Pipeline with GitHub Actions & Docker (No Cloud Needed)
