import customtkinter, CTkMenuBar, CTkTable, tkinter, tkinter.filedialog, tkinter.messagebox, sys, csv, typing, openpyxl, os, My_Organizer_AI_Window, My_Organizer_Interface, ctypes

class Program(customtkinter.CTk, My_Organizer_Interface.My_Organizer_Interface): 
    def __init__(self: typing.Self, *args, **kwargs): 
        customtkinter.CTk.__init__(self, *args, **kwargs) 
        
        self.title(f"My Organizer")
        self.geometry(f"900x700") 
        self.protocol(f"WM_DELETE_WINDOW", sys.exit)
        self.bind(f"<F11>", lambda event: self.__fullscreen__())
        
        self.appmenu: CTkMenuBar.CTkMenuBar = CTkMenuBar.CTkMenuBar(self)
            
        self.addbutton: customtkinter.CTkButton = self.appmenu.add_cascade(f"Add row", command=self.__new_line__)
        self.editbutton: customtkinter.CTkButton = self.appmenu.add_cascade(f"Edit cell", command=self.__edit_line__)
        self.deletebutton: customtkinter.CTkButton = self.appmenu.add_cascade(f"Delete row", command=self.__delete_line__)
        self.loadbutton: customtkinter.CTkButton = self.appmenu.add_cascade(f"Load table", command=self.__load_data__)
        self.savebutton: customtkinter.CTkButton = self.appmenu.add_cascade(f"Save table", command=self.__save_data__)
        self.cleanbutton: customtkinter.CTkButton = self.appmenu.add_cascade(f"Clean table", command=self.__clean_table__)
        self.aichatbot: customtkinter.CTkButton = self.appmenu.add_cascade(f"AI", command=lambda: My_Organizer_AI_Window.AI_Window())
        self.darktheme: customtkinter.CTkButton = self.appmenu.add_cascade(f"Dark theme", command=lambda: customtkinter.set_appearance_mode(f"Dark"))
        self.lighttheme: customtkinter.CTkButton = self.appmenu.add_cascade(f"Light theme", command=lambda: customtkinter.set_appearance_mode(f"Light"))

        self.tableframe: customtkinter.CTkScrollableFrame = customtkinter.CTkScrollableFrame(self)
        self.tableframe.pack(fill=f"both", expand=True)

        self.tablevalue: list[str] = [[f"Name and surname", f"Manager", f"Department", f"Job title", f"Working hours", f"Additional comment"]] 

        self.table: CTkTable.CTkTable = CTkTable.CTkTable(self.tableframe, values=self.tablevalue) 
        self.table.pack(fill=f"both", expand=True)

        self.tablevaluecount: int = 0

    @typing.override
    def __new_line__(self: typing.Self) -> None:
        self.nameinput: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"Name and surname", text=f"Enter name and surname")

        self.name_value: str = self.nameinput.get_input()
        if self.name_value == f"" or self.name_value is None: tkinter.messagebox.showerror(f"Error", f"No input data"); return

        self.managerinput: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"Manager", text=f"Enter manager")

        self.manager_value: str = self.managerinput.get_input()
        if self.manager_value == f"" or self.manager_value is None: tkinter.messagebox.showerror(f"Error", f"No input data"); return

        self.departmentinput: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"Department", text=f"Enter department")

        self.department_value: str = self.departmentinput.get_input()
        if self.department_value == f"" or self.department_value is None: tkinter.messagebox.showerror(f"Error", f"No input data"); return
                
        self.jobtitleinput: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"Job title", text=f"Enter job title")

        self.jobtitle_value: str = self.jobtitleinput.get_input()
        if self.jobtitle_value == f"" or self.jobtitle_value is None: tkinter.messagebox.showerror(f"Error", f"No input data"); return         
        
        self.hoursinput: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"Working hours", text=f"Enter working hours")

        self.hours_value: str = self.hoursinput.get_input()
        if self.hours_value == f"" or self.hours_value is None: tkinter.messagebox.showerror(f"Error", f"No input data"); return

        self.additionalcommentinput: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"Additional comment", text=f"Enter additional comment")

        self.comment_value: str = self.additionalcommentinput.get_input()
        if self.comment_value == f"" or self.comment_value is None: tkinter.messagebox.showerror(f"Error", f"No input data"); return

        self.tablevaluecount += 1
        row_values: list[str] = [self.name_value, self.manager_value, self.department_value, self.jobtitle_value, self.hours_value, self.comment_value]
        
        self.table.add_row(values=row_values)
        if self.tablevaluecount > 1: self.tablevalue.append(row_values)
        
    @typing.override
    def __edit_line__(self: typing.Self) -> None:  
        self.columnline: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"Column", text=f"Enter column")

        self.columnline_value: str = self.columnline.get_input()
        if self.columnline_value is None: tkinter.messagebox.showerror(f"Error", f"No input data"); return

        self.rowline: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"Row", text=f"Enter row")

        self.rowline_value: str = self.rowline.get_input()
        if self.rowline_value == f"0": tkinter.messagebox.showerror(f"Error", f"Cannot change the heading"); return
        elif self.rowline_value is None: tkinter.messagebox.showerror(f"Error", f"No input data"); return

        self.newvalue: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"new value", text=f"Enter new value")

        self.new_value_str: str = self.newvalue.get_input()
        if self.new_value_str is None: return

        try:
            self.row_idx: int = int(self.rowline_value)
            self.col_idx: int = int(self.columnline_value)
            
            self.tablevalue[self.row_idx][self.col_idx] = self.new_value_str
            self.table.pack_forget()
            self.table = CTkTable.CTkTable(self.tableframe, values=self.tablevalue)
            self.table.pack(fill=f"both", expand=True)
            
        except ValueError:
            tkinter.messagebox.showerror(f"Error", f"Invalid row or column number")

    @typing.override
    def __delete_line__(self: typing.Self) -> None: 
        self.rowline: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"Row", text=f"Enter row")

        self.rowline_value: str = self.rowline.get_input()
        if self.rowline_value is None: tkinter.messagebox.showerror(f"Error", f"No input data"); return

        try:
            self.row_index: int = int(self.rowline_value)
            if self.row_index >= len(self.tablevalue): tkinter.messagebox.showerror(f"Error", f"Row index out of range"); return
            
            self.tablevalue.pop(self.row_index)
            self.table.pack_forget()
            self.table = CTkTable.CTkTable(self.tableframe, values=self.tablevalue)
            self.table.pack(fill=f"both", expand=True)
            self.tablevaluecount -= 1
            
        except ValueError:
            tkinter.messagebox.showerror(f"Error", f"Invalid row number")

    @typing.override
    def __load_data__(self: typing.Self) -> None: 
        self.tablevalue[:] = [] 
        try:
            self.filename: str = tkinter.filedialog.askopenfilename(filetypes=[(f"All Supported Files", f"*.csv;*.xlsx"), (f"CSV Files", f"*.csv"), (f"Excel Files", f"*.xlsx")])
            if not self.filename: return

            match os.path.splitext(self.filename)[1]:
                case ".csv":
                    with open(self.filename, f"r+", newline=f"") as self.file:
                        self.reader: csv.Reader = csv.reader(self.file)
                        for self.row in self.reader:
                            if len(self.row) != 6: 
                                tkinter.messagebox.showerror(f"Error", f"Wrong table format")
                                return                    
                        
                            else: self.tablevalue.append(self.row)
                
                case ".xlsx":
                    self.workbook: openpyxl.Workbook = openpyxl.load_workbook(self.filename)
                    self.sheet = self.workbook.active
                    for self.row in self.sheet.iter_rows(values_only=True):
                        if len(self.row) != 6: 
                            tkinter.messagebox.showerror(f"Error", f"Wrong table format")
                            return
                    
                        else: self.tablevalue.append(list(self.row))
                
                    self.workbook.close()

        except Exception as e:
            tkinter.messagebox.showerror(f"Error", f"Failed to load file: {str(e)}")

        self.table.pack_forget() 
        self.table: CTkTable.CTkTable = CTkTable.CTkTable(self.tableframe, values=self.tablevalue) 
        self.table.pack(fill=f"both", expand=True) 

    @typing.override
    def __save_data__(self) -> None: 
        self.data: list[str] = self.tablevalue[:] 
        try:
            self.filename: str = tkinter.filedialog.asksaveasfilename(filetypes=[(f"CSV Files", f"*.csv"), (f"Excel Files", f"*.xlsx")], defaultextension=[(f"CSV Files", f"*.csv"), (f"Excel Files", f"*.xlsx")])
            if not self.filename: return

            match os.path.splitext(self.filename)[1]:
                case ".csv":
                    with open(self.filename, f"w+", newline=f"") as self.file:
                        self.writer = csv.writer(self.file)
                        self.writer.writerows(self.data)
            
                case ".xlsx":
                    self.workbook: openpyxl.Workbook = openpyxl.Workbook()
                    self.sheet = self.workbook.active
                    for self.row in self.data:
                        self.sheet.append(self.row)
                
                    self.workbook.save(self.filename)
                    self.workbook.close()

        except Exception as e:
            tkinter.messagebox.showerror(f"Error", f"Failed to save file: {str(e)}")

    @typing.override
    def __clean_table__(self: typing.Self) -> None:
        self.tablevalue: list[[str]] = [[f"Name and surname", f"Manager", f"Department", f"Job title", f"Working hours", f"Additional comment"]]
        self.table.pack_forget()
        self.table: CTkTable.CTkTable = CTkTable.CTkTable(self.tableframe, values=self.tablevalue)
        self.table.pack(fill=f"both", expand=True)
        self.tablevaluecount: int = 0

    @typing.override
    def __fullscreen__(self: typing.Self) -> None:
        if self.attributes(f"-fullscreen"): self.attributes(f"-fullscreen", False)
        
        else: self.attributes(f"-fullscreen", True)

        if customtkinter.get_appearance_mode()=="Dark": value=1
        
        else: value=0
    
        try:
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1 = 19

            if ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(value)), ctypes.sizeof(ctypes.c_int(value))) != 0: ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1, ctypes.byref(ctypes.c_int(value)), ctypes.sizeof(ctypes.c_int(value)))
        
        except Exception as err: pass

if __name__ == f"__main__":
    Program().mainloop()