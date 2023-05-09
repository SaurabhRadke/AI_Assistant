import tkinter as tk
import subfiles.Chatbot
import subfiles.prompt2
import subfiles.Salesforce
root=tk.Tk() # use to create new chat nav
root.geometry('350x450+30+400')
def getresult(message):
    arr=message.split(" ")
    if arr[0]=="Find":
        textarea.insert("end", "\nBot : Processing.... ")
        Location=arr[5]
        range=arr[-1]
        subfiles.Chatbot.Find_A_House(Location,range)
    elif arr[0]=="Add":
        textarea.insert("end", "Bot : Processing.... ")
        subfiles.prompt2.create_lead_salesforce()
    elif arr[0]=="Log":
        textarea.insert("end", "Bot : Processing.... ")
        subfiles.Salesforce.log_a_call_salesforce()

def botReply():
    question=query.get()
    textarea.insert("end","\nYou : "+question)
    query.delete(0, "end")
    getresult(question)



root.title("Chat Bot for new prompt")
root.config(bg="aquamarine")
# Headear Logo
head=tk.PhotoImage(file='subfiles/head1.png')
Insert_head=tk.Label(root,image=head)
Insert_head.config(bg='aquamarine')
Insert_head.pack()

#Frame[Conatiner for message]
Centeral_frame=tk.Frame(root)
Centeral_frame.pack()
scrol=tk.Scrollbar(Centeral_frame)
scrol.pack(side='right')

#Text area
textarea=tk.Text(Centeral_frame,font=('time new roman',10,'bold'),height=10,yscrollcommand=scrol.set)
textarea.pack(side='left')
scrol.config(command=textarea.yview)

#Enter message
query=tk.Entry(root,font=('verdana',10,'bold'),width=30)
query.pack(pady=15)

#Buttom
btn = tk.Button(root, text = 'Send !', bd = '5',command = botReply)
btn.pack()
root.mainloop() # use to hold our