from textwrap import shorten
from django.shortcuts import render
import pyshorteners

# Create your views here.
def app(request):
    if request.method == 'POST':
        longURL = request.POST['long_url']
        shortener = pyshorteners.Shortener()
        try:
            shortened_url = shortener.tinyurl.short(longURL)
        except:
            pass
        context = {'short_url':shortened_url}
    else:
        context = {}
    return render(request, 'app/urlshortner.html', context)
