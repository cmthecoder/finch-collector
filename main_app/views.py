from django.shortcuts import render
from django.http import HttpResponse

class Finch:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'tabby', 'Kinda rude.', 3),
  Finch('Sachi', 'tortoiseshell', 'Looks cute.', 0),
  Finch('Fancy', 'bombay', 'Happy feathers.', 4),
  Finch('Bonk', 'selkirk rex', 'Chirps loudly.', 6)
]

# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches})