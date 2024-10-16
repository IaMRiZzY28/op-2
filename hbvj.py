newj =open('newfile.txt','x')
newj.close()

import os
if os.path.exists('filenew.txt'):   
    os.remove('filenew.txt')
else:
    print('file does not exists')
filenew = open("filenew,txt",'w')
filenew.write('kukudukuuuuuu')
filenew.close()
os.remove('Codingal.txt')