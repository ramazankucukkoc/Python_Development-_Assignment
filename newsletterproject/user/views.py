from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
       if request.method == 'POST':      
                
        # get form values
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
           auth.login(request,user)
           print('login başarılı')
           return redirect('index')
        else:
           print('kullanıcı adı veya parola yanlış')
           return render(request,'user/login.html')
       else:
           return render(request,'user/login.html')
       
def logout(request):
       return render(request,'user/logout.html')

def register(request):
       if request.method == 'POST':      
                
        # get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            # Username
            if User.objects.filter(username = username).exists():
                print('bu kullanıcı adı daha önce alınmış')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    print('bu email daha önce alınmış')
                    return redirect('register')  
                else:
                    # her şey güzel
                    user = User.objects.create_user(username=username, password= password,email=email)
                    user.save()
                    print('kullanıcı oluşturuldu.')
                    return redirect('login')
        else:            
            print('parolalar eşleşmiyor')
            return redirect('register')
       else:
        return render(request, 'user/register.html')


