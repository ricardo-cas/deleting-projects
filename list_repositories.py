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
    show_repos()
    show_public_repos()

# show user logged
def show_user():
    print(f'\n--------------------Login: {login} --------------------')

def show_repos():
    for repo in user.get_repos():
        print(f'\n {repo}')

def show_public_repos():
    print(f'Total de repositórios publicos: {user.public_repos()}')
 


# Main Python command method
if __name__ == "__main__":
    main()