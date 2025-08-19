CREATE PROCEDURE FlyttaBok 
    @FromBID INT, 
    @ToBID INT, 
    @ISBN CHAR(13), 
    @Amount INT = 1
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRANSACTION;

    -- Kontrollera att från-butiken har tillräckligt
    IF EXISTS (
        SELECT 1 FROM LagerSaldo
        WHERE ButikID = @FromBID AND ISBN = @ISBN AND Antal >= @Amount
    )
    BEGIN
        -- Minska antal i från-butiken
        UPDATE LagerSaldo
        SET Antal = Antal - @Amount
        WHERE ButikID = @FromBID AND ISBN = @ISBN;

        -- Om till-butiken redan har boken → uppdatera
        IF EXISTS (
            SELECT 1 FROM LagerSaldo
            WHERE ButikID = @ToBID AND ISBN = @ISBN
        )
        BEGIN
            UPDATE LagerSaldo
            SET Antal = Antal + @Amount
            WHERE ButikID = @ToBID AND ISBN = @ISBN;
        END
        ELSE
        BEGIN
            -- Annars lägg till ny rad
            INSERT INTO LagerSaldo (ButikID, ISBN, Antal)
            VALUES (@ToBID, @ISBN, @Amount);
        END

        COMMIT;
    END
    ELSE
    BEGIN
        PRINT 'Fel: Inte tillräckligt antal i från-butiken.';
        ROLLBACK;
    END
END;


SELECT 
    ISBN
FROM 
    Böcker
WHERE 
    Böcker.Titel LIKE '%Predikanten%' 

SELECT
    Titel,
    Antal,
    Butiker.ButikNamn

FROM 
    Böcker
JOIN 
    LagerSaldo 
    ON LagerSaldo.ISBN = Böcker.ISBN
JOIN 
    Butiker 
    ON Butiker.ID = LagerSaldo.ButikID
WHERE 
    Böcker.ISBN = '9780450417382'

SELECT * FROM Böcker WHERE ISBN = 9789137132133;

SELECT * FROM LagerSaldo WHERE ISBN = 9789137132133;

SELECT 
    Böcker.Titel,
    LagerSaldo.Antal,
    Butiker.ButikNamn
FROM 
    Böcker
JOIN 
    LagerSaldo ON LagerSaldo.ISBN = Böcker.ISBN
JOIN 
    Butiker ON Butiker.ID = LagerSaldo.ButikID
WHERE 
    Böcker.ISBN = '9789137132133';


-- Hitta böcker och ge all info om boken, författare, gener, pris, utgivnings år, 
-- Hur många som finns i butik