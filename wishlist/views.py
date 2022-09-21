from django.shortcuts import render
from wishlist.models import BarangWishlist

from django.http import HttpResponse
from django.core import serializers

# Import untuk Lab 3 (Membuat form registrasi)
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Buat form login
from django.contrib.auth import authenticate, login

# Buat fungsi logout
from django.contrib.auth import logout

# import fungsi untuk merestriksi akses halaman wishlist
from django.contrib.auth.decorators import login_required

# Import fungsi untuk menambahkan cookies
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse




# Create your views here.
@login_required(login_url='/wishlist/login/') # Agar halaman wishlist hanya dpt diakses pengguna yg terauntetikasi (login)
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'M Fauzan Rizky',
    'last_login': request.COOKIES['last_login'],
}
    return render(request, "wishlist.html", context)



# Membuat sebuah fungsi yang menerima parameter request (XML)
def request_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Membuat sebuah fungsi yang menerima parameter request (JSON)
def request_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Mengembalikan Data Berdasarkan ID dalam Bentuk JSON/XML
# Membuat sebuah fungsi yang menerima parameter request dan ID (Disini saya menggunakan json)
def show_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# Membuat sebuah fungsi register yang menerima parameter request
# (LAB 3) berfungsi untuk menghasilkan formulir registrasi secara otomatis 
# dan menghasilkan akun pengguna ketika data di-submit dari form.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# Buat form login (lab 3)
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Buat fungsi logout (lab 3)
def logout_user(request):
    # Menambahkan mekanisme penghapusan cookie last_login saat pengguna logout
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response
