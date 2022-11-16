from django.urls import path

from t4t.chat.views import chat_start, chat_room, check_room

urlpatterns = [
    path('start-chat/', chat_start, name='chat start'),
    path('<str:room>/', chat_room, name='chat room'),
    path('check-room', check_room, name='check room'),

]
