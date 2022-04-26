# Datasets 
Data for each study is given in the corresponding folder. Jupyter notebooks in each foldered named `<dataset-name>_dataset_overview.pynb` open each relevant datafile and discuss the contents. 

Most datasets contain files for the following data:
- `Abundance data`: Usually a file of the form `abundance.csv`. A CSV file containing the relative microbial abundances (read counts for 16S DADA2 output or relative abundance ratios for MetaPhlAn output) for each sample ID and corresponding amplicon sequence.
- `Taxonomy data`: Usually a file of the form `dada2_placements.csv`. This file maps each amplicon sequence to a taxonomy.
- `Sample metadata`: Usually file of the form `sample_metadata.csv`. A CSV file that specifies the time and subject ID for each sample ID.
- `Subject metadata`: Usually file of the form `subject_data.csv`. A CSV file that gives the host status/classification label for each subject ID. 
- `Phylogenetic tree`: Newick or jplace file

A few exceptions to the above file structure are for the David, Brooks, and Shao datasets. For the David dataset, the amplicon sequence information is contained in a separate file. The accompanying jupyter notebook shows how to load this data and map it to the rest of the data.

The brooks and shao datasets are given in pickled files. Corresponding jupyter notebooks open and process these files to obtain the relevant data. [add me]

## MDITRE

All of the original processed and raw datasets for this course can also be found on the MDITRE github repo [here](https://github.com/gerberlab/mditre/tree/master/mditre/tutorials/datasets). Information for installing and using the MDITRE package can be found on the main [MDITRE page](https://github.com/gerberlab/mditre). The accompanying paper for MDITRE can be found [here](https://www.biorxiv.org/content/10.1101/2021.12.15.472835v1). References for the original studies on each dataset are also provided in the [references directory](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/references).

## 16S and shotgun metagenomics datasets

The 16S datasets are processed with Dada2, an optional tutorial for which is given in this course module [here](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/optional_DADA_2_tutorial). Information and tutorials on MetaPhlan can be found on the Huttenhower lab webpage [here](https://huttenhower.sph.harvard.edu/metaphlan/).
