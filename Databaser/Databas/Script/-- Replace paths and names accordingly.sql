USE master;
GO

RESTORE DATABASE everyloop
FROM DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\everyloop.bak'
WITH 
    MOVE 'everyloop' TO 'c:\Everloop\everyloop.bak.mdf',
    MOVE 'everyloop_log' TO 'c:\Everloop\everyloop_log.ldf',
    REPLACE;
GO

