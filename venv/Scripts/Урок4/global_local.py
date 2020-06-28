global_var = 1
def my_f():
    global global_var
    local_var = 100
    print(local_var)
    global_var = 999
my_f()
print(global_var)
#print(local_var)