
from app import DL_impl,SL_models

# 
# |||||||||||   This is the module used for implementations in the service layer ||||||||||||||||
#

# getting all the posts from the DL layer and wrapping it in SL model classes so that it can get 
# the perfect structre of the json that we need.
def get_all_posts():

	posts = DL_impl.get_all_posts()
	if posts is not None:
		PL_post_model = []  
		key = []                             # List of SL models for stroing the different posts.
		for post in posts:
			comments = post.comments.all()               # post.comments provides an appenderQuery of sqlAlchemy,So we need to call ".all()" 
														 # for running that query and the results is stored temporary in comments. 
			
			p = SL_models.Post(post.postid,post.post,
					post.date,post.lat,post.lon,post.likes,
					post.author.userid,comments)

			PL_post_model.append(p)

		return PL_post_model
	else:
		return null
	
	
# Getting the table names of the Post table 
def get_Post_table_headers():
	header = DL_impl.get_posts_column_names()
	return {"header" : header}

# getting all the comments from the DL layer and wrapping it in SL model classes so that it can get 
# the perfect structre of the json that we need.
def get_all_comments():

	comments = DL_impl.get_all_comments()
	if comments is not None:
		PL_comment_model = []
		for comment in comments:
			c = SL_models.Comment(comment.commentid,
					comment.comment,comment.date,comment.parent_post.postid)
			PL_comment_model.append(c)

		return PL_comment_model
	else:
		return null

# getting all the users from the DL layer and wrapping it in SL model classes so that it can get 
# the perfect structre of the json that we need.
def get_all_users():

	users = DL_impl.get_all_users()
	if users is not None:
		PL_user_model = []
		for user in users:
			u = SL_models.User(user.userid,user.username,user.email,user.userImage);
			PL_user_model.append(u)

		return PL_user_model
	else:
		return null 



	