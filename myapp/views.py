from django.shortcuts import render
from django.http import HttpResponse #, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def index(request):
    title = "Django Course!!"
    return render(request,"index.html", {
        "titulo": title
    }) #Las llaves son para incluir dentro de un html un valor/consulta, en este caso en el archivo index. 

def hello(request,username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    username = "Aye" #Html siempre toma lo que se le envía como texto STRING, no diferencia entre int, float o bool. 
    return render(request,"about.html", {
        "username" : username 
    })

def projects(request):
    #project_list = Project.objects.values()
    projects = Project.objects.all() #Lista de proyectos 
    #return JsonResponse(project_list) lo dejarmos como comentario para no olvidarnos porque ahora se incluye un html que dará formato a la web. 
    return render(request,"projects/projects.html",{
        "projects" : projects
    })

def tasks(request): #,id #Se termina resolviendo de esta manera, debido a que si no se encuentra un id salta error. 
    #Este es un error controlable: 
    #task_using_error_controler = get_object_or_404(Task, id=id) #Lo mismo se puede hacer para buscar por nombre las tareas, 
    #return HttpResponse("task: %s" %task_using_error_controler.title ) //IDEM PROJECTS
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html",{
        "tareas": tasks 
    })

"""def tasks(request,id):  #EL ERROR NO ES CONTROLADO, FORMA TÍPICA DE ESCRIBIRLO.
        task_by_id = Task.objects.get(id=id)
        return HttpResponse("task: %s" %task_by_id.title)"""

def create_task(request):
    if request.method == "GET": 
        #SHOW INTERFASE
        return render(request, "tasks/create_task.html",{
            'form': CreateNewTask()
        })
    else: 
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == "GET": 
        #SHOW INTERFASE
        return render(request, "projects/create_project.html",{
            'form': CreateNewProject()
        })
    else: 
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_details(request, id):
    project = get_object_or_404(Project, id=id)
    tasks_project = Task.objects.filter(project_id=id)
    return render(request, "projects/details.html", {
        "project" : project,
        "tasks" : tasks_project
        })