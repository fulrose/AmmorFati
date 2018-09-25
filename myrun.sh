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

labeled=`realpath $3`
ls $labeled
if [ $? -ne 0 ]; then
	echo "error about labeled file"
	exit 1
fi

echo ""
echo "Data Preprocessing Start !"

#python2 ${AMMOR_HOME}/data_preprocess.py ${treat} ${control} ${BAMPATH} ${CISGENOMEPATH} ${CHIPPATH}

#echo "$dataPreprocess"

export treat_bam=${treat%%.bam}_filtered.bam
export control_bam=${control%%.bam}_filtered.bam

export treat_bed=${treat%%.bam}_filtered.bed
export control_bed=${control%%.bam}_filtered.bed

export treat_aln=${treat%%.bam}_filtered.aln
export control_aln=${control%%.bam}_filtered.aln

export myLabeled=$labeled
export cisgenome_list=${CHIPPATH}cisgenome_list.txt


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


