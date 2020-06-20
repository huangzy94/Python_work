ControlFocus("打开", "", "Edit1")

WinWait("[CLASS:#32770]", "", 10)

ControlSetText("打开", "", "Edit1", "D:\Python_work\file_image\动物检测检疫证明.jpg")

Sleep(2000)

ControlClick("打开", "", "Button1")