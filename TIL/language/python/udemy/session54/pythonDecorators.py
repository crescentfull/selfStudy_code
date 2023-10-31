class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        # *args : Unlimited Positional Arguments(무제한 위치 인자)
        # **kwargs : Unlimited keyword Argument(무제한 키워드 인자)
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            print("NOT LOGGED IN")
    return wrapper

@is_authenticated_decorator
def creat_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
    
new_user = User("Song")
new_user.is_logged_in = True
creat_blog_post(new_user)