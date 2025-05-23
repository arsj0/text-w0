import customtkinter as ctk
from ui.home_view import HomeView
from ui.guide_view import GuideView
from utils import app_config

class AppFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        # --- Top Navigation ---
        self.top_nav_frame = ctk.CTkFrame(self, height=30, corner_radius=0, fg_color='transparent')
        self.top_nav_frame.pack(fill="x", side="top")

        self.app_title_label = ctk.CTkLabel(
            self.top_nav_frame,
            text=app_config.APP_NAME,
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.app_title_label.pack(side="left", padx=20, pady=10)

        # --- Tab View for Main Content ---
        self.tab_view = ctk.CTkTabview(self, corner_radius=8)
        self.tab_view.pack(fill="both", expand=True, padx=0, pady=(5,0)) # pady top adjusted

        self.tab_view.add(app_config.TAB_HOME)
        self.tab_view.add(app_config.TAB_GUIDE)
        self.tab_view.set(app_config.TAB_HOME) # Set default tab

        # Configure tab appearance (optional, if defaults are not sufficient)
        # self.tab_view._segmented_button.configure(font=ctk.CTkFont(size=14))


        # --- Home Tab Content ---
        self.home_view = HomeView(self.tab_view.tab(app_config.TAB_HOME))
        self.home_view.pack(fill="both", expand=True, padx=5, pady=5)

        # --- Guide Tab Content ---
        self.guide_view = GuideView(self.tab_view.tab(app_config.TAB_GUIDE))
        self.guide_view.pack(fill="both", expand=True, padx=5, pady=5)
