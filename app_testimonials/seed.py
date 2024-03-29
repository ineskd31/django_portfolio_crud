from django_seed import Seed
from .models import Testi


def run():
    seeder = Seed.seeder()
    
    
    datas = [
        {
            "name": "Saul Goodman",
            "job": "Ceo Founder",
            "citation": "Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.",
            "image": "static/img/testimonials/testimonials-1.jpg"
        },
        {
            "name": "Sara Wilsson",
            "job": "Designer",
            "citation": "Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.",
            "image": "static/img/testimonials/testimonials-2.jpg"
        },
        {
            "name": "Jena Karlis",
            "job": "Store Owner",
            "citation": "Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.",
            "image": "static/img/testimonials/testimonials-3.jpg"
        },
        {
            "name": "Matt Brandon",
            "job": "Freelancer",
            "citation": "Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.",
            "image": "static/img/testimonials/testimonials-4.jpg"
        },
        {
            "name": "John Larson",
            "job": "Entrepreneur",
            "citation": "Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.",
            "image": "static/img/testimonials/testimonials-5.jpg"
        },
    ]
    
    for el in datas:
        seeder.add_entity(Testi, 1, el)
        
    seeder.execute()
    print('TESTI DONE')