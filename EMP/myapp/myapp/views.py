from django.http import HttpResponse
from django.shortcuts import render
def test(request):
    print("hello test fundtion is calll")
    return HttpResponse("<h1>hello ia am mohd fazil</h1>")
    # return render(request,"dashboard.html")

def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        print(password)
    
    # return HttpResponse("<h1> hello this is home page</h1>")
    return render(request,"./emp/home.html")
