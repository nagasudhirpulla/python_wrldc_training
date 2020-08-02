### Using Oracle instant client to interface with oracle

If oracle database is not installed in the PC running the python script, 
Oracle Instant client is required for interfacing with Oracle database

### Steps to install Oracle instant client
* Download Oracle  Instant Client Package - Basic zip file
* Create an installation directory like ```c:\oml4rclient_install_dir```
* Copy the zip file to the installation directory like 
```c:\oml4rclient_install_dir\instantclient-basic-windows.x64-12.1.0.2.0.zip```
* Unzip the zip file there. Now all the instant client files may in a folder like
```c:\oml4rclient_install_dir\instantclient_19_6```
* Include the above folder path in ```PATH``` and ```OCI_LIB64``` system environment variables

If we get an error in python something like "32 bit instant client not found", then remove the 64 bit files and folders and install a 32 bit version of instant client

We also need cx_Oracle module to interface with Oracle in python - https://oracle.github.io/python-cx_Oracle/
```
pip install cx_Oracle
```

### Links
* Official docs - https://docs.oracle.com/en/database/oracle/r-enterprise/1.5.1/oread/installing-oracle-database-instant-client.html#GUID-A61C2824-B9C7-4344-A7A2-E7FE0F05695D