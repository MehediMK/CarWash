from django import template

register = template.Library()


@register.filter(name='checkpath')
def check_path(path):
    data = path.split('/')
    # print(data[-2])
    return data[-2]

# filter .899 from 344.899
@register.filter(name='adecimalplace')
def decimalplace(number):
    num = str(number)
    # print(num[-3:])
    return num[-3:]

# filter 344 from 344.899
@register.filter(name='bdecimalplace')
def bdecimalplace(number):
    num = str(number)
    # print(num[-3])
    return num[:-3]


from django.utils.safestring import mark_safe
import markdown
# filter used for post link and list
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

    
