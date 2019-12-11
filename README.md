<img src="https://www.giotto.ai/static/vector/logo.svg" alt="logo" width="850"/>

# shape-of-molecules
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


## Data
The HIV dataset was introduced by the Drug
Therapeutics Program (DTP) AIDS Antiviral Screen, which
tested the ability to inhibit HIV replication for over 40 000
compounds. In the original dataset the chemical compounds were classified
into 3 different classes: confirmed inactive (CI), confirmed active (CA)
and confirmed moderately active (CM). As done in this [paper](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc02664a), 
the two classes CA and CM were grouped into one single class "Active".

## Feature Creation
The assumption we made is that each match can be modelled as the attributes of the 
starting eleven of the two teams. Since in this way the number of features was too 
high, an additional aggregation step was required (see the notebook for further 
details). 

Thus, each match can be considered as a vector in a vector space and the totality of 
matches can be viewed as a point cloud.

For capturing local information surrounding a match, we computed persistent homology 
of its k-nearest neighbours and use it as a feature. 

## Model
We cross-validated a random forest classifier and train it to predict the outcome of 
a match. In order to validate our results, we used an elo-rating system and the odds 
of the market as baselines. 

## Results
Our results show that our model out-performs the elo-rating system and is 
comparable to the market.  

## Notebook overview
Given the promising results, we tried to simulate an entire championship with the 
ultimate purpose of evaluating the impact that a player would have had if hired by 
our favorite team. Therefore, we offer the possibility to select both the favorite 
player and the lucky team where to insert him. Then you can simulate the championship
and check if your player improves the final ranking of his new team (little spoiler: 
Messi does!). 

Enjoy!

## Requirements
In order to run the notebook, the following python packages are required: 

- scikit-learn (>= 0.21.3)
- numpy (>= 1.14.0)
- networkx (>= 2.4)
- giotto-learn (>= 0.1.3)
- rdkit (>= 2018.03.4.0)
- deepchem (>= 2.2.1.dev54)
- keras (>= 2.3.1)
- pandas (>=0.25.2)

To install rdkit and deepchem with conda:


    conda install -c deepchem -c rdkit


