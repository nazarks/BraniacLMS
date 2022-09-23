from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def user_date_time(value):
    return mark_safe(f'<script>document.write(new Date("{value}").toLocaleString());</script>')
