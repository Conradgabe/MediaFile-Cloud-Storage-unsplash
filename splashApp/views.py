from django.shortcuts import render
from django.http import HttpResponse
from .models import Splash


# upload the images to the db
def upload(request):
    if request.method == "POST":
        image_name = request.GET.get("name")
        image_url = request.GET.get("url")
        image_pic = request.FILES.get("pic")#
        if image_name != None and image_url != None:
            splash = Splash.objects.create(
                label=image_name, url=image_url
            )
            return redirect("uploaded")
        elif image_name != None and image_pic != None:
            splash = Splash.objects.create(
                label=image_name, picture=image_pic
            )
            return redirect("uploaded")
        else:
            return HttpResponse("Upload an image or a valid image url")
    return render(request, "upload.html")


# shows all images in the db
def all_images(request):
    splashes = Splash.objects.all()
    images_with_url = {}
    images_without_url = {}
    for splash in splashes:
        if splash.label != None and splash.url != None:
            images_with_url["image_one"]["image_label"] = splash.label
            images_with_url["image_one"]["image_url"] = splash.url
        elif splash.label != None and splash.picture != None:
            images_without_url["image_one"]["image_label"] = splash.label
            images_without_url["image_one"]["image_url"] = splash.picture.url
        else:
            return HttpResponse("Image with that label or url does not exist")
    context = {
        "images_with_url": images_with_url,
        "images_without_url": images_without_url
    }
    return render(request, "all_images.html", context)

# static page for show successful upload
def uploaded(request):
    return render(request, "uploaded.html")

# filer the label and returns the users search result images
def search(request):
    return render(request, "search.html")