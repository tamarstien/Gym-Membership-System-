from Gym import Gym

g=Gym()
print(g.register_member("324566678","Hadassa",22))
# print(g.add_course("erobi"))
# print(g.enroll_member_to_class("324566678","erobi"))
g.add_treiner("342566672","racheli" ,24)

g.add_course("zomba","racheli")
g.add_course("asd","racheli")
g.add_course("fre","racheli")
g.add_course("fregg","racheggggli")

print(g.get_courses_by_trainer("racheli"))