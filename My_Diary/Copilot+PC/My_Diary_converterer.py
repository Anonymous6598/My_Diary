import aspose.words, tkinter.filedialog

class My_Diary_converterer:
    def pdf_to_docx() -> None:
        try:
            file: str = tkinter.filedialog.askopenfilename(title=f"convert pdf file to docx", filetypes=[(f"Pdf file (*.pdf)", f"*.pdf")], defaultextension=[(f"Pdf file (*.pdf)", f"*.pdf")])
            converted_file: aspose.words.Document = aspose.words.Document(file)
            converted_file.save(f"{file}.docx")

        except RuntimeError: pass

    def docx_to_pdf() -> None:
        try:
            file: str = tkinter.filedialog.askopenfilename(title=f"convert docx file to pdf", filetypes=[(f"Word file (*.docx)", f"*.docx")], defaultextension=[(f"Word file (*.docx)", f"*.docx")])
            converted_file: aspose.words.Document = aspose.words.Document(file)
            converted_file.save(f"{file}.pdf")

        except RuntimeError: pass

    def pdf_to_txt() -> None:
        try:
            file: str = tkinter.filedialog.askopenfilename(title=f"convert pdf file to txt", filetypes=[(f"Pdf file (*.pdf)", f"*.pdf")], defaultextension=[(f"Pdf file (*.pdf)", f"*.pdf")])
            converted_file: aspose.words.Document = aspose.words.Document(file)
            converted_file.save(f"{file}.txt")

        except RuntimeError: pass

    def txt_to_pdf() -> None:
        try:
            file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert txt file to pdf", filetypes=[(f"Text file (*.txt)", f"*.txt")], defaultextension=[(f"Text file (*.txt)", f"*.txt")])
            converted_file: aspose.words.Document = aspose.words.Document(file)
            converted_file.save(f"{file}.pdf")

        except RuntimeError: pass

    def docx_to_txt() -> None:
        try:
            file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert docx file to txt", filetypes=[(f"Word file (*.docx)", f"*.docx")], defaultextension=[(f"Word file (*.docx)", f"*.docx")])
            converted_file: aspose.words.Document = aspose.words.Document(file)
            converted_file.save(f"{file}.txt")
    
        except RuntimeError: pass

    def txt_to_docx() -> None:
        try:
            file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert txt file to docx", filetypes=[(f"Text file (*.txt)", "*.txt")], defaultextension=[(f"Text file (*.txt)", f"*.txt")])
            converted_file: aspose.words.Document = aspose.words.Document(file)
            converted_file.save(f"{file}.docx")

        except RuntimeError: pass