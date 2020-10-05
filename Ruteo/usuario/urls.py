from django.conf.urls import url
from usuario import views
from django.urls import path

urlpatterns = [
	path('getUsers',views.get_users),
	path('addUser',views.add_user),
	path('editUser/<int:id_usuario>',views.edit_user),
	path('deleteUser/<int:id_usuario>',views.delete_user),
 ]