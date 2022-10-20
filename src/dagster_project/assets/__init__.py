import sys
from dagster_dbt import load_assets_from_dbt_project
from dagster import file_relative_path

sys.path.append('../../')
from asset_registry import PROJECT_NAME, DB_NAME, dagster_input_assets, dagster_output_assets

# Project Config
DBT_PROJECT_PATH = file_relative_path(__file__, f"../../{PROJECT_NAME}")
DBT_PROFILES = file_relative_path(__file__, f"../../{PROJECT_NAME}/config")
DB_PATH = file_relative_path(__file__, f"{DBT_PROJECT_PATH}/database/")

# Input Asset Config
input_methods = [i for i in dir(dagster_input_assets) if i[:2] != '__']
input_vars = vars()

for method in input_methods:
    input_vars[method] = getattr(dagster_input_assets, method)

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, 
    profiles_dir=DBT_PROFILES,
    key_prefix=[PROJECT_NAME], )


# Output Asset Config
output_methods = [i for i in dir(dagster_output_assets) if i[:2] != '__']
output_vars = vars()

for method in output_methods:
    output_vars[method] = getattr(dagster_output_assets, method)