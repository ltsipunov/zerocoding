from django.shortcuts import render,redirect
from .models import Film
from .forms import Films_postForm

def films(request):
    films =  Film.objects.all().order_by('-id')
    return render(request, 'films.html',
            {'records': films,
                     'title': 'Приложение Films',
                    'header': 'Список фильмов',
                   'empty': 'Нет фильмов для показа'})

def details(request,id_value):
    film = Film.objects.get(pk=id_value)
    return render(request, 'details.html',{'rec':film})

def fill(request):
    error = ''
    if request.method == 'POST':
        form = Films_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films')
        else:
            error = "Ошибка заполнения данных"
    form = Films_postForm()
    return render(request, 'fill.html',{'form':form,'error': error,'submit_label': 'Добавить фильм'})