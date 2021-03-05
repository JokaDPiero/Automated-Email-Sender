import pyaudio
import speech_recognition as sr
import pyttsx3 
import smtplib
from email.message import EmailMessage
import getpass

engine=pyttsx3.init()
listener=sr.Recognizer()

def get_info():
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            #audio=listener.record(mic,duration=5)
            audio=listener.listen(mic,timeout=5)
            info=listener.recognize_google(audio)
            print(info)
            return info.lower()
    except:
        talk("Could not recognize your voice try again.")
        return "None"
    
def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def get_email_info():
    talk("To whom do you want to send the E-mail sir!")
    name=get_info()
    if name=='None':
        get_email_info()
    rcvr=names[name]
    print(names[name])
    talk("What will be the subject sir!")
    sub=get_info()
    print(sub)
    talk("Tell me the body of the E-mail sir!")
    body=get_info()
    print(body)
    send_mail(rcvr,sub,body)
    print("Email sent successfully!!!")
    talk("Do you want to continue sir?")
    send_more=get_info()
    if 'yes' in send_more:
        get_email_info()
    
def send_mail(receiver,subject,body):
    user=input("Enter your username(sender) :")
    password=getpass.getpass(prompt='Enter your password (sender) :')
    talk("The Email will be sent from "+user)
    talk("The receiver is "+receiver)

    port_tls=587
    port_ssl=465

    server=smtplib.SMTP('smtp.gmail.com',port_tls)
    #or server=smtplib.SMTP_SSL('smtp.gmail.com',port_ssl)
    server.ehlo()
    server.starttls()
    server.login(user,password)
    
    email=EmailMessage()
    email['From']=user
    email['To']=receiver
    email['Subject']=subject
    email.set_content(body)
    server.send_message(email)
    server.close() 

if __name__=='__main__':
    #Add people and their user names to send mail
    names={
        'xyz':'xyz@gmail.com',
        'abc':'abc@gmail.com',
        'pqr':'pqr@rediffmail.com',
        'lmn':'lmn@microsoft.com'
    }
    get_email_info()