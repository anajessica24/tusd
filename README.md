# TUSD

Estudo de dados da ANEEL sobre a TUSD (Energia Solar).

**Fonte de dados:** [dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/tarifas-distribuidoras-energia-eletrica)

---

## O que é a TUSD

A **Tarifa de Uso do Sistema de Distribuição (TUSD)** é o valor cobrado pelas distribuidoras de energia elétrica pelo uso da rede de distribuição.  

Ela **não se refere ao consumo de energia**, mas sim ao custo de levar a eletricidade até o consumidor final — cobrindo manutenção, operação e investimentos na infraestrutura de distribuição.  

Na conta de luz, aparece como um dos componentes do valor total pago pelo cliente.

---

## Análise de Tarifas TUSD - Subgrupo B4 da ENERGISA

Este projeto tem como objetivo **analisar a evolução das tarifas de TUSD** para o **subgrupo B4** da distribuidora **ENERGISA (ESE)** ao longo dos anos.  

O dataset utilizado contém informações de tarifas homologadas pela ANEEL, incluindo **valores médios, máximos e mínimos** para diferentes períodos.

---

## Estrutura do Projeto

### Arquivo CSV: `tarifas_tusd.csv`

Contém os dados de tarifas, incluindo:

- `DatGeracaoConjuntoDados` — Data de geração do conjunto de dados  
- `DscREH` — Resolução Homologatória  
- `SigAgente` — Sigla do agente de distribuição  
- `NumCNPJDistribuidora` — CNPJ da distribuidora  
- `DatInicioVigencia`, `DatFimVigencia` — Datas de início e fim de vigência  
- `DscBaseTarifaria` — Descrição base tarifária  
- `DscSubGrupo`, `DscSubClasse` — Subgrupo e subclasse  
- `DscClasse`, `DscDetalhe` — Classe e detalhe da tarifa  
- `VlrTUSD` — Valor da TUSD  

### Script Python: `analise02.py`

Responsável por:

- Ler o arquivo CSV (tratando diferentes codificações UTF-8 e Latin1)  
- Converter a coluna `VlrTUSD` para valores numéricos  
- Filtrar os dados do subgrupo B4 da ENERGISA  
- Agrupar os dados por ano de início de vigência  
- Calcular **média, mínimo e máximo** das tarifas por ano  
- Plotar a evolução anual das tarifas  

---

## Dependências

- Python >= 3.8  
- Pandas  
- Matplotlib  

Instalação via pip:

```bash
pip install pandas matplotlib
