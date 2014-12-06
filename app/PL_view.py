from app import app,api
from app import DL_models,SL_impl,PL_fields
from flask import render_template,jsonify,request
from flask.ext.restful import Resource, fields, marshal_with
import json, collections


@app.route('/')
def index():
	#api_manager.create_api(tweets,methods=['GET','POST'])
	return app.send_static_file('index.html')
 
# Creating web service for getting the list of posts. 
class PostList(Resource):
	
	@marshal_with(PL_fields.posts_fields)
	def get(self):
		posts = SL_impl.get_all_posts()
		return posts

api.add_resource(PostList, '/twitter/api/v1.0/posts', endpoint = 'posts')


# Creating a web service to get the table headers of the Post table

class PostListHeader(Resource):
	def get(self):
		postHeaders = SL_impl.get_Post_table_headers()
		print "printing post headers" 
		return postHeaders

api.add_resource(PostListHeader, '/twitter/api/v1.0/postsheaders', endpoint = 'postsheaders')

# Creating web service for getting the list of posts.
class CommentList(Resource):

	@marshal_with(PL_fields.comment_fields)
	def get(self):
		comments = SL_impl.get_all_comments()
		#comments = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(str(comments))
		return comments

api.add_resource(CommentList, '/twitter/api/v1.0/comments', endpoint = 'comments')

# Creating web service for getting the list of users.

class UserList(Resource):

	@marshal_with(PL_fields.user_rest)
	def get(self):
		users = SL_impl.get_all_users()
		return {"users" : users}

	def post(self):
		json_data = request.get_json(force= True)
		print json_data
		return json_data

api.add_resource(UserList, '/twitter/api/v1.0/users', endpoint = 'users')