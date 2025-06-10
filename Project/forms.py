import random

from django import forms
from django.core.exceptions import ValidationError

from .models import *


def random_url() -> str:
    """
    Creates random and unique URL pattern.
    :return: random url
    """
    short = ""
    for i in range(8):  # Creating the short URL.
        short += chr(random.randint(65, 90))
        short += chr(random.randint(97, 122))
    while ShortUrl.objects.filter(URL=short).exists():  # Making sure that the URL is unique:
        short = ""
        for i in range(8):
            short += chr(random.randint(65, 90))
            short += chr(random.randint(97, 122))
    return short


def short_url_func(url: str) -> str:
    """
    Makes the URL shorter
    :param url: long URL www.example.com.
    :return: Shorter URL.
    """
    # Creating long URL source
    short_url, created = ShortUrl.objects.get_or_create(source_url=url)
    if not created:  # Then there is already a shorter URL for the given link.
        if short_url.URL is None or short_url.URL == "":
            short_url.URL = random_url()
            short_url.save()
        return short_url.URL

    # Making short URL:
    short_url.URL = random_url()
    short_url.save()
    return short_url.URL


class UrlForm(forms.Form):
    class Meta:
        model = ShortUrl
        fields = ["source_url"]

    source_url = forms.URLField(max_length=3000)

    def clean_source_url(self):
        source_url = self.cleaned_data["source_url"]
        return source_url
