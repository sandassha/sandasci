from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.contrib.auth import authenticate, login, logout
from forms import LoginForm,RegisterForm
import markdown2, urlparse
from CiWeb import settings
URL=settings.URL


def index(request):
    username = request.COOKIES.get('cookie_username','')
    if not username:
        response = HttpResponseRedirect('/login')
    else:
        response = HttpResponseRedirect('/dashboard')
    return response
    # # latest_article_list = Article.objects.query_by_time()
    # # loginform = LoginForm()
    # # context = {'latest_article_list': latest_article_list, 'loginform':loginform}
    # username = request.COOKIES.get('cookie_username','')
    # # return render(request, './pages/index.html', {'username':username})
    # return render_to_response('./pages/index.html',{'username':username,'menuName':'dashboard'})



def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, './pages/login.html', {'form': form})
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect('/')
            response.set_cookie('cookie_username',username,3600)
            return response
        else:
            return HttpResponseRedirect('/login')

# @login_required
def log_out(request):
    response = HttpResponseRedirect('/login')
    response.delete_cookie('cookie_username')
    logout(request)
    return response


# @login_required
def dashboard(request):
    username = request.COOKIES.get('cookie_username','')

    return render_to_response('./pages/index.html',{'username':username,'menuName':'dashboard','url':URL})

def charts(request):
    username = request.COOKIES.get('cookie_username','')

    return render_to_response('./pages/index.html',{'username':username,'menuName':'charts','url':URL})

def ci(request):
    username = request.COOKIES.get('cookie_username','')

    return render_to_response('./pages/index.html',{'username':username,'menuName':'ci','url':URL})
def cd(request):
    username = request.COOKIES.get('cookie_username','')

    return render_to_response('./pages/index.html',{'username':username,'menuName':'cd','url':URL})

def settings(request):
    username = request.COOKIES.get('cookie_username','')

    return render_to_response('./pages/index.html',{'username':username,'menuName':'settings','url':URL})






