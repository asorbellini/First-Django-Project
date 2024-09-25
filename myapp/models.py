from django.db import models

# Create your models here.

#Se va a trabajar con una aplicación de proyectos y tareas
class Project(models.Model):
    name = models.CharField(max_length=200)
    #Para que aparezca el nombre del proyecto dentro de la descripción del mismo y no ProjectObject(n°) se utiliza el siguiente método: 
    def __str__(self) -> str:
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #ON_DELETE: Indica que cuando se elimine uno de los proyectos, se elimine completamente todas las tareas referenciadas al mismo. 
    done = models.BooleanField(default= False)

    #Para que aparezca el nombre del proyecto dentro de la descripción del mismo y no ProjectObject(n°) se utiliza el siguiente método: 
    def __str__(self) -> str:
        return self.title + " - " + self.project.name

