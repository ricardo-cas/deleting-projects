from github import Github
import sys
import os

# machine variables

token = os.environ.get('gt') 

#  Github login stuff
g = Github(token)
user = g.get_user()
login = user.login

def show_user():
    print(login)

if __name__ == "__main__":
    show_user()