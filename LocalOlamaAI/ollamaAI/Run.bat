@echo off
pip install -r requirements.txt
echo.
echo Done installing requirements, Running Code...
timeout /t 5

:: Simulate clear screen by printing a large number of newline characters
for /L %%i in (1,1,50) do echo.

python Ollama_main.py