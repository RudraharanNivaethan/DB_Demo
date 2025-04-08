from django.db import models

# Create your models here.
# Create your models here.
class Guide:
    id: int
    name: str
    designation: str
    image: str

class Package:
    id: int
    location: str
    price: int
    no_of_people: int
    image: str