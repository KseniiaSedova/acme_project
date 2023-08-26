from django.shortcuts import render, get_object_or_404, redirect

from .models import Birthday
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown


def birthday_list(request):
    template_name = 'birthday/birthday_list.html'
    birthdays = Birthday.objects.all()
    context = {'birthdays': birthdays}
    return render(request, template_name, context)


def birthday(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
    else:
        instance = None
    form = BirthdayForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
    template_name = 'birthday/birthday.html'   
    return render(request, template_name, context=context)


def delete_birthday(request, pk=None):
    instance = get_object_or_404(Birthday, pk=pk)
    form = BirthdayForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')
    return render(request, 'birthday/birthday.html', context)
        
    