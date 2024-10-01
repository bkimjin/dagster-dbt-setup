# Dagster

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).

## Getting started

Create the following environment variable:
| Environment Variable | Definition | Comments |
|----------------------|------------|----------|
| `DAGSTER_HOME`| Full path to the subdirectory `ndr_tests` | This is where the Dagster dev environment will live and persist. Create this subdirectory if it doesn't exist. |
| `DBT_TARGET` | `dev` | Only production runs should be `prod`. |
| `DBT_ROLE` | `dbt_engineer` | In most use cases, developers will use dbt_engineer. Contact the DE team if you are not part of the team. |
|`DBT_SCHEMA`| `<first initial><last name>` | This is the naming convention we're using for development environments. |
|`DBT_WH`| `development_wh` | In most use cases, developers will use dbt_engineer. Contact the DE team if you are not part of the team. |

Install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.

You can start writing assets in the sub directory `ndr/assets`. The assets are automatically loaded into the Dagster code location as you define them.

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Adding dbt entities

Refer here to build dbt assets in dagster: https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/load-dbt-models

### Schedules and sensors

If you want to enable Dagster [Schedules](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules) or [Sensors](https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors) for your jobs, the [Dagster Daemon](https://docs.dagster.io/deployment/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.

## Deploy on Dagster Cloud

The easiest way to deploy your Dagster project is to use Dagster Cloud.

Check out the [Dagster Cloud Documentation](https://docs.dagster.cloud) to learn more.
