# from sqlalchemy import create_engine

# engine = create_engine("postgresql+psycopg2://postgres:1234@127.0.0.1:5432/general")

# with open("yandex_lr2", "r", encoding="utf-8") as f:
#     sql = f.read()

# with engine.connect() as conn:
#     conn.execute(sql)
#     print("✅ Дамп выполнен")


import chardet

with open("yandex_lr2", "rb") as f:
    result = chardet.detect(f.read())

print("Определённая кодировка:", result["encoding"])
