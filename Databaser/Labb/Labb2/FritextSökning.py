from sqlalchemy import create_engine
from sqlalchemy import text
import os


server = "localhost"
database = "BookHandel"
username = "bok_läsare"
password = "säkert_lösenord"
driver = "ODBC Driver 17 for SQL Server"

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}"
)
engine = create_engine(connection_string)

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def lookfortitle(title):

    # Fritextsökning med parameter för att skydda mot SQL-injection
    stmt = text("""
    SELECT 
        Böcker.ISBN, 
        Böcker.Titel, 
        Butiker.ButikNamn, 
        LagerSaldo.Antal 
    FROM 
        Böcker 
    JOIN 
        LagerSaldo ON LagerSaldo.ISBN = Böcker.ISBN 
    JOIN 
        Butiker ON Butiker.ID = LagerSaldo.ButikID 
    WHERE 
        Böcker.Titel LIKE :title
    """)

    with engine.connect() as conn:
        result = conn.execute(stmt, {"title": f"%{title}%"}).fetchall()
        if result:
            for row in result:
                print(f"Titel: {row.Titel}, ISBN: {row.ISBN}, Butik: {row.ButikNamn}, Antal: {row.Antal}")
        else:
            print("Inga böcker hittades.")


while True:
        clear_terminal()  
        input_title = input("Söker boktitel: ")
        print("------------------\n")  

        try:
            # Show result from found books
            lookfortitle(input_title)
                
        except Exception as e:
            # If book is not found or another error occurs, notify the user
            print(f"\nKunde inte hitta titel '{input_title}'. Error: {e}")
            input("\nTryck Enter för att frösöka igen...")
            continue  
       
        again = input("\n\nVill du söka upp en till bok? (j/n): ").lower()
        if again != "j":

            print("Hej då!")
            break  
