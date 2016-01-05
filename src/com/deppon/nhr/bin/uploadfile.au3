;ControFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("文件上传","","Edit1")

;Wait 10 seconds for the Upload window to appear
WinWait("[Class:#32770]","",10)

;Set the File name text on the Edit filed

ControlSetText("文件上传","","Edit1","d:\119937\Desktop\data\stuAuthImport.xlsx")
Sleep(2000)

;Click on the OPen button

ControlClick("文件上传","","Button1")