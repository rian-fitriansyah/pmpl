from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
       Item.objects.create(text=request.POST['item_text'])
       return redirect('/')

    items = Item.objects.all()
    list_item = Item.objects.count()
    comment = ''

    if list_item == 0: 
       comment = 'yey, waktunya berlibur'
    elif list_item < 5: 
       comment = 'sibuk tapi santai'
    else: 
       comment='oh tidak'

    return render(request, 'home.html', {'comment':comment, 'items':items})
