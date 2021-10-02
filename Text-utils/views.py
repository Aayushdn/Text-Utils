# this file is made by me - Aayush swodari
from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    return render(request,"index.html")

def check_page(request):
    # initial varriables
    checked =""
    checked2 = ""
    purpose = []
    text = request.POST.get("text","none")
    operation0 = request.POST.get("removepunc","off")
    operation = request.POST.get("fullcaps","off")
    operation2 = request.POST.get("smallcaps","off")
    operation3 = request.POST.get("titlecaps","off")
    operation4 = request.POST.get("titlesmall","off")
    operation5 = request.POST.get("checkbox5","on")
    
    # check for the options
    if operation0 == "on":
        purpose.append("remove punctution") # append the purpose list with the string 
        for i in text:
            if i not in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
                checked = checked + i
                text = checked # store the output to text

    if operation == "on":
        purpose.append("capitalize all letter")
        checked = text.upper()
        text = checked

    if operation2 == "on":
        purpose.append("  make all small letter")
        checked = text.lower()
        text = checked

    if operation3 == "on":
        purpose.append("  make title capital")
        checked = text.title()
        text = checked

    if operation4 == "on":
        purpose.append("  make title small")
        raw_tex = text[0]
        rae2 = raw_tex.lower()
        ec_list = []
        ec_list.extend(text)
        ec_list[0] = rae2
        checked = "".join(ec_list)
        text = checked

    # render it
    params = {'annalyzed_text': checked}
    return render(request, 'index.html', params)




def contact_page(request):
    return render(request,"contact.html")
