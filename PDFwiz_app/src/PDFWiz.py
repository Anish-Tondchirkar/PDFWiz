


import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import PyPDF2 as pp
from PyPDF2 import PdfFileMerger, PdfFileReader
import PIL
from PIL import Image, ImageTk
import fitz

pdfs = []
img = []
merge_tab = None
img2pdf_tab = None
# pdf2img_tab = None
# compress_tab = None
# notebook = None
import os
import tempfile
from PyPDF2 import PdfFileReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog, messagebox



def compress_pdf():
    if len(pdfs) == 0:
        messagebox.showerror("Error", "Please select a PDF file to compress")
        return

    # Create PdfFileWriter object
    output_pdf = pp.PdfWriter()

    for pdf_file in pdfs:
        # Open each PDF file using PdfFileReader
        input_pdf = pp.PdfReader(pdf_file)
        

        # Iterate over each page and add it to the output_pdf
        for page_number in range(len(input_pdf.pages)):
            page = input_pdf.pages[page_number]
            page.compress_content_streams()  # Compress the content stream of the page
            output_pdf.add_page(page)

    # Output compressed PDF file
    output_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    with open(output_path, 'wb') as output_file:
        output_pdf.write(output_file)

    print("PDF compression complete.")
    messagebox.showinfo("Done", "PDF compressed successfully")




def merge_pdf():
    if len(pdfs) == 0:
        messagebox.showerror("Error","Please select PDF files")
        return
    # Merge selected PDF files using PyPDF2
    merger = pp.PdfMerger()  #PdfFileMerger is class from PyPDF2 Module that allows us to merge pdfs
    for pdf_file in pdfs:
        merger.append(pdf_file)
    
    # Output merged PDF file
    output_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    merger.write(output_path)
    merger.close()
    print("PDF merge complete.")
    messagebox.showinfo("Done","PDF files merged and Downloaded")



def img_to_pdf():
    if len(img) == 0:
        messagebox.showerror("Error","Please select images")
        return
    # Convert selected image files to PDF using PIL
    pdf_merger = pp.PdfMerger()
    for image_file in img:
        image = Image.open(image_file)
        pdf_path = image_file + ".pdf"
        image.save(pdf_path, "PDF")
        pdf_merger.append(pdf_path)
    
    # Output merged PDF file
    output_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    pdf_merger.write(output_path)
    pdf_merger.close()
    print("Image to PDF conversion complete.")
    messagebox.showinfo("Done","PDF downloaded successfully")




def pdf_to_img():
    if len(pdfs) == 0:
        messagebox.showerror("Error", "Please select PDF file")
        return

    pdf_file = pdfs[0]  # Only process the first selected PDF file

    # Open the PDF file using PyMuPDF
    doc = fitz.open(pdf_file)
    output_kuthe = filedialog.asksaveasfilename(defaultextension='.jpg')
    if output_kuthe:
        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            pix = page.get_pixmap()
            image_path = pdf_file.replace('.pdf', f'_page{page_number}.jpg')
            pix.save(image_path, "JPEG")

        doc.close()
        
        print("PDF to image conversion complete.")
        messagebox.showinfo("Done","PDF to Image conversion complete")
    

def select_pdf():
    # Open pdfs in pc
    global pdfs, merge_tab, img2pdf_tab, pdf2img_tab, compress_tab
    pdfs = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")], multiple=True)
    if pdfs:
        active_tab = notebook.index(notebook.select())  # Get the index of the currently active tab

        if active_tab == 0:  # Merge PDF tab
            # Clear existing labels
            for widget in merge_tab.winfo_children():
                if isinstance(widget, tk.Label) and widget.winfo_y() > 40:
                    widget.destroy()

            # Display selected PDFs
            for i, pdf in enumerate(pdfs):
                label = tk.Label(merge_tab, text=pdf, width=83, anchor="w", background="antiquewhite")
                label.place(x=15, y=50 + (i * 30))
        
        elif active_tab == 2:  # PDF to JPG tab
            # Check if more than one PDF is selected
            if len(pdfs) > 1:
                messagebox.showerror("Error", "Please select only one PDF file")
            if len(pdfs) == 1:
                pdf = pdfs[0]
                # Display selected PDF
                label = tk.Label(pdf2img_tab, text=pdf, width=83, anchor="w", background="antiquewhite")
                label.place(x=15, y=50)

        elif active_tab == 3:  # Compress PDF tab
            # Check if more than one PDF is selected
            if len(pdfs) > 1:
                messagebox.showerror("Error", "Please select only one PDF file")
            if len(pdfs) == 1:
                pdf = pdfs[0]
                # Display selected PDF
                label = tk.Label(compress_tab, text=pdf, width=83, anchor="w", background="antiquewhite")
                label.place(x=15, y=50)

def select_img():
    # Open file dialog to select multiple image files
    global img
    img = filedialog.askopenfilenames(filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
    if img:
        print("Selected images:",img)
        for i,im in enumerate(img):
            label = tk.Label(img2pdf_tab,text=im,width=83,anchor="w", background="antiquewhite")
            label.place(x=15, y=50 + (i * 30))
def pdfwiz():
    global notebook,compress_tab,merge_tab,pdf2img_tab,img2pdf_tab
    root = tk.Tk()
    root.title("PDFWiz")
    root.iconbitmap('C:\\Users\\Anish Tondchirkar\\Coding\\Python\\Projects\\PDFwiz_app\\resources\\Pdfwiz.ico')
    
    window_width = 700
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # GUI BG color
    root.config(bg="royalblue")


    
    m1 = Image.open("C:\\Users\\Anish Tondchirkar\\Coding\\Python\\Projects\\PDFwiz_app\\resources\\m1.png").resize((28,28))
    m2 = ImageTk.PhotoImage(m1)
    to_pdf = Image.open("C:\\Users\\Anish Tondchirkar\\Coding\\Python\\Projects\\PDFwiz_app\\resources\\2pdf.png").resize((28,28))
    pdfff = ImageTk.PhotoImage(to_pdf)
    to_img = Image.open("C:\\Users\\Anish Tondchirkar\\Coding\\Python\\Projects\\PDFwiz_app\\resources\\2img.png").resize((28,28))
    imggg = ImageTk.PhotoImage(to_img)
    comp = Image.open("C:\\Users\\Anish Tondchirkar\\Coding\\Python\\Projects\\PDFwiz_app\\resources\\c1.png").resize((28,28))
    cp = ImageTk.PhotoImage(comp)

    notebook = ttk.Notebook(root)
    notebook.pack()

    # creating tabs
    merge_tab = tk.Frame(notebook,background="antiquewhite")

    # merge_tab.config(height=400)
    sel_pdfs = tk.Button(merge_tab,text="Select PDF files",fg="white",font=("Arial", 10,"bold"),background="#3F829D",padx=10,pady=10,relief="groove",command=select_pdf)#relief ne button chi style shadow asa
    # khitri bolu apan te change hote.....Flat,raised,sunken,groove,ridge he taytle types
    sel_pdfs.place(x=165,y=0)
    mer = tk.Button(merge_tab,text="Merge PDF files",padx=10,pady=10,relief="groove",fg="white",font=("Arial", 10,"bold"),background="#3F829D",command=merge_pdf)
    mer.place(x=305,y=0)

    img2pdf_tab = tk.Frame(notebook,background="antiquewhite")
    sel_imgs = tk.Button(img2pdf_tab,text="Select Images",fg="white",font=("Arial", 10,"bold"),background="#3F829D",padx=10,pady=10,relief="groove",command=select_img)
    sel_imgs.place(x=165,y=0)
    convert = tk.Button(img2pdf_tab,text="Convert to PDF",padx=10,pady=10,relief="groove",fg="white",font=("Arial", 10,"bold"),background="#3F829D",command=img_to_pdf)
    convert.place(x=305,y=0)


    pdf2img_tab = tk.Frame(notebook,background="antiquewhite")
    sel_pdf1 = tk.Button(pdf2img_tab,text="Select PDF file",fg="white",font=("Arial", 10,"bold"),background="#3F829D",padx=10,pady=10,relief="groove",command=select_pdf)
    sel_pdf1.place(x=165,y=0)
    convert = tk.Button(pdf2img_tab,text="Convert to IMG",padx=10,pady=10,relief="groove",fg="white",font=("Arial", 10,"bold"),background="#3F829D",command=pdf_to_img)
    convert.place(x=305,y=0)


    compress_tab = tk.Frame(notebook,height=300,background="antiquewhite")
    sel_pdf2 = tk.Button(compress_tab,text="Select PDF file",fg="white",font=("Arial", 10,"bold"),background="#3F829D",padx=10,pady=10,relief="groove",command=select_pdf)
    sel_pdf2.place(x=165,y=0)
    but = tk.Button(compress_tab,text="Compress PDF",padx=10,pady=10,relief="groove",fg="white",font=("Arial", 10,"bold"),background="#3F829D",command=compress_pdf)
    but.place(x=305,y=0)


    # adding tabs to notebook
    notebook.add(merge_tab, text = "       Merge PDF       " , image=m2, compound="right")
    notebook.add(img2pdf_tab, text = "       JPG to PDF       ", image=pdfff,compound="right")
    notebook.add(pdf2img_tab, text = "       PDF to JPG       ",image=imggg,compound="right")
    notebook.add(compress_tab, text = "       Compress PDF       ",image=cp,compound="right")




    root.mainloop()

pdfwiz()