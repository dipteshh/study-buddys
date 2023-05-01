from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Design'},
    {'id': 3, 'name': 'Web development'},
]

# Create your views here.


def home(request):
    context = {'rooms': rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            break
    context = {'room': room}
    return render(request, "base/room.html", context)
