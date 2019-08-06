#Setup project to work in xampp with Postgresql on Windows

## Required

- xampp with php 7.2 installed
- Postgresql 10+ installed

## Getting postgreSQL to talk with PHP

1. Open php.ini file located in C:\xampp\php.
2. Uncomment the following lines in php.ini:<br>
    **extension=pdo_pgsql**<br>
    **extension=pgsql**
3. Restart Apache.
4. Done.

## Integrating phpPgAdmin to XAMPP – postgreSQL Database Administration tool

1. To download **phpPgAdmin**, go to the [Github repository](https://github.com/phppgadmin/phppgadmin) and clone the repository to **C:\xampp\phppgadmin**.
2. In **C:\xampp\phppgadmin\conf**, rename the **config.inc.php-dist** file to **config.inc.php**
3. Edit the **config.inc.php** and replace all instances of the following with the values below:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$conf['servers'][0]['host'] = 'localhost';<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$conf['servers'][0]['pg_dump_path'] = 'C:\\program files\\Postgresql\\11\\bin\\pg_dump.exe';<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$conf['servers'][0]['pg_dumpall_path'] = 'C:\\program files\\Postgresql\\11\\bin\\pg_dumpall.exe';<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$conf['extra_login_security'] = false;
4. Edit XAMPP’s httpd-xampp.conf and add the below code:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Alias /phppgadmin "C:/xampp/phppgadmin/"<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<directory "C:/xampp/phppgadmin"><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AllowOverride AuthConfig<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Require all granted<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\</directory>    
5. Restart Apache.
6. You should now be able to use phpPgAdmin when you visit http://localhost/phppgadmin.