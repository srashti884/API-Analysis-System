import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root@localhost/api_analysis"
)

files = ["categories", "users", "products"]

for file in files:

    df = pd.read_csv(
        f"data/csv/{file}.csv"
    )

    df.to_sql(
        name=file,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"{file} loaded successfully")