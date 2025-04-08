from django.shortcuts import render
from . models import Guide,Package  # importing Model classes to update the webpages dynamically

# Create your views here.
def home(request):
    guide1 = Guide()
    guide1.id = 1
    guide1.name = 'Ava Muller'
    guide1.designation = 'Translator'
    guide1.image = 'img/team-1.jpg'

    guide2 = Guide()
    guide2.id = 2
    guide2.name = "Marcus Braun"
    guide2.designation = "Travel Expert"
    guide2.image = 'img/team-2.jpg'

    guide3 = Guide()
    guide3.id = 3
    guide3.name = "Alyssa Hades"
    guide3.designation = "Local Cuisine Expert"
    guide3.image = 'img/team-3.jpg'

    guide4 = Guide()
    guide4.id = 4
    guide4.name = "Domnic Torreto"
    guide4.designation = "Hiking Guide"
    guide4.image = 'img/team-4.jpg'

    guides = [guide1,guide2,guide3,guide4]

    package1 = Package()
    package1.id = 1
    package1.location = 'France'
    package1.price = 800
    package1.no_of_people = 2
    package1.image = 'img/package-1.jpg'

    package2 = Package()
    package2.id = 2
    package2.location = 'Maldives'
    package2.price = 100
    package2.no_of_people = 2
    package2.image = 'img/package-2.jpg'

    package3 = Package()
    package3.id = 3
    package3.location = 'Bora Bora'
    package3.price = 800
    package3.no_of_people = 2
    package3.image = 'img/package-3.jpg'

    package4 = Package()
    package4.id = 4
    package4.location = 'Australia'
    package4.price = 900
    package4.no_of_people = 2
    package4.image = 'img/package-4.jpg'

    package5 = Package()
    package5.id = 5
    package5.location = 'USA'
    package5.price = 500
    package5.no_of_people = 2
    package5.image = 'img/package-5.jpg'

    package6 = Package()
    package6.id = 5
    package6.location = 'Bali'
    package6.price = 200
    package6.no_of_people = 2
    package6.image = 'img/package-6.jpg'

    packages = [package1,package2,package3,package4,package5,package6]

    return render(request, 'index.html', {'guides': guides, 'packages': packages})