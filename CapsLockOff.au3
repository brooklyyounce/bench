HotKeySet("{`}", "Terminate")

While True
	Sleep(3000)
	Opt("SendCapslockMode", 0)
	Send("{CAPSLOCK off}")
WEnd



Func Terminate()
    Exit
EndFunc