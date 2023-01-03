tel = {}
address = {}

def addNewName_Phone1(name,phone):
    tel.update({name: phone})

def addAdress2(name,loc):
    x = tel.keys()
    if name in x:
        address.update({name:loc})
    else:
        print('not found')

def delWithName3(name):
    tel.pop(name)
    address.pop(name)

def search_phone_number4(name):
    if name in tel:
        print(tel[name])

def change_name5(name, newname):
    if name in (tel and address):
        tel[newname] = tel.pop(name)
        address[newname] = address.pop(name)
    else:
        print('not found!')

def sorting6():
    mytel_list = list(tel.items())
    myaddress_list = list(address.items())

    mytel_list.sort()
    myaddress_list.sort()

    print('tel : ', mytel_list)
    print('address : ', myaddress_list)




'''test = {'momad' : '1231' ,'wwer' : 'ewr', 'hd' : '12' ,'ali':'021'}
d = {'ali' : 'asdas'}
test['mamad'] = test.pop('ali') # it's worked!

mytest_list = list(test.items())
mytest_list.sort()
print(mytest_list)'''


print('1. Add name and phone number.')
print('2. Add name and address.')
print('3. Delete phone number and address.')
print('4. Searching for phone number.')
print('5. Change your name.')
print('6. Print sorting value of tel and address dict.')