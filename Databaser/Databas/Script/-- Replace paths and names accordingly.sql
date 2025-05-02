USE master;
GO

RESTORE DATABASE everyloop
FROM DISK = 'F:\AI-24-programering\Python-programing-Hannes-Fredriksson\Databaser\Databas\everyloop.bak'
WITH 
    MOVE 'everyloop' TO 'F:\AI-24-programering\Python-programing-Hannes-Fredriksson\Databaser\Databas\everyloop.bak.mdf',
    MOVE 'everyloop_log' TO 'F:\AI-24-programering\Python-programing-Hannes-Fredriksson\Databaser\Databas\everyloop_log.ldf',
    REPLACE;
GO

