INSERT INTO Författare (
    Förnamn, 
    Efternamn,
    Födelsedatum
)
VALUES
('Astrid', 'Lindgren', '1907-11-14', '2002-01-28'),
('J.K.', 'Rowling', '1965-07-31', NULL),
('George', 'Orwell', '1903-06-25', '1950-01-21'),
('Camilla', 'Läckberg', '1974-08-30', NULL),
('Stephen', 'King', '1947-09-21', NULL);

GO

INSERT INTO Böcker (
    ISBN,
    Titel,
    Språk,
    Utgivningsdatum,
    Pris,
    FörfattarID

)

VALUES
-- Astrid Lindgren
('9789129703301', 'Pippi Långstrump', 'Svenska', '1945-11-25', 129.00, 1),
('9789129704216', 'Emil i Lönneberga', 'Svenska', '1963-01-01', 119.00, 1),
('9789129704728', 'Ronja Rövardotter', 'Svenska', '1981-09-15', 139.00, 1),

-- J.K. Rowling
('9780747532743', 'Harry Potter och De Vises Sten', 'Engelska', '1997-06-26', 199.00, 2),
('9780747538493', 'Harry Potter och Hemligheternas Kammare', 'Engelska', '1998-07-02', 209.00, 2),
('9780747542155', 'Harry Potter och Fången från Azkaban', 'Engelska', '1999-07-08', 219.00, 2),

-- George Orwell
('9780451524935', '1984', 'Engelska', '1949-06-08', 149.00, 3),
('9780451526342', 'Animal Farm', 'Engelska', '1945-08-17', 129.00, 3),
('9780451528124', 'Down and Out in Paris and London', 'Engelska', '1933-01-09', 159.00, 3),

-- Camilla Läckberg
('9789137131556', 'Isprinsessan', 'Svenska', '2003-08-01', 149.00, 4),
('9789137132133', 'Predikanten', 'Svenska', '2004-05-01', 159.00, 4),
('9789137132720', 'Stenhuggaren', 'Svenska', '2005-06-01', 169.00, 4),

-- Stephen King
('9780450417399', 'Carrie', 'Engelska', '1974-04-05', 149.00, 5),
('9780450417382', 'The Shining', 'Engelska', '1977-01-28', 179.00, 5),
('9780450417368', 'It', 'Engelska', '1986-09-15', 199.00, 5);

GO

INSERT INTO Butiker(
    Namn,
    [Address]
)

VALUES
('Bokcentralen Stockholm', 'Drottninggatan 10, Stockholm'),
('Bokcentralen Göteborg', 'Avenyn 25, Göteborg'),
('Bokcentralen Malmö', 'Storgatan 5, Malmö'),
('Bokcentralen Uppsala', 'Forumgallerian 1, Uppsala');

GO

INSERT INTO Kunder(
    Förnamn,
    Efternamn,
    Adress


)

VALUES
('Anna', 'Svensson', 'Storgatan 1, Malmö'),
('Erik', 'Johansson', 'Lundavägen 45, Lund'),
('Sara', 'Nilsson', 'Sveavägen 33, Stockholm'),
('Johan', 'Larsson', 'Södra Vägen 2, Göteborg'),
('Linda', 'Andersson', 'Östra Hamngatan 11, Göteborg');

GO

INSERT INTO LagerSaldo (
    ButikID,
    ISBN,
    Antal
)

VALUES 
-- Bokcentralen Stockholm
(1, '9789129703301', 10),
(1, '9780747532743', 6),
(1, '9780451524935', 5),

-- Bokcentralen Göteborg
(2, '9789137131556', 4),
(2, '9780450417382', 8),
(2, '9780747538493', 3),

-- Bokcentralen Malmö
(3, '9789129704216', 7),
(3, '9780450417399', 5),
(3, '9780451526342', 6),

-- Bokcentralen Uppsala
(4, '9780747542155', 9),
(4, '9780450417368', 2),
(4, '9789129704728', 4);

GO

INSERT INTO Ordrar (
    KundID,
    ISBN,
    ButikID,
    Antal,
    PrisVidKöp
)

VALUES 
(1, '9789129703301', 1, 1, 129.00),  
(1, '9780451526342', 3, 1, 129.00), 
(2, '9780450417382', 2, 1, 179.00),
(2, '9780747542155', 4, 1, 219.00), 
(3, '9780747532743', 1, 1, 199.00),  
(4, '9780450417368', 4, 1, 199.00),  
(5, '9789137132133', 2, 1, 159.00),  
(5, '9789129704728', 4, 1, 139.00);