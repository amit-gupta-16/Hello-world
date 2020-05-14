from my_decorators import do_twice

# @do_twice
# def say_whee(name):
#     print(f"whee! {name}")

# a = say_whee("karishma")
# b = say_whee("Amit")
# print(a,b)

@do_twice
def return_greet(name):
    print("Creating greeting")
    return f"Hi {name}"

a = return_greet("amit")
print(a)

print(return_greet.__name__)