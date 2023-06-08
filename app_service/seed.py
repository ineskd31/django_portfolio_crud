from django_seed import Seed
from .models import Service

def run():
    seeder = Seed.seeder()
    
    datas = [
        {
            "titre": "Lorem Ipsum",
            "description": "Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident",
            "icon": "bi bi-briefcase"
        },
        {
            "titre": "Dolor Sitema",
            "description": "Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata",
            "icon": "bi bi-card-checklist"
        },
        {
            "titre": "Sed ut perspiciatis",
            "description": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur",
            "icon": "bi bi-bar-chart"
        },
        {
            "titre": "Magni Dolores",
            "description": "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
            "icon": "bi bi-binoculars"
        },
        {
            "titre": "Nemo Enim",
            "description": "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque",
            "icon": "bi bi-brightness-high"
        },
        {
            "titre": "Eiusmod Tempor",
            "description": "Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi",
            "icon": "bi bi-calendar4-week"
        },
    ]

    for el in datas:
        seeder.add_entity(Service, 1, el)
        
    seeder.execute()
    print('GOOD')