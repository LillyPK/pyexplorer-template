import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk

class FileExplorer(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("File Explorer")
        self.state('zoomed')  # Start maximized
        
        # Configure main window grid
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self._create_top_header()
        self._create_secondary_header()
        self._create_main_content()
        
    def _create_top_header(self):
        # Top header frame
        header_frame = ttk.Frame(self, padding="5")
        header_frame.grid(row=0, column=0, sticky="ew")
        
        # Tabs
        notebook = ttk.Notebook(header_frame)
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)
        notebook.add(tab1, text="Tab 1")
        notebook.add(tab2, text="Tab 2")
        notebook.pack(fill='x', pady=(0, 5))
        
        # Navigation frame
        nav_frame = ttk.Frame(header_frame)
        nav_frame.pack(fill='x')
        
        # Navigation buttons
        ttk.Button(nav_frame, text="←").pack(side='left', padx=2)
        ttk.Button(nav_frame, text="→").pack(side='left', padx=2)
        ttk.Button(nav_frame, text="↑").pack(side='left', padx=2)
        ttk.Button(nav_frame, text="⟳").pack(side='left', padx=2)
        
        # Path entry
        path_entry = ttk.Entry(nav_frame)
        path_entry.pack(side='left', fill='x', expand=True, padx=5)
        path_entry.insert(0, "Location: C:\\Users\\...")
        
        # Search entry
        search_frame = ttk.Frame(nav_frame)
        search_frame.pack(side='left', fill='x', expand=True, padx=5)
        
        search_entry = ttk.Entry(search_frame)
        search_entry.pack(fill='x')
        search_entry.insert(0, "Search")
        
    def _create_secondary_header(self):
        # Secondary header frame
        secondary_header = ttk.Frame(self, padding="5")
        secondary_header.grid(row=1, column=0, sticky="ew")
        
        # Sort dropdown
        sort_var = tk.StringVar()
        sort_dropdown = ttk.Combobox(secondary_header, textvariable=sort_var)
        sort_dropdown['values'] = ('Name', 'Date modified', 'Type', 'Size')
        sort_dropdown.set('Sort by')
        sort_dropdown.pack(side='left')
        
        # View buttons
        view_frame = ttk.Frame(secondary_header)
        view_frame.pack(side='right')
        
        ttk.Button(view_frame, text="Grid View").pack(side='left', padx=2)
        ttk.Button(view_frame, text="List View").pack(side='left', padx=2)
        
    def _create_main_content(self):
        # Main content frame
        main_frame = ttk.Frame(self)
        main_frame.grid(row=2, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        
        # Sidebar
        sidebar = ttk.Frame(main_frame, padding="5")
        sidebar.grid(row=0, column=0, sticky="ns")
        
        # Quick Access
        ttk.Label(sidebar, text="Quick Access", font=('TkDefaultFont', 9, 'bold')).pack(anchor='w', pady=(0, 5))
        quick_access = ['Desktop', 'Downloads', 'Documents', 'Pictures', 'Music', 'Videos']
        for item in quick_access:
            ttk.Button(sidebar, text=item, style='Sidebar.TButton').pack(fill='x', pady=1)
            
        # This PC
        ttk.Label(sidebar, text="This PC", font=('TkDefaultFont', 9, 'bold')).pack(anchor='w', pady=(10, 5))
        drives = ['Local Disk (C:)', 'Data (D:)']
        for drive in drives:
            ttk.Button(sidebar, text=drive, style='Sidebar.TButton').pack(fill='x', pady=1)
        
        # Files display area
        files_frame = ttk.Frame(main_frame)
        files_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # Create a canvas with scrollbar for the files
        canvas = tk.Canvas(files_frame)
        scrollbar = ttk.Scrollbar(files_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create a grid of file items
        for i in range(20):
            frame = ttk.Frame(scrollable_frame, padding=5)
            frame.grid(row=i//4, column=i%4, padx=5, pady=5)
            
            # Placeholder for file icon
            icon_frame = ttk.Frame(frame, width=64, height=64, style='Icon.TFrame')
            icon_frame.pack()
            icon_frame.pack_propagate(False)
            
            ttk.Label(frame, text=f"File {i+1}").pack()
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def _create_styles(self):
        style = ttk.Style()
        style.configure('Sidebar.TButton', anchor='w')
        style.configure('Icon.TFrame', background='lightgray')

if __name__ == "__main__":
    app = FileExplorer()
    
    # Configure styles for buttons and frames
    app._create_styles()
    
    app.mainloop()