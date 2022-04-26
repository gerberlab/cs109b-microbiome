# cs109b-microbiome

This folder is organized as follows:
- `datasets`: This folder contains subfolders with each of the datasets. Each dataset has been copied over from the [MDITRE page](https://github.com/gerberlab/mditre/tree/master/mditre/tutorials/datasets). Corresponding jupyter notebooks named `<dataset-name>_dataset_overview.pynb` demonstrating the contents each dataset are included in each subfolder.
- `optional_DADA_2_tutorial`: This folder contains a jupyter notebook demonstrating how DADA2 is used to process raw 16S rRNA amplicon sequencing reads to create a read table of Amplicon Sequence Variants (ASVs) and using phyloseq to generate taxonomy.
- `references`: This folder contains the original papers for each of the studies, as well as the MITRE and MDITRE papers.

Links to the datasets are given below along with the original papers for each study. 

For more details on the datasets you can read the [MITRE](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/MITRE.pdf) and [MDITRE](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/MDITRE.pdf) papers. 

## Datasets

- Dataset 1: [Bokulich 2016](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/datasets/bokulich)
  - Study of the gut microbiomes of infants sampled over the first two years of life with classification tasks of (a) diet (breast fed vs formula) and (b) mode of birth (vaginal or c-section).
  - Data type: 16S amplicon
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Bokulich_2016.pdf)

- Dataset 2: [Brooks 2017](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/datasets/brooks)
  - A study of gut microbiomes of 30 infants sampled over 75 days. Classification task of mode of birth (vaginal versus C-section).
  - Data type: Shotgun metagenomics
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Brooks_2017.pdf)

- Dataset 3: [David 2014](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/datasets/david)
  - Study of microbiomes of 20 healthy adults receiving dietary interventions (plant based vs animal).
  - Data type: 16S amplicon
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/David_2014.pdf)

- Dataset 4: [DiGiulio 2015](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/datasets/digiulio)
  - A study of the vaginal microbiomes of 37 pregnant women (at term vs pre-term delivery).
  - Data type: 16S amplicon
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/DiGiulio_2015.pdf)

- Dataset 5: [Kostic 2015](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/datasets/kostic)
  - A study of the gut microbiomes of 17 infants sampled over the first 3 years of life. Classifying normal vs development of type 1 diabetes.
  - Data type: Shotgun metagenomics
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Kostic_2015.pdf)

- Dataset 6: [Vatanen 2016](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/datasets/vatanen)
  - A study of the gut microbiomes of 117 children sampled over the first three years of life. Classification task of nationality (Russian versus Estonian/Finnish).
  - Data type: 16S amplicon
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Vatanen_2016.pdf)

- Dataset 7: [Shao 2019](https://github.com/gerberlab/cs109b-microbiome/tree/main/2022/datasets/shao). [note to potentially remove or move to the bottom]
  - Note: this dataset has very little time-series data, may not want to use
  - A study of gut microbiomes of 282 infants (after filtering for subjects with fewer than three timepoints) sampled over 424 days. Classification task of mode of birth (vaginal versus C-section).
  - Data type: Shotgun metagenomics
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Shao_2019.pdf)


We also have a folder going into the detail of how amplicon sequencing data is analyzed and converted into ASV (ASVs) in the folder [add me]


### TODO: (slides) remove laterr
- focus on the domain...
- context what the should be looking for groups of bugs, what we are predicting, could integrate with features
- this is Bokulich 2016. infants and what the data means... and give a concrete example of what we would want to predict and what the hand engineered in this example might be.... there are ofcourse many others... one detailed example kostic... could reference mitre for ideaas of what features, average, slope, time window...
  - Data type: 16S amplicon
- note that the vaginal microbiome is a totally different environment... way less diversity
- one slide on shotgun [TG]
- slides on contextualizing interpretability [GU]
- hand making features (time windows, slopes, averages, collapsing bug, phylogeny(long sequences), taxonomy, raw (short sequence) [TG and GG and GU]
- 4->5 slides on datasets [GU]
- MDITRE example
- add code example showing multindexes for fast taxonomy collapsing [TG]
- working with neweck files both slides and jupyter notebooks
- at least one jupyter notebook for one set of data maybe ultimately one for each
