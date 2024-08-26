from customtkinter import *

class Button:
        
    def __init__(self, master, text, text_color, fg_color, hover_color, border_color, border_width, corner_radius = 6):
        self.btn = CTkButton(master = master, text= text, text_color= text_color, corner_radius= corner_radius, fg_color= fg_color, hover_color= hover_color, border_color= border_color, border_width= border_width)
        self.btn.place(relx = 0.5, rely = 0.5, anchor = "center")
    
    def __init__(self, master):
        my_font = CTkFont(family="Arial Black", size= 20)
        self.btn = CTkButton(master = master, height = 100, width = 300, fg_color = "transparent", text_color = "gray20", border_color="black", border_width=2, font = my_font)
        self.btn.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.setHoverColors("white", "black")

    def setHoverColors(self, color1, color2):
        self.btn.bind("<Enter>", lambda event: self.btn.configure(text_color=color1)) 
        self.btn.bind("<Leave>", lambda event: self.btn.configure(text_color=color2))
        self.btn.bind("<Enter>", lambda event: self.btn.configure(fg_color=color2)) 
        self.btn.bind("<Leave>", lambda event: self.btn.configure(fg_color="transparent"))
    
    def moveButton(self, relx, rely, anchor):
        self.btn.place(relx = relx, rely = rely, anchor = anchor)

    def configure(self, config_option, config_text):
        if config_option == "text":
            self.btn.configure(text = config_text)
        elif config_option == "command":
            self.btn.configure(command = config_text)
