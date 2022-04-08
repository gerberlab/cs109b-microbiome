# cs109b-microbiome





TODO: (readme) [GU]

- Introduce structure of this folder

For more details on the datasets you can read [MITRE]() and [MDITRE]() paper but here are the datasets


Each dataset is organized as follows -> so folder structure


- Dataset 1: [Bokulich 2016](https://github.com/gerberlab/mditre/tree/master/mditre/tutorials/datasets/raw/bokulich)
  - description amplicon vs shotgun
  - Study of the gut microbiomes of infants sampled over the first two years of life with classification tasks of (a) diet (breast fed vs formula) and (b) mode of birth (vaginal or c-section)
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Bokulich_2016.pdf)

- Dataset 2: [Brooks 2017]()
  - todo: unpickle and save as separate files
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Brooks_2017.pdf)

- Dataset 3: [David 2014](https://github.com/gerberlab/mditre/tree/master/mditre/tutorials/datasets/raw/david)
  - Study of microbiomes of 20 healthy adults receiving dietary interventions (plant based vs animal)
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/David_2014.pdf)

- Dataset 4: [DiGiulio 2015](https://github.com/gerberlab/mditre/tree/master/mditre/tutorials/datasets/raw/digiulio)
  - A study of the vaginal microbiomes of 37 pregnant women (at term vs pre-term delivery) 
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/DiGiulio_2015.pdf)

- Dataset 5: [Kostic 2015](https://github.com/gerberlab/mditre/tree/master/mditre/tutorials/datasets/raw/t1d)
  - A study of the gut microbiomes of 17 infants sampled over the first 3 years of life. Classifying normal vs development of type 1 diabetes.
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Kostic_2015.pdf)

- Dataset 6: [Shao 2019]()
  - todo: unpickle and save as separate files
  - A study of gut microbiomes of 282 infants (after filtering for subjects with fewer than three timepoints) sampled over 424 days (vaginal versus C-section)
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Shao_2019.pdf)

- Dataset 7: [Vatanen 2016]()
  - todo: figure out unpickle issue
  - A study of the gut microbiomes of 117 children sampled over the first three years of life. (Russian versus Estonian/Finnish nationality)
  - [paper](https://github.com/gerberlab/cs109b-microbiome/blob/main/2022/references/Vatanen_2016.pdf)

We alos have a folder going into the detail of how amplicon sequencing data is analyzed and converted into ASV (ASVs) in the folder [add me]



TODO: (slides) remove laterr
- one slide on shotgun [TG]
- slides on contextualizing interpretability [GU+GG]
- hand making features (time windows, slopes, averages, collapsing bug, phylogeny(long sequences), taxonomy, raw (short sequence) [TG and GG and GU]
- 4->5 slides on datasets [GU]
- MDITRE example
- add code example showing multindexes for fast taxonomy collapsing [TG]
- working with neweck files both slides and jupyter notebooks
- at least one jupyter notebook for one set of data maybe ultimately one for each
