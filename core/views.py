from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .tasks import say_hello_task
from .models import Adhkar, Type , Doaa , DoaaType, Tasbih

def landing_page(request) :
    return render(request, "landing.html")

def index(request) :
    types = Type.objects.all()
    adhkar = Adhkar.objects.all()
    return render(request, "index.html", {"adhkar":adhkar,"types":types})

def adhkar_by_types(request, type_id):
    type_obj = Type.objects.get(id=type_id)
    adhkar = Adhkar.objects.filter(type=type_obj)
    types = Type.objects.all()
    return render(request, "index.html", {"adhkar": adhkar, "types": types})

def doaa_view(request) :
    doaa = Doaa.objects.all()
    doaa_types = DoaaType.objects.all()
    print(doaa)
    return render(request, "doaa.html",{"doaa":doaa,"doaa_types":doaa_types})

def doaa_by_type(request,type_id) :
    doaa_type = DoaaType.objects.get(id=type_id)
    doaa = Doaa.objects.filter(type=doaa_type)
    doaa_types = DoaaType.objects.all()
    return render(request, "doaa.html", {"doaa": doaa, "doaa_types": doaa_types})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "You are now logged in.")
            return redirect("/")
        else:
            return redirect('/')

    return render(request, "login.html")

@login_required(login_url='/login')
def logout_view(request):
    logout(request)  # end user session
    return redirect("login")  # redirect back to login page

def register_view(request) :
    return render(request, 'register.html')



@login_required(login_url='/login')
def tasbih_view(request) :
    user = request.user
    tasbih , created = Tasbih.objects.get_or_create(
        user=user,
        defaults={"tasbih_count": 0}
        )
    tasbih.tasbih_count += 1
    tasbih.save()
    return redirect('/tasbih')

@login_required(login_url='/login')
def tasbih(request) :
    tasbih = Tasbih.objects.get(user=request.user)
    tasbih_count = tasbih.tasbih_count
    progress = min(tasbih_count, 100)
    return render(
        request ,
        "tasbih_page.html",
        {"tasbih":tasbih,"tasbih_count":tasbih_count,"progress":progress}
    )

@login_required(login_url='/login')
def reset_tasbih(request) :
    tasbih = Tasbih.objects.get(user=request.user)
    tasbih.tasbih_count = 0
    tasbih.save()
    return redirect('/tasbih')