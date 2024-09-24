from django.shortcuts import render
from django.http import HttpResponse  # Du musst HttpResponse importieren
from django.template import loader  # Hier wird loader importiert, um das Template zu laden

def helloworld(request):
    template = loader.get_template('index.html')  # Lade das Template 'index.html'
    return HttpResponse(template.render())  # Render das Template und gib es zurück