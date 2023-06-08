from django_seed import Seed
from .models import Skills

def run():
    seeder = Seed.seeder()
    
    skills = [
        {"name":"HTML", "percent":100},
        {"name":"CSS", "percent":80},
        {"name":"JavaScript", "percent":70},
        {"name":"PHP", "percent":60},
        {"name":"WordPress", "percent":90},
        {"name":"PhotoShop", "percent":50},
    ]
    for element in skills:
        seeder.add_entity(Skills, 1, element)

    seeder.execute()
    print('DONE')
