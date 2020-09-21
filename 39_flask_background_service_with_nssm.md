This guide helps you in setting up a flask server as a windows background service

## Create a batch file to run the server
An example batch file would be like
```bat
REM run_server.bat
call project_env\Scripts\activate.bat
call python server.py
```

## setup nssm.exe in the windows server
* download nssm from https://nssm.cc/download
* In the 'Path' system environment variable, add the path of nssm.exe, so that nssm.exe can be recognized in command line

## Create a batch file to setup the flask server as a background service with nssm
An example batch file would be like
```bat
rem setup_service.bat
call nssm.exe install mis_dashboard "%cd%\run_server.bat"
call nssm.exe set mis_dashboard AppStdout "%cd%\logs\mis_dashboard.log"
call nssm.exe set mis_dashboard AppStderr "%cd%\logs\mis_dashboard.log"
call sc start mis_dashboard
```
run setup_service.bat file to run the flask server as a background service

## NSSM commands explained
### create a windows service by name mis_dashboard
```bat
nssm.exe install mis_dashboard "path\to\run_server.bat"
```

### editing a windows service by name mis_dashboard via nssm GUI
```bat
nssm.exe edit mis_dashboard
```

### Setup output stream files for service name mis_dashboard
```bat
nssm.exe set mis_dashboard AppStdout "path\to\app_output.log"
nssm.exe set mis_dashboard AppStderr "path\to\app_output.log"
```

## Controlling windows background services via command line
You can also run services.msc command to control windows services via windows GUI also
### start/delete/pause/stop a service in windows
```bat
sc start svc_name
sc delete svc_name
sc pause svc_name
sc stop svc_name
```

### see a service info in windows
```bat
sc query svc_name
```

## Useful links

### nssm usage guide
* https://www.techcoil.com/blog/how-to-use-nssm-to-run-a-python-3-application-as-a-windows-service-in-its-own-python-3-virtual-environment/
* https://nssm.cc/usage

### run flask app as a windows service without nssm using pywin32
* Run flask app as a windows service using pywin32 module - https://stackoverflow.com/questions/23550067/deploy-flask-app-as-windows-service

* Run flask app pyinstaller exe file as a windows service - https://stackoverflow.com/questions/55677165/python-flask-as-windows-service

### run an infinite loop as a service using pywin32
* http://ryrobes.com/python/running-python-scripts-as-a-windows-service/
