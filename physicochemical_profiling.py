
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import csv

def physicochemical_profiling(sequence):
    """
    Calculate physicochemical properties of a protein sequence.
    
    Parameters:
        sequence (str): Protein sequence
    
    Returns:
        dict: Calculated properties
    """
    analysis = ProteinAnalysis(sequence)

    return {
        "Molecular Weight (Da)": round(analysis.molecular_weight(), 2),
        "Isoelectric Point (pI)": round(analysis.isoelectric_point(), 2),
        "GRAVY": round(analysis.gravy(), 3),
        "Instability Index": round(analysis.instability_index(), 2)
    }


def analyze_fasta(fasta_file, output_csv="physicochemical_results.csv"):
    """
    Analyze multiple protein sequences from a FASTA file.
    
    Parameters:
        fasta_file (str): Path to FASTA file
        output_csv (str): Output CSV filename
    """
    results = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq)
        props = physicochemical_profiling(seq)

        result_row = {
            "Sequence_ID": record.id,
            "Sequence_Length": len(seq),
            **props
        }
        results.append(result_row)

        # Print results to console
        print(f"\nResults for {record.id}")
        for k, v in props.items():
            print(f"{k}: {v}")

    # Write results to CSV
    with open(output_csv, mode="w", newline="") as csvfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nAll results saved to {output_csv}")


if __name__ == "__main__":
    fasta_input = "input_proteins.fasta"
    analyze_fasta(fasta_input)
