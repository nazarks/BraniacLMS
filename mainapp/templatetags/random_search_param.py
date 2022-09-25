import random

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def random_search_param(value):
    """
    Функция принимает текст и возвращает его, заменяя рандомные слова ссылками где эти слова являются get параметрами
    :max_len - всего количество слов для выборки с начала текста
    :default_count_words - сколько слов надо выбрать
    Если длина текста недостаточна, количество слов будет уменьшено
    :return: mark_safe(output_string)
    """
    max_len = 15
    default_count_words = 5
    count_words = len(value.split())

    if count_words < max_len:
        max_len = count_words
    param_list = random.sample(
        value.split()[: max_len - 1], count_words - 1 if count_words < default_count_words else default_count_words
    )

    output_string = ""
    for word in value.split():
        if word in param_list:
            word = f"<a href='https://www.google.com/search?q={word}' target='_blank'>{word}</a>"
        output_string += word + " "

    return mark_safe(output_string)
