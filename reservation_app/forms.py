from django import forms
from .models import Room, RoomReservation


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"


# class ReserveRoomForm(ModelForm):
#     class Meta:
#         model = RoomReservation
#         fields = ['date', 'description']


# class ReserveRoomForm(forms.Form):
#     date = forms.DateField(widget=forms.SelectDateWidget)
#     description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}))
