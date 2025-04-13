import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "notes_data.json"

def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(FILE_NAME, "w") as f:
        json.dump(notes, f, indent=4)

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Catatan")

        self.notes = load_notes()

        # Frame input
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack(pady=5)
        self.content_text = tk.Text(root, height=5, width=40)
        self.content_text.pack(pady=5)

        self.save_button = tk.Button(root, text="Simpan Catatan", command=self.save_note)
        self.save_button.pack(pady=5)

        # Listbox
        self.notes_listbox = tk.Listbox(root, width=50)
        self.notes_listbox.pack(pady=10)
        self.notes_listbox.bind("<Double-Button-1>", self.show_note)

        self.delete_button = tk.Button(root, text="Hapus Catatan", command=self.delete_note)
        self.delete_button.pack(pady=5)

        self.update_notes_listbox()

    def save_note(self):
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()
        if not title or not content:
            messagebox.showwarning("Peringatan", "Judul dan isi catatan harus diisi!")
            return

        self.notes.append({"title": title, "content": content})
        save_notes(self.notes)
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
        self.update_notes_listbox()

    def update_notes_listbox(self):
        self.notes_listbox.delete(0, tk.END)
        for note in self.notes:
            self.notes_listbox.insert(tk.END, note["title"])

    def show_note(self, event):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            note = self.notes[selected_index[0]]
            messagebox.showinfo(note["title"], note["content"])

    def delete_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            del self.notes[selected_index[0]]
            save_notes(self.notes)
            self.update_notes_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
