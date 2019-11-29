from flask import Blueprint,render_template,request
from ijot1.models import User,user_schema,users_schema

apimod = Blueprint('api',__name__,template_folder='templates')

@apimod.route('/index',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		# fetch data 
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']

		new_user = User(name=name,email=email,password=password)

		return user_schema.jsonify(new_user)

	return render_template('index.html')