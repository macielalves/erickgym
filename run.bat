@echo off
setlocal

if "%~1"=="" (
    python.exe manage.py runserver 0.0.0.0:8000
    goto :end
) else (
  python.exe manage.py %*
  goto :end
)

:end
endlocal