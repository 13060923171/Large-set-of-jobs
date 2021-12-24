class SchoolMember(object):
    '''学习成员基类'''
    member = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        '注册'
        print('just enrolled a new school member [%s].' % self.name)
        SchoolMember.member += 1

    def tell(self):
        print('----%s----' % self.name)
        for k, v in self.__dict__.items():
            print(k, v)
        print('----end-----')

    def __del__(self):
        print('开除了[%s]' % self.name)
        SchoolMember.member -= 1


class Teacher(SchoolMember):
    '教师'

    def __init__(self, name, age, sex, salary, course):
        SchoolMember.__init__(self, name, age, sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        print('Teacher [%s] is teaching [%s]' % (self.name, self.course))


class Student(SchoolMember):
    '学生'
    def __init__(self, name, age, sex, course, tuition):
        SchoolMember.__init__(self, name, age, sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self, amount):
        print('student [%s] has just paied [%s]' % (self.name, amount))
        self.amount += amount







try:
    number = int(input("请输入数字："))
    list = []
    list.append(number)
    while True:
        if number == list[0]:
            t1 = Teacher('Wusir', 28, 'M', 3000, 'python')
            t1.tell()
            with open('data.txt','w')as f:
                f.write('运行成功')
            break
        elif number == list[0]:
            s1 = Student('haitao', 38, 'M', 'python', 30000)
            h = s1.tell()
            with open('data.txt','w')as f:
                f.write('运行成功')
            break
        elif number == list[0]:
            s2 = Student('lichuang', 12, 'M', 'python', 11000)
            print('SchoolMember.member')
            with open('data.txt', 'w')as f:
                f.write('运行成功')
            break
except:
    print('请输入正确的数字！！')