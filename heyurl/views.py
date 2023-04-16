from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url, Click
import random
import string 
from django_user_agents.utils import get_user_agent

from django.db import connection
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def index(request):
    urls = Url.objects.order_by('-created_at')
    context = {'urls': urls}
    return render(request, 'heyurl/index.html', context)


def generate_random_url():
    SHORT_URL_LENGTH = 5
    CHARACTER_OPTIONS = string.ascii_letters + string.digits
    random_url = "".join(random.choices(CHARACTER_OPTIONS, k=SHORT_URL_LENGTH))
    return random_url


def store(request):
    # FIXME: Insert a new URL object into storage
    new_original_url = request.POST.get("original_url")
    validate_URL = URLValidator()
    try:
        validate_URL(new_original_url)
    except ValidationError:
        messages.add_message(request, messages.ERROR, 'URL is not valid')
        return redirect("/")

    if Url.objects.filter(original_url=new_original_url).exists():
        messages.add_message(request, messages.ERROR, 'URL already exists')
        return redirect("/")
    else:
        while True:
            new_short_url = generate_random_url()
            if not Url.objects.filter(short_url=new_short_url).exists():
                break
        
        new_url = Url.objects.create(short_url=new_short_url, original_url=new_original_url)
        print(new_url)
        print(connection.queries)
        messages.add_message(request, messages.SUCCESS, 'Short URL Created')
        return redirect("/")


def short_url(request, short_url):
    # FIXME: Do the logging to the db of the click with the user agent and browser
    if Url.objects.filter(short_url=short_url).exists():
        url = Url.objects.get(short_url=short_url)
        current_clicks = url.clicks
        Url.objects.filter(short_url=short_url).update(clicks=current_clicks+1)
        user_agent = get_user_agent(request)
        Click.objects.create(url=url, browser=user_agent.browser.family, platform=user_agent.os.family)
        return redirect(url.original_url)
    else:
        return render(request, 'heyurl/not_found.html')
    

def statistics(request, short_url):
    url_statistics = Click.objects.values("platform", "browser", "created_at").filter(url__short_url=short_url)
    url = Url.objects.get(short_url=short_url)
    #print("\n\n", connection.queries, "\n\n")
    context = {'url_statistics': url_statistics, "url": url}
    return render(request, 'heyurl/statistics.html', context)