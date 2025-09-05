from config.settings import PROJECT_APPS
from os import system

if __name__ == '__main__':
    
    for app in PROJECT_APPS:
        system(f'python manage.py test {app}')