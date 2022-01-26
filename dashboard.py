from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from course import CourseClass
from student import studentClass
from result import ResultClass
from report import ReportClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student  Result Management System")
        self.root.geometry("1550x790+0+0")
        self.root.config(bg="white")

       
    
        #=========title=====
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT, font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        
        #======Menu=======
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white" )
        M_Frame.place(x=10,y=70,width=1490,height=90)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=220,height=50)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=260,y=5,width=220,height=50)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=500,y=5,width=220,height=50)
        btn_view=Button(M_Frame,text="View",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=740,y=5,width=220,height=50)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=980,y=5,width=220,height=50)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1230,y=5,width=220,height=50)
        

        #========COntent ======
        self.bg_img=Image.open("image/n1.png")
        self.bg_img=self.bg_img.resize((1000,320),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)


        self.lb1_bg=Label(self.root,image=self.bg_img).place(x=470,y=200,width=920,height=350)

        #====update details=====
        self.lb1_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white").place(x=460,y=580,width=300,height=100)
      
        self.lb1_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white").place(x=780,y=580,width=300,height=100)
      
        self.lb1_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white").place(x=1100,y=580,width=300,height=100)
      
      
         #========Footer=====
        Footer=Label(self.root,text="SRMS-Student Result Management System\nContact us for any technical Issue:987XXXX09", font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)


    def add_course(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=CourseClass(self.new_win) 


    def add_student(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=studentClass(self.new_win)  
 

    def add_result(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=ResultClass(self.new_win)  
    

    def add_report(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=ReportClass(self.new_win)  
    

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()