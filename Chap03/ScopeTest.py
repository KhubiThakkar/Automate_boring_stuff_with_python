#Global variables can be read from a Local Scope
# def spam():
#     print(eggs)

# eggs = 48
# spam()
# print(eggs)

#Local and Global variables with same name 
def spam():
    eggs = 'spam local'
    print(eggs)
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs = 'global'
bacon()
print(eggs)