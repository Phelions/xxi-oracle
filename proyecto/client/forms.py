from django import forms
from manager.models import Mesa, Reserva
# class ReservaForm(forms.ModelForm):
#     class Meta:
#         model = Reserva
#         fields = ['fecha', 'hora', 'mesa', 'cliente']
#         widgets = {
#             'fecha': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
#             'hora': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
#             'mesa': forms.Select(attrs={'class':'form-control'}),
#             'cliente': forms.Select(attrs={'class':'form-control'}),
#         }

class ReservaForm(forms.ModelForm):
    class Meta:
        
        model = Reserva
        fields = ['fecha', 'hora', 'mesa', 'cliente']
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'hora': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'mesa': forms.Select(attrs={'class':'form-control'}),
            'cliente': forms.Select(attrs={'class':'form-control'}),
        }
        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'mesa': 'Mesa',
            'cliente': 'Cliente',
        }