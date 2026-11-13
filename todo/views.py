from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def todolist(request):
    queryset = Todolist.objects.all()
    Completed = Todolist.objects.filter(is_completed = True)
    incomplete = Todolist.objects.filter(is_completed = False)

    context = {
        'tasks':queryset,
        'Completed': Completed,
        'Incompleted': incomplete
    }
    return render(request, 'home.html' , context )


def create(request): 
    if request.method =='POST':
     title = request.POST.get('title')
     description = request.POST.get('description')
     
     Todolist.objects.create(title = title , description=description)
     return redirect( '/todolist/')
    
    return render (request, 'create.html')


def mark_complete(request,id):
   task = Todolist.objects.get(id=id)
   task.is_completed = not task.is_completed
   task.save()
   
   return redirect('/todolist/')


def edit(request,id):
   task = Todolist.objects.get(id=id)
   if request.method == 'POST':
      title = request.POST.get('title')
      description = request.POST.get('description')
      task.title = title
      task.description= description
      task.save()
      return redirect('/todolist/')
   

   context = {
      'task':task
   }
   return render(request, 'edit.html',context)
   
   

def delete(request,id):
   task = Todolist.objects.get(id=id)
   task.delete()

   return redirect('/todolist/')



 



   



    

   
   





