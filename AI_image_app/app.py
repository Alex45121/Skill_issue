import tkinter as tk
from tkinter import filedialog, Label, Button, Canvas
from PIL import Image, ImageTk
import model_2_load

class Style_App:
    def __init__(self,root):
        self.root = root
        self.root.title = "AI Style Sheet"
 
        self.root.geometry("700x600")
        self.root.configure(background = "gray")

        self.label = Label(root, text="Upload an image to evaluate style", font=("Helvetica",14))
        self.label.pack(pady=10)

        self.upload_btn = Button(root, text="📂 Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        self.canvas = Canvas(root, width=256, height=256, bg = "black")
        self.canvas.pack(pady=10)

        self.predict_btn = Button(root, text = "Analyze Image", command = self.predict_image)
        self.predict_btn.pack(pady=10)

        self.result_label = Label(root, text="Results", font=("Helvetica",12))
        self.result_label.pack(pady = 10)

        self.image = None
        self.image_path = None

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetype=[("Image Files","*.jpg *.jpeg *.png")])
        if self.image_path:
            self.image= Image.open(self.image_path)
            self.image= self.image.convert("RGB")
            img_resized = self.image.resize((256,256))
            self.tk_image = ImageTk.PhotoImage(img_resized)
            self.canvas.create_image(128,128, image = self.tk_image)

    def predict_image(self):
        if self.image_path:
            prediction = model_2_load.predict_image(self.image)
            
            labels = ["Style Look", "Prop Style", "Color Grading", "Scene Mood"]

            print("Prediction shape:", prediction.shape)
            print("Prediction type:", type(prediction))
            scores = prediction.squeeze(0)
            result = " || ".join([f"{label}: {score:.2f}" for label,score in zip(labels,scores)])
            self.result_label.config(text=result, bg="black", fg = "green")


if __name__ =="__main__":
    root = tk.Tk()
    app = Style_App(root)
    root.mainloop()