from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=25)
    apellido_paterno=models.CharField(max_length=25)
    apellido_materno=models.CharField(max_length=25)
    edad=models.IntegerField(default=0)
    def getAll():
        usuarios=Usuario.objects.all().order_by('id_usuario')
        return usuarios
    def getId(id_usuario):
        usuario=Usuario.objects.get(id_usuario=id_usuario)
        return usuario
    def createUser(usuario):
        u=Usuario.objects.create( nombres=usuario['nombres']
                                ,apellido_materno=usuario['apellido_materno']
                                ,apellido_paterno=usuario['apellido_paterno']
                                ,edad=usuario['edad'])
        u.save()
        return u
    def editUser(usuario, id_usuario):
        u=Usuario.objects.get(id_usuario=id_usuario)
        u.apellido_materno=usuario['apellido_materno']
        u.apellido_paterno=usuario['apellido_paterno']
        u.edad=usuario['edad']
        u.nombres=usuario['nombres']
        u.save()
        return u
    def deleteUser(id_usuario):
        print(id_usuario)
        u=Usuario.objects.get(id_usuario=int(id_usuario))
        u.delete()

