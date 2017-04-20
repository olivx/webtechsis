from django import template
from django.contrib.auth.models import Group , User

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    # Super usuario é sempre permitido !
    if user.is_superuser:
        return True
    return user.groups.filter(name__contains=group_name).exists()

