from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define the User schema
class User(BaseModel):
    id: int
    name: str
    email: str

# In-memory array to store users
users = []

# Create a new user
@app.post("/users/", response_model=User)
def create_user(user: User):
    if any(u.id == user.id for u in users):
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    users.append(user)
    return user


@app.get("/")
def base_root():
    return {'success':"Server Started successfully  "}
# Read all users
@app.get("/users/", response_model=List[User])
def read_users():
    return users

# Read a single user by ID
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update a user by ID
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for idx, user in enumerate(users):
        if user.id == user_id:
            users[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Delete a user by ID
@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    users.remove(user)
    return user
