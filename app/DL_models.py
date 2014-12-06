from app import db

#
#   |||||||||||   Data Layer models |||||||||||||
#


#This is the model responsible for storing the
#posts in a persistent way.

class Post(db.Model):
	__tablename__ = 'post'
	__table_args__ = {'extend_existing':True}
	postid = db.Column(db.Integer,primary_key=True)
	post = db.Column(db.String(64))
	date = db.Column(db.DateTime)
	lat = db.Column(db.Integer)
	lon = db.Column(db.Integer)
	likes = db.Column(db.Integer)
	userid = db.Column(db.Integer,db.ForeignKey('user.userid'))
	comments = db.relationship('Comment',backref="parent_post",lazy="dynamic")


# This model is responsible for storing the User
# in a persistent way

class User(db.Model):
	userid = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(30))
	email = db.Column(db.String(20))
	userImage = db.Column(db.String(40))
	posts = db.relationship('Post',backref="author",lazy='dynamic')


# This model is responsible for storing the Comment
# in a persistent way

class Comment(db.Model):
	commentid = db.Column(db.Integer,primary_key=True)
	comment = db.Column(db.String(120))
	date = db.Column(db.DateTime)
	postid = db.Column(db.Integer,db.ForeignKey('post.postid'))


	
