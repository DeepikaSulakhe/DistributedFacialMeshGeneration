import PySimpleGUI as sg
import sys

sg.theme("Default1")
layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Generate")]]


def runWindowGui():
    window = sg.Window('Video file Browser', layout, size=(600,150))
    filepath = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Generate":
            filepath = values["-IN-"]
            break

    window.close()
    return filepath


def getFilePath():
    filepath = runWindowGui()
    if filepath == None:
        print("file not chosen !! Exiting!")
        sys.exit(0)
    if not filepath.endswith(".mp4"):
        print("please choose a video file in mp4 format")
        sys.exit(0)
    
    print(filepath)
    return filepath

#getFilePath()
    