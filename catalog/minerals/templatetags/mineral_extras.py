import random
import string

from django import template


register = template.Library()


@register.simple_tag
def random_mineral():
    return random.randint(1,873)


@register.simple_tag
def categories():
    return ['Silicate', 'Oxide', 'Sulfate', 'Sulfide', 'Carbonate', 'Halide',
           'Sulfosalt', 'Phosphate', 'Borate', 'Organic', 'Arsenate', 'Native',
           'Other']


@register.simple_tag
def alphabet():
    return list(string.ascii_uppercase)


@register.simple_tag
def colors():
    return ['red', 'green','brown', 'blue', 'yellow', 'orange', 'purple']
