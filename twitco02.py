# ******************* Dictionary คือ ข้อมูลหลายข้อมูล ที่เป็น key:value แก้ไขได้ ไม่มีลำดับ ซ้ำได้ ***************
# key เป็น string/integer ส่วน Value เป็นอิหยังก็ได้
my_dic = {'name':'mod','age':30,555:999,'flag':True, 'wow':[10,20,30]}
my_dic2 = { 'data':(10,20,30,40),
            'data2':(2,5,6),
            'data3':(56,4,7),
            'data4':{'x':111,
                     'y':222}}
#การเข้าถึงข้อมูลใดข้อมูลหนึ่ง
print(my_dic['name'])
print(my_dic[555])
my_dic['age'] = 50
print(my_dic)
#อยากแสดงผล 20 ออกมาทำไง
print(my_dic['wow'][1])
#อยากแสดงผล 222 ออกมาทำไง
print(my_dic2['data4']['y'])
my_dic2['data5'] = 888
print(my_dic2)
# การเข้าถึงทุกข้อมูล
for xx in my_dic.keys() :
    print(xx)

print('======================')

for xx in my_dic.values() :

    print(xx)

print('======================')

for xx,yy in my_dic.items() :

    print(xx, '- ', yy)

print('======================')

# Dictionary Method 
my_dic.popitem()
my_dic.popitem()
my_dic.popitem()
print(my_dic)
my_dic2.pop('data3')
print(my_dic2)
print('======================')
print(my_dic2['data2'])
print(my_dic2.get('data2'))