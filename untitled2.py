from tkinter import*

rootTk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background="snow")

enter_word=Entry(root)
enter_word.place(relx=0.5,relx=0.4,anchor=CENTER)

label=Label(root, text="Ascii name",bg="light blue",fg="yellow")

def asciiConverter():
    input_word= enter_word.get()
    
    for letter in input_word:
        label["text"] += str(ord(letter)) + ""
        
        btn=Button(root,text="This is your Ascii name",command=asciiConverter,bg="gold",fg="gray")
        btn.place=(relx=0.6,rely=0.6,anchor=CENTER)
        
        label.place(relx=0.6,rely=0.7,anchor=CENTER)
        
        root.mainloop()
        