from django.shortcuts import render, redirect
from dosen.models import Dosen
from dosen.forms import FormDosen
from django.contrib import messages

def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()

    return redirect('hapus_dosen', id_dosen=id_dosen)


def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
           form.save()
           messages.success(request, "Data Berhasil Diperbaharui!")
           return redirect('ubah_dosen', id_dosen=id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }
    return render(request, template, konteks)


# Create your views here.
def dosen(request):
    context = {
        'lecturer': Dosen.objects.all()
        
    }
    return render(request, "dosen.html", context)



def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data Berhasil Disimpan"
            konteks = {
                'form': form,
                'pesan' : pesan,
            }

            return render(request, 'tambah-dosen.html', konteks)

    else:
        form = FormDosen()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-dosen.html', konteks)
