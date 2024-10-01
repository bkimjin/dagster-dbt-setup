from dagster import Definitions, load_assets_from_package_module
from dagster_dbt import DbtCliResource

from . import assets
from .project import ndr_project

all_assets = load_assets_from_package_module(assets)

defs = Definitions(
    assets=all_assets,
    resources={
        "dbt": DbtCliResource(project_dir=ndr_project),
    },
)
