import tkinter as tk
window=tk.Tk()
def click(event):
    value=display.get()
    text=event.widget.cget('text')
    if text == "=":
        result=eval(value)
        display.delete('0',tk.END)
        display.insert(tk.END,result)
    elif text == "C":
        display.delete('0',tk.END)
    else:
        display.insert(tk.END,text)
    

window.title('calculator')
# window.geometry('310x550')
window.resizable(False,False)
display=tk.Entry(window,font=('Arial',25),justify='right')
display.pack(padx=10,pady=10,ipady=10)
btn_frame=tk.Frame(window)
btn_frame.pack()
btn_labels=['7','8','9','*',
            '4','5','6','-',
            '1','2','3','+',
            'C','0','=','/',]
i=0
for label in btn_labels:
    button=tk.Button(btn_frame,text=label,font=('Arial',18),padx=20,pady=20,)
    button.grid(row=i//4,column=i%4,padx=10,pady=10)
    button.bind('<Button-1>',click)
    i=i+1
    
window.mainloop()