validator = {
      "$jsonSchema": {
         "bsonType": "object",
         "required": [ "title", "note" , "author"],
         "properties": {
            "title": {
               "bsonType": "string",
               "description": "must be a string and is required"
            },
            "note":{
               "bsonType": "string",
               "description": "must be a string and is required"
            },
            "author":{
              "bsontype":"objectId",
              "description":"User should be authenticated"
            }
            }
         }
      }

user_validator = {
      "$jsonSchema": {
         "bsonType": "object",
         "required": [ "username", "email", "password" ],
         "properties": {
            "username": {
               "bsonType": "string",
               "uniqueItems": "true",
               "maxlength":24,
               "description": "must be a string and is required"
            },
            "email":{
               "bsonType": "string",
              "uniqueItems": "true",
              "pattern" : "^.+\@.+$",
               "description": "must be a string and is required"
            },
            "password":{
               "bsonType": "string",
               "minLength":8,
               "maxLength":32,
               "description": "must be a string and is required and shoul be between 8 to 32 characters"

            }
            
            }
         }
      }