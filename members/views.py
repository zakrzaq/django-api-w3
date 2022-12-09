from django.shortcuts import render

# Sample response 
from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Hello world!")

# Display an HTML template
from django.template import loader

# def index(request):
#   template = loader.get_template('index.html')
#   return HttpResponse(template.render())

from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  output = "<ul>"
  for x in mymembers:
    output += "<li>" + x["firstname"] + "</li>"
  output += "</ul>"
  return HttpResponse(output)
