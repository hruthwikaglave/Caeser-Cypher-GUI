import tkinter as tk
from tkinter import ttk, messagebox

def caesar_cipher(text, shift, direction):
    """Encrypts or decrypts the text using the Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift * (-1 if direction == "right" else 1)) % 26 + base)
        else:
            result += char
    return result

class CaesarCipherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Caesar Cipher")
        self.configure(background="light gray")

        self.color_1 = "white"
        self.color_2 = "blue"
        self.color_3 = "light blue"

        self._create_widgets()

    def _create_widgets(self):
        title_label = ttk.Label(
            self,
            text="Caesar Cipher",
            font=("Arial", 22, "bold"),
            background=self.color_2,
            foreground=self.color_1
        )
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        input_frame = ttk.LabelFrame(self, text="Input", padding=10)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(input_frame, text="Message:").grid(row=0, column=0, sticky="w")
        self.message_entry = ttk.Entry(input_frame, width=50)
        self.message_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Shift:").grid(row=1, column=0, sticky="w")
        self.shift_spinbox = ttk.Spinbox(input_frame, from_=1, to=25, width=5)
        self.shift_spinbox.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(input_frame, text="Encrypt", command=self.encrypt).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(input_frame, text="Decrypt", command=self.decrypt).grid(row=2, column=1, padx=5, pady=5)

        output_frame = ttk.LabelFrame(self, text="Output", padding=10)
        output_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(output_frame, text="Result:").grid(row=0, column=0, sticky="w")
        self.result_text = tk.Text(output_frame, width=50, height=5)
        self.result_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def encrypt(self):
        message = self.message_entry.get()
        shift = int(self.shift_spinbox.get())
        if not message:
            messagebox.showwarning("Warning", "Please enter a message.")
            return
        encrypted = caesar_cipher(message, shift, "left")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, encrypted)

    def decrypt(self):
        message = self.message_entry.get()
        shift = int(self.shift_spinbox.get())
        if not message:
            messagebox.showwarning("Warning", "Please enter a message.")
            return
        decrypted = caesar_cipher(message, shift, "right")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, decrypted)

if __name__ == "__main__":
    app = CaesarCipherApp()
    app.mainloop()
