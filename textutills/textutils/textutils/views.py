# I created this file
from django.shortcuts import render

# let's learn to lying pipeline

link = "http://127.0.0.1:8000"
char_counter_link = "http://127.0.0.1:8000/charcounter"
remove_punc_link = "http://127.0.0.1:8000/removepunc"
capitalize_link = "http://127.0.0.1:8000/capatilazed"
newline_remover_link = "http://127.0.0.1:8000/newlinermvr"
space_remover_link = "http://127.0.0.1:8000/spaceremover"


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtxt = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')  # Default value is 'off' if checkbox not checked
    print(removepunc)
    print(djtxt)

    if removepunc == 'on':  # Check if checkbox is checked
        punctuation_list = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzer = ""
        for char in djtxt:
            if char not in punctuation_list:
                analyzer = analyzer + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_txt': analyzer}
    else:
        params = {'purpose': 'No Operation Selected', 'analyzed_txt': djtxt}

    return render(request, 'analyze.html', params)


