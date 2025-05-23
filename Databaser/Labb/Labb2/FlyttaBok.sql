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

