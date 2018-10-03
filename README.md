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

4. Install MongoDB & start services
```sh
$ mongo
MongoDB shell version v4.0.2
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 4.0.2
Server has startup warnings:
2018-10-03T12:29:15.474+0900 I STORAGE  [initandlisten]
2018-10-03T12:29:15.474+0900 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2018-10-03T12:29:15.474+0900 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2018-10-03T12:29:16.335+0900 I CONTROL  [initandlisten]
2018-10-03T12:29:16.335+0900 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-10-03T12:29:16.335+0900 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-10-03T12:29:16.335+0900 I CONTROL  [initandlisten]
---
```

* * *

## LABELED DATA
```
```
* * *

## Configuration
If you want to set options about 'spearmint' or other detection tool, check the config files in the 'config' directory.
you can change the parameter range for each tool, the maximum number of jobs, and the number of threads.
```json
{
    "language"        : "PYTHON",
    "experiment-name" : "macs2_test",
    "polling-time"    : 1,
    "resources" : {
        "my-machine" : {
            "scheduler"         : "local",
            "max-concurrent"    : 4,
            "max-finished-jobs" : 10
        }
    },
    
```
```json

    "variables" : {
        "q" : {
            "type" : "FLOAT",
            "size" : 1,
            "min"  : 0.001,
            "max"  : 0.8
        },
        "m_s" : {
            "type" : "INT",
            "size" : 1,
            "min" : 1,
            "max" : 50
        },
        "m_d" : {
            "type" : "INT",
            "size" : 1,
            "min" : 20,
            "max" : 200
      }
   }
}
```
* * *

## Getting started
1. Run the AmmorFati.
```sh
$ sh ammorfati.sh </Treat(input) file of chipseq data/> </Control file of chipseq data/> </train label file/> </test label file/>
```
You need 4 files (Treat file, Control file, label file for train, label file for test)
* * *

## CITATION
1. Ziyu Wang, Masrour Zoghi, Frank Hutter, David Matheson, Nando de Freitas. “Bayesian Optimization in High Dimensions via Random Embeddings”. Proceedings of the Twenty-Third International Joint Conference on Artificial Intelligence, 2013, pp. 1778-1784.
2. Jasper Snoek, Hugo Larochelle, Ryan P.Adams. “Practical Bayesian Optimization of Machine Learning Algorithms”. Advances in Neural Information Processing System 25(NIPS 2012), 2012.
3. Toby Dylan Hocking, Patricia Goerner-Potvin, Andreanne Morin,Xiaojian Shao, Tomi Pastinen and Guillaume Bourque. “Optimizing ChIP-seq peak detectors using visual labels and supervised machine learning”, Advance Access Publication Date: 21 November 2016

* * *
