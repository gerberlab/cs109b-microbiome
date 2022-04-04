---
title: Installing DADA2
...

Before exploring the DADA2 tutorial in the notebook

```
DADA2_short_tutorial.ipynb
```

we need to make a `conda` environment with `DADA2` installed and install an `R` kernel pointing `jupyter` to the `conda` environment. These are the installation steps I took to get a local `conda`{.bash} environment. Similar steps will work in linux.

First we need to install the appropriate packages into a new `conda` environment that we will call __rmicrobiome__.

```bash
conda create -n rmicrobiome \
  -c conda-forge \
  -c bioconda \
  -c defaults \
  -c r \
  --override-channels \
  bioconductor-dada2=1.18.0 \
  bioconductor-phyloseq \
  r-r.utils \
  r-irkernel \
  jupyterlab
```
Now activate the new `conda`{.bash} environment
```bash
conda activate rmicrobiome
```

Now we are linking this environment to `Jupyter`.

```bash
R -e 'IRkernel::installspec(name = "rmicrobiome",
      displayname = "rmicrobiome")'
```
>[InstallKernelSpec] Installed kernelspec rmicrobiome in /Users/teg14/Library/Jupyter/kernels/rmicrobiome


Open `R`
```bash
R
```
Check package versions to ensure things were installed properly

```R
packageVersion("dada2")
```
>[1] ‘1.18.0’

```R
packageVersion("phyloseq")
```
>[1] ‘1.34.0’

```R
quit()
```

You are now back in the terminal. Double check to make sure you have the __rmicrobiome__ kernel. Launch jupyter (if on your mac you can do this from the terminal with command `jupyter notebook`)

![](figures/r_kernel.png){width=200}

Now open

```
DADA2_short_tutorial.ipynb
```

and be sure to set it to the appropriate kernel

<!--
pandoc -f markdown -o install_dada2.html install_dada2.md --template=GitHub.html5  --self-contained -t html5
pandoc -f markdown -o install_dada2.pdf install_dada2.md --template=GitHub.html5  --self-contained -t html5
-->
