from django.shortcuts import render, redirect
from staf.models import Staf
from staf.forms import FormStaf
from django.contrib import messages

def hapus_staf(request, id_staf):
    staf = Staf.objects.filter(id=id_staf)
    staf.delete()

    return redirect('hapus_staf', id_staf=id_staf)

def ubah_staf(request, id_staf):
    staf = Staf.objects.get(id=id_staf)
    template = 'ubah-staf.html'
    if request.POST:
        form = FormStaf(request.POST, instance=staf)
        if form.is_valid():
           form.save()
           messages.success(request, "Data Berhasil Diperbaharui!")
           return redirect('ubah_staf', id_staf=id_staf)
    else:
        form = FormStaf(instance=staf)
        konteks = {
            'form':form,
            'staf':staf,
        }
    return render(request, template, konteks)







# Create your views here.
def staf(request):
    context = {
        'staf': Staf.objects.all()

    }
    return render(request, "staf.html", context)


def tambah_staf(request):
    if request.POST:
        form = FormStaf(request.POST)
        if form.is_valid():
            form.save()
            form = FormStaf()
            pesan = "Data Berhasil Disimpan"
            konteks = {
                'form': form,
                'pesan' : pesan,
            }

            return render(request, 'tambah-staf.html', konteks)

    else:
        form = FormStaf()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-staf.html', konteks)
