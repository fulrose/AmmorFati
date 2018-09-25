#!bin/sh

CHIPPATH="${AMMOR_HOME}/chipData/"
BAMPATH="${AMMOR_HOME}/tools/bamtools/build/install/bin/"
CISGENOMEPATH="${AMMOR_HOME}/tools/cisgenome/bin/"

echo "AMMOR HOME ::"
echo $AMMOR_HOME

echo ""

treat=`realpath $1`
ls $treat

if [ $? -ne 0 ]; then
	echo "error about treat file"
	exit 1
fi

control=`realpath $2`
ls $control
if [ $? -ne 0 ]; then
	echo "error about control file"
	exit 1
fi

echo ""
echo "Data Preprocessing Start !"

dataPreprocess=`python2 ${AMMOR_HOME}/data_preprocess.py ${treat} ${control} ${BAMPATH} ${CISGENOMEPATH}`
echo "$dataPreprocess"

treat_bam=${treat%%.bam}_filtered.bam
control_bam=${control%%.bam}_filtered.bam

treat_bed=${treat%%.bam}_filtered.bed
control_bed=${control%%.bam}_filtered.bed

treat_aln=${treat%%.bam}_filtered.aln
control_aln=${control%%.bam}_filtered.aln

#echo $treat_bam
#echo $control_bam
#echo $treat_bed
#echo $control_bed
#echo $treat_aln
#echo $control_aln

echo "Data Preprocessing Done !"

echo ""
echo "----------------------------------------"
echo ""



