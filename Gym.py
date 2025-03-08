from course import Course
from  members import Members
from trainers import Trainers

class Gym:
    def __init__(self):
        self.trainers_dict={}
        self.members_dict= {}
        self.course_dict={}


    def register_member(self, id,name,age):
        members=Members(id,name,age)
        self.members_dict[id]=members
        return f"very nice' be thin!! {members.name}"

    def add_course(self,name,treiner_name):
        course=Course(name,treiner_name)
        self.course_dict[name]=course
        return "course seccsefully 😀😀😁😁"

    def add_treiner(self,id,name,age):
        trainer=Trainers(id,name,age)
        self.trainers_dict[id]=trainer
        return "trainer seccsefully 😀😀😁😁"


    def enroll_member_to_class(self,id,course_name):
        if not self.members_dict.get(id):
            raise Exception ("user not exists😯😯")
        if not self.course_dict.get(course_name):
            raise Exception("oopss! there is no course")
        self.members_dict[id].courses.append(course_name)
        self.course_dict[course_name].num_of_participate+=1
        print(self.course_dict)
        return "very nice one two three go..."

    def get_courses_by_trainer(self,treiner_name):
        return [c for c in self.course_dict.values() if c.treiner_name==treiner_name]