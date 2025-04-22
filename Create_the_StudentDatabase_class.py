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
        print(f" student id:{self._student_id},name:{self._name},department:{self._department}")
        
        if self._is_enrolled:
            print("enrolled")
        else:
            print("not enrolled")
        
data = Student(10, 'Tusbala', 'CST') 
 

# Replia  System

while True:
              print(" /n ===== Student Menu =====")
              
              print("1. View All Students")
              print("2. Enroll Student")
              print("3. Drop Student")
              print("4. Exit")

              choies=int(input("Enter the choiess => "))
              
              if choies==1:    
                 for stu in StudentDatabase.student_list:
                     stu.view_student_info()
              elif choies==2:
                    sid=int(input("Student ID to enroll : "))
                    found=False
                    for stu in StudentDatabase.student_list:
                        if stu._student_id==sid:
                            stu.enroll_student()
                            found=True
                            break
                    if not found:
                            print("Student is not Enrolled :")
                            
              elif choies==3:
                   sid=int(input("Student ID to DropStudent : "))
                   found=False
                   for stu in StudentDatabase.student_list:
                       if stu._student_id==sid:
                           stu.drop_student()
                           found=True
                           break
                   if not found:
                         print("Student Id is not DropStudent   : ")
                   
              elif choies==4:
                 exit()
                  
    

 
