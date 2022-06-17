# GhBot
![CLI](assets/cli.png)

A simple github bot to retrieve data from github and track user activity:

## Tools Used:
- BeautifulSoup
- Requests
- FastAPI
- Flask

## Installation

Clone the project:

    git clone https://github.com/jassics/learning-python.git

Navigate to the `GhBot`:

    cd projects/GhBot/

Install using conda:

    conda create -n ghbot python=3.9

    conda activate ghbot

    pip install -r requirements.txt

## Run the application:
Run the Script:

    python main.py -u "your_github_username"

Run the API service:

    uvicorn api:app --reload

Run the Post request: 

    python post.py -u "your_github_username"

![FastAPI](assets/fast_api.png)

Run the Flask App:
    
    python app.py

Open browser and navigate to http://127.0.0.1:5000/

![Flask](assets/flask.png)
