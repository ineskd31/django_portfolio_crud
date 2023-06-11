from django_seed import Seed
from .models import Contact

def run():
    seeder = Seed.seeder()
    
    
    
    
    seeder.add_entity(Contact, 1, {
        'location': 'A108 Adam Street, New York, NY 535022',
        'email': 'info@example.com',
        'number': '+1 5589 55488 55s'
    })
    seeder.execute()
    print("CONTACT GOOD")