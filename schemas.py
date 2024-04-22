from pydantic import BaseModel
import datetime

class Usercreate(BaseModel):
    username:str
    password: str
    email: str
    
    