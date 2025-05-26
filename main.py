import tkinter as tk
from tkinter import ttk, scrolledtext
from exa_py import Exa
import traceback
from datetime import datetime
import time

class ModernButton(ttk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        
    def on_enter(self, e):
        self.configure(style='AccentHover.TButton')
        
    def on_leave(self, e):
        self.configure(style='Accent.TButton')

class ExaSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exa Search")
        self.root.geometry("1200x800")
        self.root.configure(bg="#ffffff")
        
        # Set window icon and taskbar
        self.root.attributes('-alpha', 0.0)  # Start fully transparent
        
        # Configure style
        self.configure_styles()
        
        # Create main frame with padding
        self.main_frame = ttk.Frame(root, padding="30", style="Main.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header with modern design
        self.create_header()
        
        # Search area with modern card design
        self.create_search_area()
        
        # Results area with modern card design
        self.create_results_area()
        
        # Status bar with modern design
        self.create_status_bar()
        
        # Initialize Exa client
        self.exa = Exa('YOUR_KEY_HERE')
        
        # Bind Enter key to search
        self.search_entry.bind('<Return>', lambda e: self.perform_search())
        
        # Set focus to search entry
        self.search_entry.focus()
        
        # Fade in animation
        self.fade_in()
        
    def fade_in(self):
        alpha = self.root.attributes('-alpha')
        if alpha < 1.0:
            alpha += 0.1
            self.root.attributes('-alpha', alpha)
            self.root.after(20, self.fade_in)
        
    def create_header(self):
        header_frame = ttk.Frame(self.main_frame, style="Main.TFrame")
        header_frame.pack(fill=tk.X, pady=(0, 30))
        
        # Modern logo/icon (you can replace this with an actual image)
        logo_label = ttk.Label(
            header_frame,
            text="🔍",
            style="Logo.TLabel",
            font=("Helvetica", 32)
        )
        logo_label.pack(pady=(0, 10))
        
        title_label = ttk.Label(
            header_frame,
            text="what's in your mind?",
            style="Title.TLabel",
            font=("Helvetica", 28, "bold")
        )
        title_label.pack(pady=(0, 5))
        
        subtitle_label = ttk.Label(
            header_frame,
            text="Powered by Exa AI",
            style="Subtitle.TLabel",
            font=("Helvetica", 14)
        )
        subtitle_label.pack()
        
    def create_search_area(self):
        search_frame = ttk.Frame(self.main_frame, style="Card.TFrame")
        search_frame.pack(fill=tk.X, pady=(0, 30))
        
        # Search input with modern styling
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            width=50,
            font=("Helvetica", 14)
        )
        self.search_entry.pack(side=tk.LEFT, padx=(30, 15), pady=25)
        
        # Modern button with hover effect
        self.search_button = ModernButton(
            search_frame,
            text="Search",
            command=self.perform_search,
            style="Accent.TButton"
        )
        self.search_button.pack(side=tk.LEFT, padx=(0, 30), pady=25)
        
    def create_results_area(self):
        results_frame = ttk.Frame(self.main_frame, style="Card.TFrame")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Results header with modern design
        results_header = ttk.Label(
            results_frame,
            text="Search Results",
            style="Header.TLabel",
            font=("Helvetica", 16, "bold")
        )
        results_header.pack(anchor="w", padx=30, pady=(25, 15))
        
        # Modern scrollable text area
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            font=("Helvetica", 12),
            bg="#ffffff",
            fg="#333333",
            padx=30,
            pady=25,
            borderwidth=0,
            highlightthickness=0
        )
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 25))
        
    def create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(
            self.main_frame,
            textvariable=self.status_var,
            style="Status.TLabel"
        )
        status_bar.pack(fill=tk.X, pady=(20, 0))
        
    def configure_styles(self):
        style = ttk.Style()
        
        # Configure colors
        style.configure("Main.TFrame", background="#ffffff")
        style.configure("Card.TFrame", background="#ffffff")
        
        # Configure labels
        style.configure("Logo.TLabel", background="#ffffff", foreground="#007bff")
        style.configure("Title.TLabel", background="#ffffff", foreground="#1a1a1a")
        style.configure("Subtitle.TLabel", background="#ffffff", foreground="#666666")
        style.configure("Header.TLabel", background="#ffffff", foreground="#1a1a1a")
        style.configure("Status.TLabel", background="#ffffff", foreground="#666666", padding=5)
        
        # Configure button styles
        style.configure(
            "Accent.TButton",
            background="#007bff",
            foreground="white",
            padding=(25, 12),
            font=("Helvetica", 12, "bold")
        )
        
        style.configure(
            "AccentHover.TButton",
            background="#0056b3",
            foreground="white",
            padding=(25, 12),
            font=("Helvetica", 12, "bold")
        )
        
        # Configure entry
        style.configure(
            "TEntry",
            padding=12,
            font=("Helvetica", 12)
        )
        
    def perform_search(self):
        query = self.search_var.get().strip()
        if not query:
            self.show_error("Please enter a search query")
            return
            
        self.results_text.delete(1.0, tk.END)
        self.status_var.set("Searching...")
        self.root.update()
        
        try:
            response = self.exa.search(
                query,
                num_results=5,
                type='keyword',
                include_domains=['https://www.tiktok.com'],
            )
            
            self.results_text.delete(1.0, tk.END)
            
            if not response.results:
                self.results_text.insert(tk.END, "No results found.\n", "no_results")
                self.status_var.set("No results found")
                return
                
            for i, result in enumerate(response.results, 1):
                self.results_text.insert(tk.END, f"Result {i}\n", "result_header")
                self.results_text.insert(tk.END, f"Title: {result.title}\n", "result_title")
                self.results_text.insert(tk.END, f"URL: {result.url}\n", "result_url")
                self.results_text.insert(tk.END, "─" * 80 + "\n\n", "separator")
                
            self.status_var.set(f"Found {len(response.results)} results")
            
            # Configure tags for styling
            self.results_text.tag_configure("result_header", font=("Helvetica", 14, "bold"), foreground="#1a1a1a")
            self.results_text.tag_configure("result_title", font=("Helvetica", 12), foreground="#333333")
            self.results_text.tag_configure("result_url", font=("Helvetica", 12), foreground="#007bff")
            self.results_text.tag_configure("separator", foreground="#e0e0e0")
            self.results_text.tag_configure("no_results", font=("Helvetica", 12), foreground="#666666")
                
        except Exception as e:
            self.show_error(f"An error occurred: {str(e)}")
            self.status_var.set("Error occurred")
            
    def show_error(self, message):
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Error: {message}\n", "error")
        self.results_text.tag_configure("error", foreground="#dc3545", font=("Helvetica", 12, "bold"))
        self.status_var.set("Error occurred")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExaSearchApp(root)
    root.mainloop()
