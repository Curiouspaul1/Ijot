from flask import Blueprint, render_template, url_for, request,g,redirect,flash,session
from ijot1 import db, ma,app
from ijot1.models import  User,Notes,note_schema
import os

sitemod = Blueprint('site', __name__, template_folder='templates')


@sitemod.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']

@sitemod.route('/index') 
def index():
	return render_template('index.html')

@sitemod.route('/signup',methods=['GET','POST'])
def signup():
	session.pop('user',None)
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
		session.pop('user',None)
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

	return render_template('signup.html')

@sitemod.route('/dashboard')
def dashboard():
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


@sitemod.route('/logout')
def logout():
	session.pop('user',None)
	
	return redirect(url_for('site.signup'))

@sitemod.route('/new_note',methods=['GET','POST'])
def new_note():
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
def get_note(id):
	note = Notes.query.get(id)
	return render_template('notepage.html')