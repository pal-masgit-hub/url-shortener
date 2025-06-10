from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
import random

from .models import *


def make_url_short(request: HttpRequest) -> HttpResponse:
    form = UrlForm()
    context = {
        "form": form,
    }

    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data["source_url"]
            url = short_url_func(long_url)
            context["url"] = url
            return redirect("view_url", url=url)
    for url in ShortUrl.objects.all():
        print(url.URL)
    return render(request, "make_url_short.html", context)


def view_url(request: HttpRequest, url) -> HttpResponse:
    try:
        short_url = ShortUrl.objects.get(URL=url)
        context = {
            "url": short_url.URL,
            "source_url": short_url.source_url,
        }
        return render(request, "shorter_url_result.html", context)
    except Exception as e:
        return HttpResponse(f"Not Found! {e}")


def redirect_url(request: HttpRequest, url) -> HttpResponse:
    try:
        short_url = ShortUrl.objects.get(URL=url)
        return redirect(short_url.source_url)
    except Exception as e:
        return HttpResponse(f"Not Found! {e}")


def random_url(request):
    urls = list(ShortUrl.objects.all())
    url = urls[random.randint(0, len(urls) - 1)].source_url
    print(url)
    return redirect(url)