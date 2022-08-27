import pandas as pd
import bearcats as bc

pd.set_option("display.float_format", lambda x: "%.2f" % x)


df = pd.DataFrame({
    "continent": ["NA", "NA", "NA", "EUR", "EUR", "ASIA", "ASIA", "ASIA"],
    "country": ["CAN", "MEX", "USA", "GBP", "FRA", "JAP", "CHN", "KOR"],
    "gdp": [60, 30, 390, 90, 85, 88, 360, 45]
})

list(df["continent"].values)


list(df["continent"].values)

list(map(lambda x: x * 2, df["continent"].values))
list(map(lambda x: x * 2, df["continent"]))



df.info()

df.shape

df.describe()


df = bc.DataFrame({
    "continent": ["NA", "NA", "NA", "EUR", "EUR", "ASIA", "ASIA", "ASIA"],
    "country": ["CAN", "MEX", "USA", "GBP", "FRA", "JAP", "CHN", "KOR"],
    "gdp": [60, 30, 390, 90, 85, 88, 360, 45]
})

df["gdp"] * 5

list(df.columns)

df.dict()
df.pandas()

df.reduce({
    "new_column_name": lambda x: x["column"].mean(),
    "new_column_name2": ("column", lambda c: c.mean()),
})

df.reduce(["continent"], {"gdp": [sum, lambda x: x.min()]})


(
    bc.DataFrame({"a": range(100)})
    .take(10, at="head")
    .reindex()
)


df = bc.DataFrame({
    "a": [1, 1, None, 1, 2, None],
    "b": [0, 0, None, None, None, None]
})

df.mutate({
    "a": lambda d: str(d["a"]).replace("nan", "0")
}).strip(["b"])

dfa = bc.DataFrame({
    "team": ["leafs", "rangers", "kings", "blackhawks"],
    "salary": [98, 87, 88, 84]
})

dfb = bc.DataFrame({
    "team": ["leafs", "rangers", "blackhawks", "senators"],
    "percent": [0.7, 0.6, 0.65, 0.30],
})

dfc = (dfa
    .join(dfb, columns=["team"])
    .strip(columns=["percent"])
    .reindex()
    .pander()
)

type(bfa)

bfc


df = pd.DataFrame(
    {
        "a": [1, 2, 3, 4, 5],
        "b": ["v", "w", "x", "y", "z"],
        "c": ["dog", "cat", "giraffe", "eel", "snake"],
        "d": [1, 3.99, None, 1_000_300.19, 0.2222],
    }
)

y = df["a"]
X = df[["b", "c", "d"]]
df.values.tolist()

pd.to_numeric()

pd.to_datetime("2018-01-01")

pd.to_numeric(df["d"])

help(df.astype)

bf = (
    bc.load("example.csv")
    .select(["a", "d"])
    .mutate({"e": lambda d: d["d"] * 5, "f": lambda d: d["e"] / 5})
    .filter(lambda d: d["a"] >= 3)
    .take(5, at="head")
    .sort(["d"], reverse=True)
    .rename({"f": "h"})
    # .sort("d")
    # .select("f")
)

df = (
    bc.load("example.csv")
    .select(["a", "d"])
    .mutate({
        "e": lambda d: d["d"] * 5,
        "f": lambda d: d["e"] / 5
    })
    .filter(lambda d: d["a"] >= 3)
    .sort(["d"], reverse=True)
    .rename({"f": "h"})
    .head(5)
)
