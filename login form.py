from tkinter import *
from tkinter import messagebox
import ast
root=Tk()
root.title("login")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
def signin():
    Username=user.get()
    Password=code.get()
    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
##    print(r.keys())
##    print(r.values())

    if Username in r.keys() and Password==r[Username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        Label(screen,text='Hello,Logged In',bg='#fff',font=('calibri(body)',50,'bold')).pack(expand=True)
        screen.mainloop()
    else:
        Message.showerror('Invalid','invalid Username or Password')
#################################################################################################################################################################
def signup_command():
    window=Toplevel(root)
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
                window.destroy()
            except:
                file=open('datasheet.txt','w')
                pp=str({'username':'password'})
                file.write(pp)
                file.close()
            else:
                Messagebox.showerror('Invalid',"Both password should match")
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


#################################################################################################################################################################
    
    
    
img=PhotoImage(file='C:/Users/user/Desktop/tim.png')
lbl=Label(root,image=img,bg='white').place(x=50,y=50)
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading=Label(frame,text="signin",fg='#57a1f8',bg="white",font=("microsoft YaHei UI light",23,'bold'))
heading.place(x=100,y=5)
#################################################################################################################################################################

def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')
user=Entry(frame,width=25,fg='black',border=0,bg='white',font=("microsoft YaHei UI light",11,))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
###################################################################################################################################################################
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name=code.get()
    if name=='':
        user.insert(0, 'Password')
code=Entry(frame,width=25,fg='black',border=0,bg="white",font=("microsoft YaHei UI light",11,))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
##################################################################################################################################################################
Button(frame,width=39,pady=7,text='signin',bg='#57a1F8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Dont't have an account?",fg='black',bg='white',font=("microsoft YaHei UI light",9))
label.place(x=75,y=270)
sign_up=Button(frame,width=6,text='sign up',fg='#57a1F8',bg='white',border=0,cursor='hand2',command=signup_command)
sign_up.place(x=215,y=270)
root.mainloop()
       
    
    
