-- a)
SELECT Title, 
    FORMAT(Season, 'S0#') + FORMAT(Episode, 'E0#') AS 'Episode'
FROM GameOfThrones;

--b)
SELECT *
INTO UsersCopy 
FROM Users;

UPDATE UsersCopy
SET UserName = lower(SUBSTRING(FirstName, 1, 2)+SUBSTRING(LastName, 1, 2))

--c)
SELECT *
INTO AirportsCopy
FROM Airports;

UPDATE AirportsCopy
SET [Time] = '-', DST = '-'
WHERE [Time] IS NULL OR DST IS NULL

--d)
SELECT *
INTO ElemnetsCopy
FROM [Elements]

DELETE FROM ElemnetsCopy
WHERE [Name] LIKE '[dkmou]%' 
        OR [Name] LIKE 'Erbium' 
        OR [Name] LIKE 'Nitrogen'
        OR [Name] LIKE 'Platinum'
        OR [Name] LIKE 'Selenium'

SELECT *
FROM ElemnetsCopy

--e)
SELECT Symbol, [Name],
CASE
    WHEN [Name] LIKE CONCAT(Symbol, '%') THEN 'Yes' 
    ELSE 'No'
END AS 'SymbolStartWith'
INTO ElementsSymbolStartWith
FROM [Elements];

-- f)
-- fel
SELECT [Name], Red, Green, Blue
INTO Colors2
FROM Colors

SELECT Colors2.*, Colors.Code
FROM Colors2
LEFT JOIN Colors ON Colors2.Name = Colors.Name; 

-- rätt
-- Ska inte kopiera fron orginal tabell utan formatera red, blue och greeen till hexadecimaler
-- 'X' säget till format att convertera till hexadecimal.  
drop table colors2

select 
	[name], red, green, blue
into colors2
from 
	colors



alter table colors2
add code as '#' + format(red, 'X2') + format(green, 'X2') + format(blue, 'X2');


SELECT * 
FROM colors2


-- g)
-- fel
SELECT [Integer], String
INTO Types2
FROM Types

SELECT Types2.*, Types.[Float], Types.Bool, Types.[DateTime]
FROM Types2
LEFT JOIN Types ON Types2.[Integer]=Types.[Integer]

-- rätt
-- igen, inte kopiera, förstod frågan fel
select 
	*,
	Integer * 0.01,
	dateadd(minute, integer, dateadd(day, Integer, '2018-12-31 09:00')),
	Integer % 2

from 
	Types2