import requests as req

base_url="https://github.com/"
username = "deepraj1729"

url = base_url+username

#GET request to github for the username
try:
    res = req.get(url)
    if res.status_code == 404:
        print("Error 404. Page not found")
    elif res.status_code == 200:
        print("Status: OK")

except Exception as e:
    print("Unable to establish connection")
    print(e)