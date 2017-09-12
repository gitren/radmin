from django import forms
from .models import Location


class LocationForm(forms.ModelForm):

    zip_code = forms.RegexField(
        label='郵便番号(ハイフンなし)',
        regex=r'^[0-9]+$',
        max_length=7,
        widget=forms.TextInput(
            attrs={'onKeyUp': "AjaxZip3.zip2addr('zip_code','','pref','city','address1','address2')"}),
    )

    class Meta:
        model = Location

        fields = ("zip_code","pref","city","address1","address2","bld")

        labels = {
            'zip_code': ('郵便番号(ハイフンなし)'),
            'pref': ('都道府県'),
            'city': ('市区群町村'),
            'address1': ('住所１'),
            'address2': ('住所２'),
            'bld': ('建物等'),
        }


