from django import template
from datetime import date
from django.contrib.auth.models import Group , User

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    # Super usuario é sempre permitido !
    if user.is_superuser:
        return True
    return user.groups.filter(name__contains=group_name).exists()

@register.filter(valid_date='valid_warning')
def valid_warning(valid_date):
    list_warning =  [5,6,7,8,9,10]

    diff_off_days = valid_date - date.today()
    if diff_off_days.days in list_warning:
        return True
    else:
        return False


@register.filter(name='valid_danger')
def valid_danger(valid_date):
    list_danger =  [4,3,2,1,0, -1,-2,-3,-4,-5]

    diff_off_day = valid_date - date.today()
    if diff_off_day.days in list_danger:
        return True
    else:
        return False

@register.filter(name='valid_success')
def valid_success(valide_date):
    diff_of_days = valide_date -  date.today()
    if diff_of_days.days > 5:
        return True
    else:
        return False