class  StudentDatabase:
    student_list=[]   
    @classmethod
    def add_student(cls,new_stu):
        
      cls.student_list.append(new_stu)  
        

class Student:
    def __init__(self,student_id,name,department):
       self._student_id=student_id
       self._name=name
       self._department=department
       self._is_enrolled=False
       StudentDatabase.add_student(self)

    def  enroll_student(self):
        
        if self._is_enrolled==True:
            print("already enrolled")
        else:
             self._is_enrolled=True
              
    def drop_student(self):
        
        if self._is_enrolled==False:
            print("The student has dropped out.")   
        else :
            self._is_enrolled=False
            print("The student has been dropped.")
    def view_student_info(self):
        print(f" student id:{self._student_id},name:{self.name},department:{self._department}")
        
        if self.enroll_student:
            print("enrolled")
        else:
            print("not enrolled")
        
data=Student(10,'tusbala','cst','yes')
 



 
