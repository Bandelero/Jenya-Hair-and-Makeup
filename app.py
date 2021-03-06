from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import requests
import os

app = Flask(__name__)

api_key = os.environ.get('sg')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
	# print('inside the form')
	# if request.method == 'POST':
	# 	k = requests.post('https://send.pageclip.co/WgweLLKyi7U0cg1fV936HzFOprgnSV3d', data = {'first_name':request.form["first"]}, auth=('gc4m9GRg7dvKTwcag98QydKwEAlp6Cdi', 'gc4m9GRg7dvKTwcag98QydKwEAlp6Cdi'))
	# 	print('k', k)
		#https://send.pageclip.co/w4fienCjC132otdR43gKyNmmWZM7ZRmC
		# print(request.form)
		# try:
		# 	message = Mail(
		# 	from_email='apetermz@gmail.com',
		# 	to_emails='apetermz@gmail.com',
		# 	subject='Jenyas Hair and Makeup Client Submission',
		# 	html_content=f'{request.form["first"]} {request.form["last"]} {request.form["phone"]} <br> {request.form["email"]} {request.form["event"]} {request.form["danceCategory"]} <br> {request.form["Hair"]} {request.form["Makeup"]}')
		# 	sg = SendGridAPIClient(api_key)
		# 	response = sg.send(message)
		# 	print(response.status_code)
		# 	print(response.body)
		# 	print(response.headers)
		# except Exception as e:
		#     print(e.message)
		# return redirect(url_for('thankyou.html'))
		# return render_template('thankyou.html', first=request.form.first, last=request.form.last, email=request.form.email)
	return render_template('form.html')
#temporary
@app.route('/thankyou')
def thankyou():
	first = request.args.get('first')
	last = request.args.get('last')
	email = request.args.get('email')

	return render_template('thankyou.html', first=first, last=last, email=email)

@app.route('/services')
def services():
	return render_template('services.html')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

@app.route('/events')
def events():
	return render_template('events.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


if __name__ == '__main__':
	app.run()