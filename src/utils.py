from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

def create_spark_session(app_name: str) -> SparkSession:
    """
    Create a Spark session with Delta Lake support.

    Args:
        app_name (str): The name of the Spark application.

    Returns:
        SparkSession: Configured Spark session.
    """
    try:
        builder = (
            SparkSession.builder
            .appName(app_name)
            .master("local[8]")
            .config("spark.driver.memory", "12g")
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        )
        spark = configure_spark_with_delta_pip(builder).getOrCreate()
    except Exception as e:
        print(f"Error creating Spark session: {e}")
        raise
    print(f"Spark session '{app_name}' created successfully.")
    return spark
