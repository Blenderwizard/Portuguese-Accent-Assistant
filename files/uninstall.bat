@echo off
taskkill /F /IM "PAccentAssistant.exe" /T

del /Q "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\PAccentAssistant.lnk"