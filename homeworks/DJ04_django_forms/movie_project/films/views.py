from django.shortcuts import render,redirect
from .models import Film
from .forms import Films_postForm

def films(request):
    films =  Film.objects.all()
    return render(request, 'films.html',
            {'records': films,
                     'title': 'Приложение Films',
                    'header': 'Список фильмов',
                   'empty': 'Нет фильмов для показа'})

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
    return render(request, 'fill.html',{'form':form,'error': error})