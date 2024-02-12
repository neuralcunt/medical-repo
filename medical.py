import customtkinter

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

class PersonalInfo(customtkinter.CTkFrame):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.personal_info_frame = MyFrame(master=self)
        self.personal_info_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        self.personal_info_label = customtkinter.CTkLabel(self.personal_info_frame, text="Enter Personal Information ", fg_color="transparent")
        self.personal_info_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        self.Name = customtkinter.CTkEntry(self.personal_info_frame, placeholder_text="Enter Name")
        self.Name.grid(row=1, column=0, padx=20, pady=10)
        
        self.Age = customtkinter.CTkEntry(self.personal_info_frame, placeholder_text="Enter Age")
        self.Age.grid(row=1, column=1, padx=20, pady=10)
        
        self.Sex = customtkinter.CTkEntry(self.personal_info_frame, placeholder_text="Enter Sex")
        self.Sex.grid(row=2, column=0, padx=20, pady=10)
        
        self.personal_info_submit_button = customtkinter.CTkButton(self.personal_info_frame, text="Submit", command=self.personal_info_submit)
        self.personal_info_submit_button.grid(row=3, column=0, padx=20, pady=10)


    def personal_info_submit(self):
        print("Personal Button Clicked")


class Settings(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.sidebar_frame = MyFrame(master=self)
        self.sidebar_frame.grid(row=0, column=0,padx=20, pady=20, sticky="nsew")

        self.button = customtkinter.CTkButton(self.sidebar_frame, text="Home", command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)
        
        self.settings_frame = MyFrame(self.sidebar_frame)
        self.settings_frame.grid(row=1, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.settings_frame, text="Appearance Mode:", anchor="center")
        self.appearance_mode_label.grid(row=0, column=0, padx=20, pady=10)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.settings_frame, values=["Dark", "Light", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=1, column=0, padx=20, pady=10)
        
        self.UI_scaling_label = customtkinter.CTkLabel(self.settings_frame, text="UI Scaling:", anchor="center")
        self.UI_scaling_label.grid(row=2, column=0, padx=20, pady=10)
        
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.settings_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=3, column=0, padx=20, pady=10)
        
    def button_click(self):
        print("button click")

    def change_appearance_mode_event(self, new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("Medical Report ")
        
#        self.grid_columnconfigure(0, weight=1)
#        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = Settings(master=self)
        self.sidebar_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


        self.main_frame = MyFrame(master=self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.personal_frame = PersonalInfo(master=self.main_frame)
        self.personal_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")



        self.button = customtkinter.CTkButton(self.main_frame,
                                              text="Upload New Report" ,
                                              command=self.button_click)
        self.button.grid(row=1, column=0, padx=20, pady=10)
    def button_click(self):
        print("button click")


            

if __name__ == "__main__":
    app = App()
    app.mainloop()
