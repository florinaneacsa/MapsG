from googleplaces import GooglePlaces, types, lang, GooglePlacesError

YOUR_API_KEY = 'AIzaSyDFD_KJwfubSSw5pEHhGXMSSD_YIJ3EKXc'

google_places = GooglePlaces(YOUR_API_KEY)

# text_search API
query_result = google_places.nearby_search(
    location='Cluj-Napoca, Cluj', keyword='Marty',
    radius=20000, types=[types.TYPE_FOOD])

if query_result.has_attributions:
    print(query_result.html_attributions)

# places
for place in query_result.places:
    print(place.name)
    print(place.geo_location)
    print(place.place_id)

# API call.
place.get_details()

# Getting place photos
for photo in place.photos:
    # 'maxheight' or 'maxwidth' is required
    photo.get(maxheight=500, maxwidth=500)
    # MIME-type, e.g. 'image/jpeg'
    var = photo.mimetype
    # Image URL
    var = photo.url
    # Original filename (optional)
    var = photo.filename
    # Raw image data
    var = photo.data

    # Adding and deleting a place
    try:
        added_place = google_places.add_place(name='Mom and Pop local store',
                                              lat_lng={'lat': 51.501984, 'lng': -0.141792},
                                              accuracy=100,
                                              types=types.TYPE_HOME_GOODS_STORE,
                                              language=lang.ENGLISH_GREAT_BRITAIN)
        print(added_place.place_id)
        print(added_place.id)

        # Delete added place
        google_places.delete_place(added_place.place_id)
    except GooglePlacesError as error_detail:
        print(error_detail)