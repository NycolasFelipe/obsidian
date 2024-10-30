:: Recuperar data e horário
For /f "tokens=1-3 delims=/ " %%a in ('date /t') do (set mydate=%%a-%%b-%%c)
For /f "tokens=1-2 delims=/:" %%a in ("%TIME%") do (set mytime=%%a:%%b)

:: Preparar mensagem do commit
set commit_msg="sync %mydate% - %mytime%"

:: Sincronizar com repositório
git fetch
git pull

:: Commit do repositório
git add *
git commit -m %commit_msg%

:: Push do repositório
git push

cmd /k