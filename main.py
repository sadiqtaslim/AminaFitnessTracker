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
  title = CTkLabel(window, text_color="hotpink", text = "Amina's Fitness Tracker", font=titlefont, bg_color="white")
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
        self.am = CTkButton(win, text='Add Meals', command=self.add,bg_color="white", fg_color="hotpink", corner_radius=64)       
        self.am.place(x=260, y=300)
        self.md = CTkButton(win, text = 'Meals of the Day', command = self.meals, bg_color="white", fg_color="hotpink", corner_radius=64)
        self.md.place(x=260, y=340)
        

      def add(self):
        class AddCal:
          def __init__(self, win):
            self.add = CTkEntry(win, bg_color="white", fg_color="white", corner_radius=64, border_color="hotpink", text_color="black")
            self.add.place(x=200, y=200)
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
    title = CTkLabel(win, text_color="hotpink", text = "Calories & Macros", font=titlefont, bg_color="white")
    title.place(x=85, y=180)
    win.mainloop()

    
  def Weight():
    window.withdraw()
    import weight

  def Steps():
    window.withdraw()
    import step
  def Workouts():
    window.withdraw()
    import workout
  def Achievements():
    window.withdraw()
    import achievements

  
  

  workouts = 0 
  workoutgoal = 10

  exercisebar = CTkProgressBar(master=window, mode = 'determinate', progress_color='hotpink', width=130)
  exercisebar.set(0)
  exercisebar.place(x=185, y=350)

  proglabel = CTkLabel(master=window, text = "0/10 Completed!", fg_color="white", bg_color="white", text_color="hotpink")
  proglabel.place(x=205, y=360)


  workout = CTkButton(master=window, text = "Workouts", command=Workouts, bg_color="white", fg_color="hotpink", corner_radius=64)
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


  
  calmac = CTkButton(master=window, text="Calories/Macros Tracker", bg_color="white", fg_color="hotpink", command=Cal,corner_radius=64)
  calmac.place(x=75, y=270)

  weight = CTkButton(master=window, text="Weight Tracker", bg_color="white", fg_color="hotpink", command=Weight,corner_radius=64)
  weight.place(x=260, y=270)

  step = CTkButton(master=window, text="Steps Tracker", bg_color="white", fg_color="hotpink", command=Steps,corner_radius=64)
  step.place(x=415, y=270)

  achievements = CTkButton(master=window, text = "Achievements", bg_color="white", fg_color="hotpink", command =Achievements, corner_radius=64)
  achievements.place(x=335, y=315)
 


  window.mainloop() 
Tracker()