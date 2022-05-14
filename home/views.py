from multiprocessing import context
from operator import and_, gt
from urllib import response
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Sum
from .models import InputModel, InOutMaterial
from .forms import InputForm, InOutForm
from .resource import MaterialResource
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib import messages



# Create your views here.

#Halaman Login
def loginView(request):
    context ={
        'title': 'Warehouse | Login'
    }
    user = None
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'pages/login.html', context)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username dan password Anda tidak tepat')
            return redirect('/login')
    

# @login_required
# def logoutView(request):
#     context ={
#         'title': 'Warehouse | Logout'
#     }
#     if request.method == "POST":
#         if request.POST["logout"]:
#             logout(request)
#         return redirect('/login')
#     print(request.user)
#     return render(request, 'pages/logout.html', context)


#Fitur Logout
class CustomLogoutView(LogoutView):
    template_name = 'pages/login.html'
    next_page = 'login'


# Halaman Utama / Beranda
@login_required(login_url='login')
def home(request):
    context ={
        'title': 'Warehouse | Beranda'
    }
    return render(request, 'pages/home.html', context)


#Halaman List Material
@login_required(login_url='login')
def material(request):
    material = InputModel.objects.all()
    total = InputModel.objects.aggregate(Sum('totalMat'))
    de_mat = InputModel.objects.filter(stock__exact=0).delete()
    if request.method == 'POST':
        tambah = InputModel.objects.get(id=request.POST['id'])
        data = {
            'nmrMat': tambah.nmrMat,
            'satuan': tambah.satuan,
            'descMat': tambah.descMat,
            'jmlMat': tambah.jmlMat,
            'hargaSat': tambah.hargaSat,
            'matIn' : tambah.matIn,
            'matOut': tambah.matOut,
            }
        tambahForm = InputForm(request.POST or None, initial=data, instance=tambah)
        masukform = InOutForm(request.POST or None)
        if tambahForm.is_valid() and masukform.is_valid():
            tambahForm.save()
            masukform.save()
            if request.POST['matOut'] == '0':
                messages.success(request, 'Material berhasil ditambahkan')
                return redirect('/material')
            elif request.POST['matIn'] == '0':
                messages.success(request, 'Material berhasil dikeluarkan')
                return redirect('/material')

    context ={  
        'title': 'Warehouse | List Material',
        'materials':material,
        'total':total,
    }
    return render(request, 'pages/material.html', context)


#Halaman Input Material
@login_required(login_url='login')
def input(request):
    if request.method == 'POST':
        forminput = InputForm(request.POST, request.FILES or None)
        masukform = InOutForm(request.POST or None)
        if forminput.is_valid() and masukform.is_valid():
            forminput.save()
            masukform.save()
            messages.success(request, 'Data berhasil diinput')
            return redirect('/material')
        else:
            messages.error(request, 'Nomor material sudah ada')
            return redirect('/input')
        # InputModel.objects.create(
        #     tglMasuk = request.POST['tglMasuk'],
        #     nmrMat = request.POST['nmrMat'],
        #     descMat = request.POST['descMat'],
        #     jmlMat = request.POST['jmlMat'],
        #     satuan = request.POST['satuan'],
        #     hargaSat = request.POST['hargaSat'],
        #     imgMat = request.FILES['imgMat'],
        # )
       
    context ={
        'title': 'Warehouse | Input Material'
    }
    return render(request, 'pages/input.html', context)


#Halaman Material Masuk
@login_required(login_url='login')
def masuk(request):
    mat_masuk = InOutMaterial.objects.filter(matOut__exact=0)
    context ={
        'title': 'Warehouse | Material Masuk',
        'matMasuk': mat_masuk
    }
    return render(request, 'pages/masuk.html', context)


#Halaman Material Keluar
@login_required(login_url='login')
def keluar(request):
    mat_keluar = InOutMaterial.objects.filter(matOut__gt=0)
    context ={
        'title': 'Warehouse | Material Keluar',
        'matKeluar': mat_keluar
    }
    return render(request, 'pages/keluar.html', context)


#Halaman Kontak
@login_required(login_url='login')
def kontak(request):
    context ={
        'title': 'Warehouse | Kontak'
    }
    return render(request, 'pages/kontak.html', context)


#Halaman Detail Material
@login_required(login_url='login')
def detail(request, random):
    detailMat = InputModel.objects.get(random=random)
    inMat = InOutMaterial.objects.filter(random=random).order_by('tglIn')
    outMat = InOutMaterial.objects.filter(random=random).order_by('tglOut')

    context ={
        'title': 'Warehouse | Detail',
        'detail': detailMat,
        'inmat': inMat,
        'outmat': outMat,
    }
    print(detailMat)
    return render(request, 'pages/detail.html', context)


# Export File Excel 
def export_xls(request):
    material = MaterialResource()
    dataset = material.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['content-Disposition'] = 'attachment; filename=material.xls'
    return response
