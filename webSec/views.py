from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import connection

# start index page
@login_required()
def index(request):
    users = get_queryset(request)
    users = [dict(zip(['id', 'username', 'first_name', 'last_name', 'gender'], row)) for row in users]
    
    data = {
        'users': users
    }
    return render(request, 'page/index.html', data)

def get_queryset(request):
    search = request.GET.get('search') or ''
    sql = f"SELECT user_id, username, first_name, last_name, gender FROM user_details WHERE username LIKE '%{ search }%' OR first_name LIKE '%{ search }%' OR last_name LIKE '%{ search }%' "
    print(sql)
    query = connection.cursor()
    query.execute(sql)
    return query.fetchall()
    

# end index page

# start login page
@csrf_exempt
def login_page(request):
    if request.user.is_authenticated:
        print('User is already authenticated')
        return redirect('/')
    elif request.method == 'POST':
        print('Login request')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Invalid login')
    print('Render login page')
    return render(request, 'page/login-page.html')
# end login page