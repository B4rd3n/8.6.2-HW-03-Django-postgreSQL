from django import template
import re

from news_portal.models import Category, Subscriber

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


@register.filter(name='is_subscribed')
def is_subscribed(user):
    categories = Category.objects.count()
    subscribed = Subscriber.objects.filter(user_sub=user).count()
    return subscribed == categories





