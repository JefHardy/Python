from tkinter import messagebox
import tkinter

def giris_yap():
    if klogin.get() == "ulas" and slogin.get() == "123":
        messagebox.showinfo(title=f"Hoşgeldiniz {klogin.get()}",message=f"Hoşgeldiniz {klogin.get()}")

window = tkinter.Tk()
window.minsize(width=300,height=300)
window.eval('tk::PlaceWindow . center')
FONT = ("Times new roman",20,"italic")
baslik = tkinter.Label(text="LOGİN FORM",font=FONT)
baslik.pack()


klogin = tkinter.Entry(width=20)
slogin = tkinter.Entry(width=20)


kloginlabel = tkinter.Label(text="Kullanıcı adı  ",font=("Times new roman",10,"normal"))
sloginlabel = tkinter.Label(text="Şifre",font=("Times new roman",10,"normal"))
login = tkinter.Button(text="Giriş Yap",command=giris_yap)


kloginlabel.pack()
klogin.pack()
sloginlabel.pack()
slogin.pack()
login.pack()

window.mainloop()
