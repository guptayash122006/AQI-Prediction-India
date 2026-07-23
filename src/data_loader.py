import pandas as pd


def load_data(file_path):
    """
    Load dataset from the given file path.

    Parameters:
        file_path (str or Path): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    try:
        df = pd.read_csv(file_path)
        print("✅ Dataset loaded successfully.")
        return df

    except FileNotFoundError:
        print("❌ Dataset file not found.")

    except Exception as e:
        print(f"❌ Error: {e}")