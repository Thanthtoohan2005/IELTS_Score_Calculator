from tkinter import *
import customtkinter

def clean_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()



def realone():
    clean_frame(mainFrame)
    customtkinter.CTkLabel(mainFrame,text="Welcome",font=("Arial",20,"bold")).pack(padx=10,pady=10)
    instruction = customtkinter.CTkLabel(mainFrame,text="For those interested in checking their band scores, there are four main components available in this app.",font=("Georgia",15)).place(relx=0.01,rely=0.1)
    instruction = customtkinter.CTkLabel(mainFrame,text="1. Overall Band Score",font=("Georgia",15)).place(relx=0.01,rely=0.2)
    instruction = customtkinter.CTkLabel(mainFrame,text="2. Reading Band Score",font=("Georgia",15)).place(relx=0.01,rely=0.3)
    instruction = customtkinter.CTkLabel(mainFrame,text="3. Listening Band Score",font=("Georgia",15)).place(relx=0.01,rely=0.4)
    instruction = customtkinter.CTkLabel(mainFrame,text="4. General Reading Band Score",font=("Georgia",15)).place(relx=0.01,rely=0.5)
    instruction = customtkinter.CTkLabel(mainFrame,text="These scores are based on the number of correct answers out of 40 questions in each section. Each score range corresponds to a different band score.",font=("Georgia",15)).place(relx=0.01,rely=0.6)


def Listening():
    clean_frame(mainFrame)
    customtkinter.CTkLabel(mainFrame, text="Listening Band Score Calculation",font=("Arial",18,"bold")).place(relx=0.41,rely=0.02)
    customtkinter.CTkButton(mainFrame,text="Back to main section",command=realone).place(relx=0.65,rely=0.25)

    Lresult_label = customtkinter.CTkLabel(mainFrame,text="",font=("Arial",18,"bold"))
    Lresult_label.place(relx=0.43,rely=0.3)


    def Listening_submit():
     answerL = listening_entry.get()
     

     if answerL == "40" or answerL == "39":
        Lresult_label.configure(text="Your band score is 9!")
     elif answerL == "38" or answerL == "37":
        Lresult_label.configure(text="Your band score is 8.5!")
     elif answerL == "36" or answerL == "35":
        Lresult_label.configure(text="Your band score is 8!")
     elif answerL == "34" or answerL =="33" or answerL == "32":
        Lresult_label.configure(text="Your band score is 7.5!")
     elif  answerL == "31" or answerL=="30":
        Lresult_label.configure(text="Your band score is 7!")
     elif answerL == "29" or answerL == "28" or answerL=="27" or answerL=="26":
        Lresult_label.configure(text="Your band score is 6.5!")
     elif answerL == "25" or answerL=="24" or answerL=="23":
        Lresult_label.configure(text="Your band score is 6!")
     elif answerL == "22" or answerL == "21" or answerL == "20" or answerL == "19" or answerL == "18":
        Lresult_label.configure(text="Your band score is 5.5!")
     elif answerL == "17" or answerL == "16":
        Lresult_label.configure(text="Your band score is 5!")
     elif  answerL == "15" or answerL == "14" or answerL == "13":
        Lresult_label.configure(text="Your band score is 4.5!")
     elif answerL == "12" or answerL == "11" or answerL == "10":
        Lresult_label.configure(text="Your band score is 4!")
     elif answerL == "9" or answerL == "8":
        Lresult_label.configure(text="Your band score is 3.5!")
     elif answerL == "7" or answerL ==  "6":
        Lresult_label.configure(text="Your band score is 3!")
     elif answerL == "5" or answerL == "4":
        Lresult_label.configure(text="Your band score is 2.5!")
     elif answerL == "3" or answerL == "2":
        Lresult_label.configure(text="Your band score is 2!")
     elif answerL == "1":
        Lresult_label.configure(text="Your band score is 1.5!")
     elif answerL == "0":
        Lresult_label.configure(text="Your band score is 0!")
     else:
        Lresult_label.configure(text="Please Enter a valid score!")

    def reset():
       listening_entry.delete(0,"end")
      
       Lresult_label.configure(text="")

    listening_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Enter number of correct answers!",width=200,height=30)
    listening_entry.place(relx=0.422,rely=0.15)

  
    listening_submit_button = customtkinter.CTkButton(mainFrame,text="Submit",hover_color="blue",command=Listening_submit)
    listening_submit_button.place(relx=0.45,rely=0.25)

    reset_button = customtkinter.CTkButton(mainFrame,text="Reset",hover_color="blue",command=reset)
    reset_button.place(relx=0.25,rely=0.25)

    


def reading():
    clean_frame(mainFrame)
    customtkinter.CTkLabel(mainFrame, text="Reading Band Score Calculation",font=("Arial",18,"bold")).place(relx=0.4,rely=0.02)
    customtkinter.CTkButton(mainFrame,text="Back to main section",command=realone).place(relx=0.65,rely=0.25)
    
    Rresult_label = customtkinter.CTkLabel(mainFrame,text="",font=("Arial",18,"bold"))
    Rresult_label.place(relx=0.43,rely=0.3)

    def reading_submit():
     answerR = reading_entry.get()
     

     if answerR == "40" or answerR =="39":
        Rresult_label.configure(text="Your band score is 9!")
     elif answerR == "38" or answerR == "37":
        Rresult_label.configure(text="Your band score is 8.5!")
     elif answerR == "36" or answerR == "35":
        Rresult_label.configure(text="Your band score is 8!")
     elif answerR == "34" or answerR =="33":
        Rresult_label.configure(text="Your band score is 7.5!")
     elif answerR == "32" or answerR == "31" or answerR=="30":
        Rresult_label.configure(text="Your band score is 7!")
     elif answerR == "29" or answerR == "28" or answerR=="27":
        Rresult_label.configure(text="Your band score is 6.5!")
     elif answerR == "26" or answerR == "25" or answerR=="24" or answerR=="23":
        Rresult_label.configure(text="Your band score is 6!")
     elif answerR == "22" or answerR == "21" or answerR == "20" or answerR == "19":
        Rresult_label.configure(text="Your band score is 5.5!")
     elif answerR == "18" or answerR == "17" or answerR == "16" or answerR == "15":
        Rresult_label.configure(text="Your band score is 5!")
     elif answerR == "14" or answerR == "13":
        Rresult_label.configure(text="Your band score is 4.5!")
     elif answerR == "12" or answerR == "11" or answerR == "10":
        Rresult_label.configure(text="Your band score is 4!")
     elif answerR == "9" or answerR == "8":
        Rresult_label.configure(text="Your band score is 3.5!")
     elif answerR == "7" or answerR ==  "6":
        Rresult_label.configure(text="Your band score is 3!")
     elif answerR == "5" or answerR == "4":
        Rresult_label.configure(text="Your band score is 2.5!")
     elif answerR == "3" or answerR == "2":
        Rresult_label.configure(text="Your band score is 2!")
     elif answerR == "1":
        Rresult_label.configure(text="Your band score is 1.5!")
     elif answerR == "0":
        Rresult_label.configure(text="Your band score is 0!")
     else:
        Rresult_label.configure(text="Please Enter a valid score!")

    def reset():
       reading_entry.delete(0,"end")
      
       Rresult_label.configure(text="")


    reading_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Enter number of correct answers!",width=200,height=30)
    reading_entry.place(relx=0.422,rely=0.15)

    reading_submit_button = customtkinter.CTkButton(mainFrame,text="Submit",hover_color="blue",command=reading_submit)
    reading_submit_button.place(relx=0.45,rely=0.25)

    reset_button = customtkinter.CTkButton(mainFrame,text="Reset",hover_color="blue",command=reset)
    reset_button.place(relx=0.25,rely=0.25)

def general_reading():
    clean_frame(mainFrame)
    customtkinter.CTkLabel(mainFrame, text="General Reading Band Score Calculation",font=("Arial",18,"bold")).place(relx=0.39,rely=0.02)
    customtkinter.CTkButton(mainFrame,text="Back to main section",command=realone).place(relx=0.65,rely=0.25)
    
    Rresult_label = customtkinter.CTkLabel(mainFrame,text="",font=("Arial",18,"bold"))
    Rresult_label.place(relx=0.43,rely=0.3)

    def general_reading_submit():
     answerR = general_reading_entry.get()
     

     if answerR == "40":
        Rresult_label.configure(text="Your band score is 9!")
     elif answerR =="39":
        Rresult_label.configure(text="Your band score is 8.5!")
     elif answerR == "37" or answerR == "38":
        Rresult_label.configure(text="Your band score is 8!")
     elif answerR == "36":
        Rresult_label.configure(text="Your band score is 7.5!")
     elif answerR == "34" or answerR == "35":
        Rresult_label.configure(text="Your band score is 7!")
     elif answerR == "32" or answerR == "33":
        Rresult_label.configure(text="Your band score is 6.5!")
     elif answerR == "30" or answerR == "31":
        Rresult_label.configure(text="Your band score is 6!")
     elif answerR == "27" or answerR == "28" or answerR == "29":
        Rresult_label.configure(text="Your band score is 5.5!")
     elif answerR == "23" or answerR == "24" or answerR == "25" or answerR == "26":
        Rresult_label.configure(text="Your band score is 5!")
     elif answerR == "19" or answerR == "20" or answerR == "21"or answerR == "22":
        Rresult_label.configure(text="Your band score is 4.5!")
     elif answerR == "15" or answerR == "16" or answerR == "17" or answerR == "18":
        Rresult_label.configure(text="Your band score is 4!")
     elif answerR == "12" or answerR == "13" or answerR == "14":
        Rresult_label.configure(text="Your band score is 3.5!")
     elif answerR == "9" or answerR ==  "10"  or answerR == "11":
        Rresult_label.configure(text="Your band score is 3!")
     elif answerR == "6" or answerR == "7" or answerR == "8":
        Rresult_label.configure(text="Your band score is 2.5!")
     elif answerR == "0" or answerR == "1" or answerR == "2" or answerR == "3" or answerR == "4" or answerR == "5":
        Rresult_label.configure(text="Your band score is 0!")
     else:
        Rresult_label.configure(text="Please Enter a valid score!")

    def reset():
       general_reading_entry.delete(0,"end")
      
       Rresult_label.configure(text="")


    general_reading_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Enter number of correct answers!",width=200,height=30)
    general_reading_entry.place(relx=0.422,rely=0.15)

    general_reading_submit_button = customtkinter.CTkButton(mainFrame,text="Submit",hover_color="blue",command=general_reading_submit)
    general_reading_submit_button.place(relx=0.45,rely=0.25)

    reset_button = customtkinter.CTkButton(mainFrame,text="Reset",hover_color="blue",command=reset)
    reset_button.place(relx=0.25,rely=0.25)


  
def OBS():
   clean_frame(mainFrame)
   customtkinter.CTkLabel(mainFrame, text="Hello! This is for your Overall Band Score calculation",font=("Arial",18,"bold")).place(relx=0.32,rely=0.02)
   customtkinter.CTkButton(mainFrame,text="Back to main section",command=realone).place(relx=0.65,rely=0.55)
   customtkinter.CTkLabel(mainFrame, text="Listening band score ",fg_color="lightyellow",corner_radius=10).place(relx=0.29,rely=0.15)
   customtkinter.CTkLabel(mainFrame, text="Reading band score",fg_color="lightyellow",corner_radius=10).place(relx=0.29,rely=0.25)
   customtkinter.CTkLabel(mainFrame, text="Writing band score",fg_color="lightyellow",corner_radius=10).place(relx=0.29,rely=0.35)
   customtkinter.CTkLabel(mainFrame, text="Speaking band score",fg_color="lightyellow",corner_radius=10).place(relx=0.29,rely=0.45)

   Oresult_label = customtkinter.CTkLabel(mainFrame,text="",font=("Arial",18,"bold"))
   Oresult_label.place(relx=0.4,rely=0.7)



   def calculate():
    
    try:
       L = float(listening_entry.get().strip())
       R = float(reading_entry.get().strip())
       W = float(writing_entry.get().strip())
       S = float(speaking_entry.get().strip())

       
       

       add = L+R+W+S
       average = add/4



       if average % 1 >= 0.75:
          result = int(average) + 1
          Oresult_label.configure(text=f"Congratulation! Your overall band score is {result}!")
          

       elif average % 1 >= 0.5:
          result = int(average)+0.5
          Oresult_label.configure(text=f"Congratulation! Your overall band score is {result}!")
      
       elif average % 1 >= 0.25:
          result = int(average)+0.5
          Oresult_label.configure(text=f"Congratulation! Your overall band score is {result}!")
       elif average > 9:
          result = int(average)
          Oresult_label.configure(text="Score must be between 0 and 9.")

       else:
          result = int(average)
          Oresult_label.configure(text=f"Congratulation! Your overall band score is {result}!")

        

       
         
   


    except ValueError:
      Oresult_label.configure(text="Please enter valid score!")
       

   def reset():
      listening_entry.delete(0,"end")
      reading_entry.delete(0,"end")
      writing_entry.delete(0,"end")
      speaking_entry.delete(0,"end")
      Oresult_label.configure(text="")

     
     

   listening_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Please enter valid band score!",width=200,height=30)
   listening_entry.place(relx=0.422,rely=0.15)

  
   

   reading_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Please enter valid band score!",width=200,height=30)
   reading_entry.place(relx=0.422,rely=0.25)
  

   writing_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Please enter valid band score!",width=200,height=30)
   writing_entry.place(relx=0.422,rely=0.35)
  
  

   speaking_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Please enter valid band score!",width=200,height=30)
   speaking_entry.place(relx=0.422,rely=0.45)
   

   

   overall_band_score_button = customtkinter.CTkButton(mainFrame,text="Calculate",hover_color="blue",command=calculate)
   overall_band_score_button.place(relx=0.45,rely=0.55)

   reset_button = customtkinter.CTkButton(mainFrame,text="Reset",hover_color="blue",command=reset)
   reset_button.place(relx=0.25,rely=0.55)


 
  
    




customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.title("IELTS Calculator")
root.geometry("400x400")


mainFrame = customtkinter.CTkFrame(root,border_color="black",border_width=2)
mainFrame.pack(side="right",fill="both",expand=True)

buttonFrame = customtkinter.CTkFrame(root,border_color="black",border_width=2)
buttonFrame.pack(side="right",fill="y",padx=11)


listeningButton= customtkinter.CTkButton(buttonFrame,text="Listening",border_color="black",border_width=2,command=Listening)
listeningButton.place(relx=0.16,rely=0.5)


readingButton= customtkinter.CTkButton(buttonFrame,text="Reading",border_color="black",border_width=2,command=reading)
readingButton.place(relx=0.16,rely=0.4)

overall_band_score = customtkinter.CTkButton(buttonFrame,text="Overall Band Score",border_color="black",border_width=2,command=OBS)
overall_band_score.place(relx=0.16,rely=0.3)

GeneralreadingButton= customtkinter.CTkButton(buttonFrame,text="General Reading",border_color="black",border_width=2,command=general_reading)
GeneralreadingButton.place(relx=0.16,rely=0.6)


realone()
root.mainloop()