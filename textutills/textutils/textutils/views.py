# I created this file
from django.shortcuts import render

# let's learn to lying pipeline
def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtxt = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')  # Default value is 'off' if checkbox not checked
    UPPERCASE = request.GET.get('UPPERCASE', 'off')
    new_line_remover = request.GET.get('new_line_remover', 'off')
    print(removepunc)
    print(djtxt)
    if(removepunc == 'on'):  # Check if checkbox is checked
        punctuation_list = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzer = ""
        for char in djtxt:
            if char not in punctuation_list:
                analyzer = analyzer + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_txt': analyzer}

    elif(UPPERCASE == 'on'):
        analyzer = ""
        for char in djtxt:
            analyzer = analyzer + char.upper()
        params = {'purpose': 'UPPERCASE TEXT', 'analyzed_txt': analyzer}

    elif(new_line_remover == 'on'):
        analyzer = ""
        for char in djtxt:
            if char != "\n":
                analyzer = analyzer + char
        params = {'purpose':'new_line_remover', 'analyzed_txt': analyzer}

    else:
        params = {'purpose': 'No Operation Selected', 'analyzed_txt': djtxt}

    return render(request, 'analyze.html', params)