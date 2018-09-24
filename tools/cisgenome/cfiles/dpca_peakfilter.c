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

int menu_dpca_peakfilter(int argv, char **argc);

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
	menu_dpca_peakfilter(argv, argc);

	/* exit */
	exit(EXIT_SUCCESS);
}

int menu_dpca_peakfilter(int argv, char **argc)
{
	char strPeakCallFile[MED_LINE_LENGTH];
	char strPeakdataFile[MED_LINE_LENGTH];
	char strRawdataFile[MED_LINE_LENGTH];
	char strOutputFolder[MED_LINE_LENGTH];
	char strOutputTitle[MED_LINE_LENGTH];

	double dFDRCut = 0.1;
	int nTransform = 0;
	int nColMeanCent = 0;
	int nColStand = 0;

	int pcOK;
	int pdOK;
	int rdOK;
	int dOK;
	int oOK;
	int ni;
	int nResult;

	/* ------------------------------- */
	/*     menu_dpca_peakfilter        */
	/* ------------------------------- */
	if(argv < 1)
	{
		printf("Error: parameter wrong!\n");
		exit(EXIT_FAILURE);
	}
	else if(argv == 1)
	{
		printf("/* ----------------------------- */\n");
		printf("    dpca_peakfilter                \n");
		printf(" -pc peak call file \n");
		printf(" -pd peak data file \n");
		printf(" -rd raw data file  \n");
		printf(" -d output folder  \n");
		printf(" -o output title  \n");
		printf(" -t transform: 0 (default) = identity; 1 = log2 transform.\n");
		printf(" -sm center x_gimk of each sample to have zero mean: 0 (default) = no; 1 = yes. \n");
		printf(" -ss standardize each sample: 0 (default) = no; 1 = yes.\n");
		printf(" -fdr FDR cutoff for claiming a peak: default = 0.1. \n");
		printf(" Example: \n");
		printf("    dpca_peakfilter -pc peakcall.txt -pd peakdata.txt -rd dpcadata.txt -d /home/work/ -o output -t 1\n");
		printf("/* ----------------------------- */\n");
		exit(EXIT_SUCCESS);
	}

	pcOK = 0;
	pdOK = 0;
	rdOK = 0;
	oOK = 0;
	dOK = 0;

	ni = 1;
	while(ni < argv)
	{
		if(strcmp(argc[ni], "-pc") == 0)
		{
			ni++;
			strcpy(strPeakCallFile, argc[ni]);
			pcOK = 1;
		}
		else if(strcmp(argc[ni], "-pd") == 0)
		{
			ni++;
			strcpy(strPeakdataFile, argc[ni]);
			pdOK = 1;
		}
		else if(strcmp(argc[ni], "-rd") == 0)
		{
			ni++;
			strcpy(strRawdataFile, argc[ni]);
			rdOK = 1;
		}
		else if(strcmp(argc[ni], "-d") == 0)
		{
			ni++;
			strcpy(strOutputFolder, argc[ni]);
			dOK = 1;
		}
		else if(strcmp(argc[ni], "-o") == 0)
		{
			ni++;
			strcpy(strOutputTitle, argc[ni]);
			oOK = 1;
		}
		else if(strcmp(argc[ni], "-t") == 0)
		{
			ni++;
			nTransform = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-sm") == 0)
		{
			ni++;
			nColMeanCent = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-ss") == 0)
		{
			ni++;
			nColStand = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-fdr") == 0)
		{
			ni++;
			dFDRCut = atof(argc[ni]);
		}
		else 
		{
			printf("Error: unknown parameters!\n");
			exit(EXIT_FAILURE);
		}

		ni++;
	}

	if((pcOK == 0) || (pdOK == 0) || (rdOK == 0) || (oOK == 0) || (dOK == 0))
	{
		printf("Error: Input Parameter not correct!\n");
		exit(EXIT_FAILURE);
	}
	else
	{
		nResult = dPCA_P_Filter_Main(strPeakCallFile, strPeakdataFile,
			strRawdataFile, strOutputFolder, strOutputTitle,
			dFDRCut, nTransform, nColMeanCent, nColStand);
	}

	return nResult;
}