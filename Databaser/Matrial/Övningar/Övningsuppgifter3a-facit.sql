-- F�retagets totala produktkatalog best�r av 77 unika produkter. Om vi kollar bland v�ra ordrar, 
-- hur stor andel av dessa produkter har vi n�gon g�ng leverarat till London?

select * from company.products;

select * from company.orders;

select * from company.order_details;

select count(*) from company.products

select
	--od.OrderId,
	--od.ProductId
	count(distinct(od.ProductId)) as NbrProd,
	count(distinct(od.ProductId)) / 77.0 as Ratio,
	count(distinct(od.ProductId)) / cast((select count(*) from company.products) as float) as Ratio
from
	company.order_details od
	inner join company.orders o on od.OrderId = o.Id
where
	o.ShipCity = 'London';


-- Till vilken stad har vi levererat flest unika produkter?
SELECT
    ShipCity,
    count(distinct(ProductID)) as 'Number of Products'
FROM    
    company.orders
	right join company.order_details on company.orders.ID = company.order_details.OrderID
group by
    ShipCity
order by
    'Number of Products' desc;

 -- Av de produkter som inte l�ngre finns I v�rat sortiment, hur mycket har vi s�lt f�r totalt till Tyskland?
 select * from company.products;


select
	*
	--sum((od.UnitPrice * od.Quantity) - (od.UnitPrice * od.Quantity * od.Discount)) as 'Amount in currency for discontinued products sold in total to Germany'
from company.order_details od
	join company.orders o on od.OrderId = o.Id
	join company.products p on od.ProductId = p.Id
where ShipCountry='Germany' and p.Discontinued=1


-- F�r vilken produktkategori har vi h�gst lagerv�rde?

select
    company.categories.CategoryName,
    sum(company.products.UnitsInStock * company.products.UnitPrice) as 'Total Stock Value'
from
    company.products
right join
    company.categories
on
    company.products.CategoryID = company.categories.ID
group by
    company.categories.CategoryName
order by
    'Total Stock Value' desc;


 -- Fr�n vilken leverant�r har vi s�lt flest produkter totalt under sommaren 2013?

 select
    company.suppliers.CompanyName,
    sum(company.order_details.Quantity) as 'Total Quantity'
from
    company.orders
right join
    company.order_details
on
    company.orders.ID = company.order_details.OrderID
right join
    company.products
on
    company.order_details.ProductID = company.products.ID
right join
    company.suppliers
on
    company.products.SupplierID = company.suppliers.ID
where
    company.orders.OrderDate >= '2013-06-01' and OrderDate <= '2013-09-01'
group by
    company.suppliers.CompanyName
order by
    'Total Quantity' desc;








