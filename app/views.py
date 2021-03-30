from django.shortcuts import render

# Create your views here.
def IndexPage(request):
    return render(request, "app/home.html")

def GetCardId(request):
    gci = request.POST['card_uid']
    print(f"---------------CARD-ID:{gci}")