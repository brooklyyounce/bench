@echo off
::        Author: Brookly Younce
:: Last Modified: 10/12/2018
::       Purpose: Force kill every instance of IE regardless of popups
:: /f --> force kill
:: /im image name of "iexplore*"

taskkill /f /im iexplore.exe
taskkill /f /im excel.exe