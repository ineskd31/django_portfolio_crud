import django
django.setup()

from app_about.seed import run
from app_skills.seed import run


if __name__ == '__main__':
    run()

