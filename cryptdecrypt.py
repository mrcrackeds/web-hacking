#!/usr/bin/env python

# Simple script to encode and decode base64
# Coded by MatriX Coder | www.matrixcoder.co.vu | www.fb.com/matrixcoder2
# TODO : From Tkinter -> Gtk

from Tkinter import *
import base64
import tkMessageBox


def base():
    choose = var.get()
    txt1 = text1.get("1.0", END)
    txt2 = text2.get("1.0", END)
    if choose == 1:
        # So we will Encode
        base64_encode = base64.b64encode(txt1)
        if base64_encode == "Cg==":
            tkMessageBox.showerror("Empty Text", "Please fill the textbox")
        else:
            text2.insert("1.0", base64_encode)
    elif choose == 2:
        # So we will Decode
        base64_decode = base64.b64decode(txt2)
        if base64_decode == "":
            tkMessageBox.showerror("Empty Text", "Please fill the textbox")
        else:
            text1.insert("1.0", base64_decode)
    else:
        tkMessageBox.showerror("Take a choice!", "Please choose to Encode or to Decode!")

root = Tk()
root.wm_title("Base64 Encode/Decode [By MatriX Coder]")
text1 = Text(root)
text1.pack()
but = Button(root, text="GO!", command=base).pack()
var = IntVar()
radio1 = Radiobutton(root, text="Encode", variable=var, value=1)
radio1.pack()
radio2 = Radiobutton(root, text="Decode", variable=var, value=2)
radio2.pack()
text2 = Text(root)
text2.pack()
root.mainloop()