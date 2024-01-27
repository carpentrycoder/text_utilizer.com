#I created this file
from django.http import HttpResponse
from django.shortcuts import render

# let's learn to lying pipeline

link = "http://127.0.0.1:8000"
char_counter_link = "http://127.0.0.1:8000/charcounter"
remove_punc_link = "http://127.0.0.1:8000/removepunc"
capitalize_link = "http://127.0.0.1:8000/capatilazed"
newline_remover_link = "http://127.0.0.1:8000/newlinermvr"
space_remover_link = "http://127.0.0.1:8000/spaceremover"


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtxt = print(request.GET.get('text','default'))
    removepunc = print(request.GET.get('removepunc','default'))
    print(removepunc)
    print(djtxt)
    return HttpResponse(f"removepunc <a href={link}>Home</a>")

# def capatilazed(request):
#     return HttpResponse(f"capatilazed <a href={link}>Home</a>")
#
# def newlinermvr(request):
#     return HttpResponse(f"newlinermvr <a href={link}>Home</a>")
#
# def spaceremover(request):
#     return HttpResponse(f"spaceremover <a href={link}>Home</a>")
#
# def charcounter(request):
#     return HttpResponse(f"charcounter <a href={link}>Home</a>")