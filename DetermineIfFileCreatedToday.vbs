'File name: DetermineIfFileCreatedToday
'Last Date Modified: 6/25/2018
'Author: Brookly Younce by679n
'Purpose: Return 1 if file created today, else return 0

Dim fso, file, createdToday, creationDate, filePath, brokenDate

Set fso = CreateObject("Scripting.FileSystemObject")

creationDate = ""
createdToday = 0


filePath = WScript.Arguments(0)

If (filePath <> "") Then
	Set file = fso.GetFile(filePath)
	creationDate = file.DateCreated
	creationDate = Split(creationDate, " ")(0)
	If (DateDiff("d", Date, creationDate) = 0) Then
		createdToday = 1
	Else
		createdToday = 0
	End If	
Else
	createdToday = 0
End If


WScript.StdOut.WriteLine createdToday
'WScript.Echo createdToday
