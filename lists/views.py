from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Создайте здесь представления свои.
from lists.forms import ItemForm, ExistingListItemForm
from lists.models import Item, List

from accounts.models import Token

from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    '''новый список'''
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List()
        list_.owner = request.user
        list_.save()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})


def view_list(request, list_id):
    '''представление списка'''
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})


def my_lists(request, email):
    '''мои списки'''
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})
