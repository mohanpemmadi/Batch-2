'''
syntax:

f = open(filename, mode)

mode - r,w  and a

'''
""" Read """
# fp = open('test.txt','r')
# print(fp.read()) # read entire file
# print(fp.read(40)) # read no of chars
# print(fp.readlines()) # read line by line

''' write '''

g = open('test2.txt','w')
# g.write('Python is a great lang and easy to learn')
# g.write('\nAbc')
# g.writelines(['line 1\n','line 2\n','line 3'])
# g.write('python')
# g.write('\njava')
g.write('c++')
print('done')

''' append '''

h = open('test3.txt','a')
# h.write('python')
# h.write('\njava')
h.write('\nc++')




