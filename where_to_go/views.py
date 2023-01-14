from django.template import loader
from django.shortcuts import render
from places.models import Place, Image
from django.templatetags.static import static


def get_map_places() -> dict:
    places = Place.objects.all()

    map_places = {"type": "FeatureCollection", "features": []}
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": static('places/moscow_legends.json') if place.id == 1 else static('places/roofs24.json')
            }
        }
        map_places['features'].append(feature)

    return map_places


def show_map(request):
    data = {'map_places': get_map_places()}
    return render(request, 'index.html', context=data)
