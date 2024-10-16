with open('Codingal.txt','w') as file:
    file.write("hibduskibdij hibduskibdij hooboduskoobdooj hbduskubduj")
file.close()

with open('Codingal.txt','r')as file:
    data=file.readlines()
    for line in data:
        word =line.split()
        print(word)
file.close()