## Required

- xampp with php 7.2 installed
- Postgresql 10+ installed

## Getting postgreSQL to talk with PHP

1. Open php.ini file located in C:\xampp\php.
2. Uncomment the following lines in php.ini:
    **extension=pdo_pgsql**
    **extension=pgsql**
3. Restart Apache.
4. Done.

## Integrating phpPgAdmin to XAMPP – postgreSQL Database Administration tool

1. To download **phpPgAdmin**, go to the [Github repository](https://github.com/phppgadmin/phppgadmin) and clone the repository to **C:\xampp\phppgadmin**.
2. In **C:\xampp\phppgadmin\conf**, rename the **config.inc.php-dist** file to **config.inc.php**
3. Edit the **config.inc.php** and replace all instances of the following with the values below:
    $conf['servers'][0]['host'] = 'localhost';
    $conf['servers'][0]['pg_dump_path'] = 'C:\\xampp\\pgsql\\9.2\\bin\\pg_dump.exe';
    $conf['servers'][0]['pg_dumpall_path'] = 'C:\\xampp\\pgsql\\9.2\\bin\\pg_dumpall.exe';
    $conf['extra_login_security'] = false;
4. Edit XAMPP’s httpd-xampp.conf and add the below code:
    Alias /phppgadmin "C:/xampp/phppgadmin/"
    <directory "C:/xampp/phppgadmin">
    AllowOverride AuthConfig
    Require all granted
    </directory>
5. Restart Apache.
6. You should now be able to use phpPgAdmin when you visit http://localhost/phppgadmin.