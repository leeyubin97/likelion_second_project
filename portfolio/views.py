from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Person
from .forms import PersonForm

# Create your views here.
def home(request):
    persons=Person.objects
    return render (request, 'portfolio/home.html', {'persons':persons})

def detail(request, person_id):
    person_detail=get_object_or_404(Person, pk=person_id)
    return render(request, 'portfolio/detail.html', {'person':person_detail})

def person_next(request):
    if request.method =="POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('detail', person_id=person.pk)
    else:
        form=PersonForm()
        return render(request, 'portfolio/next.html', {'form':form}) 

def person_edit(request, person_id):
    person=get_object_or_404(Person,pk=person_id)
    if request.method =="POST":
        form = PersonForm(request.POST,instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('detail', person_id=person.pk)
    else:
        form=PersonForm(instance=person)
        return render(request, 'portfolio/edit.html', {'form':form}) 

def person_delete(request, person_id):
    person=get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect('home')         