from fastapi.datastructures import Default
import ormar
import pydantic
import datetime

from db.base import metadata, database
from pydantic import BaseModel, ValidationError, validator
import datetime

class Users(ormar.Model):
    class Meta():
        tablename = "applications"
        metadata = metadata
        database = database

    id:int  = ormar.Integer(primary_key=True)
    name_user:str  = ormar.String(max_length=255)
    phone_user:str  = ormar.String(max_length=255)
    email_user:str = ormar.String(max_length=255)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    cheked_apll:bool = ormar.Boolean(default=False)



from pydantic import BaseModel


class CreateUsers(BaseModel):
    name_user:str
    phone_user:str 
    email_user:str 

class UpdateUsers(BaseModel):
    cheked_apll:bool
    





