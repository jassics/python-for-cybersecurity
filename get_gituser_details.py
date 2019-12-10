import json
import requests
import sys

if len(sys.argv) !=2:
    print("Please pass the username")
    print("Ex: python {} <username>".format(sys.argv[0]))
    exit(0)

username = sys.argv[1]

api_url_base = 'https://api.github.com/' 
headers = {'Content-Type': 'application/json', 'User-Agent': 'Python Student', 'Accept': 'application/vnd.github.v3+json'}

def get_user_details(username):
    user_url = '{}users/{}'.format(api_url_base, username)
    response = requests.get(user_url, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

def get_repos(username):      
    repo_url = '{}users/{}/repos'.format(api_url_base, username)
    response = requests.get(repo_url, headers=headers)
    
    if response.status_code == 200:
        return (response.content)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

# Print User details
user_details = get_user_details(username) # It's a binary string

if user_details is not None:
    # convert it to utf-8 encoded json string
    user_in_json = user_details.decode('utf-8') 
    
    # Load the JSON to a Python list & dump it back out as formatted JSON 
    user_detail_dict = json.loads(user_in_json) 

    print("\n" + "="*10 + " User details of username: " + username + " " + "="*10 )
    print("User Name: {}".format(user_detail_dict['name']))
    print("Bio: {}".format(user_detail_dict['bio']))
    print("Company: {}".format(user_detail_dict['company']))
    print("Email: {}".format(user_detail_dict['email']))
    print("Location: {}".format(user_detail_dict['location']))
    print("Following: {}".format(user_detail_dict['following']))
    print("Followers: {}".format(user_detail_dict['followers']))
    print("Public Repo count: {}".format(user_detail_dict['public_repos']))
    print("Account created at: {}".format(user_detail_dict['created_at']))
    print("="*50)
else:
    print('No User Found')

# Print Repo list details
repo_list = get_repos(username) # It's a binary string

if repo_list is not None:
    repo_in_json = repo_list.decode('utf-8') # convert it to utf-8 encoded json string

    # Load the JSON to a Python list & dump it back out as formatted JSON 
    repo_list = json.loads(repo_in_json) 
    print("\n" + "="*10 + " Repo details of username: " + username + " " + "="*10 )

    for repo_dict in repo_list:
        print("*"*10 + " Repo Name: {}".format(repo_dict['name']) + " " + "*"*10)
        print("Description: {}".format(repo_dict['description']))
        print("Repo url: {}".format(repo_dict['clone_url']))
        print("Is it forked one : {}".format(repo_dict['fork']))
        print("Created at: {}".format(repo_dict['created_at']))
        print("Updated at: {}".format(repo_dict['updated_at']))
        print("Language: {}".format(repo_dict['language']))
        print("Fork Count: {}".format(repo_dict['forks_count']))
        print("*"*50 + "\n")
else:
    print('No Repo List Found')
