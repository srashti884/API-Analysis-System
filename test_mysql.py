from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root@localhost/api_analysis"
)

try:
    with engine.connect() as conn:
        print("Connected Successfully!")
except Exception as e:
    print("Error:", e)