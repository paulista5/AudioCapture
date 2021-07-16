def userEntity(item) -> dict:

    return {
        "_id":str(item['_id']),
        "name":item['name'],
        "language":item['language'],
        "session_id": item['session_id'],
        "audio_array":item['audio_array']
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]