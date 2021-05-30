from tkinter import *
from pytube import YouTube

root = Tk()
root.title("YouTube video Downloader")
root.geometry('500x300')
root.config(bg='white')

Label(root,text='Download Youtube video ',font=('Helvetica',18,'bold'),bg='blue').grid(row=0,padx=120,pady=5)
Label(root,text='Enter Url ',font=('Helvetica',18),fg='green',bg='blue').grid(row=1,padx=120,pady=20)

user_url = Entry(root,font=('Helvetica',"18"))
user_url.grid(row=2,padx=120,pady=5)

def download():
    url=YouTube(str(user_url.get()))
    content=url.streams.first()
    content.download()
    Label(root,text='Video Downloaded',font=('Helvetica',18,'bold'),bg='blue').grid(row=3,padx=120,pady=10)
Button(root,text='Download',command=download,fg="green",bg='black',font=('Helvetica',18,'bold')).grid(row=4,padx=120,pady=25)
root.mainloop()    

