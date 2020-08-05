#I have created this file - Manpreet
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')
    #return HttpResponse("Home")



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    # Check which checkbox is on
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
#        
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Changed to Uppercase', 'analyzed_text':analyzed}
            djtext = analyzed
       
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if(djtext[index] == " " and djtext[index+1] == " "):
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines', 'analyzed_text':analyzed}
        djtext = analyzed
        
    
    
    if (charcount == "on"):
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose':'Total character count', 'analyzed_text':analyzed}
        djtext = analyzed
        return render(request, "analyze.html", params) 
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            params = {'purpose':'Removed NewLines', 'analyzed_text':analyzed}
    if(newlineremover!="on" and charcount!="on" and extraspaceremover!="on" and fullcaps!="on" and removepunc!="on"):
        return HttpResponse("Please select any operation and try again")
        
   
    return render(request, 'analyze.html', params)
#def capfirst(request):
 #   return HttpResponse('''Capitalize first <br> <a href = "http://127.0.0.1:8000/removepunc"> removepunc</a>''')

#def newlineremove(request):
 #   return HttpResponse('''newlineremove  <br> <a href = "http://127.0.0.1:8000/capitalizefirst"> capfirst</a>''')

#def spaceremove(request):
 #   return HttpResponse('''space remove  <br> <a href = "http://127.0.0.1:8000/newlineremove"> newlineremove</a>''')

#def charcount(request):
 #   return HttpResponse('''char count <br> <a href = "http://127.0.0.1:8000/spaceremove"> spaceremove</a>''')
