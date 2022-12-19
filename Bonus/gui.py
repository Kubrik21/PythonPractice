import PySimpleGUI as sg
import zipCreator as zip

label1=sg.Text("Choose files")
input1=sg.Input()
choose_button1=sg.FilesBrowse("Choose")

label2=sg.Text("Select destination")
input2=sg.Input()
choose_button2=sg.FolderBrowse("Choose")

compress_button=sg.Button("Compress", key="compress")
window = sg.Window("File Compressor",layout=[[label1,input1,choose_button1],
                                             [label2,input2,choose_button2],
                                             [compress_button]])
while True:
    event,values=window.read()
    match event:
        case "compress":
            print(event, values)
            filepaths = values["Choose"].split(";")
            folderpath = values["Choose0"]
            zip.compress(filepaths,folderpath)

window.close()