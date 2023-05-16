from jinja2 import FileSystemLoader
from jinja2 import Environment

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template("main.html")
msg = tm.render()

print(msg)

