from tkinter import *
from tkinter import messagebox
from mydb import Database
from myapi import API


class NlPApp:
    def __init__(self):
        
        #create db object
        self.db=Database()
        self.api=API()
        
        
        self.root = Tk()
        self.root.title("NlP APP")
        self.root.iconbitmap("resources/logo.png")
        self.root.geometry("800x800")
        self.root.configure(bg="#1C2B4A")  

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        
        self.clear( )
        main_label = Label(self.root, text="NLP Dashboard", bg="#1C2B4A", fg="white", width=50)
        main_label.pack(pady=(30, 20), padx=(10, 10))
        main_label.configure(font=("verdana", 40, "bold"))

        main_labe2 = Label(self.root, text="Login Page ", bg="#1C2B4A", fg="white")
        main_labe2.pack()
        main_labe2.configure(font=("verdana", 30, 'bold'))

        label1 = Label(self.root, text="Email Address ", bg="#1C2B4A", fg="white")
        label1.pack(pady=(30, 30))

        self.email_input = Entry(self.root, bg="white", fg="black", width=50)
        self.email_input.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.root, text="Password", bg="#1C2B4A", fg="white")
        label2.pack(pady=(30, 30))

        self.password_input = Entry(self.root, bg="white", fg="black", width=50,show="*")
        self.password_input.pack(pady=(5, 10), ipady=5)

        login_btn = Button(self.root, text="Sign In", width=20, height=3, bg="white", fg="black",command=self.perform_login)
        login_btn.pack(pady=(10, 10))

        label2 = Label(self.root, text="Don’t have an account?", bg="#1C2B4A", fg="white")
        label2.pack(pady=(30, 30))

        redirect_btn = Button(self.root, text="Sign Up", bg="white", fg="black",command=self.signup_gui)
        redirect_btn.pack(pady=(20, 10))
    
    
    def signup_gui(self):
        self.clear()
        
        
        main_label = Label(self.root, text="NLP Dashboard", bg="#1C2B4A", fg="white", width=50)
        main_label.pack(pady=(30, 20), padx=(10, 10))
        main_label.configure(font=("verdana", 40, "bold"))

        main_labe2 = Label(self.root, text="Sign Up Page ", bg="#1C2B4A", fg="white")
        main_labe2.pack()
        main_labe2.configure(font=("verdana", 30, 'bold'))
        
        label3 = Label(self.root, text="Name ", bg="#1C2B4A", fg="white")
        label3.pack(pady=(30, 30))

        self.name_input = Entry(self.root, bg="white", fg="black", width=50)
        self.name_input.pack(pady=(5, 10), ipady=5)

        label1 = Label(self.root, text="Email Address ", bg="#1C2B4A", fg="white")
        label1.pack(pady=(30, 30))

        self.email_input = Entry(self.root, bg="white", fg="black", width=50)
        self.email_input.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.root, text="Password", bg="#1C2B4A", fg="white")
        label2.pack(pady=(30, 30))

        self.password_input = Entry(self.root, bg="white", fg="black", width=50,show="*")
        self.password_input.pack(pady=(5, 10), ipady=5)

        register_btn = Button(self.root, text="Sign Up", width=20, height=3, bg="white", fg="black",command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label2 = Label(self.root, text="Already have an account?", bg="#1C2B4A", fg="white")
        label2.pack(pady=(30, 30))

        redirect_btn = Button(self.root, text="Login", bg="white", fg="black",command=self.login_gui)
        redirect_btn.pack(pady=(20, 10))
        
        
    def clear(self):
        #clearing the existing Gui
        for i in self.root.pack_slaves():
            i.destroy()
            
    def perform_registration(self):
        #fetch data from the GUI
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        
        
        respone =self.db.add_data(name,email,password)
        if respone:
            messagebox.showinfo("Success","Sign up completed")
        else:
            messagebox.showerror("Error ","Email already exists")
    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        
        response =self.db.search(email,password)
        if response:
            messagebox.showinfo("Success","Login suceesful")
            self.home_gui()
        else:
            messagebox.showerror("Error ","Incorrect Email/Password")
            
        
    def home_gui(self):
        self.clear()
        
        main_label = Label(self.root, text="NLP Dashboard", bg="#1C2B4A", fg="white", width=50)
        main_label.pack(pady=(30, 20), padx=(10, 10))
        main_label.configure(font=("verdana", 40, "bold"))
        
        sentimen_btn = Button(self.root, text="Sentiment Analysis", width=50, height=5, bg="white", fg="black",command=self.perform_Sentiment_Analysis)
        sentimen_btn.pack(pady=(30, 30))
        
        NER = Button(self.root, text="Name Entity Recognition", width=50, height=5, bg="white", fg="black",command=self.perform_Ner)
        NER.pack(pady=(30, 30))
        
        emotion_btn = Button(self.root, text="Headline Generation", width=50, height=5, bg="white", fg="black",command=self.headline_generation)
        emotion_btn.pack(pady=(30, 30))
        
        emotion_btn = Button(self.root, text="Logout", width=50, height=5, bg="white", fg="black",command=self.login_gui)
        emotion_btn.pack(pady=(30, 30))

        
        
    def perform_Sentiment_Analysis(self):
        self.clear()       
        main_label = Label(self.root, text="NLP Dashboard", bg="#1C2B4A", fg="white", width=50)
        main_label.pack(pady=(30, 20), padx=(10, 10))
        main_label.configure(font=("verdana", 40, "bold"))
        
        
        main_label2 = Label(self.root, text="Sentiment Analysis", bg="#1C2B4A", fg="white", width=30)
        main_label2.pack(pady=(30, 20), padx=(10, 10))
        main_label2.configure(font=("verdana", 20, "bold"))
        
        label1 = Label(
        self.root,
        text="Enter the text",
        bg="#1C2B4A",
        fg="white",
        width=40,
        height=3,
        font=("Helvetica", 20, "bold")  # ← This is the magic line
            )
        label1.pack(pady=(10, 10))
        
        self.senti_input = Entry(self.root, bg="white", fg="black", width=40)
        self.senti_input.pack(pady=(5, 10), ipady=5)
        
        
        sentiment_btn = Button(self.root, text="Analyse Sentiment ", bg="white", fg="black",command=self.do_senti)
        sentiment_btn.pack(pady=(20, 10))
        
        self.sentiment_result = Label(self.root, text="", bg="#1C2B4A", fg="white", width=30)
        self.sentiment_result.pack(pady=(30, 20), padx=(10, 10))
        self.sentiment_result.configure(font=("verdana", 30))
        
        redirect_btn = Button(self.root, text="GO Back", bg="white", fg="black",command=self.home_gui)
        redirect_btn.pack(pady=(20, 10))
        

    def do_senti(self):
        text=self.senti_input.get()
        response=self.api.sentimental_analysis(text)
        text = ''
        for i in response['scored_labels']:
            label = i['label']
            score = round(i['score'], 3)
            text += f"{label} -> {score}\n"
        
        self.sentiment_result['text']=text
        
        
    
        


    def headline_generation(self):
        self.clear()       
        main_label = Label(self.root, text="NLP Dashboard", bg="#1C2B4A", fg="white", width=50)
        main_label.pack(pady=(30, 20), padx=(10, 10))
        main_label.configure(font=("verdana", 40, "bold"))
        
        
        main_label2 = Label(self.root, text="Headline Generation", bg="#1C2B4A", fg="white", width=30)
        main_label2.pack(pady=(30, 20), padx=(10, 10))
        main_label2.configure(font=("verdana", 20, "bold"))
        
        label1 = Label(
        self.root,
        text="Enter the text",
        bg="#1C2B4A",
        fg="white",
        width=40,
        height=3,
        font=("Helvetica", 20, "bold")  # ← This is the magic line
            )
        label1.pack(pady=(10, 10))
        
        self.senti_input = Entry(self.root, bg="white", fg="black", width=40)
        self.senti_input.pack(pady=(5, 10), ipady=5)
        
        
        sentiment_btn = Button(self.root, text="Generate headline ", bg="white", fg="black",command=self.do_head_)
        sentiment_btn.pack(pady=(20, 10))
        
        self.headline_generation_result = Label(
        self.root,
        text="",
        bg="#1C2B4A",
        fg="white",
        wraplength=700,  # pixels
        justify="center",
        font=("verdana", 20),
    )
        self.headline_generation_result.pack(pady=(30, 20), padx=(20, 20))

        
        redirect_btn = Button(self.root, text="GO Back", bg="white", fg="black",command=self.home_gui)
        redirect_btn.pack(pady=(20, 10))
        

    def do_head_(self):
        text=self.senti_input.get()
        response=self.api.generate_headline(text)
        self.headline_generation_result.config(text=response["summary_text"])
        

    def perform_Ner(self):
        self.clear()       
        main_label = Label(self.root, text="NLP Dashboard", bg="#1C2B4A", fg="white", width=50)
        main_label.pack(pady=(30, 20), padx=(10, 10))
        main_label.configure(font=("verdana", 40, "bold"))
        
        
        main_label2 = Label(self.root, text="Name Entity Recognition", bg="#1C2B4A", fg="white", width=30)
        main_label2.pack(pady=(30, 20), padx=(10, 10))
        main_label2.configure(font=("verdana", 20, "bold"))
        
        label1 = Label(
        self.root,
        text="Enter the text",
        bg="#1C2B4A",
        fg="white",
        width=40,
        height=3,
        font=("Helvetica", 20, "bold")  # ← This is the magic line
            )
        label1.pack(pady=(10, 10))
        
        self.senti_input = Entry(self.root, bg="white", fg="black", width=40)
        self.senti_input.pack(pady=(5, 10), ipady=5)
        
        label1 = Label(
        self.root,
        text="Search Word",
        bg="#1C2B4A",
        fg="white",
        width=40,
        height=3,
        font=("Helvetica", 20, "bold")  # ← This is the magic line
            )
        label1.pack(pady=(10, 10))
        
        self.senti_input2 = Entry(self.root, bg="white", fg="black", width=40)
        self.senti_input2.pack(pady=(5, 10), ipady=5)
        
        
        sentiment_btn = Button(self.root, text="Perform NER", bg="white", fg="black",command=self.do_ner)
        sentiment_btn.pack(pady=(20, 10))
        
        self.ner_result = Label(self.root, text="", bg="#1C2B4A", fg="white", width=30)
        self.ner_result.pack(pady=(30, 20), padx=(10, 10))
        self.ner_result.configure(font=("verdana", 30))
        
        redirect_btn = Button(self.root, text="GO Back", bg="white", fg="black",command=self.home_gui)
        redirect_btn.pack(pady=(20, 10))
        

    def do_ner(self):
        text=self.senti_input.get()
        search=self.senti_input2.get()
        response=self.api.name_entity_search(text,search)
        text = ''
        for entity in response['entities']:
            entity_text = entity['text']
            entity_type = entity['type']
            text += f"{entity_text} -> {entity_type}\n"

        self.ner_result.config(text=text)

        

    
        
    


        
            
nlp = NlPApp()