from django.shortcuts import render
from wishlist.models import BarangWishlist

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html", context)

data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'M Fauzan Rizky'
}


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
def show_json_by_id(request):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
