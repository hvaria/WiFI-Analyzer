import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from customtkinter import *
from scapy.all import sniff
from tkinter import scrolledtext
import threading
import subprocess
from datetime import datetime

"""
THIS PROJECT REQUIRES WINPCAP OR NCAP DRIVERS INSTALLED AND RUNNING
"""

__project_submitted_by__ = "Himanshukumar Varia"
__project_title__ = "WiFi Analyzer"

class SnifferApp:
    def __init__(self, master):
        self.master = master
        self.sniffer_running = False

        # Set theme
        set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

        master.title("WiFi Analyzer")
        master.geometry("800x600")

        # Menu bar
        menubar = tk.Menu(master)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Project Info", command=self.info)
        help_menu.add_command(label="Help", command=self.help)
        menubar.add_cascade(label="About", menu=help_menu)
        master.config(menu=menubar)

        # Tab view
        notebook = ttk.Notebook(master)
        notebook.pack(fill="both", expand=True)

        # Tabs
        sniffer_tab = CTkFrame(notebook)
        devices_tab = CTkFrame(notebook)
        notebook.add(sniffer_tab, text="Network Sniffer")
        notebook.add(devices_tab, text="Saved Passwords")

        # Sniffer Tab
        self.start_button = CTkButton(sniffer_tab, text="Start Sniffer", command=self.start_sniffer)
        self.stop_button = CTkButton(sniffer_tab, text="Stop Sniffer", command=self.stop_sniffer, state=DISABLED)
        self.save_button = CTkButton(sniffer_tab, text="Save As TXT", command=self.save_as_txt, state=DISABLED)
        self.text_area = scrolledtext.ScrolledText(
            sniffer_tab, wrap=tk.WORD, width=80, height=25, background="#2B2B2B", foreground="#D1D1D1", font=("Consolas", 10)
        )

        self.start_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.save_button.pack(pady=10)
        self.text_area.pack(pady=20, fill="both", expand=True)

        # Devices Tab
        self.passwords_list = tk.Listbox(devices_tab, background="#1b1b1b", foreground="green", font=("Consolas", 12))
        self.passwords_list.pack(fill="both", expand=True, padx=10, pady=10)
        self.load_saved_passwords()

    def start_sniffer(self):
        if not self.sniffer_running:
            self.sniffer_running = True
            self.start_button.configure(state=DISABLED)
            self.stop_button.configure(state=NORMAL)
            self.save_button.configure(state=DISABLED)
            threading.Thread(target=self.sniff_traffic, daemon=True).start()

    def stop_sniffer(self):
        self.sniffer_running = False
        self.start_button.configure(state=NORMAL)
        self.stop_button.configure(state=DISABLED)
        self.save_button.configure(state=NORMAL)

    def sniff_traffic(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sniffer started...\n")
        self.text_area.config(state=tk.DISABLED)

        while self.sniffer_running:
            packet = sniff(count=1)[0]
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.text_area.config(state=tk.NORMAL)
            self.text_area.insert(tk.END, f"[{timestamp}] {packet.summary()}\n")
            self.text_area.config(state=tk.DISABLED)

        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sniffer stopped.\n")
        self.text_area.config(state=tk.DISABLED)

    def save_as_txt(self):
        try:
            text = self.text_area.get(0.0, tk.END).strip()
            if text:
                file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
                if file_path:
                    with open(file_path, "w") as file:
                        file.write(text)
                    messagebox.showinfo("Saved", "File saved successfully!")
            else:
                messagebox.showwarning("No Data", "No data to save.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def load_saved_passwords(self):
        try:
            data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
            all_profiles = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]
            for profile in all_profiles:
                results = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8").split("\n")
                password = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
                display_text = f"{profile:<30}| {password[0] if password else 'N/A'}"
                self.passwords_list.insert(tk.END, display_text)
        except Exception as e:
            self.passwords_list.insert(tk.END, f"Error loading passwords: {e}")

    def info(self):
        messagebox.showinfo(
            "Project Info",
            "Project Name: WiFi Analyzer\n"
            "Project Submitted by: Rohan Kishore\n"
            "Programming Language: Python\n"
            "Libraries: Scapy, Tkinter, CustomTkinter"
        )

    def help(self):
        messagebox.showinfo(
            "Help",
            "This application has two tabs:\n"
            "1. Network Sniffer: Monitors network traffic for analysis.\n"
            "2. Saved Passwords: Displays saved WiFi passwords on this device.\n\n"
            "Ensure WinPcap or Ncap drivers are installed."
        )


if __name__ == "__main__":
    root = CTk()
    app = SnifferApp(root)
    root.mainloop()
