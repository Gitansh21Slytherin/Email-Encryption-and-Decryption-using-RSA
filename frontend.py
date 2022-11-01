from tkinter import *
import smtplib
import time

import tkinter as tk
#import config
root = Tk()

#set up size of the window
root.geometry("1200x6000")


# set up the title of window
root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)


##################################################
lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="Message E&D using \n RSA",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

################################################

# Initializing variables
P = DoubleVar()
Q = DoubleVar()
E = DoubleVar()
mode = tk.StringVar()
msg = tk.StringVar()
keygen = tk.StringVar()
Result = tk.StringVar()
toemail = tk.StringVar()
password = tk.StringVar()
email = tk.StringVar()

##################################################################################################

# labels for the p#################################################
lblp = tk.Label(f1, font=('arial', 16, 'bold'),
               text="P", bd=16, anchor="w")

lblp.grid(row=1, column=0)
# Entry box for the p
txtp = tk.Entry(f1, font=('arial', 16, 'bold'),
               textvariable=P, bd=10, insertwidth=4,
               bg="powder blue", justify='right')


txtp.grid(row=1, column=1)
# labels for the q #################################################
lblQ = tk.Label(f1, font=('arial', 16, 'bold'),
               text="Q", bd=16, anchor="w")

lblQ.grid(row=2, column=0)


# Entry box for the q
txtQ = tk.Entry(f1, font=('arial', 16, 'bold'),
               textvariable=Q, bd=10, insertwidth=4,
               bg="powder blue", justify='right')

txtQ.grid(row=2, column=1)

#Label for e #################################################
lblE = tk.Label(f1, font=('arial', 16, 'bold'),
               text="E", bd=16, anchor="w")

lblE.grid(row=3, column=0)


# Entry box for the e
txtE = tk.Entry(f1, font=('arial', 16, 'bold'),
               textvariable=E, bd=10, insertwidth=4,
               bg="powder blue", justify='right')

txtE.grid(row=3, column=1)

# labels for the mode #################################################
lblmode = tk.Label(f1, font=('arial', 16, 'bold'),
                text="Mode(e/d)",
                bd=16, anchor="w")

lblmode.grid(row=4, column=0)
# Entry box for the mode
txtmode = tk.Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue", justify='right')

txtmode.grid(row=4, column=1)

# labels for the keygen#################################################
lblkey = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="Key Generator", bd=16, anchor="w")

lblkey.grid(row=5, column=0)

# Entry box for the keygen
txtkey = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=keygen, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtkey.grid(row=5, column=1)

# labels for the result#################################################
lblResult = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="The Result-", bd=16, anchor="w")

lblResult.grid(row=2, column=2)

# Entry box for the result
txtResult = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtResult.grid(row=2, column=3)

# labels for the  message#################################################
lblmsg = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="Message", bd=16, anchor="w")

lblmsg.grid(row=1, column=2)

# Entry box for the message
txtmsg = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=msg, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtmsg.grid(row=1, column=3)

# labels for the  email#################################################
lblemail = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="Mail Id", bd=16, anchor="w")

lblemail.grid(row=3, column=2)

# Entry box for the email
txtemail = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=email, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtemail.grid(row=3, column=3)
# labels for the  password#################################################
lblpass = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="Password", bd=16, anchor="w")

lblpass.grid(row=4, column=2)

# Entry box for the password
txtpass = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=password, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtpass.grid(row=4, column=3)

# labels for the  toemail#################################################
lbltoemail = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="TO", bd=16, anchor="w")

lbltoemail.grid(row=5, column=2)

# Entry box for the message
txttoemail = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=toemail, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txttoemail.grid(row=5, column=3)

###################################################################################################

import rsa_code

######################

#defining functions ###############



def Results():
    return (1)

def keygen():
    return(1)


def Reset():
    P.set("")
    Q.set("")
    E.set("")
    mode.set("")
    msg.set("")
    keygen.set("")
    Result.set("")

def qExit():
    root.destroy()

def qMail():
    try:
        Email =email.get()
        Password = password.get()
        msges = Result.get()
        toEmail = toemail.get()
        print("Message= ", (Result.get()))
        subject = "Test subject"
        #msg = "Hello there, how are you today?"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(Email, Password)
        message = 'Subject: {}\n\n{}'.format(subject, msges)
        server.sendmail(Email, toEmail, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")




### buttons

# Show message button
btnTotal = tk.Button(f1, padx=11, pady=5, bd=11,
                 fg="black", font=('arial', 8, 'bold'),
                 width=9,text="Show Message", bg="powder blue",
                  command=Results).grid(row=7, column=1)

# Reset button
btnReset = tk.Button(f1, padx=10, pady=4, bd=10,
                 fg="black", font=('arial', 8, 'bold'),
                 width=8, text="Reset", bg="green",
                  command=Reset).grid(row=7, column=2)


#mail button
btnMail = tk.Button(f1, padx=10, pady=4, bd=10,
                 fg="black", font=('arial', 8, 'bold'),
                 width=8, text="Mail", bg="blue",
                 command=qMail).grid(row=7, column=0)

#keygen button
btnkg = tk.Button(f1, padx=10, pady=4, bd=10,
                 fg="black", font=('arial', 8, 'bold'),
                 width=9, text="Generate Key", bg="green",
                 command=keygen).grid(row=7, column=3)

# Exit button
btnExit = tk.Button(f1, padx=10, pady=4, bd=10,
                 fg="black", font=('arial', 8, 'bold'),
                 width=8, text="Exit", bg="red",
                 command=qExit).grid(row=7, column=4)


root.mainloop()