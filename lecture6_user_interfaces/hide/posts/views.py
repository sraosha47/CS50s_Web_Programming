import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def posts(request):

    #get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    #generate 'posts' for demo purposes
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    #delay response
    time.sleep(1)

    #return list of posts as JSON
    return JsonResponse({
        "posts": data
    })
#basically created an API