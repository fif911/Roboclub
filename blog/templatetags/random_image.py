import random
from django import template

register = template.Library()

@register.simple_tag
def random_im(num):
    Wlist= ['home/pic/news_1.jpg', 'home/pic/news_2.jpg', 'home/pic/news_3.jpg', 'home/pic/news_4.jpg']

    return random.choice(Wlist)
