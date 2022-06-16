# GhBot
A simple github bot to retrieve data from github and track user activity:

    - BeautifulSoup
    - Requests
    - FastAPI
    - Flask

### To install:
    
    git clone https://github.com/jassics/learning-python.git
    
    cd projects/GhBot/
    
    pip install -r requirements.txt

### To Run:
Run the Script:

    python main.py -u "your_github_username"

Run the API service:

    uvicorn api:app --reload

Run the Post request: 

    python post.py -u "your_github_username"

Run the Flask App:
    
    python app.py

Open browser and navigate to http://127.0.0.1:5000/