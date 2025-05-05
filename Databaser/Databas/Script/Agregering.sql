select 
	count(*) as 'Antal rader', 
	count(Meltingpoint) as 'Antal värden i Meltingpoint', 
	count(Boilingpoint) as 'Antal värden i Boilingpoint',
	count(*) - count(Meltingpoint) as 'Antal nullvärden i Meltingpoint',
	count(*) - count(Boilingpoint) as 'Antal nullvärden i Boilingpoint'
from 
	Elements
where
	Number <= 20


SELECT 
    [Group], 
    sum(Mass) AS 'Total Massa',
    min(Meltingpoint) AS 'Minsta smöltpunkt',
    max(Meltingpoint) AS 'Högsta smältpunkt',
    AVG(Meltingpoint) AS 'Medel Smältpunkt',
    STRING_AGG(Symbol, ', ') AS 'Symbols'
FROM [Elements]
GROUP BY 
    [Group];


CREATE TABLE teachers(id int primary key identity(100, 5),
name NVARCHAR(max),
birthdate DATETIME2);

INSERT INTO teachers VALUE('Teachers', GETDATE());

SELECT * from teachers

delete from teachers where id BETWEEN 99 AND 187;

TRUNCATE TABLE teachers;

SELECT NEWID();

CREATE TABLE products(
        id UNIQUEIDENTIFIER PRIMARY KEY,
        name NVARCHAR(max)
)

INSERT INTO products VALUES(NEWID(), 'Mitt Produktnamn')
SELECT * FROM products;