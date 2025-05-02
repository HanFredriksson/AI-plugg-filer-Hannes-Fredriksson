-- Komtarer: Noramlat skriver man SELECT * FROM [Srevernamn].[Databasnamn].[Schemanamn].[Tabellnamn]
/*
Blockkommentar
*/

SELECT top 10 FirstName, LastName, ID, FirstName + ' ' +LastName as 'Fullname' FROM users;

SELECT * FROM Users WHERE FirstName <> 'Frida';

SELECT top 5 percent * FROM Users;

SELECT * FROM GameOfThrones;

SELECT * FROM Users WHERE FirstName LIKE '[ab]%' ORDER BY FirstName;

SELECT DISTINCT [Directed by], Season FROM GameOfThrones

SELECT 
    Episode,
    Title,
    [U.S. viewers(millions)],
    CASE 
        WHEN [U.S. viewers(millions)] < 3 THEN 'FEW'
        WHEN [U.S. viewers(millions)] < 6 THEN 'Average'
    END AS 'Viewers'
FROM 
    GameOfThrones
WHERE
    Season < 5;

SELECT LEN(FirstName) as 'Length', FirstName FROM Users;
SELECT LEN(FirstName)AS 'Length Cracters', DATALENGTH(Firstname) AS 'Data Size', FirstName FROM Users;

SELECT IDENTITY(int, 1, 1) AS Ident, * INTO users2 FROM Users

SELECT * FROM users2;

SELECT GETDATE();
SELECT GETUTCDATE()
SELECT DATEDIFF(YEAR, '1981-02-04', GETDATE());

SELECT DATEFROMPARTS(192, 2, 4);
SELECT ISDATE('2025-13-12 15:55:93');
SET DATAFIRST 1;
SELECT DATEPART(WEEKDAY, GETDATE()); 

SELECT ABS(-5), SIN(1), COS(1+2*PI()), TAN(1), DEGREES(PI()), RADIANS(180.0);

SELECT CHOOSE(2, 'röd', 'grön', 'blå');

SELECT IIF(1=1, 'Sant', 'Falskt');