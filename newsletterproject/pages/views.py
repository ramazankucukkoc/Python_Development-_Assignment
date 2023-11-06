from django.shortcuts import render
from django.http import HttpResponse
# görüntü index isminde olacak index.html sayfasını gönderecek.



def index(request):
       return render(request,'pages/index.html')

def about(request):
       return render(request,'pages/about.html')



