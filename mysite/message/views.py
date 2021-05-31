import json
from django.http import HttpResponse

data = {
    "Name": "Larry-Manuel",
    "Track": "Backend(Python)",
    "Message": "Hi i'm still making it work!!"
}

# Create your views here.

def index(request):
    # return HttpResponse(data)
    return HttpResponse(json.dumps(data))