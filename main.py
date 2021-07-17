from tkinter import *
from tkinter.filedialog import *
from PIL import Image, ImageTk
import cv2
import os


class GUI(Tk):
    def __init__(self, title="Window", width=200, height=200, bg="white", resizableX=0, resizableY=0):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)

    def start(self):
        self.mainloop()


def formatName(fileName):
    if len(fileName) > 20:
        return f"{fileName[:8]}....{fileName[-8:]}"
    else:
        return fileName


def openImage():
    global ORG_IMG, CON_IMG
    file = askopenfilename(defaultextension=".png", filetypes=[("All Files", "*.*")])
    try:
        ORG_IMG = cv2.imread(file)
        file_name = formatName(os.path.basename(file))
        photo = Image.open(file)
        image = ImageTk.PhotoImage(photo)
        if file_name != "":
            openFile.set(file_name)
        saveBtn.config(state=ACTIVE)
    except Exception as e:
        openFile.set("Try again")
        saveBtn.config(state=DISABLED)


def saveImage():
    global CON_IMG
    file = asksaveasfilename(defaultextension=".png", filetypes=[("All Files", "*.*")])
    if file != "":
        CON_IMG = cv2.bitwise_not(ORG_IMG)
        cv2.imwrite(file, CON_IMG)
        saveFile.set("Converted")


if __name__ == '__main__':
    BACKGROUND = "#61edc3"
    ORG_IMG = None
    CON_IMG = None

    # Making Window
    root = GUI(title="Ghost Maker", width=370, height=110, bg=BACKGROUND)

    # Open Frame
    open_frame = Frame(root, bg=BACKGROUND)
    open_frame.pack(fill=X, pady=10)
    openBtn = Button(open_frame, text="Open Image", command=openImage, width=10)
    openFile = StringVar()
    openLabel = Label(open_frame, textvariable=openFile, bg=BACKGROUND, font="lucida 14")
    openBtn.grid(row=0, column=0, padx=10)
    openLabel.grid(row=0, column=1, padx=10)

    # Save Frame
    save_frame = Frame(root, bg=BACKGROUND)
    save_frame.pack(fill=X, pady=10)
    saveBtn = Button(save_frame, text="Convert", command=saveImage, width=10, state=DISABLED)
    saveFile = StringVar()
    saveLabel = Label(save_frame, textvariable=saveFile, bg=BACKGROUND, font="lucida 14")
    saveBtn.grid(row=0, column=0, padx=10)
    saveLabel.grid(row=0, column=1, padx=10)

    # Starting Window
    root.start()
