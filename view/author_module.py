import tkinter as tk

from tkinter import ttk

from controller.author_controller import AuthorController


class AuthorModule(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.entry_id = None
        self.create_window()
        self.controller = AuthorController()
        self.create_widgets()

    def create_window(self):
        self.title("Author Module")
        self.geometry("600x400")
        self.resizable(False, False)

    def create_widgets(self):
        ttk.Label(self, text="Manage Authors", font=("Segoe UI", 14, "bold")).pack(pady=(10, 5))

        form_frame = ttk.LabelFrame(self, text="Author Form")
        form_frame.pack(fill="x", padx=15, pady=10)

        ttk.Label(form_frame, text="Author ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = ttk.Entry(form_frame, width=40)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)
