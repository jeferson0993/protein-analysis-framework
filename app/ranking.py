import numpy as np

def rank_candidates(df, weights):

    norm = (df - df.min()) / (df.max() - df.min())
    score = (
        norm["mw"] * weights[0] +
        (-norm["gravy"]) * weights[1] +
        norm["aromaticity"] * weights[2]
    )

    df["score"] = score
    return df.sort_values("score", ascending=False)
