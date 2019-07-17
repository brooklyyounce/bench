#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.14.2
 Author:         Brookly Younce

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here


$time = 0
$interval = 0
$totalTime = 0
$numTimesExecuted = 0


$intervalInMinutes = InputBox("Minutes", "After how many minutes should Scroll Lock be repeated?", "", "")
$interval = convertFromMinutesToMiliseconds(Int($intervalInMinutes))

$timeToRun = InputBox("Hours", "How many hours should this run? ", "", "")
$totalTime = convertFromHoursToMiliseconds(Int($timeToRun))


While $time < $totalTime
	Sleep($interval)
	Send("{SCROLLLOCK}")
	Send("{SCROLLLOCK}")
	$time = $time + $interval
	$numTimesExecuted = $numTimesExecuted + 1
WEnd

MsgBox("", "Scroll Lock Program ending. It executed " + String($numTimesExecuted) + " times.", "")


Func convertFromMinutesToMiliseconds($timeInMinutes)
	Return $timeInMinutes * 60000
EndFunc

Func convertFromHoursToMiliseconds($timeInHours)
	Local $minsFromHours = $timeInHours * 60
	Return convertFromMinutesToMiliseconds($minsFromHours)
EndFunc