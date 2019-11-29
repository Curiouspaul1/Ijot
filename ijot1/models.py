from ijot1 import db,ma

class User(db.Model):
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	name = db.Column(db.String(100))	
	email = db.Column(db.String(200))
	password = db.Column(db.String(100))
	notes = db.relationship('Notes',backref='author')


class Notes(db.Model):
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	title = db.Column(db.String(100))
	body = db.Column(db.Text())
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

# User Schema
class UserSchema(ma.Schema):
	class Meta:
		fields = ('id','name','email','password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Note Schema
class NoteSchema(ma.Schema):
	class Meta:
		fields = ('id','title','body')

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)