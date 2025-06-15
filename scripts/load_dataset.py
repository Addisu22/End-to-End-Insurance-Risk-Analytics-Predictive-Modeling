import pandas as pd

def load_data(filepath, sep='|', chunksize=100_000):
    """
    Load a large delimited data in chunks, process each chunk, and return a combined DataFrame.

    Parameters:
        filepath (str): Path to the file.
        sep (str): Field separator used in the file.
        chunksize (int): Number of rows to read per chunk.

    Returns:
        pd.DataFrame: Combined DataFrame after processing chunks.
    """
    chunks = []
    try:
        for i, chunk in enumerate(pd.read_csv(filepath, sep=sep, chunksize=chunksize, engine='python', low_memory=True)):
            # print(f"🔄 Processing chunk {i + 1}...")

            # Convert date column (if exists)
            if 'TransactionMonth' in chunk.columns:
                chunk['TransactionMonth'] = pd.to_datetime(chunk['TransactionMonth'], errors='coerce')

            # Optional: filter only rows with claims > 0
            # if 'TotalClaims' in chunk.columns:
            #     chunk = chunk[chunk['TotalClaims'].fillna(0).astype(float) > 0]

            chunks.append(chunk)

        df = pd.concat(chunks, ignore_index=True)
        print(f"✅ Loaded total {len(df)} rows.")
        return df

    except FileNotFoundError:
        print("File not found. Please check the path.")
    except pd.errors.ParserError as e:
        print(f"Parsing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")