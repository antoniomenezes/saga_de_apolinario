import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import customtkinter
import chardet
from sys import platform

#pip install tkinter-tooltip
from tktooltip import ToolTip

from saga_rules import *

#customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
#customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Saga de Apolinário")

        if platform == "linux" or platform == "linux2":
            ico = Image.open('app_logo.png')
            photo = ImageTk.PhotoImage(ico)
            self.wm_title("Saga de Apolinário")
            self.wm_iconphoto(False, photo)
        elif platform == "win32":
            self.iconbitmap("app_logo.png")    

        #self.geometry(f"{1100}x{580}")
        self.geometry(f"{1440}x{900}")
        
        self.background="#282c34"
        self.bg_color="#282c34"

        #menubar = MenuBar(self)
        #self.config(menu=menubar)

        #menubar = tk.Menu()
        
        # Create the first menu.
        #file_menu = tk.Menu(menubar, tearoff=False)
        # Append the menu to the menubar.
        #menubar.add_cascade(menu=file_menu, label="File")

        menubar = Menu(self, background="#212121", foreground="#cab8a4", activebackground="#cab8a4", 
            activeforeground="#0d0d0d", selectcolor="#0d0d0d", disabledforeground="#212121", border=0)

        fileMenu = Menu(menubar, tearoff=False, background="#212121", foreground="#cab8a4", activebackground="#cab8a4", 
            activeforeground="#0d0d0d", selectcolor="#0d0d0d", disabledforeground="#212121", border=0)

        menubar.add_cascade(menu=fileMenu, label="File")

        fileMenu.add_command(label="Exit", command=self.exit_event)
        
        self.config(menu=menubar)

        #for menu_item in self.all_menubars():
        #    menu_item.config(background="#212121", foreground="#cab8a4", 
        #        activebackground="#0d0d0d", activeforeground="#cab8a4", 
        #        selectcolor="#0d0d0d", disabledforeground="#212121")

        # configure grid layout (4x4)
        self.grid_columnconfigure((1,3), weight=2)
        self.grid_columnconfigure(2, weight=40)
        #self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0,3), weight=1)
        self.grid_rowconfigure(1, weight=17)
        self.grid_rowconfigure(2, weight=1)

        #img = PhotoImage(file="openbook.png")
        pil_image = Image.open("app_logo.png")
        pil_image = pil_image.resize((24,24))
        img = customtkinter.CTkImage(pil_image)

        pil_image2 = Image.open("shutdown.png")
        pil_image2 = pil_image2.resize((24,24))
        img2 = customtkinter.CTkImage(pil_image2)

        pil_image3 = Image.open("app_logo.png")
        pil_image3 = pil_image3.resize((24,24))
        img3 = customtkinter.CTkImage(pil_image3)

        pil_image4 = Image.open("app_logo.png")
        pil_image4 = pil_image4.resize((24,24))
        img4 = customtkinter.CTkImage(pil_image4)

        editor_font = customtkinter.CTkFont(family="Overpass Mono SemiBold", size=16)
        editor_encoding = None

        #ctk.CTkButton(root, image = img).pack(side = LEFT)

        #img = Image.open('hocuspocus.png')
        #photo = ImageTk.PhotoImage(img)
        #app.wm_iconphoto(False, photo)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0) #width=100, corner_radius=0)
        
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky= "nsew") #sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((0, 5), weight=1)

        #self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        
        #self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, image = img, text='', width=30, height=30, fg_color="#0d0d0d", command=self.open_text_dialog_event)
        #ToolTip(self.sidebar_button_1, msg="About", delay=0.01, follow=True, parent_kwargs={"bg": "black", "padx": 3, "pady": 3}, fg="#0d0d0d", bg="#cab8a4", padx=7, pady=7)
        #self.sidebar_button_1.grid(row=1, column=0, padx=4, pady=2)

        #self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        
        #self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, image = img3, text='', width=30, height=30, fg_color="#0d0d0d", command=self.find_text)
        #ToolTip(self.sidebar_button_2, msg="Search Text", delay=0.01, follow=True, parent_kwargs={"bg": "black", "padx": 3, "pady": 3}, fg="#0d0d0d", bg="#cab8a4", padx=7, pady=7)
        #self.sidebar_button_2.grid(row=2, column=0, padx=4, pady=2)

        #self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        #self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, image = img4, text='', width=30, height=30, fg_color="#0d0d0d", command=self.save_text_dialog_event)
        #ToolTip(self.sidebar_button_3, msg="Save Text File", delay=0.01, follow=True, parent_kwargs={"bg": "black", "padx": 3, "pady": 3}, fg="#0d0d0d", bg="#cab8a4", padx=7, pady=7)
        #self.sidebar_button_3.grid(row=3, column=0, padx=4, pady=2)

        #self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, image = img, text='', width=30, height=30, fg_color="#0d0d0d")
        #self.sidebar_button_4.grid(row=4, column=0, padx=4, pady=2)

        #self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="")
        #self.logo_label.grid(row=5, column=0, padx=4, pady=1)

        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, image = img2, text='', width=30, height=30, fg_color="#0d0d0d", command=self.exit_event)
        ToolTip(self.sidebar_button_5, msg="Exit", delay=0.01, follow=True, parent_kwargs={"bg": "black", "padx": 3, "pady": 3}, fg="#0d0d0d", bg="#cab8a4", padx=7, pady=7)        
        self.sidebar_button_5.grid(row=6, column=0, padx=4, pady=8)

        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="Digite o número da escolha, um texto ou ENTER para FIM", corner_radius=6, fg_color="#0d0d0d", text_color="#cab8a4", font=editor_font)
        self.entry.bind('<Return>', self.escrever_no_textbox)
        #self.entry.bind(self.escrever_no_textbox)
        self.entry.grid(row=2, column=2, sticky="nsew") #, sticky="nsew")

        self.textbox = customtkinter.CTkTextbox(master=self, corner_radius=6, fg_color="#0d0d0d", text_color="#cab8a4", border_spacing=22, wrap="word", padx=2, pady=2, font=editor_font, spacing1=10, spacing2=10, spacing3=10) #width=400, 
        self.textbox.grid(row=1, column=2, sticky="nsew") #, sticky="nsew")
        #self.textbox.insert("0.0", "Some example text!\n" * 50)

        history_text = run_saga('')
        self.textbox.insert(tk.END, history_text+'\n')

    def escrever_no_textbox(self, event):
        #print("add element:", self.entry.get())
        entry_text = self.entry.get()
        self.textbox.insert(tk.END, entry_text+'\n')
        self.entry.delete(0, tk.END)
        history_text = run_saga(entry_text)
        self.textbox.insert(tk.END, history_text+'\n')
        if '--- FIM ---' in history_text:
            self.textbox.insert(tk.END, '\nUma nova história se inicia...\n')
            history_text = run_saga('')
            self.textbox.insert(tk.END, history_text+'\n')
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def exit_event(self):
        exit()


if __name__ == "__main__":
    app = App()
    app.mainloop()    

