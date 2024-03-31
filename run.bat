@echo OFF

:start
  echo Iniciando o server
  python.exe manage.py runserver 0.0.0.0:8000
  pause
  goto end



:end
  echo Closing
