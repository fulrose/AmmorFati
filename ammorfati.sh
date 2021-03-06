#!bin/sh

CHIPPATH="${AMMOR_HOME}/chipData/"

export SPEARMINTPATH="${AMMOR_HOME}/spearmint/spearmint/"
SPEARMINTWORK="${AMMOR_HOME}/spearmint/workspace/"

BAMPATH="${AMMOR_HOME}/tools/bamtools/build/install/bin/"
export CISGENOMEPATH="${AMMOR_HOME}/tools/cisgenome/bin/"
export MACS2PATH="${AMMOR_HOME}/tools/macs/bin/"
export SICERPATH="${AMMOR_HOME}/tools/SICERpy/SICERpy/"
export SWEMBLPATH="${AMMOR_HOME}/tools/swembl/"

echo "----------------------------------------"
echo ""
echo "##### AMMORFATI #####"
echo ""
echo "----------------------------------------"

echo "AMMOR HOME ::"
echo $AMMOR_HOME

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

cur_time=`date`
`echo "AmmorFati start time ${cur_time}" > ammor_time.log`

start_sec=`date "+%s"`

echo "----------------------------------------"
echo ""
echo "1. Data Preprocessing Start !"

#python2 ${AMMOR_HOME}/data_preprocess.py ${treat} ${control} ${BAMPATH} ${CHIPPATH} ${train_file} ${test_file}

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

bam_end=`date "+%s"`
t_res=`echo "$bam_end - $start_sec" | bc`
echo "Data Preprocess Done : $t_res" >> ammor_time.log

echo ""
echo "----------------------------------------"
echo "----------------------------------------"
echo ""
echo "2. Pre Test Labeled Run... (about default parameter)"
#python2 pre_optimized.py
echo ""
echo "Pre Test labeled Done (temp/<tool>/test*)"

pre_test=`date "+%s"`
t_res=`echo "$pre_test - $start_sec" | bc`
echo "Pre Test labeled Done : $t_res" >> ammor_time.log

echo ""
echo "----------------------------------------"
echo "----------------------------------------"
echo ""
echo "3.Run Spearmint..."
echo ""
echo "----------------------------------------"
echo "#1 macs2 optimizing start !"
echo ""
#python2 ${SPEARMINTPATH}/main.py ${SPEARMINTWORK}/macs2
echo ""
echo "#1 macs2 Done!"

macs_end=`date "+%s"`
t_res=`echo "$macs_end - $start_sec" | bc`
echo "Macs Done : $t_res" >> ammor_time.log

echo "----------------------------------------"
echo "#2 swembl optimizing start !"
echo ""
#python2 ${SPEARMINTPATH}/main.py ${SPEARMINTWORK}/swembl
echo ""
echo "#2 swembl Done!"

swembl_end=`date "+%s"`
t_res=`echo "$swembl_end - $start_sec" | bc`
echo "Swembl Done : $t_res" >> ammor_time.log

echo "----------------------------------------"
echo "#3 cisgenome optimizing start !"
echo ""
#python2 ${SPEARMINTPATH}/main.py ${SPEARMINTWORK}/cisgenome
echo ""
echo "#3 cisgenome Done!"

cisgenome_end=`date "+%s"`
t_res=`echo "$cisgenome_end - $start_sec" | bc`
echo "Cisgenome Done : $t_res" >> ammor_time.log

echo "----------------------------------------"
echo "#4 SICER optimizing start !"
echo ""
#python2 ${SPEARMINTPATH}/main.py ${SPEARMINTWORK}/SICER
echo ""
echo "#4 SICER Done!"

SICER_end=`date "+%s"`
t_res=`echo "$SICER_end - $start_sec" | bc`
echo "SICER Done : $t_res" >> ammor_time.log

echo "----------------------------------------"
echo "----------------------------------------"

echo ""
echo "Wait for finishing the spearmint... (20s)"
#sleep 20
echo ""

echo "----------------------------------------"
echo "----------------------------------------"
echo ""
echo "Post Optimized Test Labeled Run... (by spearmint's optimized param)"
#python2 post_optimized.py
echo ""
echo "Post Test labeled Done (temp/<tool>/optimized*)"

post_test=`date "+%s"`
t_res=`echo "$post_test - $start_sec" | bc`
echo "Post optimized Done : $t_res" >> ammor_time.log

echo ""
echo "----------------------------------------"
echo ""
echo "ALL Done !!"
echo ""
echo "----------------------------------------"
echo "----------------------------------------"
