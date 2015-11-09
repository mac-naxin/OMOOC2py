from bottle import Bottle
from bottle import route, run, debug
from jinja2 import Environment, FileSystemLoader

# _*_ coding:utf-8 _*_

app = Bottle(__name__)

env = Environment(loader=FileSystemLoader('./templates'))
tmpl_diary = env.get_template('home.html')


@app.route('/', methods =['GET', 'POST'])  
def dairy():
	return tmpl_diary.render()



if __name__ == '__main__':
	debug(True)
	app.run(host="localhost", port=8080, reloader=True)