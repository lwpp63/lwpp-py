from tkinter import *  
  

window = Tk()  
window.title("Добро пожаловать в приложение Python TK_INTER")  
window.geometry('600x400')
window.resizable(height = False, width = False)
window.iconphoto(True, PhotoImage(file=('icons8.png')))
fon = PhotoImage(file=('fon.png'))
Label(window, image = fon).pack()
lbl = Label(window, text="Привет", font=("Arial Bold", 50))  
lbl.place(relx = 0.2, rely = 0.1, anchor = CENTER)  
btn = Button(window, text="Не нажимать!")  
btn.place(relx = 0.9, rely = 0.1, anchor = CENTER)  
window.mainloop()
