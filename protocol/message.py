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

def server_status_message():
    return {
  "type": "server_status",
  "payload": {
    "status": "online",
    "uptime_seconds": 3600,
    "connected_users": 45,
    "total_messages": 15234,
    "version": "1.0.0"
  }
}

def serialize_message(message):
    return json.dumps(message)

