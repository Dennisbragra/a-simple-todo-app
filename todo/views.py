from django.shortcuts import render, redirect
from .models import ToDo
#from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
	objs = ToDo.objects.all()

	if request.method =='POST':
		new_content = ToDo(content = request.POST['content'])
		new_content.save()
		return redirect('/')

	return render(request, 'base.html', {'objects':objs})


def deletetodo(request, todo_id):
	obj_to_delete = ToDo.objects.get(id = todo_id)

	obj_to_delete.delete()

	return redirect('/')
