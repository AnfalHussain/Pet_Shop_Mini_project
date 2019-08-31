from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Pet
from .forms import PetForm, UpdatePetForm



def list(request):
    context = {
        "pets":Pet.objects.all(),
    }
    return render(request, 'list.html', context)


def pet_detail(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)
    context = { 
        "pet": pet_obj, 
    }
    return render(request, 'pet-detail.html', context)

def pet_create(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit = False)
            pet.owner = request.user
            pet.save()
            return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)



def pet_update(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)
    form = UpdatePetForm(instance=pet_obj)
    if request.method == "POST":
        form = UpdatePetForm(request.POST, request.FILES, instance=pet_obj)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "pet_obj": pet_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def pet_delete(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)
    pet_obj.delete()
    return redirect('list')



