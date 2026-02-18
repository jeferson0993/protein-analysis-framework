import os
from stage1_processing import clean_sequences
from stage2_analysis import compute_features
from ranking import rank_candidates
from stage3_construct import build_construct
from structure import mock_structure_prediction
from report import generate_report

def run_pipeline(args):

    os.makedirs("results", exist_ok=True)

    records = clean_sequences(args.input)
    df = compute_features(records)

    ranked = rank_candidates(df, args.weights)

    top_ids = ranked.head(5)["id"].tolist()
    top_seqs = [str(r.seq) for r in records if r.id in top_ids]

    construct = build_construct(top_seqs)

    with open("results/final_construct.fasta","w") as f:
        f.write(">Construct\n")
        f.write(construct)

    if args.structure:
        structure_info = mock_structure_prediction(construct)
        print("Structure:", structure_info)

    if args.report:
        generate_report(ranked)

    print("Pipeline completed.")
