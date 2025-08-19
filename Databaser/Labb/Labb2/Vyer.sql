CREATE VIEW TitlarPerFörfattare AS
SELECT 
    F.Förnamn + ' ' + F.Efternamn AS Namn,
    CASE
        WHEN F.Dödsdatum IS NULL THEN DATEDIFF(YEAR, F.Födelsedatum, GETDATE()) 
        ELSE DATEDIFF(YEAR, F.Födelsedatum, F.Dödsdatum)
    END AS Ålder,
    COUNT(DISTINCT Böcker.ISBN) AS Titlar,
    SUM(Böcker.Pris * LagerSaldo.Antal) AS Lagervärde

FROM Författare AS F

JOIN Böcker 
    ON Böcker.FörfattarID = F.ID

LEFT JOIN LagerSaldo
    ON LagerSaldo.ISBN = Böcker.ISBN

GROUP BY F.Förnamn + ' ' + F.Efternamn, F.Födelsedatum, F.Dödsdatum;


CREATE VIEW Övriga_tabeller AS
SELECT 
    k.ID,
    k.Förnamn + ' ' + k.Efternamn AS Namn,
    SUM(o.Antal * o.PrisVidKöp) AS TotalSpenderat
FROM 
    Kunder k
JOIN 
    Ordrar o ON k.ID = o.KundID
JOIN 
    Böcker b ON o.ISBN = b.ISBN
GROUP BY 
    k.ID, k.Förnamn, k.Efternamn;