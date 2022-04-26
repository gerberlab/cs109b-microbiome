Each dataset contains the following data files:
- `Abundance data`: Usually a file of the form `abundance.csv`. A CSV file containing the relative microbial abundances (read counts for 16S DADA2 output or relative abundance ratios for MetaPhlAn output) for each sample ID.
- `Sample metadata`: Usually file of the form `sample_metadata.csv`. A CSV file that specifies the time and subject ID for each sample ID.
- `Subject metadata`: Usually file of the form `subject_data.csv`. A CSV file that gives the host status/classification label for each subject ID. 
- `Phylogenetic tree`: Newick or jplace file

# MDITRE

All of the original processed and raw datasets for this course can be found on the MDITRE github repo [here](). Information for installing and using the MDITRE package  can be found on the main [MDITRE page](https://github.com/gerberlab/mditre). The accompanying paper for MDITRE can be found [here](https://www.biorxiv.org/content/10.1101/2021.12.15.472835v1). References for the original studies on each dataset are also provided in the `references` subdirectory.

# 16S and shotgun metagenomics datasets

We've also included a couple simple notebooks in this directory to give an overview of the contents of the David dataset (16s) and the Kostic dataset (shotgun metagenomics). The 16S dataset is processed with Dada2, an optional tutorial for which is given in this course module [here](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/optional_DADA_2_tutorial). Information and tutorials on MetaPhlan can be found on the Huttenhower lab webpage [here](https://huttenhower.sph.harvard.edu/metaphlan/).
