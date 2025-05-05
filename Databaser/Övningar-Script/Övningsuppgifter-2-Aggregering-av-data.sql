-- a)
SELECT [Period],
    MIN(Number) AS 'from',
    MAX(Number) AS 'to',
    FORMAT(AVG(CONVERT(float, Stableisotopes)), 'N2') AS 'average isotopes',
    STRING_AGG(Symbol, ', ') as 'Agg Symbols'
FROM Elements
GROUP BY [Period]

--b)

SELECT City, Region, Country,
COUNT(City) as 'Customers'

FROM company.customers
GROUP By City, Region, Country
HAVING COUNT(City) > 2


-- c)

SELECT * FROM GameOfThrones
DECLARE @epinfo AS NVARCHAR(max) = '';


SELECT *    
FROM GameOfThrones