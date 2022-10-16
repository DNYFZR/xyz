<h2 align="center"><b> 🧬 XYZ 🧬 </b></h2>

<p align="center">Data Pipeline using Dagster, dbt & DuckDB</p><br>

<h3 align="center"><b> 🧱 Project Build </b></h3>

---

Taking a minimalist approach to these tools, with the aim of developing a streamlined data processing system with minimal user input. Docker may also play a part in the final design.

In testing this project :

- Raw data will be fetched with Pandas
- Processed using dbt
- Stored within DuckDB
- Orchestration handled with Dagster
- Outputs will be visaulized using Plotly or Streamlit (TBD)


<br><h3 align="center"><b> 🌿 Dev Environment </b></h3>

---

This repo has been developed in the following environment :

````yaml
Environment:
  - Python: 3.10.8
  - setuptools: 63.2.0
  - pip: 22.2.2

Dependencies:
  dbt: 
    - dbt-core: 1.3.0
    - dbt-duckdb: 1.2.2
  dagster: 
    - dagster: 1.0.13
    - dagit: 1.0.13
    - dagster-dbt: 0.16.13
    - dagster-duckdb: 0.16.13
    - dagster-duckdb-pandas: 0.16.13
  pandas: 1.5.0
  plotly: 5.10.0
  pytest: 7.1.3 
````

<br><h3 align="center"><b> 📚 Notes </b></h3>

From the command line : 

- To clone the template project from Dagster :

````cli
dagster project from-example --name dbt_dagster --example tutorial_dbt_dagster 
````

- To run the workflow :

````cli
cd <dir containing workspace.yml>

dagit
````

- To terminate :

````cli
ctrl+c
````

References :

- Dagster & Docker: [Deploying Dagster to Docker](https://docs.dagster.io/deployment/guides/docker)
- Dagster Guide : [Dagster, dbt & DuckDB tutorial](https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster)
- dbt dev project: [jaffle shop](https://github.com/dbt-labs/jaffle_shop)

---
---
