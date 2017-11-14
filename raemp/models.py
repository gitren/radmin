import uuid
import os
from django.db import models
from datetime import datetime
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


# 住所
class Location(models.Model):
    # 郵便番号
    zip_code = models.CharField(verbose_name="郵便番号", max_length=10)
    # 都道府県
    pref = models.CharField(verbose_name="都道府県", max_length=20)
    # 市区群町村
    city = models.CharField(verbose_name="市区群町村", max_length=20)
    # 住所１
    address1 = models.CharField(verbose_name="住所１", max_length=20)
    # 住所２
    address2 = models.CharField(verbose_name="住所２", max_length=20)
    # 建物等
    bld = models.CharField(verbose_name="建物等", max_length=20, blank=True)
    # 作成日
    created_at = models.DateField(verbose_name="作成日", default=datetime.now)
    # 更新日
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return self.pref + ' ' + self.city + ' ' + self.address1 + ' ' + self.address2 + ' ' + self.bld


# 個人
class Person(models.Model):
    # 姓漢字
    s_name_kanji = models.CharField(verbose_name="姓（漢字）", max_length=20)
    # 名前漢字
    f_name_kanji = models.CharField(verbose_name="名前（漢字）", max_length=20)
    # 姓カナ
    s_name_kana = models.CharField(verbose_name="姓（カナ）", max_length=20)
    # 名前カナ
    f_name_kana = models.CharField(verbose_name="名前（カナ）", max_length=20)
    # 住所
    person_address = models.ForeignKey(Location, verbose_name="住所", default=None)
    # 作成日
    created_at = models.DateField(verbose_name="作成日", default=datetime.now)
    # 更新日
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return self.s_name_kanji + self.f_name_kanji


# 店舗
class Shop(models.Model):
    # 店舗名称漢字
    shop_name_kanji = models.CharField(verbose_name="店舗名称（漢字）", max_length=20)
    # 店舗名称カナ
    shop_name_kana = models.CharField(verbose_name="店舗名称（カナ）", max_length=20)
    # 店舗住所
    shop_address = models.ForeignKey(Location, verbose_name="住所", default=None)
    # 作成日
    created_at = models.DateField(verbose_name="作成日", default=datetime.now)
    # 更新日
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return self.shop_name_kanji


# 店舗従業員
class Employee(Person):
    # 所属店舗
    shop_id = models.ForeignKey(Shop)


# 派遣要員
class TempStaff(Person):
    # RANK
    RANK_CHOICES = (
        ('S', 'Sランク'),
        ('A', 'Aランク'),
        ('B', 'Bランク'),
        ('C', 'Cランク'),
        ('D', 'Dランク'),
        ('E', 'Eランク'),
    )
    # RANK
    rank_type = models.CharField(verbose_name="ランク", max_length=1, choices=RANK_CHOICES, default=None)


# 写真
class Image(models.Model):
    def get_image_path(self, filename):
        """カスタマイズした画像パスを取得する.

        :param self: インスタンス (models.Model)
        :param filename: 元ファイル名
        :return: カスタマイズしたファイル名を含む画像パス
        """
        prefix = 'photos/'
        name = str(uuid.uuid4()).replace('-', '')
        extension = os.path.splitext(filename)[-1]
        return prefix + name + extension

    # 畫像種類
    IMAGE_TYPE_CHOICES = (
        ('0', '写メ'),
        ('1', '証明書'),
    )
    image_type = models.CharField(verbose_name="画像種類", max_length=1, choices=IMAGE_TYPE_CHOICES, default=None)
    # イメージファイル
    image_file = models.ImageField(verbose_name="画像ファイル", upload_to=get_image_path, default=None)

    # 大サイズ
    big = ImageSpecField(source="image_file",
                         processors=[ResizeToFill(1280, 1024)],
                         format='JPEG'
                         )

    # サムネイル
    thumbnail = ImageSpecField(source='image_file',
                               processors=[ResizeToFill(250, 250)],
                               format="JPEG",
                               options={'quality': 60}
                               )

    # 中サイズ
    middle = ImageSpecField(source='image_file',
                            processors=[ResizeToFill(600, 400)],
                            format="JPEG",
                            options={'quality': 75}
                            )

    # 小サイズ
    small = ImageSpecField(source='image_file',
                           processors=[ResizeToFill(75, 75)],
                           format="JPEG",
                           options={'quality': 50}
                           )

    # 作成日
    created_at = models.DateField(verbose_name="作成日", default=datetime.now)
    # 更新日
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)


# 派遣要員写真
class TempStaffImage(Image):
    # 派遣要員ID
    tempstaff_id = models.ForeignKey(TempStaff)


# シフト
class Shift(models.Model):
    # 日付
    date = models.DateField(verbose_name="日付")
    # シフト対象店舗ID
    shop_id = models.ForeignKey(Shop, verbose_name="対象店舗")
    # シフト対象要員ID
    staff_id = models.ForeignKey(TempStaff, verbose_name="対象要員")
    # 備考
    notes = models.TextField(max_length=100)
    # 作成日
    created_at = models.DateField(verbose_name="作成日", default=datetime.now)
    # 更新日
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)
