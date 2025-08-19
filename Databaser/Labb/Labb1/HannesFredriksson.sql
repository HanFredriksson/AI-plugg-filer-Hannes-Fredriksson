SELECT 
    Spacecraft, 
    [Launch date], 
    [Carrier rocket], 
    Operator, 
    [Mission type]

INTO 
    SuccessfulMissions
FROM 
    MoonMissions

GO

UPDATE SuccessfulMissions
SET Operator = LTRIM(Operator)

GO

UPDATE SuccessfulMissions
SET Spacecraft = 
    CASE 
        WHEN CHARINDEX('(', Spacecraft) > 0 
        THEN RTRIM(LEFT(Spacecraft, CHARINDEX('(', Spacecraft) - 1))
        ELSE Spacecraft
    END

GO

SELECT 
    Operator, 
    [Mission type],
    COUNT(Operator) AS  'Mission count'


FROM 
    SuccessfulMissions
GROUP BY   
    Operator, 
    [Mission type]
HAVING  
    COUNT(Operator) > 1
ORDER BY Operator, 
    [Mission type]

GO

SELECT *,
    CONCAT(FirstName, ' ', LastName) AS 'Name',
    CASE
        WHEN    
            SUBSTRING(RIGHT(ID, 2), 1, 1) % 2 = 0  THEN 'Female' 
        ELSE 
            'Male' 
    END AS 
        'Gender'

INTO    
    NewUsers
FROM 
    Users

GO

SELECT UserName,
    COUNT(UserName) AS 'duplicates' 

FROM NewUsers
GROUP By UserName
HAVING COUNT(UserName) > 1 

GO

ALTER TABLE NewUsers
ALTER COLUMN UserName NVARCHAR(50);
WITH DuplicateUsers AS (
    SELECT ID,
        UserName,
           ROW_NUMBER() OVER (PARTITION BY UserName ORDER BY ID) AS du
    FROM NewUsers
)
UPDATE NU
SET UserName = LEFT(DU.UserName + CAST(DU.du AS NVARCHAR), 50)
FROM NewUsers NU
JOIN DuplicateUsers DU ON NU.ID = DU.ID
WHERE DU.du > 1;

EXEC sp_help 'NewUsers';

GO

DELETE FROM NewUsers
WHERE Gender = 'Female' and LEFT(ID, 2) < 70

GO

INSERT INTO NewUsers
VALUES ('890225-6651', 
    'hanfre', 
    '10f8jvbfw54i6lcxvo8ezr8unlxi105h', 
    'Hannes', 
    'Fredriksson', 
    'hanfre@mail.se', 
    '076-6589321', 
    'Hannes Fredriksson', 
    'Male'
)

GO

SELECT Gender,
    AVG(datediff(YEAR, CONVERT(date, LEFT(ID, 6)), GETDATE())) as 'avarage age'

FROM NewUsers
GROUP BY Gender

GO

SELECT company.products.Id,
    company.products.ProductName,
    company.suppliers.CompanyName,
    company.categories.CategoryName
FROM   
    company.products
INNER JOIN 
    company.suppliers 
ON 
    company.products.SupplierId = company.suppliers.Id
INNER JOIN 
    company.categories
ON 
    company.products.SupplierId = company.categories.Id

GO

SELECT  
    company.regions.RegionDescription,
    COUNT(company.regions.RegionDescription) AS 'Total employees'
FROM 
    company.employees
JOIN 
    company.territories
ON 
    company.employees.City = company.territories.TerritoryDescription
RIGHT JOIN 
    company.regions 
ON 
    company.regions.Id = company.territories.RegionId
GROUP BY 
    company.regions.RegionDescription

GO

SELECT 
    r.RegionDescription,
    COUNT(DISTINCT e.ID) AS [Total employees]
FROM   
    company.regions r
JOIN 
    company.territories t ON t.RegionID = r.ID
JOIN 
    company.employee_territory et ON et.TerritoryID = t.ID
JOIN 
    company.employees e ON e.ID = et.EmployeeID
GROUP BY 
    r.RegionDescription

GO

SELECT  
    CONCAT(E.FirstName, ' ', E.LastName) AS EmployeeName,
    E.ID AS Employee,
    CASE 
        WHEN   
            M.Id IS NULL THEN 'Nobody'
        ELSE 
            CONCAT(M.FirstName, ' ', M.LastName)
    END AS 
        ManagerName

FROM    
    company.employees E
LEFT JOIN   
    company.employees M ON E.ReportsTo = M.ID