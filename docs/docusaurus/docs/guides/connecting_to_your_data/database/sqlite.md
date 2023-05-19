---
title: How to connect to a SQLite database
---

import Prerequisites from '../components/prerequisites.jsx'
import WhereToRunCode from '../components/where_to_run_code.md'
import NextSteps from '../components/next_steps.md'
import Congratulations from '../components/congratulations.md'
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import TechnicalTag from '@site/docs/term_tags/_tag.mdx';
import SqlAlchemy2 from '/docs/components/warnings/_sql_alchemy2.md'

This guide will help you connect to data in a SQLite database.
This will allow you to <TechnicalTag tag="validation" text="Validate" /> and explore your data.

## Prerequisites

<Prerequisites>

- Have access to data in a SQLite database

</Prerequisites>


## Steps

### 1. Choose how to run the code in this guide

<WhereToRunCode />

### 2. Install required dependencies

First, install the necessary dependencies for Great Expectations to connect to your SQLite database by running the following in your terminal:

<SqlAlchemy2 />

```console
pip install sqlalchemy
```

### 3. Configure the URL for your SQLite database

Since SQLite connects to file-based databases, the URL format is slightly different from other DBs.
For this guide we will use a `connection_string` that looks like this:

```
sqlite:///<PATH_TO_DB_FILE>
```   

For more details on different ways to specify database files and information on how to connect to an in-memory SQLite database, please refer to the documentation on [SQLAlchemy](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlite).

### 4. Instantiate your project's DataContext

Import these necessary packages and modules.

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_yaml_example.py imports"
```

Load your DataContext into memory using the `get_context()` method.

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_yaml_example.py get_context"
```

### 5. Configure your Datasource

<Tabs
  groupId="yaml-or-python"
  defaultValue='yaml'
  values={[
  {label: 'YAML', value:'yaml'},
  {label: 'Python', value:'python'},
  ]}>

<TabItem value="yaml">

Put your connection string in this template:

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_yaml_example.py datasource_yaml"
```

Run this code to test your configuration.

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_yaml_example.py test_yaml_config"
```

</TabItem>

<TabItem value="python">

Put your connection string in this template:

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_python_example.py datasource_config"
```

Run this code to test your configuration.

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_python_example.py test_yaml_config"
```

</TabItem>

</Tabs>

You will see your database tables listed as `Available data_asset_names` in the output of `test_yaml_config()`.

Feel free to adjust your configuration and re-run `test_yaml_config` as needed.

### 6. Save the Datasource configuration to your DataContext

Save the configuration into your `DataContext` by using the `add_datasource()` function.

<Tabs
  groupId="yaml-or-python"
  defaultValue='yaml'
  values={[
  {label: 'YAML', value:'yaml'},
  {label: 'Python', value:'python'},
  ]}>

<TabItem value="yaml">

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_yaml_example.py add_datasource"
```

</TabItem>

<TabItem value="python">

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_python_example.py add_datasource"
```

</TabItem>

</Tabs>

### 7. Test your new Datasource

Verify your new <TechnicalTag tag="datasource" text="Datasource" /> by loading data from it into a <TechnicalTag tag="validator" text="Validator" /> using a `BatchRequest`.

<Tabs
  defaultValue='runtime_batch_request'
  values={[
  {label: 'Using a SQL query', value:'runtime_batch_request'},
  {label: 'Using a table name', value:'batch_request'},
  ]}>

<TabItem value="runtime_batch_request">

Here is an example of loading data by specifying a SQL query.

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_yaml_example.py query batch_request"
```

</TabItem>

<TabItem value="batch_request">

Here is an example of loading data by specifying an existing table name.

```python name="tests/integration/docusaurus/connecting_to_your_data/database/sqlite_python_example.py batch request table name"
```

</TabItem>

</Tabs>

<Congratulations />

## Additional Notes

To view the full scripts used in this page, see them on GitHub:

- [sqlite_yaml_example.py](https://github.com/great-expectations/great_expectations/blob/develop/tests/integration/docusaurus/connecting_to_your_data/database/sqlite_yaml_example.py)
- [sqlite_python_example.py](https://github.com/great-expectations/great_expectations/blob/develop/tests/integration/docusaurus/connecting_to_your_data/database/sqlite_python_example.py)

## Next Steps

<NextSteps />