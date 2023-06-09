from django_seed import Seed
from .models import PortImage, PortFilter


def run():
    seeder = Seed.seeder()
    
    
    image = [
        {"name": "app", "image": "img/portfolio/portfolio-1.jpg"},
        {"name": "web", "image": "img/portfolio/portfolio-2.jpg"},
        {"name": "app", "image": "img/portfolio/portfolio-3.jpg"},
        {"name": "card", "image": "img/portfolio/portfolio-4.jpg"},
        {"name": "web", "image": "img/portfolio/portfolio-5.jpg"},
        {"name": "app", "image": "img/portfolio/portfolio-6.jpg"},
        {"name": "card", "image": "img/portfolio/portfolio-7.jpg"},
        {"name": "card", "image": "img/portfolio/portfolio-8.jpg"},
        {"name": "web", "image": "img/portfolio/portfolio-9.jpg"},
    ]
    
    
    filter = [
        {"name": "app"},
        {"name": "card"},
        {"name": "web"},
    ]
    
    
    for e in image:
        seeder.add_entity(PortImage, 1, e)
        
        
    for el in filter:
        seeder.add_entity(PortFilter, 1, el)
        
        
    seeder.execute()
    print('PORTO DONE')