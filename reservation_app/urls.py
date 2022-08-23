from django.urls import path
from .views import (
    AddRoomView,
    ListRoomsView,
    DeleteRoomView,
    ModifyRoomView,
    ReserveRoomView,
    RoomDetailsView,
)

urlpatterns = [
    path('home/', ListRoomsView.as_view(), name="main_page"),
    path('room/new/', AddRoomView.as_view(), name="add_room"),
    path('room/delete/<int:id>/', DeleteRoomView.as_view(), name="delete_room"),
    path('room/modify/<int:id>/', ModifyRoomView.as_view(), name="modify_room"),
    path('room/reserve/<int:id>/', ReserveRoomView.as_view(), name="reserve_room"),
    path('room/details/<int:id>/', RoomDetailsView.as_view(), name="details_room"),
]
