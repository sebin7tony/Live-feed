


#
#  |||||||||  Models for the Service Layer   ||||||||||||||
#

# Class structre which is compatible with the json result in SL.
class Post(object):
	def __init__(self,postid,post,date,lat,lon,likes,author,comments):
		self.postid=postid
		self.post=post
		self.date=date
		self.lat=lat
		self.lon=lon
		self.likes=likes
		self.author=author
		self.comments=comments 

# Class structre which is compatible with the json result in SL_models
class Comment(object):
	def __init__(self,commentid,comment,date,parent_post):
		self.commentid = commentid
		self.comment = comment
		self.date = date
		self.postid = parent_post

# Class structure which is compatible with the json result in SL_Model
class User(object):
	def __init__(self,userid,username,email,userImage):
		self.userid = userid
		self.username = username
		self.email = email
		self.userImage = userImage

