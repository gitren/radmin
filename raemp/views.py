from .calendarlib import Calendar

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django_tables2 import SingleTableView

from raemp.tables import *
from .forms import *
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView, ListView
from .models import *

import datetime


# 住所関連Viewクラス

class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = "raemp/location_form.html"

    def get_success_url(self):
        # 成功時にリダイレクトするURL
        return "/raemp/location/table"


class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = "raemp/location_form.html"
    success_url = "/raemp/location/table"  # 成功時にリダイレクトするURL


class LocationDeleteView(DeleteView):
    model = Location
    success_url = "/raemp/location/table"  # 成功時にリダイレクトするURL
    template_name = "raemp/generic_confirm_delete.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # 確認画面のタイトル
        context['form_title'] = '所在地 削除'

        return context


class LocationTableView(SingleTableView):
    model = Location
    table_class = LocationTable

    def get_template_names(self):
        return "raemp/location_table.html"


# 店舗関連Viewクラス

class ShopTableView(SingleTableView):
    model = Shop
    table_class = ShopTable

    def get_template_names(self):
        return "raemp/shop_table.html"


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm
    template_name = "raemp/shop_form.html"
    success_url = "/raemp/shop/table"  # 成功時にリダイレクトするURL


class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = "raemp/shop_form.html"
    success_url = "/raemp/shop/table"  # 成功時にリダイレクトするURL


class ShopDeleteView(DeleteView):
    model = Shop
    success_url = "/raemp/shop/table"  # 成功時にリダイレクトするURL
    template_name = "raemp/generic_confirm_delete.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # 確認画面のタイトル
        context['form_title'] = '店舗 削除'

        return context


# 個人関連Viewクラス

class PersonTableView(SingleTableView):
    model = Person
    table_class = PersonTable

    def get_template_names(self):
        return "raemp/person_table.html"


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "raemp/person_form.html"
    success_url = "/raemp/person/table"  # 成功時にリダイレクトするURL


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "raemp/person_form.html"
    success_url = "/raemp/person/table"  # 成功時にリダイレクトするURL


class PersonDeleteView(DeleteView):
    model = Person
    success_url = "/raemp/person/table"  # 成功時にリダイレクトするURL
    template_name = "raemp/generic_confirm_delete.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # 確認画面のタイトル
        context['form_title'] = '個人 削除'

        return context


# 画像関連Viewクラス

class ImageTableView(SingleTableView):
    model = Image
    table_class = ImageTable

    def get_template_names(self):
        return "raemp/image_table.html"


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm
    template_name = "raemp/image_form.html"
    success_url = "/raemp/image/table"  # 成功時にリダイレクトするURL


class ImageUpdateView(UpdateView):
    model = Image
    form_class = ImageForm
    template_name = "raemp/image_form.html"
    success_url = "/raemp/image/table"  # 成功時にリダイレクトするURL


class ImageDeleteView(DeleteView):
    model = Image
    success_url = "/raemp/image/table"  # 成功時にリダイレクトするURL
    template_name = "raemp/generic_confirm_delete.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # 確認画面のタイトル
        context['form_title'] = '画像 削除'

        return context


# 月間カレンダー関連Viewクラス

class MonthlyCalendarView(TemplateView):
    template_name = 'raemp/calendar.html'

    def get_context_data(self, *args, **kwargs):
        """カレンダーオブジェクトをcontextに追加する."""
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        # /アクセスの場合
        if year is None and month is None:
            date = datetime.datetime.now()

        # yearとmonthの指定がある場合
        elif year and month:
            date = datetime.datetime(
                year=int(year), month=int(month), day=1
            )

        month_html_calendar = Calendar(date).formatmonth()
        context = super().get_context_data(*args, **kwargs)

        # mark_safeでhtmlがエスケープされないようにする
        context['calendar'] = mark_safe(month_html_calendar)
        return context


# 週間カレンダー関連Viewクラス

class WeeklyCalendarView(TemplateView):
    """週間カレンダーのView."""

    template_name = 'raemp/calendar.html'

    def get_context_data(self, *args, **kwargs):
        week = int(self.kwargs.get('week', 1))
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        # /アクセスの場合
        if year is None and month is None:
            date = datetime.datetime.now()

        # yearとmonthの指定がある場合
        elif year and month:
            date = datetime.datetime(
                year=int(year), month=int(month), day=1
            )

        calendar = Calendar(date)
        html = calendar.formatweek_table(week, year, month)

        context = super().get_context_data(*args, **kwargs)
        context['calendar'] = mark_safe(html)
        return context


# シフト関連Viewクラス

class ShiftCreateView(CreateView):
    """シフトの作成ビュー."""

    model = Shift
    form_class = ShiftForm
    template_name = "raemp/calendar_shift.html"

    def form_valid(self, form):
        """シフトの日付に、該当の日付を入れて保存する."""
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.datetime(
            year=int(year), month=int(month), day=int(day))
        schedule = form.save(commit=False)
        schedule.date = date
        schedule.save()
        return render(self.request, 'raemp/calendar_shift_close.html')


class ShiftListView(ListView):
    model = Shift
    template_name = "raemp/calendar_shift_list.html"

    def get_queryset(self):
        """その日付のスケジュールを返す."""
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.datetime(
            year=int(year), month=int(month), day=int(day)
        )
        queryset = Shift.objects.filter(
            date=date
        )
        return queryset


# 派遣要員関連Viewクラス

class TempStaffTableView(SingleTableView):
    model = TempStaff
    table_class = TempStaffTable

    def get_template_names(self):
        return "raemp/generic_table.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # テーブルのタイトル
        context['table_title'] = '派遣要員一覧'
        # 登録先のURL
        context['create_link'] = '/raemp/tempstaff/create'
        # 登録ボタンの名称
        context['create_button_name'] = '新規登録'

        return context


class TempStaffCreateView(PersonCreateView):
    model = TempStaff
    form_class = TempStaffForm
    template_name = "raemp/generic_form.html"
    success_url = "/raemp/tempstaff/table"  # 成功時にリダイレクトするURL

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # フォームのタイトル
        context['form_title'] = '派遣要員 新規登録'
        # formへのjavascriptの追加
        context['form_additional_script'] = ''
        # formへのencryptiontypeの追加
        context['form_enc_type'] = ''

        return context


class TempStaffUpdateView(UpdateView):
    model = TempStaff
    form_class = TempStaffForm
    template_name = "raemp/generic_form.html"
    success_url = "/raemp/tempstaff/table"  # 成功時にリダイレクトするURL

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # フォームのタイトル
        context['form_title'] = '派遣要員 変更'
        # formへのjavascriptの追加
        context['form_additional_script'] = ''
        # formへのencryptiontypeの追加
        context['form_enc_type'] = ''

        return context


class TempStaffDeleteView(DeleteView):
    model = TempStaff
    success_url = "/raemp/tempstaff/table"  # 成功時にリダイレクトするURL
    template_name = "raemp/generic_confirm_delete.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # 確認画面のタイトル
        context['form_title'] = '派遣要員 削除'

        return context
