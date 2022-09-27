from flask import request
from flask_restful import Resource
from ..models.user import User
from ..database import user_db, get_db_connection
from .auth_api import PartiallyProtectedApi
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import restful_api,app

class UsersSearchApi(Resource):
	decorators = [jwt_required(optional=True)]	#Add appropriate decorators
	def get(self):
		email = request.args.get('email')
		app.logger.info(f"email is {email}")
		if not email:
			app.logger.error("Missing registered Email in request parameter!")
			return {'message': 'email is mandatory'},400 		
		conn = get_db_connection()
		user = user_db.get_user_details_from_email(conn,email)
		if not user:
			app.logger.info("User not found in DB")
			return {'message': f'User {email} not found in db'}
		identity_email = get_jwt_identity()
		if identity_email:
			app.logger.info(f"User {identity_email} details: ")
			return user.to_json()
		else:
			app.logger.info("User logged in with partial permissions")
			return {'name':user.name, 'email':user.email}
		close_db_connection(conn)

		#pass #Add logic to give full user details if accesed by a user with valid token else return just name and email

# Uncomment the below line by adding a valid url mapping for the user search API
restful_api.add_resource(UsersSearchApi, '/api/users/search')