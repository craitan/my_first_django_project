from django.shortcuts import render, redirect

from t4t.chat.forms import ChatCreateForm
from t4t.chat.models import Room


# Create your views here.
def chat_start(request):
    if request.method == 'GET':
        form = ChatCreateForm()
    else:
        form = ChatCreateForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.save()
            #TODO: have to redirect to the chat
            #return redirect('my items', pk=request.user.pk)

    context = {
        'form': form,
    }
    return render(request, 'chat/start-chat.html', context)


def chat_room(request, room):
    return render(request, 'chat/chat-room.html')


def check_room(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect(room)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()