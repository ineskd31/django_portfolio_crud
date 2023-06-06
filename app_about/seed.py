from django_seed import Seed
from .models import About



def run():
    seeder = Seed.seeder()
    
    seeder.add_entity(About, 1, {
        "intro": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Recusandae ab dicta tempora quaerat",
        "birthday": "1 May 1995",
        "website": "www.example.com",
        "phone": "+123 456 7890",
        "city": "New York, USA",
        "age": 30,
        "degree": "Master",
        "email": "email@example.com",
        "freelance": "Available",
        "description": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Expedita, similique odio iusto in reiciendis voluptatem vero quis soluta nemo blanditiis nihil, earum mollitia porro voluptates! Quo dolorem repudiandae consectetur voluptate.",
    })
    seeder.execute()
    print("gogooooo")
    