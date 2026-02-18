import argparse
from pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(
        description="Protein Analysis Framework"
    )

    parser.add_argument("--input", required=True,
                        help="Input FASTA file")
    parser.add_argument("--weights", nargs=3, type=float,
                        default=[0.4,0.3,0.3],
                        help="Weights for scoring metrics")
    parser.add_argument("--structure", action="store_true",
                        help="Enable structural prediction")
    parser.add_argument("--report", action="store_true",
                        help="Generate PDF report")

    args = parser.parse_args()

    run_pipeline(args)

if __name__ == "__main__":
    main()
