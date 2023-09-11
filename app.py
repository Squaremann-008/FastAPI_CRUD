from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Person, SessionLocal, engine

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new person
@app.post("/persons/", response_model=Person)
def create_person(person: Person, db: Session = Depends(get_db)):
    db_person = Person(name=person.name, age=person.age)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

# Read a person by name
@app.get("/persons/{name}", response_model=Person)
def read_person_by_name(name: str, db: Session = Depends(get_db)):
    db_person = db.query(Person).filter(Person.name == name).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

# Update a person by name
@app.put("/persons/{name}", response_model=Person)
def update_person_by_name(name: str, updated_info: Person, db: Session = Depends(get_db)):
    db_person = db.query(Person).filter(Person.name == name).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    for attr, value in updated_info.dict().items():
        setattr(db_person, attr, value)
    db.commit()
    db.refresh(db_person)
    return db_person

# Delete a person by name
@app.delete("/persons/{name}")
def delete_person_by_name(name: str, db: Session = Depends(get_db)):
    db_person = db.query(Person).filter(Person.name == name).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    db.delete(db_person)
    db.commit()
    return {"message": "Person deleted successfully"}
