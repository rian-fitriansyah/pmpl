from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List
from django.core.exceptions import ValidationError

def home_page(request):
    list_item = Item.objects.count()
    comment = ''

    if list_item == 0: 
       comment = 'yey, waktunya berlibur'
    elif list_item < 5: 
       comment = 'sibuk tapi santai'
    else: 
       comment='oh tidak'

    return render(request, 'home.html', {'comment':comment})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    list_item = Item.objects.count()
    comment = ''

    if list_item == 0:
       comment = 'yey waktunya berlibur'
    elif list_item <5:
       comment = 'sibuk tapi santai'
    else:
       comment= 'oh tidak'

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('/lists/%d/' % (list_.id,))
    return render(request, 'list.html', {'list': list_, 'comment':comment})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect('/lists/%d/' % (list_.id,))
