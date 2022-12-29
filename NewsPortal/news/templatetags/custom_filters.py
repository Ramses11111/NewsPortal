from django import template

register = template.Library()

bad_words = [
    'редиска',
    'сосиска',
    'навухудоносор',
    'гамбурский',
    'моргалы',
]

@register.filter(name="censor")
def censor(value):
    if not isinstance(value, str):
        raise TypeError(f"Ошибка: переменная {value} должна быть строкой")
    for bw in value.split():
        if bw.lower() in bad_words:
            value = value.replace(bw, list(bw)[0] + ((len(bw) - 1) * "*"))
    return value