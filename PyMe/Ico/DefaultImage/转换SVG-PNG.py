import os
import tkinter as tk
from PIL import Image, ImageTk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
 
def WalkAllResFiles(parentPath,alldirs=True,extName=None,sortBy = "Name"):
    ResultFilesArray = []
    if os.path.exists(parentPath) == True:
        for fileName in os.listdir(parentPath):
            newPath = parentPath +'\\'+ fileName
            if os.path.isdir(newPath):
                if extName == None:
                    ResultFilesArray.append(newPath)
                if alldirs == True:
                    ResultFilesArray.extend(WalkAllResFiles(newPath,alldirs,extName))
            else:
                if extName == None:
                    file_extension = os.path.splitext(fileName)[1]
                    ResultFilesArray.append(newPath)
                else:
                    file_extension = os.path.splitext(fileName)[1].replace('.','')
                    file_extension_lower = file_extension.lower().strip()
                    file_extName_lower = extName.lower().strip()
                    if file_extension_lower == file_extName_lower:
                        ResultFilesArray.append(newPath)      
    return sorted(ResultFilesArray,key=lambda x:len(x))

 
root = tk.Tk()
AllSVGFile = WalkAllResFiles(".",True,"svg")
for svgPathName in AllSVGFile:
    drawing = svg2rlg(svgPathName)
    pngPathName = svgPathName.replace(".svg",".png")
    renderPM.drawToFile(drawing,pngPathName, bg='#00000000', fmt="PNG")
    os.remove(svgPathName)
