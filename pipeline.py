from etl import pipeline_calcular_kpi_vendas_consolidado

pasta_argumento:str = 'data'
formato_saida:list = ["csv"]


pipeline_calcular_kpi_vendas_consolidado(pasta_argumento,formato_saida)