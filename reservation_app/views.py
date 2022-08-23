from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import ValidationError
from .forms import AddRoomForm
from django.views import View
from .models import Room, RoomReservation
from datetime import date


class AddRoomView(View):
    def get(self, request):
        return render(request, "add_room.html", {"form": AddRoomForm()})

    def post(self, request):
        room_form = AddRoomForm(request.POST)
        if room_form.is_valid():
            room_form.save()
            return redirect("main_page")
        return render(request, "add_room.html", {"form": room_form})  # notatka o przechowywaniu błędów w instancji


class ListRoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()

        for room in rooms:
            if RoomReservation.objects.filter(date=date.today()).filter(room=room):
                room.reserved = True
            else:
                room.reserved = False
        return render(request, "rooms.html", {"rooms": rooms})


class DeleteRoomView(View):
    def get(self, request, id):
        room = get_object_or_404(Room, id=id)
        room.delete()
        return redirect("main_page")


class ModifyRoomView(View):
    def get(self, request, id):
        room = get_object_or_404(Room, id=id)
        return render(request, "add_room.html", {"form": AddRoomForm(instance=room)})

    def post(self, request, id):
        room = get_object_or_404(Room, id=id)
        room_form = AddRoomForm(request.POST, instance=room)
        if room_form.is_valid():
            room_form.save()
            return redirect("main_page")
        return render(request, "add_room.html", {"form": room_form})  # notatka o przechowywaniu błędów w instancji


class ReserveRoomView(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        reservations = RoomReservation.objects.filter(room=room).filter(date__gte=date.today()).order_by("date")
        return render(request, "reserve_room.html", {"room": room, "reservations": reservations})

    def post(self, request, id):
        room = Room.objects.get(id=id)
        reservation_date = request.POST["reservation-date"]
        desc = request.POST["comment"]

        try:
            if RoomReservation.objects.filter(room=room, date=reservation_date):
                return render(request, "reserve_room.html", {"room": room, "error": "Room already reserved!"})
        except ValidationError:
            return render(request, "reserve_room.html", {"room": room, "error": "You need to provide a date"})
        if date.fromisoformat(reservation_date) < date.today():
            return render(request, "reserve_room.html", {"room": room, "error": "Cannot reserve room in the past!"})
        RoomReservation.objects.create(room=room, date=reservation_date, description=desc)
        return redirect('main_page')


class RoomDetailsView(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        reservations = RoomReservation.objects.filter(room=room).filter(date__gte=date.today()).order_by("date")
        return render(request, "room_details.html", {"room": room, "reservations": reservations})
