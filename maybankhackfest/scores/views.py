from django.http import HttpResponse
import os
from scores.ranking import *

# Create your views here.
def index(request):
    return HttpResponse("Welcome to WannaDex!"+str(request))

def getscores(request):
    return HttpResponse(path())

def getscorescustom(request):
    return HttpResponse(get_scores_columns(request))


