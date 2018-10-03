# AmmorFati

Fast and convenient data mining tool for Chip-seq analyses.

'AmmorFati' optimizes peak call tools, like MACS2 or Cisgenome, and increases detection probability by hyper parameter optimization

>AmmorFati : 'Amm' is the Korean pronunciation of cancer. 'Fati' means 'fate' in Latin. 'AmmorFati' is a compound word that combines these words'


* * *

## INSTALL
> Dependency
- [MACS2](https://github.com/taoliu/MACS)
- [SICERpy](https://github.com/dariober/SICERpy)
- [Cisgenome](www.biostat.jhsph.edu/~hji/cisgenome/)
- [SWEMBL](https://github.com/stevenwilder/SWEMBL)
- [Bamtools](https://github.com/pezmaster31/bamtools)
- [Spearmint](https://github.com/HIPS/Spearmint)
- MongoDB

> Environment
- Ubuntu 18.04 LTS
- python2.7
  - scipy
  - numpy
  - pymongo

> Install
1. Install Ammorfati

2. export env path named 'AMMOR_HOME' where 'AmmorFati' program is located.
```sh
$ export AMMOR_HOME=</AmmorFati/root>
```

3. Make 'data' diretory and 'tools' diretory
- 'data' is dir where the chipseq file is located and 'tools' is dir where the 'peak detection tools' like MACS and 'bamtools' are located. If these files are in a different location, you must modify the path inside the script file.
```sh
#!bin/sh

CHIPPATH="${AMMOR_HOME}/chipData/" # data dir

export SPEARMINTPATH="${AMMOR_HOME}/spearmint/spearmint/"
SPEARMINTWORK="${AMMOR_HOME}/spearmint/workspace/"

BAMPATH="${AMMOR_HOME}/tools/bamtools/build/install/bin/"
export CISGENOMEPATH="${AMMOR_HOME}/tools/cisgenome/bin/"
export MACS2PATH="${AMMOR_HOME}/tools/macs/bin/"
export SICERPATH="${AMMOR_HOME}/tools/SICERpy/SICERpy/"
export SWEMBLPATH="${AMMOR_HOME}/tools/swembl/"
```
* * *

## LABELED DATA
```
```
* * *

## Getting start
```
```
* * *

## CITATION
1. Ziyu Wang, Masrour Zoghi, Frank Hutter, David Matheson, Nando de Freitas. “Bayesian Optimization in High Dimensions via Random Embeddings”. Proceedings of the Twenty-Third International Joint Conference on Artificial Intelligence, 2013, pp. 1778-1784.
2. Jasper Snoek, Hugo Larochelle, Ryan P.Adams. “Practical Bayesian Optimization of Machine Learning Algorithms”. Advances in Neural Information Processing System 25(NIPS 2012), 2012.
3. Toby Dylan Hocking, Patricia Goerner-Potvin, Andreanne Morin,Xiaojian Shao, Tomi Pastinen and Guillaume Bourque. “Optimizing ChIP-seq peak detectors using visual labels and supervised machine learning”, Advance Access Publication Date: 21 November 2016

* * *
