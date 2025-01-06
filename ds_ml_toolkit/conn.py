import pyspark.sql
from pyspark.sql import SparkSession

class SnowflakeConn:
    """
    Singleton Design Pattern

    Connect with Snowflake for:
    1. Fetching SQL query results in PySpark DataFrame.
    2. Saving PySpark DataFrame to Snowflake table.
    """

    def __init__(self, scope: str, database: str, warehouse: str, role: str, sfUrl: str, sfUser: str, sfPassword: str) :
        self.scope = scope
        self.database = database
        self.warehouse = warehouse
        self.role = role
        self.sfUrl = sfUrl
        self.sfUser = sfUser
        self.sfPassword = sfPassword
        self.__credentials = {
            "sfUrl": sfUrl,
            "sfUser": sfUser,
            "sfPassword": sfPassword,
        }

    def conn_config(self):
        """Return Snowflake connection configuration."""
        return {
            **self.__credentials,
            "sfDatabase": self.database,
            "sfWarehouse": self.warehouse,
            "sfRole": self.role,
        }

    def load_raw_data(self, _sql: str) -> pyspark.sql.DataFrame:
        """Load result of SQL query into a PySpark DataFrame."""
        connection = self.conn_config()
        return SparkSession.builder.getOrCreate().read \
            .format("snowflake") \
            .options(**connection) \
            .option("query", _sql) \
            .load()

    def save_data(self, df: pyspark.sql.DataFrame, schema: str, table: str, _mode: str):
        """Save PySpark DataFrame to a Snowflake table."""
        connection = self.conn_config()
        connection.update({"sfSchema": schema})
        try:
            df.write \
                .format("snowflake") \
                .mode(_mode) \
                .options(**connection) \
                .option("dbtable", table) \
                .save()
        except Exception as exc:
            raise Exception(f"Error saving data to Snowflake: {exc}")

    @staticmethod
    def read_sql_file(filepath: str) -> str:
        """Read SQL query from a file."""
        try:
            with open(filepath, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")

    def __repr__(self):
        return f"SnowflakeConn(scope={self.scope}, database={self.database}, warehouse={self.warehouse})"