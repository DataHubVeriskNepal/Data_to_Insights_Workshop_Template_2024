# Ingestion

## Overview
This section provides a Python-based solution to load data from CSV files into Snowflake tables. It includes functionality to:
- Connect to Snowflake.
- Load data from CSV files into the corresponding Snowflake tables.
- Move processed files to an archive directory.

## Project Structure
- `Snowflake.py`: Contains the `Snowflake` class which handles the connection to Snowflake and data loading operations.
- `main.py`: The main script to execute the data loading process.
- `data/`: Directory containing subdirectories with CSV files. Each subdirectory corresponds to a Snowflake table.
- `archive/`: Directory where processed CSV files are moved after loading.
- `run.bat`: Batch file to run the `main.py` script.
- 
## Requirements
- Snowflake trial account
- Python 3.x
- `snowflake-connector-python`
- `pandas`

## Installation & Setup
1. Clone the repository.
2. Install the required Python packages:
    ```sh
    pip install snowflake-connector-python pandas
    ```
   OR
    ```sh
    pip install -r requirements.txt
    ```
3. Open Snowflake and create a database and schema using SQL commands under SQL dir

## Usage
### Running the Script through python
1. Set the following environment variables with your Snowflake credentials:
    - `SNOWFLAKE_USER`
    - `SNOWFLAKE_PASSWORD`
    - `SNOWFLAKE_ACCOUNT`
    - `SNOWFLAKE_WAREHOUSE`
    - `SNOWFLAKE_DATABASE`
    - `SNOWFLAKE_SCHEMA`
    - `LOOKUP_FILE` (path to the lookup CSV file)

2. Run the `main.py` script:
    ```sh
    python main.py <data_dir> <batch_size>
    ```
    - `<data_dir>`: Path to the directory containing subdirectories with CSV files.
    - `<batch_size>`: Number of rows to load in each batch.

### Running through the Batch File
1. Run the batch script using following command:
    ```sh
    ./run.bat <data_dir> <batch_size> <load_lookup_flag> 
    ```

## Example
To load data from the `data` directory with a batch size of 1000:
```sh
./run.bat data 1000 no
```

To load the lookup table
```sh
./run.bat data 1000 y
```