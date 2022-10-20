# Asset registry
import pandas as pd, plotly.express as px
from dagster import AssetIn, MetadataValue, asset, file_relative_path

# Project Info
PROJECT_NAME = "dbt_project"
DB_NAME = "dagster.duckdb"

# Asset Sources
CUSTOMERS_RAW = "https://docs.dagster.io/assets/customers.csv"
ORDERS_RAW = "https://docs.dagster.io/assets/orders.csv"

# Output Schema
OUTPUT_NAME = "OrderCount.html"

# Asset Config

class dagster_input_assets:
    @asset(key_prefix=[PROJECT_NAME], group_name="staging")
    def customers_raw() -> pd.DataFrame:
        return pd.read_csv(CUSTOMERS_RAW)

    @asset(key_prefix=[PROJECT_NAME], group_name="staging")
    def orders_raw() -> pd.DataFrame:
        return pd.read_csv(ORDERS_RAW)


class dagster_output_assets:
    @asset(ins={"customers": AssetIn(key_prefix=[PROJECT_NAME])}, group_name="staging", )
    def order_count_plot(context, customers: pd.DataFrame):
        fig = px.histogram(customers, x = 'number_of_orders')
        fig.update_layout(bargap = 0.25)

        chart_path = file_relative_path(__file__, f"../output/{OUTPUT_NAME}")
        fig.write_html(chart_path, auto_open=True)

        context.add_output_metadata({"plot_url": MetadataValue.url(f"file://{chart_path}")})