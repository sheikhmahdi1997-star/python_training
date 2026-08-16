class Person:
    def __init__(self , firstname , lastname , n_code , email , username , password):
        self.lastname=lastname
        self.firstname= firstname
        self.national_code= n_code
        self.email=email
        self.username= username
        self.__password=password
        self.is_logged_in= False

    def __str__(self):
        return f"\nfirstname is {self.firstname}, lastname is {self.lastname}, email is {self.email} "

    def login(self , username , password):
        if self.username == username and self.__password == password:
            print(f"\n'{self.username}' is logged in successfully. ✅")   
            self.is_logged_in = True
            return True
        else:
            print(f"\nIncorrect username or password! ❌")     


class Student(Person):
    def __init__(self, firstname, lastname, n_code, email, username, password , student_id , major):
        super().__init__(firstname, lastname, n_code, email, username, password)
        self.student_id = student_id
        self.major = major


    def add_course(self , course):
        if self.is_logged_in :
            course.set_course(self.student_id)
        else:
            print("Please login at first.")

class Professor(Person):
    def __init__(self, firstname, lastname, n_code, email, username, password, profs_id ,department ):
        super().__init__(firstname, lastname, n_code, email, username, password)
        self.profs_id = profs_id
        self.department = department

    def add_grade(self , course , student_id , grade ):
        if self.is_logged_in:
            course.set_grade(student_id , grade)
        else:
            print(f"\nPlease login at first.")


class Course:
    def __init__(self , course_name ,  course_id , units , capacity ):
        self.course_name = course_name
        self.course_id = course_id
        self.units = units
        self.capacity = capacity
        self.all_student={}
        self.profs_id = None
        self.course_list=[]

    def set_course(self ,student_id):
        if len(self.all_student) < self.capacity:
            self.all_student[student_id] = None
            print(f"You assigning succeccfully. ✅")
            print(f"{self.all_student}")
        else:
            print(f"Sorry the capacity is full.")


    def set_grade(self , student_id , grade ):
        if student_id in self.all_student:
            self.all_student[student_id]= grade
            print(f"Grade added successfully. ✅")
            print(f"{self.all_student}")


sud_1=Student("Mahdi" , "Sheikh" , "274" , "gmail.com" , "mahdi_sheikh" ,"pw", "St_01" , "data science")


course_1=Course("math" , "Co_01" , 3 , 10)
sud_1.login("mahdi_sheikh" , "pw")
sud_1.add_course(course_1)

profs_1=Professor("mahdi" , "sheikh" ,"275", "email", "mahdi.sheikh", "pw", "p_01", "computer science")
profs_1.login("mahdi.sheikh", "pw")
profs_1.add_grade(course_1,"St_01",20)





        
        

    