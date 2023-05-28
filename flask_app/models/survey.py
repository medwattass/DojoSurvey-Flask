from ..config.mysqlconnection import connectToMySQL
from flask import flash


class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.database = data['database']
        self.framework = data['framework']
        self.all_data = []
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, `database`, framework, comment) VALUES (%(name)s, %(location)s, %(language)s, %(database)s, %(framework)s, %(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)
    
    @staticmethod
    def validate_survey(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if dojo['location'] == '--- Choose a location ---':
            flash("You must select a location.")
            is_valid = False
        if dojo['language'] == '--- Choose a programming language ---' :
            flash("You must select a programming language.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Your comment must be at least 3 characters.")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all_data(cls, id_data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        all_data = []
        results = connectToMySQL('dojo_survey_schema').query_db(query, id_data)
        for row in results:
            all_data.append(cls(row))
        return all_data
