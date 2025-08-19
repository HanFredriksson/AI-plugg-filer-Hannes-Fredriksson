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
select * from GameOfThrones

DECLARE @epinfo AS NVARCHAR(max) = '';

WITH SeasonSummary AS (
    SELECT
        Season,
        MIN([Original air date]) AS StartDate,
        MAX([Original air date]) AS Enddate,
        COUNT(*) AS EpsidoeCount,
        CAST(AVG([U.S. viewers(millions)])AS decimal (10,2)) AS AVGViewers


    FROM
        GameOfThrones
    GROUP BY
        Season
)


SELECT @epinfo = @epinfo +
    'Säsong ' + CAST(Season AS varchar) + ' sändes från ' + 
    FORMAT(StartDate, 'MMMM', 'sv') + ' till ' + 
    FORMAT(Enddate, 'Y', 'sv') + '. Totalt sändes '+
    CAST(EpsidoeCount AS varchar) +' avsnitt, som i genomsnitt sågs av ' +
    CAST(AVGViewers AS varchar) +  ' människor i USA ' + CHAR(13) + CHAR(10)

FROM 
    SeasonSummary

ORDER BY
    Season;

PRINT @epinfo; 

-- d)
SELECT * FROM Users

SELECT 
    CONCAT(FirstName, ' ', LastName) AS 'Namn',
    datediff(YEAR, CONVERT(date, LEFT(ID, 6)), GETDATE()) as 'Ålder',
    CASE
        WHEN SUBSTRING(RIGHT(ID, 2), 1, 1) % 2 = 0 THEN 'Kvinna' 
        ELSE 'Man' 
    END AS 'Kön'
FROM Users

ORDER BY 
    FirstName,
    LastName

-- e)

SELECT * from Countries
SELECT COLUMN_NAME, DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Countries'



SELECT [Region],
    COUNT(Country) AS 'Antalet länder',
    SUM(convert(bigint, [Population])) AS 'Totalt antal invånare',
    SUM([Area (sq# mi#)]) AS 'Total area',
    SUM(convert(bigint, [Population]))/SUM([Area (sq# mi#)]) AS 'Medel befolkningstäthet',
    ROUND(AVG(CONVERT(float, replace([Infant mortality (per 1000 births)], ',', '.'))), 0) AS 'spädbarnsdödligheten per 100.000 födslar'

FROM Countries

GROUP BY
    [Region]

--f)
SELECT * FROM Airports

SELECT COLUMN_NAME, DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Airports'

SELECT 
   RIGHT(rtrim([Location served]), CHARINDEX(',', REVERSE(RTRIM([Location served]))+',')-1) as 'Country',
   COUNT(IATA) AS 'Number of Airports',
   sum(CASE WHEN ICAO is null then 1 else 0 end) AS 'Airports with no ICAO',
   sum(CASE WHEN ICAO is null then 1 else 0 end) / cast(COUNT(IATA) as float) as 'Procent of none ICAO'
FROM Airports
GROUP BY 
       RIGHT(rtrim([Location served]), CHARINDEX(',', REVERSE(RTRIM([Location served]))+',')-1)
