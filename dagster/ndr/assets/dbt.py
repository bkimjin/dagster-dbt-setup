from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from ..project import ndr_project

@dbt_assets(manifest=ndr_project.manifest_path)
def ndr_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()