from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .forms import ArtRequestForm
from openai import OpenAI
import os
import requests
from django.core.files.base import ContentFile
from .models import GeneratedImage
import uuid
from django.http import HttpResponse


def artgpt(request):
    generated_images = GeneratedImage.objects.all()
    context = {"generated_images": generated_images}
    return render(request, "artgpt/art_ai.html", context)


@csrf_protect
def generate_artwork(request):
    if request.method == "POST":
        form = ArtRequestForm(request.POST)

        if form.is_valid():
            openai_api_key = form.cleaned_data["openai_api_key"]
            gender = form.cleaned_data["gender"]
            primary_color = form.cleaned_data["primary_color"]
            props = form.cleaned_data["props"]

            prompt = os.getenv("ART_PROMPT_TEMPLATE").format(
                gender=gender, primary_color=primary_color, props=props
            )

            client = OpenAI(api_key=openai_api_key)
            try:
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    quality="hd",  # stanrdard or hd
                    n=1,
                )
                image_url = response.data[0].url

                # Download the image
                image_response = requests.get(image_url)
                image_response.raise_for_status()  # Raise an exception for HTTP errors

                # Generate a random UUID for the image filename
                random_uuid = uuid.uuid4()

                # Save the image to the GeneratedImage model
                image = GeneratedImage(
                    gender=gender,
                    primary_color=primary_color,
                    props=props,
                )
                image.image.save(
                    f"generated_image_{random_uuid}.png",
                    ContentFile(image_response.content),
                    save=True,
                )

                context = {
                    "image_url": image_url,
                }

                return render(
                    request, "artgpt/htmx/generate_artwork_valid.html", context
                )

            except Exception as e:
                context = {"error": e}
                return render(
                    request, "artgpt/htmx/generate_artwork_error.html", context
                )

        else:
            # If form is not valid, return errors
            print("Form is not valid")
            return render(request, "artgpt/htmx/generate_artwork_error.html")


def artwork_modal(request):
    if request.method == "POST":
        # Manage the open and close state
        modal_action = request.POST.get("modal_action")
        modal_close = True if modal_action == "close" else False

        if modal_close:
            return render(request, "artgpt/htmx/testing.html")

        else:
            # Retrieve the values from the post request
            image_url = request.POST.get("image_url")

            context = {"image_url": image_url}

            return render(request, "artgpt/htmx/open_modal_art.html", context)
    else:
        return HttpResponse("Invalid request")
