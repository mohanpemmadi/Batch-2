import json


f = open('sample.json')
data = json.load(f)

print(data)

# # for obj in data:
# #     print(obj['name'])
#
# new_record = {"name": "srinu","age": 40}
# data.append(new_record)
#
# # print(data)
#
# g = open('test.json','w')
# json.dump(data,g)
#
# print('done')