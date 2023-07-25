# Importing Modules

from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os



class Stg_tech :

    # Main Frame - Encode and Decode Page Only
    def main(self, root):
        root.title("IMAGE STEGANOGRAPHY")
        root.geometry('500x600')
        root.resizable(width=False, height=False)
        root.config(bg = '#FFF8DC')
        frame = Frame(root)
        frame.grid()
        
        title = Label(frame,text='Image Steganography')
        title.config(font=('Skia',25, 'bold')) # Marker Felt, Skia, Skia, Herculanum, Luminari
        title.grid(pady=10)
        title.config(bg = '#FFF8DC')  # color code : #e3f4f1
        title.grid()
        title.grid(row=1)

        encode = Button(frame, text='Encode', command= lambda :self.encode_frame1(frame), padx=14, bg='#FFF8DC')
        encode.config(font=('Skia','14'), bg='#FFF8DC')
        encode.grid(row=2)

        decode = Button(frame, text='Decode', command= lambda :self.decode_frame1(frame), padx=14, bg='#FFF8DC')
        decode.config(font=('Skia','14'), bg='#FFF8DC')
        decode.grid(pady = 12)
        decode.grid(row=3)

        im1 = Image.open("/Users/juvarajiyasmacbook/Documents/Gautam/IBM SkillsBuild/st3.jpeg")
        im2 = im1.resize((440,400))
        test = ImageTk.PhotoImage(im2)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=30, y=170)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

    
    # For destroying frame when called
    def back(self, frame):
        frame.destroy()
        self.main(root)
    

    # HomePage/Basic GUI for Encode Page - MAIN
    def encode_frame1(self, F):
        F.destroy()
        F2 = Frame(root)
        label1= Label(F2,text='Select the Image in which \nyou want to hide text :')
        label1.config(font=('Skia',25, 'bold'),bg = '#FFF8DC')
        label1.grid()

        button_bws = Button(F2, text='Select', command= lambda: self.encode_frame2(F2))
        button_bws.config(font=('Skia',18), bg='#FFF8DC')
        button_bws.grid()

        button_back = Button(F2, text='Cancel', command= lambda: Stg_tech.back(self,F2))
        button_back.config(font=('Skia',18), bg='#FFF8DC')
        button_back.grid(pady=15)
        button_back.grid()

        F2.grid()


    # HomePage/Basic GUI for decode Page - MAIN
    def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Skia',25,'bold'),bg = '#FFF8DC')
        label1.grid()
        label1.config(bg = '#FFF8DC')

        button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
        button_bws.config(font=('Skia',18), bg='#FFF8DC')
        button_bws.grid()

        button_back = Button(d_f2, text='Cancel', command=lambda : Stg_tech.back(self,d_f2))
        button_back.config(font=('Skia',18), bg='#FFF8DC')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()


    # Encode image - SUB 1
    # Function for encoding text to image
    def encode_frame2(self,e_F2):
        e_pg= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes=([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing ! ")
        else:
            my_img = Image.open(myfile, 'r')
            new_img = my_img.resize((300,200))
            img = ImageTk.PhotoImage(new_img)
            label3 = Label(e_pg,text='Selected Image')
            label3.config(font=('Skia',14,'bold'))
            label3.grid()
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()
            lable2 = Label(e_pg, text='Enter the Messsage :')
            lable2.config(font=('Skia',14,'bold'))
            lable2.grid(pady=15)
            text_a = Text(e_pg, width=50, height=10)
            text_a.grid()
            encode_button = Button(e_pg, text="Cancel", command=lambda : Stg_tech.back(self,e_pg))
            encode_button.config(font=('Skia',14), bg='#FFF8DC')
            data = text_a.get("1.0", "end-1c")
            button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img), Stg_tech.back(self, e_pg)])   # Calling Encoding Function
            button_back.config(font=('Skia',14), bg='#FFF8DC')
            button_back.grid(pady=15)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F2.destroy()
    

    # Decode image - SUB 1
    # Function for decoding hidden text from image
    def decode_frame2(self,d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes= ([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error", "You have selected nothing! ")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4 = Label(d_F3, text='Selected Image :')
            label4.config(font=('Skia',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)    # Calling decode function
            label2 = Label(d_F3, text='Hidden Data is :')
            label2.config(font=('Skia',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command=lambda : self.frame3(d_F3))
            button_back.config(font=('Skia',14),bg='#FFF8DC')
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()

    # Function called from (Decode Image - SUB 1) to decode data
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''

        while(True):
            pixels = [ value for value in image_data.__next__()[:3] +
                image_data.__next__()[:3] +
                image_data.__next__()[:3] ]
            
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'
            
            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 !=0:
                return data

    # Function called from (Encode image - SUB 1) for Encoding data 
    # ED_P1 - Accepting Text
    def enc_fun(self, text_a, myImg):
        data = text_a.get("1.0", "end-1c")
        if(len(data) == 0):
            messagebox.showerror("Alert","Please enter text in TextBox")
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=([('png','*.png')]), defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w, self.d_image_h  = newImg.size
            messagebox.showinfo("Success!","Encoding Successful!\nFile is saved in directory you selected")
    
    
    # Function called from ( enc_fun ) ED_P1 - Accepting Text
    # ED_P2 - enter data pixels in image
    def encode_enc(self, newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            # Adding modified pixels in the new image
            newImg.putpixel((x,y), pixel)
            if (x == w-1):
                x = 0
                y += 1
            else:
                x += 1
    
    # Function called from ( ED_P2 - enter data pixels in image )
    # ED_P3 - Function to modify the data
    def modify_Pix(self, pix, data):
        dataList  = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)

        for i in range(dataLen):

            # Extracting 3 pixels at a time
            pix = [ value for value in imgData.__next__()[:3] +
                imgData.__next__()[:3] +
                imgData.__next__()[:3] ]
            
            for j in range(0,8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1
                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
                
            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
            
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    # Function called from (ED_P3 - Function to modify the data)
    # ED_P4 - for generating data
    def generate_Data(self, data):
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        
        return new_data

    # Function called from (Decode image - SUB 1)
    # For cancel/back button
    def frame3(self, frame):
        frame.destroy()
        self.main(root)

# GUI 

root = Tk()
o = Stg_tech()
o.main(root)
root.mainloop()


