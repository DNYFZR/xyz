## Refer to Using dbt with Dagster, part two for info about this file:
## https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/part-two
import pandas as pd, plotly.express as px
from dagster_dbt import load_assets_from_dbt_project
from dagster import AssetIn, MetadataValue, asset, file_relative_path

# Project Config
PROJECT_NAME = "dbt_project"
DBT_PROJECT_PATH = file_relative_path(__file__, f"../../{PROJECT_NAME}")
DBT_PROFILES = file_relative_path(__file__, f"../../{PROJECT_NAME}/config")

# Data Config
DB_NAME = "dagster.duckdb"
CUSTOMERS_RAW = "https://docs.dagster.io/assets/customers.csv"
ORDERS_RAW = "https://docs.dagster.io/assets/orders.csv"

# Asset Config
@asset(key_prefix=[PROJECT_NAME], group_name="staging")
def customers_raw() -> pd.DataFrame:
    return pd.read_csv(CUSTOMERS_RAW)

@asset(key_prefix=[PROJECT_NAME], group_name="staging")
def orders_raw() -> pd.DataFrame:
    return pd.read_csv(ORDERS_RAW)

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, 
    profiles_dir=DBT_PROFILES,
    key_prefix=[PROJECT_NAME], )


# Create Dagster Asset
@asset(ins={"customers": AssetIn(key_prefix=[PROJECT_NAME])}, group_name="staging", )
def order_count_plot(context, customers: pd.DataFrame):
  fig = px.histogram(customers, x = 'number_of_orders')
  fig.update_layout(bargap = 0.25)

  chart_path = file_relative_path(__file__, "OrderCount.html")
  fig.write_html(chart_path, auto_open=True)

  context.add_output_metadata({"plot_url": MetadataValue.url(f"file://{chart_path}")})
  