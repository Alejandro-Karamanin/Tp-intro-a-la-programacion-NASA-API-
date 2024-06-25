# capa de servicio/lógica de negocio

from ..transport import transport
from ..dao import repositories
from ..generic import mapper
from django.contrib.auth import get_user




# ¡OJO! el parámetro 'input' indica si se debe buscar por un valor introducido en el buscador.
def getAllImages(input=None):
    images = []
    # obtiene un listado de imágenes desde transport.py y lo guarda en un json_collection.
    json_collection = transport.getAllImages(input)  
    #recorre el listado de objetos JSON, lo transforma en una NASACard y lo agrega en el listado de images. Ayuda: ver mapper.py
    for object in json_collection:
        imageToConvertIntoNasaCard = mapper.fromRequestIntoNASACard(object)
        images.append(imageToConvertIntoNasaCard)  
    return images

def getImagesBySearchInputLike(input):
    selectedImages = []
    for NasaCard in images:
        if search_msg.lower() in NasaCard.title.lower() or search_msg.lower() in NasaCard.description.lower(): 
            selectedImages.append(NasaCard)
    return selectedImages

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    if request.method == 'POST':
            fav = mapper.fromTemplateIntoNASACard(request)
            if fav:
                fav.user = request.user
                return repositories.saveFavourite(fav)
    return None

# usados en el template 'favourites.html'
def getAllFavouritesByUser(request):
    if request.user.is_authenticated:
        user = get_user(request)
        favourite_list = repositories.getAllFavouritesByUser(user) # buscamos desde el repositorio TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            nasa_card = mapper.fromRepositoryIntoNASACard(favourite) # transformamos cada favorito en una NASACard, y lo almacenamos en nasa_card.
            mapped_favourites.append(nasa_card)

        return mapped_favourites
    else:
        return None


def deleteFavourite(request):
    if request.method == 'POST':
        favId = request.POST.get('id')
        if favId:
            return repositories.deleteFavourite(favId) # borramos un favorito por su ID.)
        return None
        