from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os.path
import time

from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import array as arr
import exifread







class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Choose a file")
        self.minsize(500, 400)
        #self.wm_iconbitmap('icon.ico')

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 50, pady = 50)

        self.button()



    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)


    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        ####Message "Path"
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        ###Making Lebel1(Path of the file)
        self.label1 = ttk.Label(self.labelFrame, text = "")
        self.label1.grid(column = 2, row = 2)
        ####Message "Modify"
        self.label2 = ttk.Label(self.labelFrame, text = "")
        self.label2.grid(column = 1, row = 3)
        ###Making Lebel3(Modified time of the file)
        self.label3 = ttk.Label(self.labelFrame, text = "")
        self.label3.grid(column = 2, row = 3)
        ####Message "Access"
        self.label4 = ttk.Label(self.labelFrame, text = "")
        self.label4.grid(column = 1, row = 4)
        ###Making Lebel5(Modified time of the file)
        self.label5 = ttk.Label(self.labelFrame, text = "")
        self.label5.grid(column = 2, row = 4)
         ####Message "Change"
        self.label6 = ttk.Label(self.labelFrame, text = "")
        self.label6.grid(column = 1, row = 5)
        ###Making Lebel7(Change time of the file)
        self.label7 = ttk.Label(self.labelFrame, text = "")
        self.label7.grid(column = 2, row = 5)
         ####Message "Size"
        self.label8 = ttk.Label(self.labelFrame, text = "")
        self.label8.grid(column = 1, row = 6)
        ###Making Lebel9(Size of the file)
        self.label9 = ttk.Label(self.labelFrame, text = "")
        self.label9.grid(column = 2, row = 6)
        ####Message "Only Directory of the file: "
        self.label10 = ttk.Label(self.labelFrame, text = "")
        self.label10.grid(column = 1, row = 7)
        ###Making Lebel9(DIrectory of the file)
        self.label11 = ttk.Label(self.labelFrame, text = "")
        self.label11.grid(column = 2, row = 7)
        ####Message "File Name: "
        self.label12 = ttk.Label(self.labelFrame, text = "")
        self.label12.grid(column = 1, row = 8)
        ###Making Lebel9(Name of the file)
        self.label13 = ttk.Label(self.labelFrame, text = "")
        self.label13.grid(column = 2, row = 8)
         ####Message "Latitue and Longitude of Image is:  "
        self.label14 = ttk.Label(self.labelFrame, text = "")
        self.label14.grid(column = 1, row = 9)
        ###Making Lebel9(Latitue and Longitude of the file)
        self.label15 = ttk.Label(self.labelFrame, text = "")
        self.label15.grid(column = 2, row = 9)
        ####Message "Date and Time of Creation:  "
        self.label16 = ttk.Label(self.labelFrame, text = "")
        self.label16.grid(column = 1, row = 10)
        ###Making Lebel9(Date and Time of Creation of the file)
        self.label17 = ttk.Label(self.labelFrame, text = "")
        self.label17.grid(column = 2, row = 10)
        ####Message "Device Name:  "
        self.label18 = ttk.Label(self.labelFrame, text = "")
        self.label18.grid(column = 1, row = 10)
        ###Making Lebel9(Device name of the file)
        self.label19 = ttk.Label(self.labelFrame, text = "")
        self.label19.grid(column = 2, row = 10)
        
        ####

        ############

        #get_coordinates(geotags)
        ###########
       
       


        #self.label.configure(text = self.filename)
        file=self.filename

        self.label.configure(text ="Path: ")
        self.label1.configure(text =file)
        self.label2.configure(text ="Modified Time:  ")
        self.label3.configure(text =time.ctime(os.path.getmtime(file)))
        self.label4.configure(text="Access Time: ")
        self.label5.configure(text =time.ctime(os.path.getatime(file)))
        self.label6.configure(text="Change Time: ")
        self.label7.configure(text =time.ctime(os.path.getctime(file)))
        self.label8.configure(text="Size: ")
        self.label9.configure(text =os.path.getmtime(file))
        self.label18.configure(text="Size: ")
        self.label19.configure(text =os.path.getmtime(file))
        
        
        

        # self.label4.configure(text="Access Time")
        
        #self.label6.configure(text =time.ctime(os.path.getctime(file)))


        #self.label.configure(text =file)


        print('File Path: ', file)
        print('Access Time: ', time.ctime(os.path.getatime(file)))
        print('Modified Time: ', time.ctime(os.path.getmtime(file)))
        print('Change Time: ', time.ctime(os.path.getctime(file)))
        print('Size: ', os.path.getmtime(file))
        #######Find Device#######
        with open(self.filename, 'rb') as f_jpg:
            tags = exifread.process_file(f_jpg, details=True)
            print (tags['Image Make'])
            print (tags['Image Model'])
    

        ######Cutting the path############
        myString=self.filename
        dirname, basename = os.path.split(myString)
        print(dirname)
        print(basename)
        self.label10.configure(text="Only Directory of the file: ")
        self.label11.configure(text =dirname)
        self.label12.configure(text="Only Base name of the file: ")
        self.label13.configure(text =basename)
        ############End of cutting path###############
        
        
        
        
        
        

        #########For Image Lat & Long  ###########
        def get_exif(filename):
            image = Image.open(filename)
            image.verify()
            return image._getexif()


        def get_labeled_exif(exif):
            labeled = {}
            for (key, val) in exif.items():
                labeled[TAGS.get(key)] = val

            return labeled



        def get_geotagging(exif):
            if not exif:
                raise ValueError("No EXIF metadata found")

            geotagging = {}
            for (idx, tag) in TAGS.items():
                if tag == 'GPSInfo':
                    if idx not in exif:
                        raise ValueError("No EXIF geotagging found")

                    for (key, val) in GPSTAGS.items():
                        if key in exif[idx]:
                            geotagging[val] = exif[idx][key]

            return geotagging

        def get_decimal_from_dms(dms, ref):

            degrees = dms[0][0] / dms[0][1]
            minutes = dms[1][0] / dms[1][1] / 60.0
            seconds = dms[2][0] / dms[2][1] / 3600.0

            if ref in ['S', 'W']:
                degrees = -degrees
                minutes = -minutes
                seconds = -seconds

            return round(degrees + minutes + seconds, 5)

        def get_coordinates(geotags):
            lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

            lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

            return (lat,lon)

        def get_date_taken(path):
            return Image.open(path)._getexif()[36867]




        try:
            exif = get_exif(self.filename)
            labeled = get_labeled_exif(exif)
            geotags = get_geotagging(exif)
            date_creation = get_date_taken(self.filename)
            print("Latitue and Longitude of Image is", get_coordinates(geotags))
            print ("Date and Time of Creation:", date_creation)
            self.label14.configure(text="Lat & Long: ")
            self.label15.configure(text = get_coordinates(geotags))
            self.label16.configure(text=" Time:  ")
            self.label17.configure(text = date_creation)
        except:
            print('Cannot find Lat & Long due to seclction of wrong file!!!')

        ##########End of Lat & Long########################  
        





root = Root()
root.mainloop()
#root.properties()












