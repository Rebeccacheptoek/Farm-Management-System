from django.shortcuts import render

farms = [
    {'id': 1, 'name':'Kitale home farm', 'location': 'Kitale', 'size': 2, 'is_mine': True},
    {'id': 2, 'name':'Eldoret home farm', 'location': 'Eldoret', 'size': 5, 'is_mine': True},
    {'id': 3, 'name':'Kinyoro maize farm', 'location': 'Kinyoro', 'size': 12, 'is_mine': False}
]

def home(request):
    context = {'farms': farms}
    return render(request, 'base_farm/home.html', context)

def farm(request, pk):
    farm = None
    for i in farms:
        if i['id'] == int(pk):
            farm = i
    context = {'farm': farm}
    return render(request, 'base_farm/farm.html', context)
