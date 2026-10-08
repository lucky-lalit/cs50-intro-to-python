dic = {'lalit':0,'shiv':1,'harsh':2,'abc':3,'xyz':-1}
def get_arg(name):
    # return dic[name]
    return "Hello world"


print(sorted(['lalit','abc','xyz'],key=get_arg))
