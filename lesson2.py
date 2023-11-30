class Group_1012:
    def __init__(self, name, gen, age, avarage_score):
        self.name = name
        self.gen = gen
        self.avarage_score = avarage_score
        self.age = age
        self.age +=1
    def study(self):
        print("Learn good")
        if self.avarage_score < 12:
            self.avarage_score += 0.1
        else:
            print("U are the best already, slow down")

student1 = Group_1012("Гончарук Олександр", "чол.", 12, 12)
student2 = Group_1012("Трофимишин Владислав", "чол", 12,12)
student3 = Group_1012("Радомська Дарина",  "жін.",  13,  12)
student4 = Group_1012("Юраш Максим","чол.", 14, 10)
student5 = Group_1012("Коваленко Макар", "чол", 13, 11.1)
print("Студента #2 в списку звати ", student2.name)
print("Середня оцінка студента №3 -", student3.avarage_score)
student2.study()
print(student2.avarage_score)
