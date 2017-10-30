from django import forms
from .models import Location, Shop


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

        fields = ("zip_code", "pref", "city", "address1", "address2", "bld")

        labels = {
            'zip_code': ('郵便番号(ハイフンなし)'),
            'pref': ('都道府県'),
            'city': ('市区群町村'),
            'address1': ('住所１'),
            'address2': ('住所２'),
            'bld': ('建物等'),
        }


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop

        fields = ("shop_name_kanji", "shop_name_kana", "shop_address")

        labels = {
            'shop_name_kanji': ('店舗名称（漢字）'),
            'shop_name_kana': ('店舗名称（カナ）'),
            'shop_address': ('店舗住所（漢字）'),
        }
