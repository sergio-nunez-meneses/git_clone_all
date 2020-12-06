import requests
import json
import os

def git_clone(github_username):
    path = os.getcwd() + '/github'

    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)

    github_api = 'https://api.github.com/users/' + github_username
    response = requests.get(github_api)

    if response.status_code == 200:
        repositories_url = response.json()['repos_url'] + '?per_page=100'
        response = requests.get(repositories_url)

        if response.status_code == 200:
            github_repositories = response.json()

            for i in range(0, len(github_repositories)):
                clone_url = github_repositories[i]['clone_url']
                command_line = 'git clone ' + clone_url
                os.system(command_line)

                if i == (len(github_repositories) - 1):
                    print('\n' + len(github_repositories) + ' repositories cloned.')
        elif response.status_code == 404:
            print('\nRepositories not found.')
        else:
            print(response.status_code, response.text)
    elif response.status_code == 404:
        print('\nUser not found.')
    else:
        print('\n', response.status_code)

github_username = input('Github username: ')
git_clone(github_username)
