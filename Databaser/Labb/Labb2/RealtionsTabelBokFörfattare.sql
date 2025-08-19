
ALTER TABLE Böcker DROP CONSTRAINT FK_Bok_Författare;
ALTER TABLE Böcker DROP COLUMN FörfattarID;

GO

-- Vi har skapat en many-to-many-relation mellan böcker och författare genom 
-- att ta bort direktlänken från 'Böcker' till 'Författare' och istället använda en kopplingstabell 'Bok_Författare'. 
-- Detta möjliggör att en bok kan ha flera författare, vilket är vanligt i verkligheten.

CREATE TABLE BokFörfattare (
    ISBN CHAR(13) NOT NULL,
    FörfattarID INT NOT NULL,

    PRIMARY KEY (ISBN, FörfattarID),
    FOREIGN KEY (ISBN) REFERENCES Böcker(ISBN),
    FOREIGN KEY (FörfattarID) REFERENCES Författare(ID)
);

GO

INSERT INTO BokFörfattare(ISBN, FörfattarID)
SELECT Böcker.ISBN, Författare.ID
FROM Böcker, Författare

GO

