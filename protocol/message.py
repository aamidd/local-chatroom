import json

def create_chat_message(sender, text):
        
    return {
        "type": "chat",
        "payload": {
            "text": text,
            "sender": sender,
        }
    }

def create_signup_message(username, password):  
    return {
        "type": "signup",
        "payload": {
            "username": username,
            "password": password,
        }
    }

def create_login_message(username, password):
    return {
        "type": "login",
        "payload": {
            "username": username,
            "password": password,
        }
    }

def serialize_message(message):
    return json.dumps(message)

