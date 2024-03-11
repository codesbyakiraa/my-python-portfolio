from tkinter import *
from tkinter import messagebox
import ast
window=Tk()
window.title('signup')
window.geometry('925x500+300+200')
window.configure(bg='#fff')
def signup():
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()
    if password==confirm_password:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)
            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()
            file=open('datasheet.txt','w')
            w=file.write(str(r))
            messagebox.showinfo('signup','successfully sign up')
        except:
            file=open('datasheet.txt','w')
            pp=str({'username':'password'})
            file.write(pp)
            file.close()
        else:
            messagebox.showerror('Invalid',"Both password should match")
def sign():
    window.destroy()
img=PhotoImage(file='C:/Users/user/Desktop/loginn.png')
Label(window,image=img,border=0,bg='white').place(x=50,y=90)
frame=Frame(window,width=350,height=390,bg='white')
frame.place(x=480,y=50)
heading=Label(frame,text='sign up',fg='#57a1f8',bg='white',font=('microsoft yahei UI light',23,'bold'))
heading.place(x=100,y=5)
#######################################################################################################
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'username')
        
    
user=Entry(frame,width=25,fg='black',border=1,bg='white',font=('microsoft yahei UI light',11))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
######################################################################################################
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
       code.insert(0,'password')
        
    
code=Entry(frame,width=25,fg='black',border=1,bg='white',font=('microsoft yahei UI light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#######################################################################################################

def on_enter(e):
  confirm_code.delete(0,'end')
def on_leave(e):
    if confirm_code.get()=='':
       confirm_code.insert(0,'password')
        
    
confirm_code=Entry(frame,width=25,fg='black',border=1,bg='white',font=('microsoft yahei UI light',11))
confirm_code.place(x=30,y=220)
confirm_code.insert(0,'password')
confirm_code.bind("<FocusIn>",on_enter)
confirm_code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
########################################################################################################
Button(frame,width=39,pady=7,text='sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text='I have an account',fg='black',bg='white',font=('microsoft yahei UI light',9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text='sign in',border=0,bg='white',fg='#57a1f8',cursor='hand2')
signin.place(x=200,y=340)



window.mainloop()
