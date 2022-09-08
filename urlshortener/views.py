from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners

# Create your views here.
def app(request):
    if request.method == 'POST':
        longURL = request.POST['long_url']
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.chilpit.short(longURL)
        context = {'short_url':shortened_url}
    else:
        context = {}
    return render(request, 'app/urlshortner.html', context)

def shorten(request):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.chilpit.short('raunakmishra.com.np')
    return HttpResponse(f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')
