from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Place


def get_map_place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_images = place.images.all()
    place_details = {
        'title': place.title,
        'imgs': [place_image.image.url for place_image in place_images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    return JsonResponse(place_details, json_dumps_params={'ensure_ascii': False, 'indent': 4})


def show_map(request):
    places = Place.objects.all()
    map_places = {'type': 'FeatureCollection', 'features': []}

    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place-details', args=[place.id])
            }
        }
        map_places['features'].append(feature)

    map_places_collection = {'map_places': map_places}
    return render(request, 'index.html', context=map_places_collection)
