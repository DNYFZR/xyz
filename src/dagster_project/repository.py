## Refer to Using dbt with Dagster, part two for info about this file:
## https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/part-two
import os
from dagster_dbt import dbt_cli_resource
from dagster import load_assets_from_package_module, repository, with_resources

from dagster_duckdb import build_duckdb_io_manager
from dagster_duckdb_pandas import DuckDBPandasTypeHandler

from dagster_project import assets
from dagster_project.assets import DBT_PROFILES, DBT_PROJECT_PATH, DB_NAME

@repository
def dbt_resource():
    duckdb_io_manager = build_duckdb_io_manager([DuckDBPandasTypeHandler()])
    return with_resources( 
        load_assets_from_package_module(assets), 
        {
            "dbt" : dbt_cli_resource.configured(
                { "project_dir" : DBT_PROJECT_PATH, "profiles_dir" : DBT_PROFILES, }),
            "io_manager" : duckdb_io_manager.configured(
                { "duckdb_path" : os.path.join(DBT_PROJECT_PATH, "/database/", DB_NAME), }),
        })
