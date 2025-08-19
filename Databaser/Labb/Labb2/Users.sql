USE [master];
GO

ALTER LOGIN sa ENABLE;
GO

ALTER LOGIN sa WITH PASSWORD = '<hannes>';
GO

EXECUTE xp_instance_regwrite N'HKEY_LOCAL_MACHINE',
    N'Software\Microsoft\MSSQLServer\MSSQLServer',
    N'LoginMode', REG_DWORD, 2;
GO

USE [master];
GO


CREATE LOGIN bok_läsare WITH PASSWORD = 'säkert_lösenord';
GO

USE BookHandel;
GO


CREATE USER bok_läsare FOR LOGIN bok_läsare;
GO


GRANT SELECT TO bok_läsare;
GO