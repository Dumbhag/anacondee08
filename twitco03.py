#OOP

class LOLTFT :
    #data/property/field/attribute
    major = "TFT"
    name = ""

    #method (มันคือ Function แต่เราไม่ต้องเรียกฟังชันก์)
    def shoHi() :
        print('Hi....')

    def introduceMySelf(self) :
        print(f'My name is {self.name}')
        print(f'My major is {self.major}')

#---------------------------
#สร้าง object
orbA = LOLTFT() #ปิดการเรียกใช้ contructor ของคลาสให้ทำงาน (ถ้ามี)
orbB = LOLTFT()


# การใช้งาน data ของ object คือ เอาค่ามันมาใช้ หรือเปลี่ยนค่าให้มันใหม่
print(orbA.major)
orbA.major = "NOOT"
orbA.name = "WOO"
orbB.name = "WEE"

# การใช้งาน data ของ object คือ สั่งเมธอด(Method)ของ object นั้นๆ ให้ทำงาน
orbA.introduceMySelf()
orbB.introduceMySelf()