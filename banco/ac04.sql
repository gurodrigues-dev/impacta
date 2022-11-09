--EXERCICIO 01 
select count (idVendas)
from VendasAnuais


--EXERCICIO 02
select sum(qtd) as TotalVendas
from VendasAnuais


--EXERCICIO 03
select min(qtd) as MenorVenda, avg(qtd) as MédiaVendas, max(qtd) as MaiorVenda
from VendasAnuais


--EXERCICIO 04
select sum(qtd) as SomaVendas, idAnodaVenda
from VendasAnuais
group by (idAnodaVenda)
order by (idAnodaVenda) desc


--EXERCICIO 05
SELECT sum(idVendas) as 'quantidade de vendas',
    Veiculo.descricao as 'modelo do veiculo',
    Modelo.descricao as 'tipo de modelo',
    Veiculo.idFabricante as 'identificador do fabricante',
    Veiculo.idModelo as 'identificador do modelo',
    Veiculo.valor as 'Valor do modelo',
    Veiculo.idAnoFabricacao as 'identificador do ano de fabricação'
FROM VendasAnuais
    inner join Veiculo on Veiculo.idVeiculo = VendasAnuais.idVeiculo
    inner join Modelo on Modelo.idModelo = Veiculo.idModelo
where Veiculo.descricao = 'CG 125' and Modelo.descricao = 'STD'
group by Modelo.descricao, 
                    Veiculo.descricao, 
                    Veiculo.idFabricante,
                    Veiculo.idModelo,
                    Veiculo.valor,
                    Veiculo.idAnoFabricacao


--EXERCICIO 06
SELECT Fabricante.Nome as 'Nome do fabricante',
    Ano.ano as 'Ano de fabricação',
    Veiculo.descricao as    'Nome do veículo',
    Modelo.descricao as 'Nome do modelo'
FROM Veiculo
    inner join Modelo on Modelo.idModelo = Veiculo.idModelo
    inner join Ano on Ano.idAno = Veiculo.idAnoFabricacao
    inner join Fabricante on Fabricante.idFabricante = Veiculo.idFabricante
order by Fabricante.Nome asc, Ano.ano desc, Veiculo.descricao asc, Modelo.descricao desc


--EXERCICIO 07
SELECT Ano.ano as 'Ano da Venda',
    Mes.mes as 'Mes da venda',
    min(VendasAnuais.qtd) as 'Menor Venda',
    max(VendasAnuais.qtd) 'Maior Venda',
    avg(VendasAnuais.qtd) as 'Média de Venda',
    sum(VendasAnuais.qtd) as 'Soma das vendas'
FROM VendasAnuais
    INNER JOIN Ano on Ano.idAno = VendasAnuais.idAnodaVenda
    INNER JOIN Mes on Mes.idMes = VendasAnuais.idMesdaVenda
WHERE Ano.ano = '2000'
GROUP BY Ano.ano, Mes.mes
ORDER BY Ano.ano asc, Mes.mes asc


--EXERCICIO 08
SELECT Ano.ano as 'Ano da Venda',
    Mes.mes as 'Mes da venda',
    min(VendasAnuais.qtd) as 'Menor Venda',
    max(VendasAnuais.qtd) 'Maior Venda',
    avg(VendasAnuais.qtd) as 'Média de Venda',
    sum(VendasAnuais.qtd) as 'Soma das vendas'
FROM VendasAnuais
    INNER JOIN Ano on Ano.idAno = VendasAnuais.idAnodaVenda
    INNER JOIN Mes on Mes.idMes = VendasAnuais.idMesdaVenda
WHERE Ano.ano = '2000'
GROUP BY Ano.ano, Mes.mes
HAVING avg(VendasAnuais.qtd) > 500
ORDER BY Ano.ano asc, Mes.mes asc