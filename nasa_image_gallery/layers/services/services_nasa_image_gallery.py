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

##Toma las NasaCard formadas y revisa si hay coincidencias en la misma con la pálabra introducida en el buscador (search_msg), si es asi lo agrega al listado "selectedImages" que posteriormente se devuelve. Ademas se pone la palaba del buscador como la del titulo y la de la descripcion en minuscula, para evitar que alguna imagen no entre en el listado por tener diferencias entre mayusculas y minusculas. // de no introducir nada en el buscador refresca la pagina usando la funcion refresh (en views la variable "refresh" esta definido como una funcion que recarga la galeria)  
def getSerchedImages(request,refresh, search_msg,images, favourite_list):
    selectedImages = []
    favourite_list 
    if search_msg == "":
        refresh
    for NasaCard in images:
        if search_msg.lower() in NasaCard.title.lower() or search_msg.lower() in NasaCard.description.lower(): 
            selectedImages.append(NasaCard)
    return selectedImages

def getImagesBySearchInputLike(input):
    return getAllImages(input)

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una NASACard.
    fav.user = '' # le seteamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.


# usados en el template 'favourites.html'
def getAllFavouritesByUser(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositorio TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            nasa_card = '' # transformamos cada favorito en una NASACard, y lo almacenamos en nasa_card.
            mapped_favourites.append(nasa_card)

        return mapped_favourites


def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.