import customtkinter as ctk
from utils import app_config

class GuideView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Guide Title
        self.title_label = ctk.CTkLabel(
            self,
            text=app_config.GUIDE_TITLE,
            font=ctk.CTkFont(size=18, weight="bold"),
            anchor="w"
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # Guide Content Textbox
        self.guide_textbox = ctk.CTkTextbox(
            self,
            wrap="word",
            font=("Arial", 13)
        )
        self.guide_textbox.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        
        self.guide_textbox.insert("1.0", app_config.GUIDE_TEXT)
        self.guide_textbox.configure(state="disabled")