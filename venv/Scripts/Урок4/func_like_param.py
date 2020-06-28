def f():
    print('Hello from other f')

def to(f_param):
    f_param()

to(f)