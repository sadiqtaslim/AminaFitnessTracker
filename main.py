from csv import *
from os import spawnve
from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk




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
                            text = 'Meals of the Day', 
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
                                 command=CalSlider)
            self.cal.set(0)
            self.cal.place(x=245, y=270)
            self.calint = CTkLabel(win,
                                   bg_color="white",
                                   text_color="black",
                                   text="")
            self.calint.place(x=450, y=265)
            self.calname = CTkLabel(win,
                                bg_color = "white",
                                text_color="hotpink",
                                text="Calories",
                                font=labelfont)
            self.calname.place(x=300,y=235)
            def Submit():
              food = self.add.get()
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
        win2 = CTk()
        addwin = AddCal(win2)
        win2.title('Add Meals') 
        win2.geometry("650x600") 
        win2.config(bg='white')
        win2.mainloop()
      def meals(self):
        class Meals:
          def __init__(self, win):
            self
        win3 = CTk()
        mealwin = Meals(win3)
        win3.title('Meals of the Day')
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
    class Meals:
      def __init__(self, win):
        self
    win4 = CTk()
    mealwin = Meals(win4)
    win4.title('Meals of the Day')
    win4.geometry("650x600")
    win4.config(bg='white')
    win4.mainloop()

  def Steps():
    class Meals:
      def __init__(self, win):
        self
    win5 = CTk()
    mealwin = Meals(win5)
    win5.title('Meals of the Day')
    win5.geometry("650x600")
    win5.config(bg='white')
    win5.mainloop()
    
  def Workouts():
    class Meals:
      def __init__(self, win):
        self
    win6 = CTk()
    mealwin = Meals(win6)
    win6.title('Meals of the Day')
    win6.geometry("650x600")
    win6.config(bg='white')
    win6.mainloop()
  def Achievements():
    class Meals:
      def __init__(self, win):
        self
    win7 = CTk()
    mealwin = Meals(win7)
    win7.title('Meals of the Day')
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