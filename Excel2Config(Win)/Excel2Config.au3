#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.6.1
 Author:         myName

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here

;  4, 6, 7

#include <Excel.au3>
#include <Array.au3>

const $START_ROW = 2
const $MAX_ROW = 999

$readme = "��������ȷ��" & @CRLF & _
	@CRLF & _
	"ʹ�÷�����" & @CRLF & _
	"  excel2config.exe [path] ( [int1] [int2] [int3] )" & @CRLF & _
	"    path: Ҫ������excel�ļ���·��" & @CRLF & _
	"    int1: Ŀ��ID������������ B ��Ϊ��2" & @CRLF & _
	"    int2: ����ID������" & @CRLF & _
	"    int3: ͳ�Ʒ�ʽ������" & @CRLF & _
	@CRLF & _
	"�������������ȱʡ��Ĭ������Ϊ�� 4, 6, 7 ����ֱ�ӽ�Excel�ļ��ϵ� excel2config.exe�ϣ�" & @CRLF & _
	"Ĭ�ϴӵ�2�п�ʼ��"
	

if $CmdLine[0] < 1 Then
	MsgBox(0, "Excel2config", $readme) 
	Exit
EndIf

$TargetIDCol = 4
$ParamIDCol = 6
$TypeCol = 7


If	$CmdLine[0] >= 2 And int($CmdLine[2]) > 0 Then
	$TargetIDCol = int($CmdLine[2])
EndIf

If	$CmdLine[0] >= 3 And int($CmdLine[3]) > 0 Then
	$ParamIDCol = int($CmdLine[3])
EndIf

If	$CmdLine[0] >= 4 And int($CmdLine[4]) > 0 Then
	$TypeCol = int($CmdLine[4])
EndIf


$sFilePath = @ScriptDir & '\' & $CmdLine[1]

; $sFilePath = @ScriptDir & "/test.xlsx"
$oExcel = _ExcelBookOpen($sFilePath, 0)
_ExcelSheetActivate($oExcel, 1)


$arrParamID = _ExcelReadArray($oExcel, $START_ROW, $ParamIDCol, $MAX_ROW, 1)
$uboundofArr = _ArraySearch($arrParamID, "")

$arrTargetID = _ExcelReadArray($oExcel, $START_ROW, $TargetIDCol, $uboundofArr, 1)
$arrParamID = _ExcelReadArray($oExcel, $START_ROW, $ParamIDCol, $uboundofArr, 1)
$arrType = _ExcelReadArray($oExcel, $START_ROW, $TypeCol, $uboundofArr, 1)

_ExcelBookClose($oExcel, 0)


$lastElement = ""
For $i = 0 to UBound($arrTargetID)-1
	if $arrTargetID[$i] == "" Then
		$arrTargetID[$i] = $lastElement
	EndIf
	$lastElement = $arrTargetID[$i]
Next

$lastElement = ""
For $i = 0 to UBound($arrType)-1
	if $arrType[$i] == "" Then
		$arrType[$i] = $lastElement
	EndIf
	$lastElement = $arrType[$i]
Next

For $i = 0 to UBound($arrType)-1
	if StringInStr($arrType[$i], "Count", 0) > 0 Then
		$arrType[$i] = "count"
	Else
		$arrType[$i] = "unknown"
	EndIf
Next

$file = FileOpen(@ScriptDir & "/config.txt", 2)

For $i = 0 to UBound($arrParamID)-1
	FileWriteLine($file, $arrTargetID[$i] & '  ' & $arrParamID[$i] & '  ' & $arrType[$i])
Next

FileClose($file)

