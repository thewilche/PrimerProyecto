from django import forms

class Juegos_form(forms.Form):
    titulo=forms.CharField(max_length=60)
    lanzamiento=forms.DateField()
    genero=forms.CharField(max_length=20)