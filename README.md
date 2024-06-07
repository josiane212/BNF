# Source

Taken and edited from this repo :
https://github.com/Living-with-machines/DiachronicEmb-BigHistData?tab=readme-ov-file#overview-of-the-tools

# Linux Version

Ubuntu-22.04
I'm running it on VSCode using the WSL.

# Conda environment 
To install packages necessary to run most of these scripts, create a conda environment with this line :

```
conda env create -f environment.yml
```

# Training the Word2Vec model

## Configuration file
Edit the [`config file`](./config.yaml/) according to the [corresponding section of the source README](DiachronicEmb-BigHistData/README.md/#specify-some-variables).

> **_IMPORTANT:_** Make sure you put all your data in a `data` folder, and update the path in the config file.

## Train the model
Run this line from the current directory :

```
python DiachronicEmb-BigHistData/scripts/training/train_diach_emb.py
``` 

The resulting models and other files will be in the `outputs` folder

# Exploration
Some notebooks (`changepoint_detection`, `dynamic_time_warping` and `visualize_diachronic_emb`) we created to explore the models, mostly for diachronic analysis, in the [exploration](DiachronicEmb-BigHistData/scripts/exploration) folder. For more information on these, check the [correponding sections of the source README](DiachronicEmb-BigHistData/README.md/#explore-pre-trained-diachronic-word-embeddings).

To explore models in other ways or to explore the "complete" models that contains all the data, check out the notebook [BF_operations.ipynb](DiachronicEmb-BigHistData/scripts/exploration/BNF_operations.ipynb). It uses the file `Similarity_interface.py` to function.

The visualisations in the `BNF_operations.ipynb` notebook are still being worked on.