# Source

Taken and edited from this repo :
https://github.com/Living-with-machines/DiachronicEmb-BigHistData?tab=readme-ov-file#overview-of-the-tools

# Linux Version

Ubuntu-22.04 on a WSL

# Conda environment 
To install packages necessary to run most of these scripts, create a conda environment with this line :

```
conda env create -f environment.yml
```

# Training the Word2Vec model

## Configuration file
Edit the [`config file`](./config.yaml/) according to the [corresponding section of the source README](diachronicEmb/README.md/#specify-some-variables).

> **_IMPORTANT:_** Make sure you put all your data in a `data` folder, and update the path in the config file.

## Train the model
Run this line from the current directory :

```
python diachronicEmb/scripts/training/train_diach_emb.py
``` 

The resulting models and other files will be in the `outputs` folder

# Exploration
Some notebooks (`changepoint_detection`, `dynamic_time_warping` and `visualize_diachronic_emb`) we created to explore the models, mostly for diachronic analysis, in the [exploration](diachronicEmb/scripts/exploration) folder. For more information on these, check the [correponding sections of the source README](diachronicEmb/README.md/#explore-pre-trained-diachronic-word-embeddings).

To explore models in other ways or to explore the "complete" models that contains all the data, check out the notebook [BNF_operations.ipynb](diachronicEmb/scripts/exploration/BNF_operations.ipynb). It uses the file `Similarity_interface.py` to function.

The visualisations in the `BNF_operations.ipynb` notebook are still being worked on.

To get general information on a corpus (number of tokens, vocabulary, etc.), use the notebook [general_info.ipynb](diachronicEmb/scripts/exploration/corpus/general_info.ipynb)