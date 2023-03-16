from django.shortcuts import render, redirect  
from cars.forms import CarForm  
from cars.models import Car  
# Create your views here.  
def new(request):  
    if request.method == "POST":  
        form = CarForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CarForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    cars = Car.objects.all()  
    return render(request,"show.html",{'cars':cars})  
def edit(request, id):  
    car = Car.objects.get(id=id)  
    return render(request,'edit.html', {'car':car})  
def update(request, id):  
    car = Car.objects.get(id=id)  
    form = CarForm(request.POST, instance = car)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'car': car})  
def destroy(request, id):  
    car = Car.objects.get(id=id)  
    car.delete()  
    return redirect("/show")  