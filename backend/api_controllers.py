#API request GET/POST/PUT/DELETE
from flask_restful import Api,Resource,reqparse
from .models import *

api=Api()

#parser for Lists
list_parser=reqparse.RequestParser()
list_parser.add_argument("title")
list_parser.add_argument("description")

class ListApi(Resource):

    def get(self,user_id):
        lists=Lists.query.filter_by(user_id=user_id).all()
        #json
        #[{'key': 'value', 'key': 'value'},....]
        user_list=[]
        for list in lists:
            list_details={}
            list_details["id"]=list.id
            list_details["title"]=list.title
            list_details["description"]=list.description
            user_list.append(list_details)
        return user_list



    def post(self,user_id):
        list_data=list_parser.parse_args()
        new_list=Lists(title=list_data["title"],description=list_data["description"],user_id=user_id)
        db.session.add(new_list)
        db.session.commit()
        return "List created!",201

    def put(self,list_id):
        list_data=list_parser.parse_args()
        list=Lists.query.filter_by(id=list_id).first()
        if list:
            list.title=list_data["title"]
            list.description=list_data["description"]
            db.session.commit()
            return "List updated!",200
        else:
            return "List not found!",400

    def delete(self,list_id):
        list=Lists.query.filter_by(id=list_id).first()
        if list:
            db.session.delete(list)
            db.session.commit()
            return "List deleted!",200
        else:
            return "List not found!",400


api.add_resource(ListApi,"/api/lists/<int:user_id>",'/api/list/update/<int:list_id>','/api/list/delete/<int:list_id>')

