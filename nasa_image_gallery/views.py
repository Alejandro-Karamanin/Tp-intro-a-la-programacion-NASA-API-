# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')

# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
##incalculable la cantidad de tiempo que estuve sin darme cuenta de que en "getAllImages" no tenia que agregar el parametro "request"
def getAllImagesAndFavouriteList(request):
    images = services_nasa_image_gallery.getAllImages()
    favourite_list = []

    return images, favourite_list

# función principal de la galería.
def home(request):
    # llama a la función auxiliar getAllImagesAndFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario*.
    # (*) este último, solo si se desarrolló el opcional de favoritos; caso contrario, será un listado vacío [].
    images = []
    favourite_list = []
    images, favourite_list = getAllImagesAndFavouriteList(request)
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list} )

# función utilizada en el buscador.
##La funcion toma el listado de todas las imagenes que devuelve la api de la nasa (como la galeria principal) , posteriormente revisa en dicho listado si la palabra del buscador (search_msg) estaba dentro de las imagenes que se remitieron usando la funcion "getSerchedImages" desde "service_nasa_image_gallery", finalmente muestra las imagenes solicitadas 
def search(request):
    images = []
    favourite_list = []
    images, favourite_list = getAllImagesAndFavouriteList(request)
    search_msg = request.POST.get('query', '')
    refresh = AplyRefresh(request,images, favourite_list)
    selectedImages = services_nasa_image_gallery.getSerchedImages(request,refresh, search_msg, images, favourite_list) 
    
    return render(request, 'home.html', {'images': selectedImages, 'favourite_list': favourite_list} )
    # si el usuario no ingresó texto alguno, debe refrescar la página; caso contrario, debe filtrar aquellas imágenes que posean el texto de búsqueda.

## Es una funcion para que recargue la pagina, funciona junto a search y getSerchedImages. 
def AplyRefresh(request,images,favourite_list):
    return render(request, 'home.html', {'images':images, 'favourite_list': favourite_list})

# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    pass


@login_required
def deleteFavourite(request):
    pass


@login_required
def exit(request):
    pass