def authenticate_user(username, password):
    if not username or not password:
        return False
    
    # Check credentials
    if len(password) < 8:
        return False
    
    return True

def delete_user(user_id):
    if user_id <= 0:
        raise ValueError("Invalid user ID")
    
    # Delete user from database
    print(f"Deleting user {user_id}")
    return True
