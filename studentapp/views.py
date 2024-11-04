from django.shortcuts import render

def NameDisplay(request):
    return render(request,'NameDisplay.html')
def StudentHomePage(request):
    return render(request,'studentapp/StudentHomePage.html')