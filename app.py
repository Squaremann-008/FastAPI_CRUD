from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person, Base
from pydantic_models import PersonResponse, PersonCreate

app = FastAPI()

# Database URL (Replace with your database URL)
DATABASE_URL = "postgresql://oiseh:5PNWs2xgyVCJza0P3lr1wsQkDN4xwWBN@dpg-cjvelut175es73fvt0v0-a.oregon-postgres.render.com/stage2db"
# SQLAlchemy database connection
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
session = Session(engine)

@app.post("/api/", response_model=PersonResponse)
def create_person(person: PersonCreate):
    # Create a new person in the database
    db_person = Person(**person.model_dump())
    session.add(db_person)
    session.commit()
    session.refresh(db_person)
    return db_person

@app.get("/api/{user_id}", response_model=PersonResponse)
def read_person(user_id: str):
    # Fetch the person from the database by name
    person = session.query(Person).filter(Person.name == user_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@app.put("/api/{user_id}", response_model=PersonResponse)
def update_person(user_id: str, updated_person: PersonCreate):
    # Fetch the person from the database by name
    person = session.query(Person).filter(Person.name == user_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")

    # Update the person's details
    for key, value in updated_person.model_dump().items():
        setattr(person, key, value)

    session.commit()
    session.refresh(person)
    return person

@app.delete("/api/{user_id}", response_model=PersonResponse)
def delete_person(user_id: str):
    # Fetch the person from the database by name
    person = session.query(Person).filter(Person.name == user_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")

    # Delete the person from the database
    session.delete(person)
    session.commit()
    return person
