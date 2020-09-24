![logo](https://raw.githubusercontent.com/giotto-ai/giotto-tda/master/doc/images/tda_logo.svg)

# The-shape-of-chemical-functions
The application of Machine Learning for biological data is one of the 
most promising and fascinating research direction of AI. In this notebook
we want to give a baseline indication to show how topological data analysis 
tools can be exploited to analyze molecules. More importantly, we show empirically
that shapes matter, in the sense that it is possible to match properties of objects with
their shapes.

The task of this use case is to classify molecules with respect to their 
inhibition property for the HIV virus. In order to achieve it, we propose a method 
to embed molecules into points of an Euclidean Space and so to represent chemical 
compounds with vectors. The method, which is based on TDA concepts, represents the 
most important part of the pipeline by learning meaningful features of molecules. Once 
the vector representation are obtained, they are used as input for a calssificator function
which is parametrized by a simple 2-hidden-layers nerual network. 

Have a lok at out [blog post](https://towardsdatascience.com/the-shape-of-chemical-functions-d1e1568d020)
to learn more.

## Data
The HIV dataset was introduced by the Drug
Therapeutics Program (DTP) AIDS Antiviral Screen, which
tested the ability to inhibit HIV replication for over 40 000
compounds. In the original dataset the chemical compounds were classified
into 3 different classes: confirmed inactive (CI), confirmed active (CA)
and confirmed moderately active (CM). As done in this [paper](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc02664a), 
the two classes CA and CM were grouped into one single class "Active".

## Feature Creation
The innovative part of using TDA in this classification problem consists in finding meaningful structural features for molecules. The idea is to embed molecules into an Euclidean Space where the Euclidean distance reflects the notion of structural dissimilarity.

In 


## Model
We cross-validated a fully connected neural network with 2 hidden layers: the hidden neurons present a ReLu activation function whereas the single output neuron has a sigmoid activation which represent the probability for an input molecule to be a HIV-inhibitor.

## Results
Our results show that the structural features found contain good quality informations on the inhibition property for the HIV viruses providing AUC-ROC scores comparable with the state-of-the-art solutions reported [here](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc02664a).
 
## Notebook overview
In this notebook we want to show how structural features can be inferred by using topological tools. In particolar, we provide atoms and bonds embedding for each molecules and, following the pipeline, we show that the classification procedure goes to very good results. Moreover, we let the user play with the hyperparameters and classificator model to see if other interesting results appear.


## Requirements
In order to run the notebook, the following python packages are required: 

- scikit-learn 0.21.3
- numpy 1.14.0
- networkx 2.4
- giotto-learn-nightly
- rdkit 2018.03.4.0
- deepchem 2.2.1.dev54
- keras 2.3.1
- pandas 0.25.2

To install rdkit and deepchem with conda:


    conda install -c deepchem -c rdkit


