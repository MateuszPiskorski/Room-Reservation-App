from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    capacity = models.PositiveSmallIntegerField()
    projector = models.BooleanField(default=False)


class RoomReservation(models.Model):
    date = models.DateField(blank=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room")
    description = models.TextField(max_length=1000, null=True)

    class Meta:
        unique_together = ('date', 'room')
