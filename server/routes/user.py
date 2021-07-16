from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import *
from bson import ObjectId
user = APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(conn.local.user.find())

@user.post('/')
async def create_session(user:User)->str:
    obj = conn.local.user.insert_one(dict(user))
    return str(obj.inserted_id)

@user.put('/{id}')
async def update_session(id, user:User)->bool:
    conn.local.user.update({ "_id": ObjectId(id)},
   { "$addToSet": {"audio_array":{"$each":dict(user)['audio_array']}}}
    )
    return False
