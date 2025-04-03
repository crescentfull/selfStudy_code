# mocking
database = {
    1: "Alice",
    2: "Bob",
    3: "charlie"
}

def get_user_from_db(user_id):
    return database.get(user_id)
