from django.shortcuts import render
from mysite.models import PegawaiReg
from django.contrib import messages


def PegawaiRegistration(request):
    if request.method == 'POST':
        if request.POST.get('nip') and request.POST.get('nama') and request.POST.get('kantor') and request.POST.get('pwd') and request.POST.get('foto') :
            saverecord = PegawaiReg()
            saverecord.nip = request.POST.get('nip')
            saverecord.nama = request.POST.get('nama')
            saverecord.kantor = request.POST.get('kantor')
            saverecord.foto = request.POST.get('foto')
            saverecord.pwd = request.POST.get('pwd')
            saverecord.save()
            messages.success(request, "Register pegawai berhasil")
            return render(request, 'index.html')
    else :
        return render(request, 'index.html')
