#MADE BY PARUL
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #parul={"name":"Parul","surname":"Verma"}
    return render (request,'index.html',)
    #return HttpResponse(str(10+2) +"\tI am trying to learn Django . Please help me God.\n <a href='https://studio.youtube.com/channel/UCtppEXMrdJvozW60ioQDsKg'> Parul Youtube Studio </a>")
def about(request):
    #return HttpResponse("I am learning to make websites using django.\n Till then check my blogs. Thanks <a href='https://simplypythonbeginner.blogspot.com/'></br>My Blog Posts about Python</a>")
    #parul={"name":"Parul","surname":"Verma"}
    return render (request,'about.html',)
def contact(request):
    #return HttpResponse("I am learning to make websites using django.\n Till then check my blogs. Thanks <a href='https://simplypythonbeginner.blogspot.com/'></br>My Blog Posts about Python</a>")
    #parul={"name":"Parul","surname":"Verma"}
    return render (request,'contact.html',)

def analyze(request):
    text = request.POST.get('text', 'default')
    # ------------------------------------------------REMOVE PUNC-------------------------------------------
    removepunc = request.POST.get('removepunc', 'off')
    if removepunc == "on":
        print(removepunc)
        
        punc = ["!", '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ' -', '.', '/', ':', ';', '<', '>', '=', '?',
                '@',
                '~', '_']
        home_page_input_text = text
        a = list(home_page_input_text)
        for items in punc:
            while items in a:
                a.remove(items)
        
        analyzed = ""
        for i in a:
            analyzed = analyzed + i
            text=analyzed
        dict = {'purpose': 'After Removing Punctuations', 'Analysed_Text': analyzed}
    # ------------------------------------------------------SPACE REMOVER-------------------------------------
    spaceremover = request.POST.get('spaceremover', 'off')

    if spaceremover == "on":
        
        home_page_input_text = text
        i = 1
        while i <= 5:
            home_page_input_text = home_page_input_text.replace("  ", " ")
            i = i + 1
            text=home_page_input_text
        dict = {'purpose': 'After Removing Spaces', 'Analysed_Text': home_page_input_text}
    # -------------------------------------------------------UPPER CASE----------------------------------------
    fullcaps = request.POST.get('fullcaps', 'off')
    if fullcaps == "on":
        
        home_page_input_text = text
        analyzed = ""
        for i in home_page_input_text:
            analyzed = analyzed + i.upper()
            text=analyzed
        dict = {'purpose': 'After Full Capitalization', 'Analysed_Text': analyzed}
    # -------------------------------------------------Remove New Line----------------------------------------
    newlineremover = request.POST.get('newlineremover', 'off')
    if newlineremover == "on":
        
        home_page_input_text = text
        analyzed = ""
        for i in home_page_input_text:
            if i != '\n' and i!="\r":
                analyzed = analyzed + i
                text=analyzed
        dict = {'purpose': 'After Removing New Line', 'Analysed_Text': analyzed}
    # -------------------------------------------------COUNTING CHARACTERS----------------------------------------
    charcount = request.POST.get('charcount', 'off')
    if charcount == 'on':
       
        home_page_input_text = text
        for i, char in enumerate(home_page_input_text):
            pass
        count = i + 1
        dict = {'purpose': 'After Counting Characters', 'Analysed_Text': f"{count} characters"}
    if removepunc!="on" and spaceremover!="on" and newlineremover!="on" and charcount!="on" and fullcaps!="on":
        return HttpResponse("Type some text and Try again!!")
    return render(request, 'analyze.html', dict)
