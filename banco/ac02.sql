--exercicio 1
GO

create view EXEC_01
as
    select Sales.Orders.orderid as 'número do pedido',
        Sales.Orders.orderdate as 'data do pedido',
        Sales.Customers.contactname as 'nome dp contato',
        Sales.Customers.country as 'pais'
    from Sales.Orders
        inner join Sales.Customers on Sales.Customers.custid = Sales.Orders.custid;

--exercicio 2
GO

create view EXEC_02
as
    select Sales.Orders.orderdate as 'data do pedido',
        Sales.Customers.contactname as 'nome do contato',
        CONCAT(HR.Employees.firstname,' ',HR.Employees.lastname) as 'nome do empregado',
        HR.Employees.country as 'pais do empregado'
    from Sales.Orders
        inner join Sales.Customers on Sales.Customers.custid = Sales.Orders.custid
        inner join HR.Employees on HR.Employees.empid = Sales.Orders.empid
    where HR.Employees.country = 'UK';

--Eexercicio 3
select Sales.Orders.orderid as 'numero do pedido',
    Sales.Orders.orderdate as 'data do pedido',
    Sales.Customers.contactname as 'contato do cliente',
    CONCAT(HR.Employees.firstname,' ',HR.Employees.lastname) as 'nome completo do empregado',
    Sales.Customers.country as 'pais do cliente'
from Sales.Orders
    inner join Sales.Customers on Sales.Customers.custid = Sales.Orders.custid
    inner join HR.Employees on HR.Employees.empid = Sales.Orders.empid
where Sales.Customers.country = 'Brazil'
order by Sales.Orders.orderdate desc;

--exercicio 4
select Sales.Orders.orderid as 'numero do pedido',
    Sales.Orders.orderdate as 'data do pedido',
    Sales.Customers.contactname as 'nome do contato',
    CONCAT(HR.Employees.firstname,' ',HR.Employees.lastname) as 'nome completo do empregado',
    HR.Employees.country as 'pais do empregado',
    Sales.Shippers.companyname as 'nome da empresa de entrega'
from Sales.Orders
    inner join Sales.Shippers on Sales.Shippers.shipperid = Sales.Orders.shipperid
    inner join HR.Employees on HR.Employees.empid = Sales.Orders.empid
    inner join Sales.Customers on Sales.Customers.custid = Sales.Orders.custid
where HR.Employees.country = 'USA' and Sales.Shippers.companyname = 'Shipper ETYNR'
    or HR.Employees.country = 'USA' and Sales.Shippers.companyname = 'Shipper GVSUA'
order by Sales.Orders.orderid desc

--exercicio 5
select Production.Products.productname as 'nome do produto',
    Production.Categories.categoryname as 'categoria do produto',
    Production.Products.unitprice as 'preco do produto'
from Production.Products
    inner join Production.Categories on Production.Categories.categoryid = Production.Products.categoryid
where Production.Products.unitprice < 30
order by Production.Products.unitprice desc;

--exercicio 6
select Production.Products.productname as 'nome do produto',
    Production.Suppliers.companyname as 'nome da empresa',
    Sales.OrderDetails.qty as 'quantidade de produtos'
from Production.Products
    inner join Production.Suppliers on Production.Suppliers.supplierid = Production.Products.supplierid
    inner join Sales.OrderDetails on Sales.OrderDetails.productid = Production.Products.productid
where Sales.OrderDetails.qty > 100
order by Production.Products.productname asc, Sales.OrderDetails.qty desc

--exercicio 7
select Production.Products.productname as 'nome do produto',
    Sales.Customers.contactname as 'nome do contato',
    Sales.Customers.companyname as 'nome da empresa',
    Sales.OrderDetails.qty as 'quantidade do produto',
    Sales.Orders.orderdate as 'data dos pedidos',
    Production.Suppliers.city as 'cidade do fornecedor',
    HR.Employees.empid as 'numero do empregado'
from Sales.Orders
    inner join Sales.Customers on Sales.Customers.custid = Sales.Orders.custid
    inner join Sales.OrderDetails on Sales.OrderDetails.orderid = Sales.Orders.orderid
    inner join Production.Products on Production.Products.productid = Sales.OrderDetails.productid
    inner join Production.Suppliers on Production.Suppliers.supplierid = Production.Products.supplierid
    inner join HR.Employees on HR.Employees.empid = Sales.Orders.empid
where Sales.Orders.orderdate between '20060701' and '20060731' and
    Sales.OrderDetails.qty >= 20 and Sales.OrderDetails.qty < 60 and
    Production.Products.productname like '%product a%' and
    Production.Suppliers.city = 'Stockholm' or Production.Suppliers.city = 'Sydney' or Production.Suppliers.city = 'Sandvika' or Production.Suppliers.city = 'Ravenna'
order by HR.Employees.empid desc