'''
Utility functions for loading and cleaning insurance data.
'''


import numpy as np
import pandas as pd


def clean_insurance_data(df: pd.DataFrame,
                         date_columns: list = None,
                         categorical_cols: list = None,
                         string_columns: list = None) -> pd.DataFrame:
    """
    Clean the insurance data DataFrame.

    Parameters:
    df (pd.DataFrame): The raw insurance data DataFrame.

    Returns:
    pd.DataFrame: A cleaned DataFrame with no missing values and correct data types.
    """
    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values (if any)
    df = df.dropna()

    # convert numerical columns to appropriate dtypes
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # convert boolean columns to bool dtype
    for col in df.select_dtypes(include=['bool']).columns:
        df[col] = df[col].astype('bool')

    # Convert date columns to datetime dtype
    for col in date_columns or []:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # Convert categorical columns to category dtype
    for col in categorical_cols or []:
        df[col] = df[col].astype('category')

    # Strip whitespace from string columns
    for col in string_columns or []:
        df[col] = df[col].astype('string')
        df[col] = df[col].str.strip()

    return df

def data_overview(df: pd.DataFrame) -> None:
    """
    Print an overview of the DataFrame including shape, data types, and missing values.

    Parameters:
    df (pd.DataFrame): The DataFrame to overview.
    """
    print("DataFrame Shape:", df.shape)
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\n📋 Dataset Info:\n", df.info())
    print("\nStatistical Summary:\n", df.describe(include='all'))
    print("\nDataFrame Head:\n", df.head())


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load insurance data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the insurance data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded insurance data.
    """
    try:
        df = pd.read_csv(file_path)
        df = clean_insurance_data(df)
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except pd.errors.ParserError:
        print("Error: There was a parsing error while reading the file.")
        raise