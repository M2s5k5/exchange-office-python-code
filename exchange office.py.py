from tkinter import *
import tkinter.ttk as ttk

def currency_converter():
    currency_converter = Tk()  
    #Naslov  
    currency_converter.title("Menjacnica paja")
    #Postavka dimenzija 
    currency_converter.geometry("500x300")
    #Centar prozora
    currency_converter.update_idletasks()
    w = currency_converter.winfo_screenwidth()
    h = currency_converter.winfo_screenheight()
    size = tuple(int(_) for _ in currency_converter.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    currency_converter.geometry("%dx%d+%d+%d" % (size + (x, y))) 

    currency_converter.rowconfigure(5, weight=1)

    currency_converter.lift()


    currency_converter.configure(background='#007780')
#Definisanje funkcije prilikom izbora valute
    def enter(event):
        #izbor pojasnjeno -- izbor*suma_value, 2 je format nema vez sa mnozenjem valute
        izbor = float(Currency_Input.get().replace(',', '.'))
        #brisanje unesene vrednosti
        Currency_Output.delete(0,END)
        Currency_Output1.delete(0,END)
        Currency_Output2.delete(0,END)
        if box.get() == "EUR":            
            Currency_Output_Label.config(text="USD")
            Currency_Output.insert(0,round(izbor*1.18,2))
            Currency_Output1_Label.config(text="Kuna")
            Currency_Output1.insert(0,round(izbor*7.60,2))
            Currency_Output2_Label.config(text="RSD")
            Currency_Output2.insert(0,round(izbor*120.00,2))
        elif box.get() == "USD":
            Currency_Output_Label.config(text="EUR")
            Currency_Output.insert(0,round(izbor*0.85,2))
            Currency_Output1_Label.config(text="Kuna")
            Currency_Output1.insert(0,round(izbor*6.42,2))
            Currency_Output2_Label.config(text="RSD")
            Currency_Output2.insert(0,round(izbor*99.79,2))
        elif box.get() == "Kuna":
            Currency_Output_Label.config(text="EUR")
            Currency_Output.insert(0,round(izbor*0.13,2))
            Currency_Output1_Label.config(text="USD")
            Currency_Output1.insert(0,round(izbor*0.16,2))
            Currency_Output2_Label.config(text="RSD")
            Currency_Output2.insert(0,round(izbor*15.53,2))

        elif box.get() == "RSD":
            Currency_Output_Label.config(text="EUR")
            Currency_Output.insert(0,round(izbor*0.0075,2))
            Currency_Output1_Label.config(text="USD")
            Currency_Output1.insert(0,round(izbor*0.010,2))
            Currency_Output2_Label.config(text="Kuna")
            Currency_Output2.insert(0,round(izbor*0.064,2))
    #definisanje izlaza iz menjacnice
    def close_currency_converter():
        currency_converter.destroy()
    #Glavni tekst u progarmu tkzv. Heder
    Headline_Label = Label(currency_converter, text='Menjacnica Paja 1.0', bg='#007780', fg='white',font=("Century Gothic",16))
    Headline_Label.grid(row=0,column=0, columnspan=2, padx=5, pady=5, sticky=W)

    Box_Headline_Label = Label(currency_converter, text='Koju valutu zelite da promenite:', bg='#007780', fg='white',font=("Century Gothic",11))
    Box_Headline_Label.grid(row=1,column=0, columnspan=1, padx=5, pady=5, sticky=W)
    #Podesavanje "Box-a" u kome se nalaze valute "--values-- je funkcija"
    box_value = StringVar() 
    box = ttk.Combobox(currency_converter, textvariable=box_value, width=10)
    box['values'] = ('EUR', 'USD', 'Kuna', 'RSD')
    box.current(0)
    box.grid(row=1,column=1, pady=5, sticky=E)
    #definisanje Currency_Input kao unos korisnika
    Currency_Input = Entry(currency_converter)
    Currency_Input.grid(row=1,column=2, padx=10, pady=5, sticky=W)

    Currency_Input.bind('<Return>',enter)

    Currency_Output_Label = Label(currency_converter, text='', bg='#007780', fg='white',font=("Century Gothic",11))
    Currency_Output_Label.grid(row=2,column=1, padx=5, pady=5, sticky=W)

    Currency_Output1_Label = Label(currency_converter, text='', bg='#007780', fg='white',font=("Century Gothic",11))
    Currency_Output1_Label.grid(row=3,column=1, padx=5, pady=5, sticky=W)   

    Currency_Output2_Label = Label(currency_converter, text='', bg='#007780', fg='white',font=("Century Gothic",11))
    Currency_Output2_Label.grid(row=4,column=1, padx=5, pady=5, sticky=W)  

    Currency_Output = Entry(currency_converter)
    Currency_Output.grid(row=2,column=2, padx=10, pady=5, sticky=W)

    Currency_Output1 = Entry(currency_converter)
    Currency_Output1.grid(row=3,column=2, padx=10, pady=5, sticky=W)

    Currency_Output2 = Entry(currency_converter)
    Currency_Output2.grid(row=4,column=2, padx=10, pady=5, sticky=W)

    Button(currency_converter,text="Izlaz",command=close_currency_converter).grid(row=6,column=0, sticky=E+S+W, pady=5, padx=5)

    currency_converter.mainloop()

currency_converter()


mainloop()