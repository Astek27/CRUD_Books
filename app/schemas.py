from pydantic import BaseModel, Field, field_validator


class CreateBook(BaseModel):
    name: str = Field(..., max_length=123)
    author: str = Field(..., max_length=123)

    @field_validator('name')
    def not_empty_name(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError('Be not empty!')
        return v 

    @field_validator('author')
    def not_empty_author(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError('Be not empty!')
        return v
    

class BookResponse(CreateBook):
    model_config = {'from_attributes': True}
    
    id: int


class CreateUser(BaseModel):
    login: str = Field(..., max_length=30)

    @field_validator('login')
    def validate_login(cls, v: str):
        if ' ' in v:
            raise ValueError('Not space simbol')
        return v

class UserResponse(CreateUser):
    model_config = {'from_attributes': True}
    id: int