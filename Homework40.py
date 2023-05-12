from jinja2 import Template


# Задание 1
# menu = [
#     {'href': '/index', 'point': 'Главная'},
#     {'href': '/news', 'point': 'Новости'},
#     {'href': '/about', 'point': 'О компании'},
#     {'href': '/shop', 'point': 'Магазин'},
#     {'href': '/contacts', 'point': 'Контакты'},
# ]
#
# link = """<ul>
# {% for p in menu -%}
#     {% if p.point == 'Главная' -%}
#     <li><a class='active' href='{{p['href']}}'>{{p.point}}</a></li>
#     {% else -%}
#         <li><a href='{{p['href']}}'>{{p.point}}</a></li>
#     {% endif -%}
# {%- endfor -%}
# </ul>"""
#
# tm = Template(link)
# msg = tm.render(menu=menu)
# print(msg)



# Задание 2
# html = """
# {%- macro text_input(type, name, placeholder) -%}
#     <input type="{{type}}" name="{{ name }}" placeholder="{{placeholder}}">
# {%- endmacro -%}
# <p>{{ text_input('text', 'firstname', 'Имя') }}</p>
# <p>{{ text_input('text', 'lastname', 'Фамилия') }}</p>
# <p>{{ text_input('text', 'address', 'Адрес') }}</p>
# <p>{{ text_input('tel', 'phone', 'Телефон') }}</p>
# <p>{{ text_input('email', 'email', 'Почта') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)