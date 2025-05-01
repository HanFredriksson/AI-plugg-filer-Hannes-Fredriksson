USE master;
GO

RESTORE DATABASE everyloop
FROM DISK = 'C:\Users\User\Documents\Programering\Plugg AI\AI-plugg-filer-Hannes-Fredriksson\Databaser\Databas\everyloop.bak'
WITH 
    MOVE 'everyloop' TO 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\everyloop.mdf',
    MOVE 'everyloop_log' TO 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\everyloop_log.ldf',
    REPLACE;
GO

