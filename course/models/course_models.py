from pydantic import BaseModel, EmailStr, constr
from enum import Enum
from uuid import UUID


class CourseCreate(BaseModel):
    course_title: str
    course_description: str
    course_duration: str
    price: str

    class Config:
        extra = "ignore"
        
class Cart(BaseModel):
    quantity:int
    
    

class CourseCreationProfile(BaseModel):
    message: str


class TokenType(str, Enum):
    USER_SIGN_UP = "USER_SIGN_UP"
    # EMPLOYEE_SIGN_UP = "EMPLOYEE_SIGN_UP"
    FORGOT_PASSWORD = "FORGOT_PASSWORD"
    EMAIL_CHANGE = "EMAIL_CHANGE"
