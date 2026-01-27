
# tkinter module and library imports


# import tkinter for creating GUI applications
import tkinter as tk
from tkinter import filedialog, messagebox


# Create the main application window


root = tk.Tk()
root.title("Ajeet Notepad")
root.geometry("800x600")


# Variable to store current file path


current_file = None


# Create a Text widget for the notepad area


text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 16),
    undo=True
)
text.pack(expand=True, fill=tk.BOTH)


# MAIN LOGIC START NOW


# Function 1 - Create New File
def new_file():
    global current_file
    if messagebox.askyesno("New File", "Unsaved changes may be lost. Continue?"):
        text.delete(1.0, tk.END)
        current_file = None
        root.title("Ajeet Notepad - New File")

# Function 2 - Open File
def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
        current_file = file_path
        root.title(f"Ajeet Notepad - {file_path}")

# Function 3 - Save File (Update)
def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Save", "File saved successfully!")
    else:
        save_as_file()

# Function 4 - Save As File
def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        current_file = file_path
        root.title(f"Ajeet Notepad - {file_path}")

# Function 5 - Append File
def append_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "a") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Append", "Content appended successfully!")

# Function 6 - Find Text
def find_text():
    def find():
        text.tag_remove("found", "1.0", tk.END)
        word = entry.get()
        if word:
            start = "1.0"
            while True:
                start = text.search(word, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(word)}c"
                text.tag_add("found", start, end)
                start = end
            text.tag_config("found", background="yellow")

    win = tk.Toplevel(root)
    win.title("Find Text")
    entry = tk.Entry(win, width=30)
    entry.pack(padx=10, pady=10)
    tk.Button(win, text="Find", command=find).pack(pady=5)

# Function 7 - Dark Mode
def dark_mode():
    text.config(bg="#1e1e1e", fg="white", insertbackground="white")


# MENU BAR


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)


# FILE MENU


file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="Append", command=append_file)
file_menu.add_separator()
file_menu.add_command(label="Find", command=find_text)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# EDIT MENU


edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))


# VIEW MENU


view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label="Dark Mode", command=dark_mode)


# START APPLICATION


root.mainloop()
