from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Location

# Create your views here.

def parking(request, pk):
    location = Location.objects.get(pk=pk)
    size = Location.objects.all().count()
    wolne = 0
    zajete = 0
    for section in location.section_set.all():
        wolne += section.spot_set.all().filter(status='free').count()
        zajete += section.spot_set.all().filter(status='occupied').count()

    prev_id = pk - 1 if pk - 1 != 0 else size
    next_id = pk + 1 if pk + 1 <= size else 1

    context = {
        'prev': {'id': prev_id, 'name':Location.objects.get(pk=prev_id).name},
        'next': {'id': next_id, 'name':Location.objects.get(pk=next_id).name},
        'location': location,
        'image': 'parking/images/{}.bmp'.format(location.image),
        'css': 'parking/css/css_{}.css'.format(location.image),
        'free': wolne,
        'occupied':  zajete,
        'address_href': f'https://www.google.com/maps/place/{(location.address).replace(" ", "+")}',
        'parking_path': True,
    }
    return render(request, 'parking/parking.html', context)

def index(request):
    context = {}
    return render(request, 'parking/index.html', context=context)

def index_parking(request):
    locations = Location.objects.all()

    context = {'object': [{'id': location.id,
                           'img_path': f'parking/images/{location.image}_lookup.png',
                           'name': location.name} for location in locations]}
    print(context)
    return render(request, 'parking/index_parking.html', context=context)
