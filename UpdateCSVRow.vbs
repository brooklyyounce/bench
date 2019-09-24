'Author: Brookly Younce
'Update CSV File row with new data

'Arguement 0 will be the file to read
'Arguement 1 will be the file to output
'Arguement 2 will be the column to match in
'Arugement 3 will be the id to match in the col in argument (2)
'Arguement 4 will be the column to replace
'Arguement 5 will be the value that will replace the value in argument(4)
Dim fso, incomingFileObj, outgoingfileObj, incomingFileString, outgoingFileString
Dim matchingCol, id, colToReplace, replaceString, readLineString, tempArray, tempNewLine
Const ForReading = 1, ForWriting = 2, ForAppending = 8

'Read these values from AA caller
outgoingFileString = WScript.Arguments(1)
incomingFileString = WScript.Arguments(0)
matchingCol = WScript.Arguments(2)
id = WScript.Arguments(3)
colToReplace = WScript.Arguments(4)
replaceString = WScript.Arguments(5)


'Make file system obj to create, read, write files
Set fso = CreateObject("Scripting.FileSystemObject")

'This file should never exist longer than the runtime of this script, create it and do not overwrite existing, just fail
Set outgoingfileObj = fso.CreateTextFile(outgoingFileString, False)
'Close outgoing obj so that we can reopen it for writing 
outgoingfileObj.Close
Set outgoingfileObj = fso.OpenTextFile(outgoingFileString, ForWriting, -2)


'Open the file with the System default format, ie, -2 param
Set incomingFileObj = fso.OpenTextFile(incomingFileString, ForReading, -2)


'For each line of the incoming file
Do Until incomingFileObj.AtEndOfStream
    tempNewLine = ""
    readLineString = incomingFileObj.ReadLine
    'MsgBox(readLineString)
    tempArray = Split(readLineString, ",")

    'If we have found the row with matching id in it
    If (StrComp(tempArray(matchingCol - 1), id) = 0) Then
        'Go to Column that was passed in and replace that value in the string
        tempArray(colToReplace - 1) = replaceString
    End If

    'Rejoin the line together and write it to outgoing file
    tempNewLine = Join(tempArray, ",")
    'MsgBox(tempNewLine)
    outgoingfileObj.WriteLine(tempNewLine)
Loop

'Close our file objs, done with these
outgoingfileObj.Close
incomingFileObj.Close

'Delete the old file
fso.DeleteFile incomingFileString

'Rename new file to old name
fso.MoveFile outgoingFileString, incomingFileString







