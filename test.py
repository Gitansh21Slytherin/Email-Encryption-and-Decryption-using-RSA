from tkinter import *
import smtplib
import time
from hashlib import sha256
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
                text="Message Encryption using \n RSA",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

################################################

# Initializing variables
P = DoubleVar()
Q = DoubleVar()
#E = DoubleVar()
msg = tk.DoubleVar()
keygen = tk.StringVar()
Result = tk.StringVar()
toemail = tk.StringVar()
password = tk.StringVar()
email = tk.StringVar()
digisign = tk.StringVar()

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


# labels for the keygen#################################################
lblkey = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="Key Generator", bd=16, anchor="w")

lblkey.grid(row=3, column=0)

# Entry box for the keygen
txtkey = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=keygen, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtkey.grid(row=3, column=1)

# labels for the result#################################################
lblResult = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="The Result-", bd=16, anchor="w")

lblResult.grid(row=1, column=2)

# Entry box for the result
txtResult = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtResult.grid(row=1, column=3)

# labels for the  message#################################################
lblmsg = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="Message", bd=16, anchor="w")

lblmsg.grid(row=4, column=0)

# Entry box for the message
txtmsg = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=msg, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtmsg.grid(row=4, column=1)

# labels for the  email#################################################
lblemail = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="Mail Id", bd=16, anchor="w")

lblemail.grid(row=2, column=2)

# Entry box for the email
txtemail = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=email, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtemail.grid(row=2, column=3)
# labels for the  password#################################################
lblpass = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="Password", bd=16, anchor="w")

lblpass.grid(row=3, column=2)

# Entry box for the password
txtpass = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=password, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtpass.grid(row=3, column=3)

# labels for the  toemail#################################################
lbltoemail = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="TO", bd=16, anchor="w")

lbltoemail.grid(row=4, column=2)

# Entry box for the message
txttoemail = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=toemail, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txttoemail.grid(row=4, column=3)

# labels for the  digital signature #################################################
lblds = tk.Label(f1, font=('arial', 16, 'bold'),
                  text="Digital Signature", bd=16, anchor="w")

lblds.grid(row=5, column=2)

# Entry box for the message
txtds = tk.Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=digisign, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtds.grid(row=5, column=3)

###################################################################################################

#import rsa
p=379
q=37
n = p * q
fi = (p - 1) * (q - 1)

list_all = []

for i in range(2,n):
    list_all.append(i + 1)

def co_prime(number):
    list1 = []
    for i in range(2,number):
        if number%i == 0:
            list1.append(i)
    return (list1)

def remove_co_prime(list):
    for i in list:
        for ii in range(1, n // 2):
            if ii * i in list_all:
                list_all.remove(i * ii)

def remove_bigger(list):
    for i in list:
        if i in list_all:
            list_all.remove(i)


def dec_key(encryption_key):
    i = 1
    while i >0:
        formula = (1 + fi * i) % encryption_key
        dec = int((1 + fi * i) / encryption_key)
        if formula == 0:
            return (dec)
        i = i + 1

def encrypt(value):
    cipher = (value**encryption_key)%n
    return(cipher)




#def decrypt(value):
 #   decrypted = (value**decryption_key)%n
  #  return(decrypted)



list_n = co_prime(n)
list_fi = co_prime(fi)

remove_co_prime(list_n)
remove_co_prime(list_fi)

listbigger = []

for i in list_all:
    if i > fi:
        listbigger.append(i)

remove_bigger(listbigger)

encryption_key= list_all[0]
decryption_key = dec_key(encryption_key)
print('encryption key is:', encryption_key)
print('decryption key is:', decryption_key,n)

######################

#defining functions ###############



def Results():
    print("Message= ", (msg.get()))

    value = int(msg.get())
    #p = int(P.get())
    #q= int(Q.get())




    Result.set(encrypt(value))
    #return(p,q)


def keygens():

    keygen.set(dec_key(encryption_key))
    #keygen.set(n)

def Reset():
    P.set("")
    Q.set("")
    E.set("")
    #mode.set("")
    msg.set("")
    keygen.set("")
    email.set("")
    password.set("")
    toemail.set("")
    Result.set("")

def qExit():
    root.destroy()

def qMail():
    try:
        Email =email.get()
        Password = password.get()
        msges = Result.get()
        toEmail = toemail.get()
        msges2 = digisign.get()
        print("Message= ", (Result.get()))
        subject = "Test subject"
        #msg = "Hello there, how are you today?"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(Email, Password)
        message = 'Subject: {}\n\nMessage: {}\n\n"Digital Signature: {}'.format(subject, msges,msges2)
        server.sendmail(Email, toEmail, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


def qDigiSign():

     message = str(int(msg.get()))
     print(message)
     hashed = sha256(message.encode("UTF-8")).hexdigest()

     digisign.set(hashed)

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
                 command=keygens).grid(row=7, column=3)

# Exit button
btnExit = tk.Button(f1, padx=10, pady=4, bd=10,
                 fg="black", font=('arial', 8, 'bold'),
                 width=8, text="Exit", bg="red",
                 command=qExit).grid(row=7, column=4)

# digital signature button
btnDigiSign = tk.Button(f1, padx=10, pady=4, bd=10,
                 fg="black", font=('arial', 8, 'bold'),
                 width=8, text="Get DS", bg="green",
                 command=qDigiSign).grid(row=9, column=2)

root.mainloop()