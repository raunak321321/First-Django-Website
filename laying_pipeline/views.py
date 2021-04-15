#I have created this file - Raunak N Somani
from  django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # params = {
    #     'name' : "Raunak",
    #     'place'  : "london"
    # } 
    
    return render(request,'Index.html')      # render three things leta h first request and other is templates and other is dictionary but it is not necessary to pass dictionary in the render.
def analyze(request):
    djtext = request.POST.get('text','default')
    # print(djtext)
    boolean = request.POST.get('removepunc',False)
    boolean1 = request.POST.get('fullcaps',False)
    boolean2 = request.POST.get('Extra_Space_Remover',False)
    print(boolean)
    print(boolean1)
    print(boolean2)
    # print(boolean)
    punctautions = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''  
    removedpunc=""
    for char in djtext:
        if char not in punctautions:
            removedpunc = removedpunc + char
    removedpunc1 = removedpunc.upper()
    removedpunc2=""
    i=0
    while(i<(len(removedpunc1))):
        # print(colors[i])
        if removedpunc1[i]==" " and removedpunc1[i+1]==" ":
            i = i +2
            while(removedpunc1[i]==" "):
                i+=1 
            i-=1
            removedpunc2=removedpunc2+removedpunc1[i]
            i+=1
        else:
            removedpunc2=removedpunc2+removedpunc1[i]
            i+=1
            

    if(boolean and boolean1 and boolean2):
        
        params = {
            'analyzed':removedpunc2
        }
        return render(request,'analyze.html',params)
    elif(boolean and boolean1):
        params = {
            'analyzed':removedpunc1
        }
        return render(request,'analyze.html',params)
    elif(boolean1 and boolean2):
        djtext1=djtext.upper()
        removedpunc3=""
        i=0
        while(i<(len(djtext1))):
        # print(colors[i])
            if djtext1[i]==" " and djtext1[i+1]==" ":
                i = i +2
                while(djtext1[i]==" "):
                    i+=1 
                i-=1
                removedpunc3=removedpunc3+djtext1[i]
                i+=1
            else:
                removedpunc3=removedpunc3+djtext1[i]
                i+=1
        params = {
            'analyzed':removedpunc3
        }
        return render(request,'analyze.html',params)
    elif(boolean and boolean2):
        removedpunc3=""
        i=0
        while(i<(len(removedpunc))):
        # print(colors[i])
            if removedpunc[i]==" " and removedpunc[i+1]==" ":
                i = i +2
                while(removedpunc[i]==" "):
                    i+=1 
                i-=1
                removedpunc3=removedpunc3+removedpunc[i]
                i+=1
            else:
                removedpunc3=removedpunc3+removedpunc[i]
                i+=1
        params = {
            'analyzed':removedpunc3
        }
        return render(request,'analyze.html',params)
    elif(boolean):
        # djtext1=djtext.upper()
        params = {
            'analyzed':removedpunc
        }
        return render(request,'analyze.html',params)
    elif(boolean2):
        removedpunc3=""
        i=0
        while(i<(len(djtext))):
        # print(colors[i])
            if djtext[i]==" " and djtext[i+1]==" ":
                i = i +2
                while(djtext[i]==" "):
                    i+=1 
                i-=1
                removedpunc3=removedpunc3+djtext[i]
                i+=1
            else:
                removedpunc3=removedpunc3+djtext[i]
                i+=1
        params = {
            'analyzed':removedpunc3
        }
        return render(request,'analyze.html',params)
    elif(boolean1):
        djtext1=djtext.upper()
        params = {
            'analyzed':djtext1
        }
        return render(request,'analyze.html',params)
    else:
        params = {
            'analyzed':djtext
        }
        return render(request,'analyze.html',params)

