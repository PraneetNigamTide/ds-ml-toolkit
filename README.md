# DS-ML-Toolkit Python Package

## Overview
The `ds-ml-toolkit` package provides a set of tools and utilities to simplify data science and machine learning workflows.

## Installation

### From Source
1. Clone the repository:
```https://github.com/PraneetNigamTide/ds-ml-toolkit```

2. Navigate to the project directory:
```cd ds-ml-toolkit```

3. Build and install the package:
```
pip3 install build
python3 -m build
pip install dist/ds_ml_toolkit-*.whl
```

### From Github
You can install the package directly from GitHub using pip. Here's how:

1. Using the Repository URL:
```
pip install git+https://github.com/PraneetNigamTide/ds-ml-toolkit.git
```

## Usage
### Importing the Package
```
from ds_ml_toolkit import SnowflakeConn
```

### Initializing the Connection
```
conn = SnowflakeConn(
    scope="my_scope",
    database="my_database",
    warehouse="my_warehouse",
    role="my_role",
    sfUrl="my_sfUrl",
    sfUser="my_sfUser",
    sfPassword="my_sfPassword"
)
```

### Fetching Data
```
sql_query = "SELECT * FROM my_table"
dataframe = conn.load_raw_data(sql_query)
dataframe.show()
```