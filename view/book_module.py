import tkinter as tk

from tkinter import ttk, messagebox
from typing import Dict, List

from controller.book_controller import BookController
from validators.book_validator import BookValidator

from repository.author_repository import AuthorRepository
from repository.publisher_repository import PublisherRepository

from model.author import Author
from model.publisher import Publisher

import pdb


class BookModule(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.controller = BookController()
        self.style = ttk.Style()

        self._authors_by_label: Dict[str, Author] = {}
        self._publishers_by_label: Dict[str, Publisher] = {}

        self.entry_isbn = None
        self.entry_title = None
        self.entry_author = None
        self.entry_publisher = None
        self.entry_year = None
        self.entry_quantity = None
        self.tree = None
        self.selected_isbn = None

        self.create_window()
        self.config_style()
        self.create_widgets()
        self.bind_events()
        self.load_books()

    def create_window(self):
        self.title("Book Module")
        self.geometry("1000x400")
        self.resizable(False, False)
        self.style.theme_use("clam")

    def config_style(self):
        self.style.configure("Valid.TEntry", fieldbackground="white")
        self.style.configure("Invalid.TEntry", fieldbackground="#ffcccc")
        self.style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        self.style.configure("TButton", padding=0)

    def create_widgets(self):
        ttk.Label(self, text="Manage Books", font=("Segoe UI", 14, "bold")).pack(pady=(10, 5))

        form_frame = ttk.LabelFrame(self, text="Books Form")
        form_frame.pack(fill="x", padx=15, pady=15)

        ttk.Label(form_frame, text="ISBN:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_isbn = ttk.Entry(form_frame, width=22)
        self.entry_isbn.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Title:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.entry_title = ttk.Entry(form_frame, width=22)
        self.entry_title.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(form_frame, text="Author:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.entry_author = ttk.Combobox(form_frame, width=20, state="readonly")
        self.entry_author.grid(row=0, column=5, padx=5, pady=5)

        ttk.Label(form_frame, text="Publisher:").grid(row=1, column=0, padx=0, pady=0, sticky="e")
        self.entry_publisher = ttk.Combobox(form_frame, width=20, state="readonly")
        self.entry_publisher.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Year:").grid(row=1, column=2, padx=0, pady=0, sticky="e")
        self.entry_year = ttk.Entry(form_frame, width=22)
        self.entry_year.grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(form_frame, text="Quantity:").grid(row=1, column=4, padx=0, pady=0, sticky="e")
        self.entry_quantity = ttk.Entry(form_frame, width=22)
        self.entry_quantity.grid(row=1, column=5, padx=5, pady=5)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)
        ttk.Button(button_frame, text="Register", command=self.register_book).grid(row=0, column=0, padx=6)
        ttk.Button(button_frame, text="Update", command=self.update_book).grid(row=0, column=1, padx=6)
        ttk.Button(button_frame, text="Delete", command=self.delete_book).grid(row=0, column=2, padx=6)
        ttk.Button(button_frame, text="Clear", command=self.clear_form).grid(row=0, column=3, padx=6)
        ttk.Button(button_frame, text="Close", command=self.destroy).grid(row=0, column=4, padx=6)

        list_frame = ttk.LabelFrame(self, text="Book List")
        list_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.tree = ttk.Treeview(
            list_frame,
            columns=("isbn", "title", "author", "publisher", "year", "quantity"),
            show="headings",
            height=8
        )
        self.tree.heading("isbn", text="ISBN")
        self.tree.heading("title", text="Title")
        self.tree.heading("author", text="Author")
        self.tree.heading("publisher", text="Publisher")
        self.tree.heading("year", text="Year")
        self.tree.heading("quantity", text="Quantity")

        self.tree.column("isbn", width=120, anchor="center")
        self.tree.column("title", width=300, anchor="w")
        self.tree.column("author", width=100, anchor="w")
        self.tree.column("publisher", width=50, anchor="w")
        self.tree.column("year", width=50, anchor="w")
        self.tree.column("quantity", width=50, anchor="w")
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        self.tree.bind("<<TreeviewSelect>>", self.on_select_book)

        self.load_author_options()
        self.load_publisher_options()

    def bind_events(self):
        self.entry_isbn.bind("<KeyRelease>", self.validate_entry_isbn)
        self.entry_title.bind("<KeyRelease>", self.validate_entry_title)
        self.entry_author.bind("<KeyRelease>", self.validate_entry_author)
        self.entry_publisher.bind("<KeyRelease>", self.validate_entry_publisher)
        self.entry_year.bind("<KeyRelease>", self.validate_entry_year)
        self.entry_quantity.bind("<KeyRelease>", self.validate_entry_quantity)
        self.entry_quantity.bind("<Return>", lambda e: self.register_book())

    def validate_entry_isbn(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if BookValidator.validate_isbn(value) else "Invalid.TEntry"
        self.entry_isbn.config(style=style)

    def validate_entry_title(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if BookValidator.validate_title(value) else "Invalid.TEntry"
        self.entry_title.config(style=style)

    def validate_entry_author(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if True else "Invalid.TEntry"
        self.entry_author.config(style=style)

    def validate_entry_publisher(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if True else "Invalid.TEntry"
        self.entry_publisher.config(style=style)

    def validate_entry_year(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if BookValidator.validate_year(value) else "Invalid.TEntry"
        self.entry_title.config(style=style)

    def validate_entry_quantity(self, event):
        value = event.widget.get().strip()
        style = "Valid.TEntry" if BookValidator.validate_quantity(value) else "Invalid.TEntry"
        self.entry_title.config(style=style)

    def register_book(self):
        isbn = self.entry_isbn.get().strip()
        title = self.entry_title.get().strip()
        year = self.entry_year.get().strip()
        quantity = self.entry_quantity.get().strip()

        author_label = self.entry_author.get().strip()
        author = self._authors_by_label.get(author_label)

        publisher_label = self.entry_publisher.get().strip()
        publisher = self._publishers_by_label.get(publisher_label)

        if not BookValidator.validate_isbn(isbn):
            messagebox.showerror("Validation Error", "Invalid ISBN. Must be numeric.")
            return

        if not BookValidator.validate_title(title):
            messagebox.showerror("Validation Error", "title must be at least 5 characters.")
            return

        if not BookValidator.validate_year(year):
            messagebox.showerror("Validation Error", "Year must be less than or equal to the current year.")
            return

        if not BookValidator.validate_quantity(quantity):
            messagebox.showerror("Validation Error", "Quantity must be greater than zero and must be numeric")
            return

        try:
            self.controller.register(isbn=isbn, title=title, author=author, publisher=publisher, year=year, quantity=quantity)
            messagebox.showinfo("Success", f"Book: '{title}' registered successfully.")
            self.load_books()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_book(self):
        if not self.selected_isbn:
            messagebox.showwarning("Warning", "Select a book to update.")
            return

        isbn = self.entry_isbn.get().strip()
        title = self.entry_title.get().strip()
        year = self.entry_year.get().strip()
        quantity = self.entry_quantity.get().strip()

        author_label = self.entry_author.get().strip()
        author = self._authors_by_label.get(author_label)

        publisher_label = self.entry_publisher.get().strip()
        publisher = self._publishers_by_label.get(publisher_label)

        if not BookValidator.validate_isbn(isbn):
            messagebox.showerror("Validation Error", "Invalid ISBN. Must be numeric.")
            return

        if not BookValidator.validate_title(title):
            messagebox.showerror("Validation Error", "title must be at least 5 characters.")
            return

        if not BookValidator.validate_year(year):
            messagebox.showerror("Validation Error", "Year must be less than or equal to the current year.")
            return

        if not BookValidator.validate_quantity(quantity):
            messagebox.showerror("Validation Error", "Quantity must be greater than zero and must be numeric")
            return

        try:
            self.controller.update(isbn=isbn, title=title, author=author, publisher=publisher, year=year, quantity=quantity)
            messagebox.showinfo("Success", "Book updated successfully.")
            self.load_books()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_book(self):
        if not self.selected_isbn:
            messagebox.showwarning("Warning", "Select a book to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you to delete this book?")
        if not confirm:
            return

        try:
            self.controller.delete(self.selected_isbn)
            messagebox.showinfo("Success", "Book deleted successfully.")
            self.load_books()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_books(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            books = self.controller.list_all()
            for book in books:
                self.tree.insert("", "end", values=(book.isbn, book.title, book.author.name, book.publisher.legal_name, book.year, book.quantity))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load books: {e}")

    def clear_form(self):
        self.entry_isbn.delete(0, tk.END)
        self.entry_title.delete(0, tk.END)
        self.entry_year.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

        if self.entry_author["values"]:
            self.entry_author.current(0)
        if self.entry_publisher["values"]:
            self.entry_publisher.current(0)

        self.entry_isbn.focus_set()

    def on_select_book(self, event):
        selected = event.widget.selection()
        if not selected:
            return

        values = self.tree.item(selected[0], "values")
        self.selected_isbn = values[0]

        self.entry_isbn.delete(0, tk.END)
        self.entry_title.delete(0, tk.END)
        self.entry_year.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

        self.entry_isbn.insert(0, values[0])
        self.entry_title.insert(0, values[1])
        self.entry_year.insert(0, values[4])
        self.entry_quantity.insert(0, values[5])

        author_name = values[2]
        publisher_legal_name = values[3]

        author_label = next(
            (label for label, author in self._authors_by_label.items() if author.name == author_name),
            None
        )
        publisher_label = next(
            (label for label, publisher in self._publishers_by_label.items() if publisher.legal_name == publisher_legal_name),
            None
        )

        if author_label:
            self.entry_author.set(author_label)
        if publisher_label:
            self.entry_publisher.set(publisher_label)

    def load_author_options(self) -> None:
        """Loads authors from repository and fills the combobox."""
        authors: List[Author] = list(AuthorRepository.get_all_authors())
        self._authors_by_label = {}

        labels: List[str] = []
        for author in authors:
            label = f"{author.author_id} - {author.name}"
            self._authors_by_label[label] = author
            labels.append(label)

        self.entry_author["values"] = labels
        if labels:
            self.entry_author.current(0)

    def load_publisher_options(self) -> None:
        """Loads publishers from repository and fills the combobox."""
        publishers: List[Publisher] = list(PublisherRepository.get_all_publishers())
        self._publishers_by_label = {}

        labels: List[str] = []
        for publisher in publishers:
            label = f"{publisher.publisher_id} - {publisher.legal_name}"
            self._publishers_by_label[label] = publisher
            labels.append(label)

        self.entry_publisher["values"] = labels
        if labels:
            self.entry_publisher.current(0)
