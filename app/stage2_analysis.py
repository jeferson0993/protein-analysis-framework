from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd

def compute_features(records):
    data = []

    for r in records:
        analysis = ProteinAnalysis(str(r.seq))

        data.append({
            "id": r.id,
            "length": len(r.seq),
            "mw": analysis.molecular_weight(),
            "gravy": analysis.gravy(),
            "aromaticity": analysis.aromaticity()
        })

    return pd.DataFrame(data)
