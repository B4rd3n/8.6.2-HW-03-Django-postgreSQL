from django import template
import re

from news_portal.models import Category, Subscriber

register = template.Library()

CENSOR_WORDS = {"Удалось", "Если", "Позволить", "СлОжнЫЕ", "сегодня", "стал"}
CENSOR_SET = {word.lower() for word in CENSOR_WORDS}

# Задание 16.2.6
FORBIDDEN_WORDS = {"Слово", "Смотреть", "Рассказывать", "Потому", "Если", "Первые", "Сезон"}
FORBIDDEN_SET = {word.lower() for word in FORBIDDEN_WORDS}


def censor_match(match):
    word = match.group()
    if word.lower() in CENSOR_SET:
        return word[0] + "*" * (len(word) - 1)
    return word


# Этот фильтр цензуры используется для post.text в news.html
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


# Задание 16.2.6 Этот фильтр цензуры используется для post.title в news.html
@register.filter
def new_censor(value):
    words = value.split(" ")
    for key, word in enumerate(words):
        if word.lower() in FORBIDDEN_SET:
            if len(word) <= 2:
                new_word = "*" * len(word)
            else:
                new_word = word[0] + "*" * (len(word) - 2) + word[-1]
            words.pop(key)
            words.insert(key, new_word)

    result = " ".join(words)
    return result







