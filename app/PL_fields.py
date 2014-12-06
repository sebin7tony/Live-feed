from flask.ext.restful import fields


#
#      |||||||||||||  Presentation layer field for json formating  |||||||||||||||||
#




user_fields = {
	'userid' : fields.String,
	'username': fields.String,
	'email': fields.String,
	'userImage':fields.String

}

user_rest  = {
	"users" : fields.Nested(user_fields)
}

comment_fields = {
	'commentid' : fields.String,
	'comment' : fields.String,
	'date' : fields.DateTime,
	'postid' : fields.String
}

posts_fields = {
    'postid': fields.String,
	'post': fields.String,
	'date' : fields.DateTime,
	'lat' : fields.String,
	'lon' : fields.String,
	'likes':fields.Integer,
	'author' : fields.String
	#'author':fields.Nested(user_fields),
	#'comments': fields.Nested(comment_fields)
}

