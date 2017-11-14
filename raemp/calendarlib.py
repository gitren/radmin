"""カレンダーを作成するためのモジュール."""
from calendar import month_name, monthrange, LocaleHTMLCalendar
import datetime
from django.shortcuts import resolve_url
from .models import Shift

DAY_HTML = """\
<td class="{css_class}">
    <a href="javascript:void(0);" \
    onclick="window.open('{open_url}','subwin','width=500,height=500');">
        {day}
    </a>
    {shift_html}
</td>
"""

SCHEDULE_LINK_AND_NUM = """\
<a href="{shift_link}">
    <span class="badge badge-primary">+{shift_num}</span>
</a>
"""


def create_day_html(year, month, day, css_class):
    """カレンダーの日付部分のhtmlを作成する.

    引数:
        year: 年
        month: 月
        day: 日
        css_class: 日付部分のhtmlに与えたいcssのクラス

    返り値:
        日付部分のhtml。具体的にはDAY_HTMLに変数を埋め込んだ文字列

    """
    date = datetime.datetime(
        year=year, month=month, day=day
    )
    all_count = Shift.objects.filter(
        date=date
    ).count()
    if all_count:
        shift_link_and_num = SCHEDULE_LINK_AND_NUM.format(
            shift_link=resolve_url(
                'raemp:shift_list',
                year=year, month=month, day=day
            ),
            shift_num=all_count
        )
    else:
        shift_link_and_num = ''

    return DAY_HTML.format(
        css_class=css_class,
        open_url=resolve_url('raemp:shift_create',
                             year=year, month=month, day=day),
        day=day,
        shift_html=shift_link_and_num
    )


def prev_or_next_url(date, num, title):
    """前月、次月へのリンクとなるhtmlを作成する.

    引数:
        date: datetime.datetimeオブジェクト。増減の基準となる日付を渡す
        num: 増減の数字。1月後は1、1月前は-1
        title: リンクとして表示される文字列。prev、next、前月、など

    返り値:
        '<a href={url}>{title}</a>'に変数を埋め込んだ文字列

    """

    date = add_months(date, num)
    url = resolve_url(
        'raemp:monthlycalendar',
        year=date.year,
        month=date.month,
    )
    return '<a href={url}>{title}</a>'.format(url=url, title=title)


def add_months(date, num):
    """datetimeオブジェクトに月を加算・減算する.

    引数:
        date: datetime.datetimeオブジェクト。増減の基準となる日付を渡す
        num: 増減の数字。1月後は1、1月前は-1

    返り値:
        n月後、n月前のawareなdatetimeオブジェクト

    """
    month = date.month - 1 + num
    year = int(date.year + month / 12)
    month = month % 12 + 1
    day = min(date.day, monthrange(year, month)[1])
    date = datetime.datetime(year=year, month=month, day=day)
    return date


class Calendar(LocaleHTMLCalendar):
    def __init__(self, date, firstweekday=0, locale=None):
        super().__init__(firstweekday, locale)
        self.date = date

    def formatday(self, day, weekday):
        """tableタグの日付部分のhtmlを作成する<td>...</td>."""

        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            day_html = create_day_html(
                self.date.year, self.date.month, day,
                self.cssclasses[weekday]
            )
            return day_html

    def formatmonthname(self, theyear, themonth, withyear=True):
        """tableタグの一番上、タイトル部分にあたるhtmlを作成する."""
        if withyear:
            # s = '%s %s' % (month_name[themonth], theyear)
            s = '%s %s' % (str(theyear) + "年", str(themonth) + "月")
        else:
            # s = '%s' % month_name[themonth]
            s = '%s' % str(themonth) + "月"
        prev_a_tag = prev_or_next_url(self.date, -1, '前へ')
        next_a_tag = prev_or_next_url(self.date, 1, '次へ')
        return '<tr><th colspan="7" class="month">{} {} {}</th></tr>'.format(
            prev_a_tag, s, next_a_tag
        )

    def formatmonth(self, theyear=None, themonth=None, withyear=True):
        """月のカレンダーを作成する."""
        if theyear is None:
            theyear = self.date.year
        if themonth is None:
            themonth = self.date.month
        v = []
        a = v.append
        a('<table class="month table">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

    def formatweek_table(self, week_index, year=None, month=None):
        """週間カレンダーを作成する."""
        if year is None and month is None:
            now = datetime.datetime.now()
        elif year and month:
            now = datetime.datetime(year=int(year), month=int(month), day=1)

        v = []
        a = v.append
        a('<table class="table week-table">')
        weeks = self.monthdays2calendar(now.year, now.month)
        now_week = weeks[week_index - 1]

        # 前週・次週の部分
        a('<tr>')
        a('<th colspan="7">')

        # 前月へのリンクを作る
        pre_date = add_months(now, -1)
        url = resolve_url(
            'raemp:weeklycalendar', year=pre_date.year,
            month=pre_date.month, week=1
        )
        a("<a href={0}>前月</a> ".format(url))

        # 1週目じゃなければ、前週のリンクを作る
        if week_index != 1:
            url = resolve_url(
                'raemp:weeklycalendar', year=now.year,
                month=now.month, week=week_index - 1
            )
            a("<a href={0}>前週</a> ".format(url))

        # 最後の週じゃなければ、次週へのリンクを作る
        if week_index != len(weeks):
            url = resolve_url(
                'raemp:weeklycalendar', year=now.year,
                month=now.month, week=week_index + 1
            )
            a("<a href={0}>次週</a> ".format(url))

        # 次月へのリンクを作る
        next_date = add_months(now, 1)
        url = resolve_url(
            'raemp:weeklycalendar', year=next_date.year,
            month=next_date.month, week=1
        )
        a("<a href={0}>次月</a> ".format(url))

        a('</th>')
        a('</tr>')

        a(self.formatweekheader())

        # 〜日 のヘッダー部分
        a('<tr>')
        for day, index in now_week:
            a('<th>')
            if day != 0:
                day_title = '{0}月{1}日'.format(now.month, day, )
                a(day_title)
            a('</th>')
        a('</tr>')

        # メインのスケジュール部分
        for day, index in now_week:
            a('<td>')
            if day != 0:
                date = datetime.datetime(
                    year=now.year, month=now.month, day=day
                )
                shifts = Shift.objects.filter(date=date)

                for shift in shifts:
                    a('★')
                    a(shift.notes)
                    a('<br>')
            a('</td>')

        a('</table>')
        return ''.join(v)
