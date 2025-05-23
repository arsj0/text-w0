import customtkinter as ctk
from ui.app_frame import AppFrame
from utils import app_config

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(app_config.APP_NAME)
        self.geometry("900x650")

        ctk.set_appearance_mode(app_config.DEFAULT_APPEARANCE_MODE)
        ctk.set_default_color_theme(app_config.DEFAULT_COLOR_THEME)

        self.app_frame = AppFrame(master=self)
        self.app_frame.pack(fill="both", expand=True, padx=10, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()