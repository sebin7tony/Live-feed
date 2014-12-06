from app import DL_models

#
#		||||||||| Data layer implementation for sqlite database ||||||||||||||
#

# Get all list of post from the database.
def get_all_posts():
	posts = DL_models.Post.query.all()
	return posts

# Get all list of comments from the database
def get_all_comments():
	comments = DL_models.Comment.query.all()
	return comments

#Get all list of users from the database
def get_all_users():
	users = DL_models.User.query.all()
	return users

#Get all the coloumn name in the Post table
def get_posts_column_names():
	columnNames = DL_models.Post.__table__.columns.keys()
	return columnNames