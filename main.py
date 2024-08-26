from button import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
def open_graph():
    
    x_labels = ["Categoría 1", "Categoría 2", "Categoría 3", "Categoría 4", "Categoría 5", "Categoría 6", "Categoría 7", "Categoría 8", "Categoría 9", "Categoría 10"]
    y_values = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    fig, ax = plt.subplots(figsize=(8,8))
    bars = plt.barh(x_labels, y_values)
    plt.show()

class appMenu:
        
    def __init__(self):
        set_appearance_mode("light")
        #set_default_color_theme("./themes/custom_palette.json")
        self.app = CTk()
        self.app.geometry("1200x700")

        # self.frame = CTkFrame(master=self.app)
        # self.frame.place(relx = 0, rely = 0, anchor = "nw")
        # self.frame.configure(width = 250)
        # self.frame.configure(height = 700)
        # self.frame.configure(corner_radius = 40)

        self.btnNC = Button(self.app)
        self.btnNC.moveButton(0.5, 0.2, "center")
        self.btnNC.configure("text", "Navegación por categorías")
        self.btnBPC = Button(self.app)
        self.btnBPC.moveButton(0.5, 0.4, "center")
        self.btnBPC.configure("text", "Búsqueda por palabra")
        self.btnBA = Button(self.app)
        self.btnBA.moveButton(0.5, 0.6, "center")
        self.btnBA.configure("text", "Búsqueda avanzada")
        self.btnG = Button(self.app)
        self.btnG.moveButton(0.5, 0.8, "center")
        self.btnG.configure("text", "Visualización de datos")
        self.btnG.configure("command", open_graph)

        self.app.mainloop()

appOut = appMenu()