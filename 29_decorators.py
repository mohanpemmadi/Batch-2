# Decorators are functions that adds extra functionality to an existing function
# without changing the original structure of the function

def sample_decorator(fun):
    print('1 - fun:', fun.__name__)
    def inner():
        print('2 - inner')
        print
        return fun()
    return inner

# def log_in(fun):
#     print('1 - fun:', fun.__name__)
#     def inner():
#         print('User is valid')
#         return fun()
#     return inner
#
# @log_in
# def home_page():
#     print('3 - home page')
#     return 'Welcome to Home page'

# @log_in
# def about_page():
#     print('3 - about page')
#     return 'Welcome to about page'


# home_page()
# about_page()

db_user = 'mohan'

def log_in(fun):
    print('1 - fun:', fun.__name__)
    def inner(name):
        if name == db_user:
            return fun(name)
        else:
            return 'user is not valid'
    return inner

# @log_in
# def home_page(name):
#     print('3 - home page')
#     print('user ', name)
#     return 'Welcome to Home page'

# @log_in
# def about_page(name):
#     print('3 - about page')
#     print('user ', name)
#     return 'Welcome to About page'
#
# print(about_page('mohan'))

def dec(fun):
    def inner():
        print('extra logic validated')
        return fun()
    return inner
@dec
def demo():
    return 'hello'

print(demo())