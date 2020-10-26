import sys
import os
from github import Github


# foldername = str(sys.argv[1])
path = os.environ.get('mp')         # add projects dirctory to the env vars
token = os.environ.get('gt')        # add github token to the env vars
# _dir = path + '/' + foldername

g = Github(token)
user = g.get_user()
login = user.login
# repo = user.create_repo(foldername)
repo = user.permissions.admin()


delete_repos = ['https://github.com/ricardo-cas/bola31245','https://github.com/ricardo-cas/bubu',
'https://github.com/ricardo-cas/bubu3',
'https://github.com/ricardo-cas/bubu5',
'https://github.com/ricardo-cas/dog',
'https://github.com/ricardo-cas/doguinho',
'https://github.com/ricardo-cas/lulu',
'https://github.com/ricardo-cas/lulu1',
'https://github.com/ricardo-cas/mel',
'https://github.com/ricardo-cas/melzinha1',
'https://github.com/ricardo-cas/melzinha2',
'https://github.com/ricardo-cas/melzinha3',
'https://github.com/ricardo-cas/melzinha5',
'https://github.com/ricardo-cas/toto123']

def list_projects():
    for x in delete_repos:
        print(x)

commands = ['git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

def deleting_itens():
    for item in delete_repos:
        for c in commands:
            os.system(c)



if __name__ == "__main__":
    list_projects()