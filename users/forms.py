from django import forms
from pantry_trackr.models import PantryItem

class PantryItemForm(forms.ModelForm):
    class Meta:
        model = PantryItem
        # fields = ['item_name', 'quantity_min', 'quantity_now']
        fields = "__all__"



# from django import forms

# class PantryForm(forms.Form):
#     item_name = forms.CharField(max_length=30)
#     quantity_min = forms.IntegerField()
#     quantity_now = forms.IntegerField()