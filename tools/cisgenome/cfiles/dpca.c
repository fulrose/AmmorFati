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

int menu_dpca(int argv, char **argc);

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
	menu_dpca(argv, argc);

	/* exit */
	exit(EXIT_SUCCESS);
}

int menu_dpca(int argv, char **argc)
{
	char strInputFile[MED_LINE_LENGTH];
	char strOutputFolder[MED_LINE_LENGTH];
	char strOutputTitle[MED_LINE_LENGTH];
	int nTransform = 0;
	int nColMeanCent = 0;
	int nColStand = 0;
	int nMColMeanCent = 1;
	int nMColStand = 0;
	double dSNRCut = 5;
	int nUsedPCAZ = 0;
	int nUseRB = 0;
	char strPeakCallFile[MED_LINE_LENGTH];
	double dPeakFDRCut = 0.5;

	int iOK;
	int dOK;
	int oOK;
	int ni;
	int nResult;

	/* ------------------------------- */
	/*     menu_dpca                   */
	/* ------------------------------- */
	if(argv < 1)
	{
		printf("Error: parameter wrong!\n");
		exit(EXIT_FAILURE);
	}
	else if(argv == 1)
	{
		printf("/* ----------------------------- */\n");
		printf("    dpca                           \n");
		printf(" -i input data file \n");
		printf(" -d output folder \n");
		printf(" -o output file header  \n");
		printf(" -t transform: 0 (default) = identity; 1 = log2 transform.\n");
		printf(" -cm center each column of D to have zero mean: 0 = no; 1 (default) = yes.\n");
		printf(" -cs standardize each column of D to have SD=1: 0 (default) = no; 1 = yes.\n");
		printf(" -sm center x_gimk of each sample to have zero mean before computing D: 0 (default) = no; 1 = yes. \n");
		printf("     Usually useful for allele-specific analysis for removing reference mapping bias. \n");
		printf(" -ss standardize each sample before computing D: 0 (default) = no; 1 = yes.\n");
		printf(" -snr signal-to-noise ratio cutoff: default = 5.\n");
		printf(" -z applying dPCA-Z filter: 0 (default) = no; 1 = yes. \n");
		printf(" -r full path for the file that contains peak calls for computing the R^B statistic or applying dPCA-Z.\n");
		printf(" Example: \n");
		printf("    dpca -i input.txt -d /home/work/ -o output -t 1\n");
		printf("/* ----------------------------- */\n");
		exit(EXIT_SUCCESS);
	}

	iOK = 0;
	oOK = 0;
	dOK = 0;

	ni = 1;
	while(ni < argv)
	{
		if(strcmp(argc[ni], "-i") == 0)
		{
			ni++;
			strcpy(strInputFile, argc[ni]);
			iOK = 1;
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
		else if(strcmp(argc[ni], "-cm") == 0)
		{
			ni++;
			nMColMeanCent = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-cs") == 0)
		{
			ni++;
			nMColStand = atoi(argc[ni]);
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
		else if(strcmp(argc[ni], "-snr") == 0)
		{
			ni++;
			dSNRCut = atof(argc[ni]);
		}
		else if(strcmp(argc[ni], "-z") == 0)
		{
			ni++;
			nUsedPCAZ = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-r") == 0)
		{
			ni++;
			nUseRB = 1;
			strcpy(strPeakCallFile, argc[ni]);
		}
		else 
		{
			printf("Error: unknown parameters!\n");
			exit(EXIT_FAILURE);
		}

		ni++;
	}

	if((iOK == 0) || (oOK == 0) || (dOK == 0))
	{
		printf("Error: Input Parameter not correct!\n");
		exit(EXIT_FAILURE);
	}
	else
	{
		nResult = dPCA_Main(strInputFile, strOutputFolder, strOutputTitle, 
			nTransform, nColMeanCent, nColStand, nMColMeanCent, nMColStand, dSNRCut,
			nUsedPCAZ, nUseRB, strPeakCallFile, dPeakFDRCut);
	}

	return nResult;
}