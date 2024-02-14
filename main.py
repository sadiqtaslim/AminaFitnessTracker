import csv
from os import spawnve
from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox
import schedule
import time
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

def Tracker():
  window = CTk() 
  window.title("Fitness Tracker")
  window.geometry("650x600") 
  window.config(bg='white')

  Autumn = "Autumn in November"
  tsize = 50
  tweight = "bold"
  
  titlefont = CTkFont(family=Autumn, size= tsize, weight= tweight)
  title = CTkLabel(window, 
                   text_color="hotpink", 
                   text = "Amina's Fitness Tracker", 
                   font=titlefont, 
                   bg_color="white")
  title.place(x=40, y=180)

  back1 = Image.open("pink2.png")
  back1data = CTkImage(dark_image=back1, light_image=back1,size=(200,200))

  backlabel1 = CTkLabel(window,image = back1data, text="")
  backlabel1.place(x=0, y=0)
  backlabel1.lower()

  back2 = Image.open("pink1.jpg")
  back2data = CTkImage(dark_image=back2, light_image=back2,size=(400,100))

  backlabel2 = CTkLabel(window,image = back2data, text="")
  backlabel2.place(x=100, y=420)
  backlabel2.lower()

 

  def Cal():


    class MyWindow:
      def __init__(self, win):
        self.am = CTkButton(win, 
                            text='Add Meals', 
                            command=self.add,
                            bg_color="white", 
                            fg_color="hotpink", 
                            hover_color="hotpink4",
                            corner_radius=64)       
        self.am.place(x=260, y=300)
        self.md = CTkButton(win, 
                            text = 'All Meals', 
                            command = self.meals, 
                            bg_color="white", 
                            fg_color="hotpink",
                            hover_color="hotpink4", 
                            corner_radius=64)
        self.md.place(x=260, y=340)
        

      def add(self):
        class AddCal:
          def __init__(self, win):

            Autumn = "Autumn in November"
            size = 20
            weight = "bold"
            labelfont = CTkFont(family=Autumn, size= size, weight= weight)

            title = CTkLabel(win,
                             text="Add Foods", 
                             font=titlefont, 
                             bg_color="white", 
                             text_color="hotpink")
            title.place(x=185, y=100)
    
            self.add = CTkEntry(win, 
                                bg_color="white", 
                                fg_color="white", 
                                corner_radius=64, 
                                border_color="hotpink", 
                                text_color="black")
            self.add.place(x=260, y=200)


            def CalSlider(value):
              self.calint.configure(text=int(value))
            

            self.cal = CTkSlider(win,
                                 bg_color="white",
                                 progress_color="hotpink",
                                 button_color= "hotpink",
                                 button_hover_color="hotpink4",
                                 orientation="horizontal",
                                 from_=0,
                                 to=200,
                                 number_of_steps=200,
                                 command=CalSlider)
            self.cal.set(0)
            self.cal.place(x=245, y=270)

            

            self.calint = CTkLabel(win,
                                   bg_color="white",
                                   text_color="black",
                                   text="")
            self.calint.place(x=450, y=263)

            self.calname = CTkLabel(win,
                                bg_color = "white",
                                text_color="hotpink",
                                text="Calories",
                                font=labelfont)
            self.calname.place(x=300,y=235)

            def Submit():
              food = self.add.get()
              calories = int(self.cal.get())
              protein = int(self.pro.get())
              carbs = int(self.carb.get())
              fats = int(self.fat.get())
              
              
              
              with open('foods.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([food, calories, protein, carbs, fats])
                self.add.delete(0, END)
            

            self.addfood = CTkButton(win,
                                text = "->",
                                width=3, 
                                bg_color="white", 
                                fg_color="hotpink", 
                                corner_radius=64, 
                                text_color="white",
                                hover_color="hotpink4",
                                command=Submit)
            self.addfood.place(x=410, y=200)

            def ProSlider(value):
              self.proint.configure(text=int(value))

            self.pro = CTkSlider(win,
                                 bg_color="white",
                                 progress_color="hotpink",
                                 button_color= "hotpink",
                                 button_hover_color="hotpink4",
                                 orientation="horizontal",
                                 from_=0,
                                 to=200,
                                 number_of_steps=200,
                                 command=ProSlider)
            self.pro.set(0)
            self.pro.place(x=245, y=320)

            

            self.proint = CTkLabel(win,
                                   bg_color="white",
                                   text_color="black",
                                   text="")
            self.proint.place(x=450, y=313)

            self.proname = CTkLabel(win,
                                bg_color = "white",
                                text_color="hotpink",
                                text="Protein",
                                font=labelfont)
            self.proname.place(x=300,y=290)

            def CarbSlider(value):
              self.carbint.configure(text=int(value))

            self.carb = CTkSlider(win,
                                 bg_color="white",
                                 progress_color="hotpink",
                                 button_color= "hotpink",
                                 button_hover_color="hotpink4",
                                 orientation="horizontal",
                                 from_=0,
                                 to=200,
                                 number_of_steps=200,
                                 command=CarbSlider)
            self.carb.set(0)
            self.carb.place(x=245, y=370)

            

            self.carbint = CTkLabel(win,
                                   bg_color="white",
                                   text_color="black",
                                   text="")
            self.carbint.place(x=450, y=363)

            self.carbname = CTkLabel(win,
                                bg_color = "white",
                                text_color="hotpink",
                                text="Carbs",
                                font=labelfont)
            self.carbname.place(x=300,y=340)

            def FatSlider(value):
              self.fatint.configure(text=int(value))
            
            self.fat = CTkSlider(win,
                                 bg_color="white",
                                 progress_color="hotpink",
                                 button_color= "hotpink",
                                 button_hover_color="hotpink4",
                                 orientation="horizontal",
                                 from_=0,
                                 to=200,
                                 number_of_steps=200,
                                 command=FatSlider)
            self.fat.set(0)
            self.fat.place(x=245, y=420)

            self.fatint = CTkLabel(win,
                                   bg_color="white",
                                   text_color="black",
                                   text="")
            self.fatint.place(x=450, y=413)

            self.fatname = CTkLabel(win,
                                bg_color = "white",
                                text_color="hotpink",
                                text="Fats",
                                font=labelfont)
            self.fatname.place(x=300,y=390)


        win2 = CTk()
        addwin = AddCal(win2)
        win2.title('Add Meals') 
        win2.geometry("650x600") 
        win2.config(bg='white')
        win2.mainloop()
      def meals(self):
        
        class Meals:
          def __init__(self, win):


            self.maclabel = CTkLabel(win,
                                     bg_color="white",
                                     fg_color="white",
                                     text_color="black",
                                     text = "Calories:          Protein:          Carbs:          Fats: ")
            self.maclabel.place(x=180, y=320)

            def Show(value):
              with open('foods.csv', 'r', newline='') as file:
                macreader = csv.reader(file)
                for row in macreader:
                  if row[0] == value:
                    c = row[1]
                    p = row[2]
                    ca = row[3]
                    f = row[4]

                    break
                self.maclabel.configure(text= f"Calories: {c}    Protein: {p}    Carbs: {ca}    Fats: {f}")
                

            def Delete():
              enterfood = CTkEntry(win, 
                              bg_color="white", 
                              fg_color="white", 
                              corner_radius=64, 
                              border_color="hotpink", 
                              text_color="black")
              enterfood.place(x=245, y=390)

              def delsubmit():
                food = list()
                with open('foods.csv', 'r', newline='') as file:
                  reader = csv.reader(file)
                  for row in reader:
                    food.append(row)
                    for f in row:
                      if f == enterfood.get():
                        food.remove(row)
                with open('foods.csv', 'w', newline='') as file:
                  writer = csv.writer(file)  
                  writer.writerows(food)
                with open('foods.csv', 'r', newline='') as file:              
                  foods = [row[0] for row in reader]
                  self.allmeals.configure(values=foods)
              submit = CTkButton(win,
                                text = "->",
                                width=3, 
                                bg_color="white", 
                                fg_color="hotpink", 
                                corner_radius=64, 
                                text_color="white",
                                hover_color="hotpink4",
                                command=delsubmit)
              submit.place(x=295,y=430)
              
            deletebtn = CTkButton(win,
                                    fg_color="hotpink",
                                    bg_color="white",
                                    hover_color="hotpink4",
                                    text="Delete",
                                    text_color="white",
                                    corner_radius=64,
                                    command=Delete)
            deletebtn.place(x=255, y=350)

            def FoodReset():
              class Warning:
                def __init__(self, win):

                  

  
                  def Final():
                    with open('foods.csv', 'w', newline='') as file:
                      pass
                    warning.destroy()

                  


                  def ShowDel():
                    
                    if self.warning.get() == 1:
                      final.pack( side = BOTTOM, pady = 10)
                    if self.warning.get() ==2:
                      final.pack_forget()

                  
                  self.warning = CTkCheckBox(win,
                                    fg_color="hotpink",
                                    bg_color="white",
                                    hover_color="hotpink4",
                                    text="Checking this means you understand that when you press the arrow button all your data will be deleted.",
                                    text_color="black",
                                    corner_radius=64,
                                    onvalue=1,
                                    offvalue=2,
                                    command = ShowDel
                                    )
                  self.warning.place(x=40, y=50)

                  final = CTkButton(win,
                                        width=3,
                                        fg_color="hotpink",
                                        bg_color="white",
                                        hover_color="hotpink4",
                                        text="->",
                                        text_color="white",
                                        corner_radius=64,
                                        command=Final)

                 
                  
              with open('foods.csv', 'r', newline='') as file:
                reader = csv.reader(file)              
                foods = [row[0] for row in reader]
                self.allmeals.configure(values=foods)
              

                  
              warning = CTk()
              warn = Warning(warning)
              warning.title('WARNING!')
              warning.geometry("700x150")
              warning.config(bg='white')
              warning.mainloop()
              
            reset = CTkButton(win,
                                    fg_color="hotpink",
                                    bg_color="white",
                                    hover_color="hotpink4",
                                    text="Reset",
                                    text_color="white",
                                    corner_radius=64,
                                    command=FoodReset)
            reset.place(x=410, y=350)


            self.allmeals = CTkComboBox(win,
                            bg_color="white",
                            fg_color="white",
                            button_color="hotpink",
                            button_hover_color="hotpink4",
                            dropdown_text_color="white",
                            dropdown_fg_color="hotpink",
                            dropdown_hover_color="hotpink4",
                            text_color="black",
                            values=["Choose a meal"], 
                            command=Show
                            )
            self.allmeals.place(relx=0.5,rely=0.45,anchor="center")
            with open('foods.csv', 'r', newline='') as file:
              reader = csv.reader(file)
              foods = [row[0] for row in reader]
              self.allmeals.configure(values=foods)

            def Total():
              with open('foods.csv', 'r', newline='') as file:
                c = 0
                p = 0
                ca = 0
                f = 0
                for row in csv.reader(file):
                  c += int(row[1])
                  p += int(row[2])
                  ca += int(row[3])
                  f += int(row[4])
              
              self.maclabel.configure(text= f"Calories: {c}    Protein: {p}    Carbs: {ca}    Fats: {f}")
              
            
            self.total = CTkButton(win,
                                    fg_color="hotpink",
                                    bg_color="white",
                                    hover_color="hotpink4",
                                    text="Total",
                                    text_color="white",
                                    corner_radius=64,
                                    command=Total)
            self.total.place(x=100,y=350)
            self.title = CTkLabel(win, 
                   text_color="hotpink", 
                   text = "All Meals", 
                   font=titlefont, 
                   bg_color="white")
            self.title.place(x=160, y=130)    

            
              
        win3 = CTk()
        mealwin = Meals(win3)
        win3.title('All Meals')
        win3.geometry("650x600")
        win3.config(bg='white')

          
        
        win3.mainloop()
      

    win=CTk() 
    mywin=MyWindow(win) 
    win.title('Calories/Macros Tracker') 
    win.geometry("650x600") 
    win.config(bg='white')
    Autumn = "Autumn in November"
    tsize = 50
    tweight = "bold"
      
    titlefont = CTkFont(family=Autumn, size= tsize, weight= tweight)
    title = CTkLabel(win, 
                     text_color="hotpink", 
                     text = "Calories & Macros", 
                     font=titlefont, 
                     bg_color="white")
    title.place(x=85, y=180)

    win.mainloop()

   



  def Weight():
    class Weight:
      def __init__(self, win):
        self.gb = CTkButton(win, 
                            text='Weight Graph', 
                            command=self.Graph,
                            bg_color="white", 
                            fg_color="hotpink", 
                            hover_color="hotpink4",
                            corner_radius=64)       
        self.gb.place(x=260, y=300)
        self.aw = CTkButton(win, 
                            text = 'Add Weight', 
                            command = self.AddWeight, 
                            bg_color="white", 
                            fg_color="hotpink",
                            hover_color="hotpink4", 
                            corner_radius=64)
        self.aw.place(x=260, y=340)

      def Graph(self):
        class Graph:
          def __init__(self, win):
            with open('weights.csv', 'r', newline='') as file:
              reader = list(csv.reader(file, delimiter=","))
            dateweight = np.array(reader[0:])
            xdate = dateweight[:,0]
            yweight = dateweight[:,1]

            frame = CTkFrame(win,
                             bg_color="white",
                             fg_color="white")
            frame.place()

            fig, ax = plt.subplots()
            canvas = FigureCanvasTkAgg(fig, master=win)  
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

            ax.plot(xdate, yweight, color="hotpink")
            
            canvas.draw()



        win6=CTk() 
        graphwin=Graph(win6) 
        win6.title('Add Weight') 
        win6.geometry("650x600") 
        win6.config(bg='white')
        win6.mainloop()

       
      def AddWeight(self):
        class Add:
          def __init__(self, win):

            Autumn = "Autumn in November"
            size = 20
            weight = "bold"
            labelfont = CTkFont(family=Autumn, size= size, weight= weight)


            self.addweight = CTkEntry(win, 
                                bg_color="white", 
                                fg_color="white", 
                                corner_radius=64, 
                                border_color="hotpink", 
                                text_color="black")
            self.addweight.place(x=260, y=270)
            self.awlabel = CTkLabel(win,
                                bg_color = "white",
                                text_color="hotpink",
                                text="Weight",
                                font=labelfont)
            self.awlabel.place(x=290, y=230)

            self.adddate = CTkEntry(win, 
                                bg_color="white", 
                                fg_color="white", 
                                corner_radius=64, 
                                border_color="hotpink", 
                                text_color="black")
            self.adddate.place(x=260,y=340)
            self.adlabel = CTkLabel(win,
                                bg_color = "white",
                                text_color="hotpink",
                                text="Date",
                                font=labelfont)
            self.adlabel.place(x=290, y=300)

            self.title = CTkLabel(win, 
                   text_color="hotpink", 
                   text = "All Meals", 
                   font=titlefont, 
                   bg_color="white")
            self.title.place(x=160, y=130)   

            def Submit():

              
              weight = int(self.addweight.get())
              date = self.adddate.get()
              
              with open('weights.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([date, weight])
                self.addweight.delete(0, END)
                self.adddate.delete(0, END)

            self.submit = CTkButton(win,
                                text = "->",
                                width=3, 
                                bg_color="white", 
                                fg_color="hotpink", 
                                corner_radius=64, 
                                text_color="white",
                                hover_color="hotpink4",
                                command=Submit)
            self.submit.place(x=410, y=300)
        win5=CTk() 
        weightwin=Add(win5) 
        win5.title('Add Weight') 
        win5.geometry("650x600") 
        win5.config(bg='white')
        win5.mainloop()
        


    win4 = CTk()
    mealwin = Weight(win4)
    win4.title('Weight Tracker')
    win4.geometry("650x600")
    win4.config(bg='white')
    win4.mainloop()

  def Steps():
    class Meals:
      def __init__(self, win):
        self
   
  def Workouts():
    class Meals:
      def __init__(self, win):
        self
    win6 = CTk()
    mealwin = Meals(win6)
    win6.title('Workouts')
    win6.geometry("650x600")
    win6.config(bg='white')
    win6.mainloop()
  def Achievements():
    class Meals:
      def __init__(self, win):
        self
    win7 = CTk()
    mealwin = Meals(win7)
    win7.title('Achievements')
    win7.geometry("650x600")
    win7.config(bg='white')
    win7.mainloop()

  
  

  workouts = 0 
  workoutgoal = 10

  exercisebar = CTkProgressBar(master=window, 
                               mode = 'determinate', 
                               progress_color='hotpink', 
                               width=130)
  exercisebar.set(0)
  exercisebar.place(x=185, y=350)

  proglabel = CTkLabel(master=window, 
                       text = "0/10 Completed!", 
                       fg_color="white", 
                       bg_color="white", 
                       text_color="hotpink")
  proglabel.place(x=205, y=360)


  workout = CTkButton(master=window, 
                      text = "Workouts", 
                      command=Workouts, 
                      bg_color="white", 
                      fg_color="hotpink",
                      hover_color="hotpink4", 
                      corner_radius=64)
  workout.place(x = 180, y =315)


  def updategoal():
    workoutgoal += 5 

  def update():
    global workouts
    progress = int(workouts/workoutgoal * 100)
    exercisebar.set(progress)
    window.update_idletasks()
    
    proglabel.config(text=f'{workouts}/{workoutgoal} Completed!')
  
  def incwork(proglabel):
    global workouts
    workouts += 1
    if workouts % workoutgoal == 0:
      updategoal()
    update(proglabel)


  
  calmac = CTkButton(master=window, 
                     text="Calories/Macros Tracker", 
                     bg_color="white", 
                     fg_color="hotpink", 
                     hover_color="hotpink4",
                     command=Cal,
                     corner_radius=64)
  calmac.place(x=75, y=270)

  weight = CTkButton(master=window, 
                     text="Weight Tracker", 
                     bg_color="white", 
                     fg_color="hotpink", 
                     hover_color="hotpink4",
                     command=Weight,
                     corner_radius=64)
  weight.place(x=260, y=270)

  step = CTkButton(master=window, 
                   text="Steps Tracker", 
                   bg_color="white", 
                   fg_color="hotpink", 
                   hover_color="hotpink4",
                   command=Steps,
                   corner_radius=64)
  step.place(x=415, y=270)

  achievements = CTkButton(master=window, 
                           text = "Achievements", 
                           bg_color="white", 
                           fg_color="hotpink", 
                           hover_color="hotpink4",
                           command =Achievements, 
                           corner_radius=64)
  achievements.place(x=335, y=315)
 


  window.mainloop() 
Tracker()