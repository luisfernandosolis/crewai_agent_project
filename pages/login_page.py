#Import fastAPI
from fastapi import FastAPI

#Creating the FastAPI instance
app = FastAPI()

#Creating the login route
@app.get("/login")
def login():
    return {"message": "Welcome to the login page!"}

#Creating the register route
@app.get("/register")
def register():
    return {"message": "Welcome to the register page!"}

#Creating the update route
@app.put("/update")
def update():
    return {"message": "Welcome to the update page!"}

#Creating the delete route
@app.delete("/delete")
def delete():
    return {"message": "Welcome to the delete page!"}