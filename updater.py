#!/bin/python3

from exif import Image
import datetime
import os

image_types = ['.jpeg', '.jpg', '.png']

#TO_DO update names in ascending order instead of time of day


# Checks for files in the current directory that have the usual photo extensions
# and changes the name of the photos to add the photo time stamp as a suffix
def updateNames():
    for File in os.listdir("."):
        file_name = os.path.splitext(File)[0]
        extension = os.path.splitext(File)[1]
        if (extension in image_types):
            with open(File, 'rb') as image_file:
                my_image_date = Image(image_file).datetime_original.replace(" ", "_")
                print(my_image_date)
                if(my_image_date in file_name):
                    continue
                else:
                    os.rename(File, my_image_date + '_' + File )


if __name__ == "__main__":
    #insert path to folder option
    updateNames()
