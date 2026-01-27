
# tkinter module and library imports


import tkinter as tk
from tkinter import filedialog, messagebox


# Create the main application window


root = tk.Tk()
root.title("Ajeet Notepad")
root.geometry("900x600")


# Global variables


current_file = None
is_dark_mode = False


# Text widget (Main Notepad Area)


text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 16),
    undo=True
)
text.pack(expand=True, fill=tk.BOTH)


# STATUS BAR (Word Count, Char Count)


status_bar = tk.Label(root, text="Words: 0 | Characters: 0 | Lines: 1", anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

def update_status(event=None):
    content = text.get(1.0, tk.END)
    words = len(content.split())
    chars = len(content) - 1
    lines = content.count("\n")
    status_bar.config(
        text=f"Words: {words} | Characters: {chars} | Lines: {lines}"
    )

text.bind("<KeyRelease>", update_status)


# FILE OPERATIONS


def new_file(event=None):
    global current_file
    if messagebox.askyesno("New File", "Unsaved changes may be lost. Continue?"):
        text.delete(1.0, tk.END)
        current_file = None
        root.title("Ajeet Notepad - New File")

def open_file(event=None):
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
        update_status()

def save_file(event=None):
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Save", "File saved successfully!")
    else:
        save_as_file()

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

def append_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "a") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Append", "Content appended successfully!")


# FIND TEXT FEATURE


def find_text(event=None):
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
    tk.Button(win, text="Find", command=find).pack()


# THEME MODE (LIGHT / DARK)


def toggle_theme():
    global is_dark_mode
    if is_dark_mode:
        text.config(bg="white", fg="black", insertbackground="black")
        is_dark_mode = False
    else:
        text.config(bg="#1e1e1e", fg="white", insertbackground="white")
        is_dark_mode = True

# AUTO SAVE FEATURE

def auto_save():
    if current_file:
        with open(current_file, "w") as file:
            file.write(text.get(1.0, tk.END))
    root.after(30000, auto_save)  # every 30 seconds

auto_save()


# EXIT CONFIRMATION


def exit_app(event=None):
    if messagebox.askyesno("Exit", "Do you want to exit the application?"):
        root.destroy()


# MENU BAR


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# FILE MENU
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="Append", command=append_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app, accelerator="Ctrl+Q")

# EDIT MENU
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=find_text, accelerator="Ctrl+F")

# VIEW MENU
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label=" Dark Mode", command=toggle_theme)


# KEYBOARD SHORTCUTS


root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-f>", find_text)
root.bind("<Control-q>", exit_app)


# START APPLICATION


root.mainloop()
