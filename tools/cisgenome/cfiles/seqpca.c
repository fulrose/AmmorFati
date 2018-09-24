#include "stdlib.h"
#include "stdio.h"
#include "string.h"
#include "math.h"
#include "limits.h"
#include "time.h"

#include "StringLib.h"
#include "MatrixLib.h"
#include "RandomLib.h"
#include "MathLib.h"
#include "MotifLib.h"
#include "SequenceLib.h"
#include "GenomeLib.h"
#include "MicroarrayLib.h"
#include "AffyLib.h"
#include "HTSequencingLib.h"

int menu_seqpca(int argv, char **argc);

int main(int argv, char **argc)
{
	int nLen;
	int nseed;

	/* init rand */
	srand( (unsigned)time( NULL ) );
	if(strcmp(OS_SYSTEM, "WINDOWS") == 0)
	{
		nseed = (int)(rand()*1000/RAND_MAX);
	}
	else
	{
		nseed = rand()%1000;
	}
	rand_u_init(nseed);


	/* ---- */
	/* menu */
	/* ---- */
	menu_seqpca(argv, argc);

	/* exit */
	exit(EXIT_SUCCESS);
}

int menu_seqpca(int argv, char **argc)
{
	char strSamplePath[LINE_LENGTH];
	char strInputPath[LINE_LENGTH];
	char strOutputPath[LINE_LENGTH];
	char strOutputFile[LINE_LENGTH];
	int nBinSize = 50;
	int nExtLen = 150;
	int nMaxPCAuto = 1;
	int nMaxPC = 3;
	double dVcut = 0.9;
	int nExportBAR = 0;
	int nKeepTempFiles = 0;
	int nApplyLog = 1;
	int nZeroShift = 1;
	int nTargetReadNum = -1;
	
	int sOK;
	int iOK;
	int oOK;
	int dOK;

	int ni;
	int nResult;

	/* ------------------------------- */
	/*     menu_seqpca                 */
	/* ------------------------------- */
	if(argv < 1)
	{
		printf("Error: parameter wrong!\n");
		exit(EXIT_FAILURE);
	}
	else if(argv == 1)
	{
		printf("/* ----------------------------- */\n");
		printf("    seqpca                \n");
		printf(" -s sample file (contains paths to *.aln files) \n");
		printf(" -i input genomic coordinates (*.cod) \n");
		printf(" -d output folder  \n");
		printf(" -o output file  \n");
		printf(" -b bin size, the resolution of peak detection (default = 50 bp) \n");
		printf(" -e read extension length  (default = 150 bp) \n");
		printf(" -log 1 (default): apply log2 transform; 0: do not apply log transform \n");
		printf(" -z 1 (default): shift mean of each bin across all samples to zero; 0: do not apply zero shift. If both -log 1 and -z 1 are used, zero-shift will be applied after the log2 transform. \n");
		printf(" -maxr maximal number of isoforms (i.e. number of principal components to be kept). If not set, the default maxr = (sample_number - 1) \n");
		printf(" -vcut variance cutoff (i.e. percentage of variance that should be explained by retained isoforms. For example, if -vcut 0.9, and if k isoforms can explain >90% variance, then only min(k,maxr) isoforms are reported. Default = 0.9 \n");
		printf(" -t target read number per sample for normalization (e.g. 1000000). If not specified, the program will use the read number of the smallest sample. \n");
		printf(" -keeptemp 1: keep intermediate files (may take big disk space); 0 (default): remove intermediate files. \n");
		printf(" Example: \n");
		printf("    seqpca -s samplelist.txt -i input.cod -d . -o test -b 100 -e 150 \n");
		printf("/* ----------------------------- */\n");
		exit(EXIT_SUCCESS);
	}

	sOK = 0;
	iOK = 0;
	oOK = 0;
	dOK = 0;
	
	ni = 1;
	while(ni < argv)
	{
		if(strcmp(argc[ni], "-s") == 0)
		{
			ni++;
			strcpy(strSamplePath, argc[ni]);
			sOK = 1;
		}
		else if(strcmp(argc[ni], "-i") == 0)
		{
			ni++;
			strcpy(strInputPath, argc[ni]);
			iOK = 1;
		}
		else if(strcmp(argc[ni], "-d") == 0)
		{
			ni++;
			strcpy(strOutputPath, argc[ni]);
			dOK = 1;
		}
		else if(strcmp(argc[ni], "-o") == 0)
		{
			ni++;
			strcpy(strOutputFile, argc[ni]);
			oOK = 1;
		}
		else if(strcmp(argc[ni], "-b") == 0)
		{
			ni++;
			nBinSize = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-e") == 0)
		{
			ni++;
			nExtLen = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-log") == 0)
		{
			ni++;
			nApplyLog = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-z") == 0)
		{
			ni++;
			nZeroShift = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-maxr") == 0)
		{
			ni++;
			nMaxPCAuto = 0;
			nMaxPC = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-vcut") == 0)
		{
			ni++;
			dVcut = atof(argc[ni]);
		}
		else if(strcmp(argc[ni], "-t") == 0)
		{
			ni++;
			nTargetReadNum = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-bar") == 0)
		{
			ni++;
			nExportBAR = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-keeptemp") == 0)
		{
			ni++;
			nKeepTempFiles = atoi(argc[ni]);
		}
		else 
		{
			printf("Error: unknown parameters!\n");
			exit(EXIT_FAILURE);
		}

		ni++;
	}

	if(nBinSize < 0)
		nBinSize = 50;
	
	if((sOK == 0) || (iOK == 0) || (oOK == 0) || (dOK == 0))
	{
		printf("Error: Input Parameter not correct!\n");
		exit(EXIT_FAILURE);
	}
	else
	{
		nResult = SeqSVD_Main(strSamplePath, strInputPath, strOutputPath, strOutputFile, 
			nTargetReadNum, nBinSize, nExtLen, nApplyLog, nZeroShift, nMaxPCAuto, nMaxPC, dVcut,
			nExportBAR, nKeepTempFiles);
	}

	return nResult;
}

