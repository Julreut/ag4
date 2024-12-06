from api import ApiAccessor

api = ApiAccessor()

# The following code creates 2000 users with different usernames and emails for performance testing

for i in range(20):
    try:
        profile_id = api.create_user(
            username=f"apiTestUser{i}", 
            password="test", 
            email=f"test{i}@example.com", 
            bio=f"This is user {i} created for performance testing.", 
            condition_id=1  # Assign condition ID 1 to all users
        )
        print(f"Created user {i} with profile ID: {profile_id}")
    except Exception as e:
        print(f"Failed to create user {i}: {e}")
