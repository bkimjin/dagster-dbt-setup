# Instructions from https://docs.dagster.io/integrations/fivetran
from dagster_fivetran import FivetranResource, build_fivetran_assets, load_assets_from_fivetran_instance
from dagster import EnvVar, with_resources, AssetKey

# Fivetran configuration
fivetran_instance = FivetranResource(
    api_key=EnvVar("FIVETRAN_API_KEY"),
    api_secret=EnvVar("FIVETRAN_API_SECRET"),
)

# Creating a Dagster asset merely initializes it within Dagster, but doesn't run the connector itself.
# This means that manually loading Fivetran jobs is only for specific connectors that we know has a
# list of tables that will not change in the future.  That way, if a table does change for some
# reason, then it will through an error.
# In a conversation with Rob on 2024-09-22, this is a non starter.

# Manually Load Fivetran assets
# This methodology requires individually creating each destination tables. This method is not scalable.

# fivetran_assets = with_resources(
#     build_fivetran_assets(
#         connector_id="botanical_stayed",
#         # destination_tables is purely for Dagster visibility. Has no impact on actual Fivetran tables
#         destination_tables=["jira.comment", "jira.epic", "jira.issue"],
#     ),
#     {"fivetran": fivetran_instance}
# )

# Automatically Load Fivetran assets
# This method loads all connectors from Fivetran into the Dagster graph.

# We need to specify the connect_to_asset_key_fn because we have multiple identical connectors (e.g.
# fivetran_metadata for both GCP and Snowflake). Therefore we define the AssetKey to include the connector
# service to be included in the name of the asset.
connector_to_asset_key_fn = lambda connector, table: AssetKey(path=[connector.service, *table.split(".")])

fivetran_assets = load_assets_from_fivetran_instance(
    fivetran_instance,
    connector_to_asset_key_fn=connector_to_asset_key_fn
)
