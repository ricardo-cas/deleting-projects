from github import Github
import sys
import os

# machine variables

token = os.environ.get('gt') 

#  Github login stuff
g = Github(token)
user = g.get_user()
login = user.login


# Methods

def main():
    show_user()

# show user logged
def show_user():
    print(f'\n--------------------Login: {login} --------------------')

# Main Python command method
if __name__ == "__main__":
    main()