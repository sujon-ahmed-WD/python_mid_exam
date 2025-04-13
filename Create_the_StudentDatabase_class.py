class  StudentDatabase:
    student_list=[]   
    @classmethod
    def add_student(cls,new_stu):
        
      cls.student_list.append(new_stu)  
        
    
        
# Student=StudentDatabase()
# Student.add_student(10)
StudentDatabase.add_student(10)
print(Student.student_list)
