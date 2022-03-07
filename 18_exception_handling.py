
'''Exception - obbnormal termination of a program'''

"""
try
except
else
finally

"""
# value = int(input('Enter a value to divide: '))

# try:
#     value = 100/result
#     print('value - ',value)
# except Exception as e:
#     print(e)
#     print('exception')
# value = 100/0
#
# try:
#     result = 100/value
#     print('value - ',result)
# except ZeroDivisionError:
#     print('except block')
#     result = 100/2
#     print(result)

# dt = {'name':'ravi','age':30}
# # dt['salary']
# key = input('Enter a key to get the data: ')

'''
try:
    print(dt[key])
except KeyError:
    print('Please enter a proper key!')
except NameError:
    print('Given name is not defined')
except ValueError:
    print('Value is incorrect')
'''
dt = {'name':'ravi','age':30}

try:
    result = 100/0
    print('try block')
except Exception as err:
    print('error block')
else:
    print('else block')
finally:
    print('finally block')

''' on success : try -> else -> finally '''
''' on failure : try -> except -> finally'''





