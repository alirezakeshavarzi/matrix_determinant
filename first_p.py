tel = {}
address = {}

def addNewName_Phone1(name,phone):
    tel.update({name: phone})
    print('Your name saved!.')

def addAdress2(name,loc):
    x = tel.keys()
    if name in x:
        address.update({name:loc})
        print('Your address saved!.')
    else:
        print('not found')

def delWithName3(name):
    if len(tel)!=0 and len(address)!=0:
        tel.pop(name)
        address.pop(name)
        print('Your name and was deleted!.')
    else:
        print('tel and address dict is empty.')

def search_phone_number4(name):
    if name in tel:
        print(tel[name])

def change_name5(name, newname):
    if name in (tel or address):

        if len(tel) != 0:
            tel[newname] = tel.pop(name)
        if len(address) != 0:
            address[newname] = address.pop(name)
        print('Your name changed.')
    else:
        print('Your name was not found!')

def sorting6():
    mytel_list = list(tel.items())
    myaddress_list = list(address.items())

    mytel_list.sort()
    myaddress_list.sort()

    print('tel : ', mytel_list)
    print('address : ', myaddress_list)




while True:
    print('1. Add name and phone number.')
    print('2. Add name and address.')
    print('3. Delete phone number and address.')
    print('4. Searching for phone number.')
    print('5. Change your name.')
    print('6. Print sorting value of tel and address dict.')

    print()
    n = int(input('Please enter a number : '))

    if n >= 1 and n <=6:
        if n==1:
            na = input('Your name : ')
            phone_n = input('Your phone number : ')

            addNewName_Phone1(na, phone_n)
            print()
        elif n==2:
            na = input('Your name : ')
            loc = input('Your address : ')

            addAdress2(na, loc)
            print()
        elif n==3:
            na = input('Your name : ')

            delWithName3(na)
            print()
        elif n==4:
            na = input('Your name : ')
            search_phone_number4(na)
            print()
        elif n==5:
            na = input('Your name : ')
            na2 = input('Enter your new name : ')

            change_name5(na, na2)
            print()
        elif n==6:
            sorting6()
            print()
        elif n==7:
            break


