from pydantic import BaseModel

class PersonResponse(BaseModel):
    id: int
    name: str
    age: int

class PersonCreate(BaseModel):
    name: str
    age: int
