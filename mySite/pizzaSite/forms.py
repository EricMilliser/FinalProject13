from django import forms
from django.forms import modelformset_factory
from .models import Order, Pizza, Topping, Review



class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'text',)


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'panType', 'sauce', 'toppings']
    
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all(), widget=forms.CheckboxSelectMultiple)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name',)
        exclude = ['price']



        





class ToppingsForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['type', 'name', 'isAvailable']


PizzaFormSet = modelformset_factory( Pizza, form=PizzaForm, extra=1)

        