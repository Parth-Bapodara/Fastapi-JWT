from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default = None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        json_schema_extra = {
            "example":{
                "title" : "Hello",
                "content" : "Welcome"
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "fullname" : "Bapodara Parth Dilip",
                "email" : "demo@gmail.com",
                "password" : "weakpassword"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "demo@gmail.com",
                "password": "weakpassword"
            }
        }