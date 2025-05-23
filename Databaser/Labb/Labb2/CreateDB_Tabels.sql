CREATE DATABASE Bookhandel;

GO

CREATE TABLE Författare (
    ID INT PRIMARY KEY IDENTITY,
    Förnamn NVARCHAR(50), 
    Efternamn NVARCHAR(50),
    Födelsedatum DATE,
    Dödsdatum DATE
);

GO

CREATE TABLE Böcker (
    ISBN CHAR(13) NOT NULL PRIMARY KEY,
    Titel NVARCHAR(100),
    Språk NVARCHAR(50),
    Utgivningsdatum DATE,
    Pris DECIMAL(10, 2) CHECK (Pris >= 0),
    FörfattarID INT,

    CONSTRAINT FK_Bok_Författare FOREIGN KEY (FörfattarID) REFERENCES Författare(ID)
);

GO

CREATE TABLE Butiker (
    ID INT PRIMARY KEY IDENTITY,
    Namn NVARCHAR(50),
    [Address] CHAR(100)
);

GO

CREATE TABLE Kunder(
    ID INT PRIMARY KEY IDENTITY,
    Förnamn NVARCHAR(50),
    Efternamn NVARCHAR(50),
    Adress NVARCHAR(100),


)

GO

CREATE TABLE LagerSaldo (
    ButikID INT NOT NULL,
    ISBN CHAR(13) NOT NULL,
    Antal INT NOT NULL CHECK (Antal >= 0),
    
    CONSTRAINT PK_LagerSaldo PRIMARY KEY (ButikID, ISBN),
    CONSTRAINT FK_LagerSaldo_Butik FOREIGN KEY (ButikID) REFERENCES Butiker(ID),
    CONSTRAINT FK_LagerSaldo_Bok FOREIGN KEY (ISBN) REFERENCES Böcker(ISBN)
);

GO

CREATE TABLE Ordrar (
    ID INT PRIMARY KEY IDENTITY,
    KundID INT NOT NULL,
    ISBN CHAR(13) NOT NULL,
    ButikID INT NOT NULL,
    Antal INT NOT NULL CHECK (Antal > 0),
    PrisVidKöp DECIMAL(10,2) NOT NULL,
    
    CONSTRAINT FK_Ordrar_KundID FOREIGN KEY (KundID) REFERENCES Kunder(ID),
    CONSTRAINT FK_Ordrar_ISBN FOREIGN KEY (ISBN) REFERENCES Böcker(ISBN),
    CONSTRAINT FK_Ordrar_ButikID FOREIGN KEY (ButikID) REFERENCES Butiker(ID)
);

GO
