from django import forms


class ClientAddForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=300)


class ClientUpdateForm(forms.Form):
    pk = forms.IntegerField(min_value=1)
    name = forms.CharField(min_length=3, max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=300)


class ProductAddForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(min_value=0.0, decimal_places=2)
    amount = forms.IntegerField(min_value=0)
    photo = forms.ImageField()


class ProductUpdateForm(forms.Form):
    pk = forms.IntegerField(min_value=1)
    title = forms.CharField(min_length=3, max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(min_value=0.0, decimal_places=2)
    amount = forms.IntegerField(min_value=0)
    photo = forms.ImageField()
