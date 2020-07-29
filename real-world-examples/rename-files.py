#!/usr/bin/python
# This is the second program shown in Kunal chawla's prank project in udacity's Programming foundation with Python.

import os

def rename_files():
  #(1) get fle names in an array from a directory
  # give your directory path based on OS
  file_list = os.listdir(r"/home/sanjeev/prank")
  saved_path = os.getcwd()
  print("Current working directory is "+saved_path )
  os.chdir(r"/home/sanjeev/prank")
   
  #(2) Rename each file by removing integer from it from the beginning of the file
  for file_name in file_list:
    print("Old File Name - "+file_name)
    print("New File Name - "+file_name.translate(NONE, "0123456789")) 
    os.rename(file_name, file_name.translate(NONE, "0123456789") )

rename_files()
