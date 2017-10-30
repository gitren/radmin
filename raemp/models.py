from django.db import models

#住所
class Location(models.Model):
    #郵便番号
    zip_code = models.CharField(verbose_name="郵便番号", max_length=10)
    #都道府県
    pref = models.CharField(verbose_name="都道府県", max_length=20)
    #市区群町村
    city = models.CharField(verbose_name="市区群町村", max_length=20)
    #住所１
    address1 = models.CharField(verbose_name="住所１", max_length=20)
    #住所２
    address2 = models.CharField(verbose_name="住所２", max_length=20)
    #建物等
    bld = models.CharField(verbose_name="建物等", max_length=20, blank=True)

    def __str__(self):
        return self.pref + ' ' + self.city + ' ' + self.address1 + ' ' + self.address2 + ' ' + self.bld


#人
class Person(models.Model):

    # 名前漢字
    f_name_kanji = models.CharField(max_length=20)
    # 姓漢字
    s_name_kanji = models.CharField(max_length=20)
    # 名前カナ
    f_name_kana = models.CharField(max_length=20)
    # 姓カナ
    s_name_kana = models.CharField(max_length=20)

    def __str__(self):
        return self.s_name_kanji + self.f_name_kanji

# 店舗
class Shop(models.Model):
    # 店舗名称漢字
    shop_name_kanji = models.CharField(verbose_name="店舗名称（漢字）", max_length=20)
    # 店舗名称カナ
    shop_name_kana = models.CharField(verbose_name="店舗名称（カナ）", max_length=20)
    # 店舗住所
    shop_address = models.ForeignKey(Location, verbose_name="住所")



#店舗従業員
class Employee(Person):
    #所属店舗
    shop_id = models.ForeignKey(Shop)

#派遣要員
class TempStaff(Person):
    #自宅住所
    home_address = models.ForeignKey(Location)


