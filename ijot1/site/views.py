from flask import render_template, url_for, request,g,redirect,flash,session
from ijot1 import db,ma
from ijot1.models import  User,Notes,note_schema
from functools import wraps
from . import sitemod
import os


"""@sitemod.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']"""

def login_required(f):
	@wraps(f)
	def function(*args,**kwargs):
		g.user = None
		if 'user' in session:
			g.user = session['user']
			current_user = g.user
			return f(current_user,*args,**kwargs)
		else:
			session['error'] = "Log in to access this service"
			return redirect(url_for('site.signin'))
	return function

@sitemod.route('/')
@sitemod.route('/index')
def index():
	return render_template('index.html')

@sitemod.route('/signup',methods=['GET','POST'])
def signup():
	if request.method == 'POST':
		# fetch data 
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']

		new_user = User(name=name,email=email,password=password)

		db.session.add(new_user)
		db.session.commit()
	return render_template('signup.html')

# user login
@sitemod.route('/signin',methods=['GET','POST'])
def signin():
	if request.method == 'POST':
		email = request.form['email']
		user = User.query.filter_by(email=email).first()
		if user != None:
			password = user.password
			if request.form['password'] == password:
				session['user'] = request.form['email']
				username = user.name
				return redirect(url_for('site.dashboard'))
			else:
				error='Password incorrect - forgot password?'
				return render_template('signup.html')
		else:
			error = 'No user with that email was found'
			return render_template('signup.html',error=error)
	if session['error']:
		return render_template('signup.html',error=session['error'])
	else:
		return render_template('signup.html'),200

@sitemod.route('/dashboard')
@login_required
def dashboard(current_user):
	if g.user:
		usermail = session['user']
		username = User.query.filter_by(email=usermail).first().name
		user_id = User.query.filter_by(email=usermail).first().id
		# check if user has notes
		data = Notes.query.filter_by(user_id=user_id).all()
		if len(data) > 0:
			notes = data
			return render_template('dashboard.html',username=username,notes=notes)
		else:
			error = "You haven't added any note yet"
			return render_template('dashboard.html',username=username,error=error)
	else:
		return redirect(url_for('site.signup'))

@sitemod.route('/note',methods=['GET','POST'])
@login_required
def note(current_user):
	data = request.get_json('id')
	id = int(data['id'])
	note = Notes.query.get(id)
	return redirect(url_for('fullfeat',note=note))
		

@sitemod.route('/logout')
@login_required
def logout(current_user):
	session.pop(current_user,None)
	
	return redirect(url_for('site.signup'))

@sitemod.route('/new_note',methods=['GET','POST'])
@login_required
def new_note(current_user):
	if request.method == 'POST':
		if g.user:
			title = request.form['note-title']
			body = request.form['note-body']
			user_id = User.query.filter_by(email=g.user).first().id
			note = Notes(title=title,body=body,user_id=user_id)
			
			# fetch the note for display
			db.session.add(note)
			db.session.commit()


	return redirect(url_for('site.dashboard'))

@sitemod.route('/get_note/<id>',methods=['GET','POST'])
@login_required
def get_note(current_user,id):
	note = Notes.query.get(id)
	return render_template('notepage.html')