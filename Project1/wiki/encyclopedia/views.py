from django.shortcuts import render
from random import randrange

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def wiki(request, entry):
    return render(request, "encyclopedia/wiki.html", {
        "title": entry,
        "content": util.get_entry(entry)
    })

def newpage(request):
    return render(request, "encyclopedia/newpage.html")


def random(request):
    entries = util.list_entries()
    entry = entries[randrange(0, len(entries))]
    return render(request, "encyclopedia/wiki.html", {
        "title": entry,
        "content": util.get_entry(entry)
    })