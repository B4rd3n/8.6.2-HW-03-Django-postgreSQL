from django import template
import re

register = template.Library()

CENSOR_WORDS = {"Удалось", "Если", "Позволить", "СлОжнЫЕ", "сегодня", "стал"}
CENSOR_SET = {word.lower() for word in CENSOR_WORDS}


def censor_match(match):
    word = match.group()
    if word.lower() in CENSOR_SET:
        return word[0] + "*" * (len(word) - 1)
    return word


@register.filter
def censor(value):
    if not isinstance(value, str):
        raise TypeError("value must be a string")

    return re.sub(r'\b\w+\b', censor_match, value)


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


