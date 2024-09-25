import csv

# Function to read SNP table (this table contains header)
def read_snp_table(file_path):
    snp_table = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            snp_table.append({
                "snp_id": row['#Marker'],      # SNP ID column in the SNP table
                "chr": row['chr'],             # Chromosome column
                "start": int(row['snp_start']),  # Start position
                "end": int(row['snp_end'])     # End position
            })
    return snp_table

# Function to read Gene table (this table does not contain header but the same column order as SNP table is respected)
def read_gene_table_no_header(file_path):
    gene_table = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            gene_table.append({
                "gene_id": row[0],  # First column in the gene table (gene ID)
                "chr": row[1],      # Second column (chromosome)
                "start": int(row[2]),  # Third column (start position)
                "end": int(row[3])   # Fourth column (end position)
            })
    return gene_table

# Function to handle multple gene matches of the same SNP
def find_genes_containing_snp(snp, gene_table):
    genes = []
    for gene in gene_table:
        if snp["chr"] == gene["chr"] and snp["start"] >= gene["start"] and snp["end"] <= gene["end"]:
            genes.append(gene)
    return genes

# Function to map SNPs to genes based on their positional overlap
def map_snps_to_genes(snp_table, gene_table):
    snp_gene_map = []
    for snp in snp_table:
        genes = find_genes_containing_snp(snp, gene_table)
        if genes:
            for gene in genes:
                snp_gene_map.append({
                    "SNP_ID": snp["snp_id"],
                    "Chr": snp["chr"],
                    "SNP_position": snp["start"],
                    "Gene_harboring_SNP": gene["gene_id"],
                    "Gene_start": gene["start"],
                    "Gene_end": gene["end"]
                })
        else:
            # Append with empty gene_id and gene positions if no gene matches
            snp_gene_map.append({
                "SNP_ID": snp["snp_id"],
                "Chr": snp["chr"],
                "SNP_position": snp["start"],
                "Gene_harboring_SNP": '',
                "Gene_start": '',
                "Gene_end": ''
            })
    return snp_gene_map

# Function to save the SNP to gene mapping to a tab-separated file
def save_mapping_to_file(snp_gene_map, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["SNP_ID", "Chr", "SNP_position", "Gene_harboring_SNP", "Gene_start", "Gene_end"], delimiter='\t')
        writer.writeheader()
        for mapping in snp_gene_map:
            writer.writerow(mapping)
    print(f"Results saved to {output_file}")

# Main execution
if __name__ == "__main__":
    # Paths to the input files (these files are adjusted according to the array and map)
    snp_file_path = '/home/najla/apps/barleymap/datasets/9k_peach_snp/9k_peach_snp.pp_Lovell_jgi2'
    gene_file_path = '/home/najla/apps/barleymap/datasets/pp_Lovell_jgi2_genes/pp_Lovell_jgi2_genes.pp_Lovell_jgi2'
    
    # Path to the output file
    output_file = '/home/najla/apps/barleymap/Download_dataset/snp_gene_mapping_9k_Lovell_jgi2.tsv'  # .tsv for tab-separated
    
    # Read the SNP and gene tables
    snp_table = read_snp_table(snp_file_path)
    gene_table = read_gene_table_no_header(gene_file_path)
    
    # Map the SNPs to genes
    snp_gene_map = map_snps_to_genes(snp_table, gene_table)
    
    # Save the mapping to a tab-separated file
    save_mapping_to_file(snp_gene_map, output_file)
