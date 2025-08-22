@echo off
for %%f in (*.py) do pylint %%f
pause
