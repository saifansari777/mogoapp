validator = {
   "validator": {
      "$jsonSchema": {
         "bsonType": "object",
         "required": [ "title", "note" ],
         "properties": {
            "title": {
               "bsonType": "string",
               "description": "must be a string and is required"
            },
            "note":{
               "bsonType": "string",
               "description": "must be a string and is required"
            }
            
            }
         }
      }
   }
