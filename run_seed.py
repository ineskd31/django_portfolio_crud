import django
django.setup()

from app_about.seed import run
from app_skills.seed import run
from app_service.seed import run
from app_testimonials.seed import run
from app_portfolio.seed import run


if __name__ == '__main__':
    run()

