#------------- Set คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันไม่ได้ (ถ้าซ้ำจะถือเป็นตัวเดียวกัน) และไม่มีลำดับ และแก้ไขไม่ได้ แต่เพิ่มลบได้ -----------
my_set = {10,20,True,10,'LOL',(20,'TOT')}

#เข้าถึงทุกข้อมูลในset 
for data in my_set :
    print(data)

# แก้ไขข้อมูลใน set ทำไม่ได้โดยตรง แต่ทำได้โดยอ้อมเหมือนกับ Tuple
my_list = list(my_set)
print(my_list)
my_list[2] = "WOW"
print(my_list)
my_set = set(my_list)
print(my_set)

# set method
my_set.add(999)
my_set.add('WOW')
print(my_set)
my_set.pop() #เอาข้อมูลออก แบบสุ่ม
print(my_set)
my_set2 = my_set.copy
print(my_set2)
my_set.remove(999)
