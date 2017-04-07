# CREST evaluation

## Objectives:
* Testing the software and comparing it to other tools that are commonly used or new on the market.*

------------

## Pipeline followed:
1. Test with clade partition cross validation.
	* We delete a whole taxon from the database and we test the deleted sequence against the troncated database. *
2. Test with ten fold cross validation.
	* We delete 10% of the sequence from the database and we test them against the new database. *
3. Calculation of the accuracy of the classifier.

## Steps:
1. Test the Unite (ITS) database
2. Test the new Silva (16S RNA) database
3. Test a known dataset from an article

## Software tested:
* [ ] LCA classifier (CREST)
* [ ] SINTAX
* [ ]  UTax
* [ ]  QIIME

-----------

## Evaluation Script:

** Scripts used: **
* Scripts/Python/evaluate.py
	* To calculate the score of each level *(for example: for one family deleted) *: the output is a table of four different scores * (True positive, True negative, False positive, False negative)* at each level. 
* Scripts/Bash/calculate_all_score.sh
	* To calculate the score of all the taxon deleted

* True positive = What is expected is what is obtained
* True negative = Nothing expected and nothing obtained
* False positive = What is obtained is different from what is expected
* False negative = We obtained nothing and something was expected



Works on every CREST output (for now).
Allows the calculation of the accuracy
python + bash script

---------
# Two different pipeline used for the following cross validation scripts:
* Use of the ART tool to simulate Illumina sequencing on the files outputed from a known database. (all the sequences have then a length of 250bp).
* The sequence are full length, no tool have been use to simulate errors

** BLAST is used for the alignment and the creation of database files to change the native database with the troncated ones **

## Clade partition cross validation script:
### For LCA classifier:
** Scripts used: **
	* Scripts/Python/cpx_lca.py
	* Scripts/Bash/pipeline_cpx_lca_250bp.sh
	* Scripts/Bash/pipeline_cpx_lca_FL.sh


### For Sintax:
** Scripts used: **
	* Scripts/Python/cpx_sintax.py


------------

## Ten fold cross validation script:
### For LCA classifier:
** Scripts used: **
	* Scripts/Python/random10.py
	* Scripts/Bash/random10_pipeline_lca_250bp.sh
	* Scripts/Bash/random10_pipeline_lca_FL.sh

### For Sintax:
** Scripts used: **
	* Scripts/Python/random10sintax.py

---------
To know the time made by my four 2.5GHz i5 processors (3.9GB RAM) is use the command `time` when I launch the scripts.


