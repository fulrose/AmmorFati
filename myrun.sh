#!bin/sh

CHIPPATH="${AMMOR_HOME}/chipData/"

SPEARMINTPATH="${AMMOR_HOME}/spearmint/spearmint/"
SPEARMINTWORK="${AMMOR_HOME}/spearmint/workspace/"

BAMPATH="${AMMOR_HOME}/tools/bamtools/build/install/bin/"
export CISGENOMEPATH="${AMMOR_HOME}/tools/cisgenome/bin/"
export MACS2PATH="${AMMOR_HOME}/tools/macs/bin/"
export SICERPATH="${AMMOR_HOME}/tools/SICERpy/SICERpy/"
export SWEMBLPATH="${AMMOR_HOME}/tools/swembl/"

echo "AMMOR HOME ::"
echo $AMMOR_HOME

echo ""

treat=`realpath $1`
if [ ! -f "$treat" ]; then
	echo "error about treat file"
	exit 1
fi

control=`realpath $2`
if [ ! -f "$control" ]; then
	echo "error about control file"
	exit 1
fi

train_labeled=`realpath $3`
if [ ! -f "$train_labeled" ]; then
	echo "error about train labeled file"
	exit 1
fi
train_file=`basename $train_labeled`

test_labeled=`realpath $4`
if [ ! -f "$test_labeled" ]; then
	echo "error about test labeled file"
	exit 1
fi
test_file=`basename $test_labeled`


echo ""
echo "Data Preprocessing Start !"

#python2 ${AMMOR_HOME}/data_preprocess.py ${treat} ${control} ${BAMPATH} ${CHIPPATH} ${train_file} ${test_file}

#echo "$dataPreprocess"

export treat_train_bam=${treat%%.bam}_filtered_train.bam
export control_train_bam=${control%%.bam}_filtered_train.bam

export treat_train_bed=${treat%%.bam}_filtered_train.bed
export control_train_bed=${control%%.bam}_filtered_train.bed

export treat_train_aln=${treat%%.bam}_filtered_train.aln
export control_train_aln=${control%%.bam}_filtered_train.aln

export treat_test_bam=${treat%%.bam}_filtered_test.bam
export control_test_bam=${control%%.bam}_filtered_test.bam

export treat_test_bed=${treat%%.bam}_filtered_test.bed
export control_test_bed=${control%%.bam}_filtered_test.bed

export treat_test_aln=${treat%%.bam}_filtered_test.aln
export control_test_aln=${control%%.bam}_filtered_test.aln


export trainLabeled=$train_labeled
export testLabeled=$test_labeled

export cisgenome_train_list=${CHIPPATH}cisgenome_train_list.txt
export cisgenome_test_list=${CHIPPATH}cisgenome_test_list.txt


echo "Data Preprocessing Done !"
echo ""
echo "----------------------------------------"
echo "----------------------------------------"
echo ""
echo "Pre Optimized Test Labeled Run..."
#python2 pre_optimized.py
python2 post_optimized.py
echo ""






echo "----------------------------------------"
echo "----------------------------------------"
echo ""
echo "Run Spearmint..."
echo ""
echo "----------------------------------------"
echo "#1 macs2 optimizing start !"
echo ""
python2 ${SPEARMINTPATH}/main.py ${SPEARMINTWORK}/macs2
echo ""
echo "#1 macs2 Done!" 
echo "----------------------------------------"
echo "#2 swembl optimizing start !"
echo ""
python2 ${SPEARMINTPATH}/main.py ${SPEARMINTWORK}/swembl
echo ""
echo "#2 swembl Done!" 
echo "----------------------------------------"
echo "#3 cisgenome optimizing start !"
echo ""
python2 ${SPEARMINTPATH}/main.py ${SPEARMINTWORK}/cisgenome
echo ""
echo "#3 cisgenome Done!" 
echo "----------------------------------------"
echo "#4 SICER optimizing start !"
echo ""
python2 ${SPEARMINTPATH}/main.py ${SPEARMINTWORK}/SICER
echo ""
echo "#4 SICER Done!"
echo "----------------------------------------"
echo "----------------------------------------"
echo ""
echo ""
echo "ALL Done !!"


echo ""
echo "----------------------------------------"
echo "----------------------------------------"


