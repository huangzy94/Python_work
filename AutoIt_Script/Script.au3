ControlFocus("��", "", "Edit1")

WinWait("[CLASS:#32770]", "", 10)

ControlSetText("��", "", "Edit1", "D:\cypress\node_modules\.bin\cypress\fixtures\���ܲ�.jpg")

Sleep(2000)

ControlClick("��", "", "Button1")