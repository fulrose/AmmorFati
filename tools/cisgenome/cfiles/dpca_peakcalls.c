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

int menu_dpca_peakcalls(int argv, char **argc);

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
	menu_dpca_peakcalls(argv, argc);

	/* exit */
	exit(EXIT_SUCCESS);
}

int menu_dpca_peakcalls(int argv, char **argc)
{
	char strdPCAParamFile[MED_LINE_LENGTH];
	char strPeakListParamFile[MED_LINE_LENGTH];
	char strCisGenomeFolder[MED_LINE_LENGTH]; 
	int dOK;
	int nResult;
	int iOK,pOK;
	int ni;

	/* init */
	strcpy(strdPCAParamFile, "");
	strcpy(strPeakListParamFile, "");
	strcpy(strCisGenomeFolder, "");
	

	/* ------------------------------- */
	/*    menu_dpca_peakcalls          */
	/* ------------------------------- */
	if(argv < 1)
	{
		printf("Error: parameter wrong!\n");
		exit(EXIT_FAILURE);
	}
	else if(argv == 1)
	{
		printf("/* ----------------------------- */\n");
		printf("    dpca_peakcalls                 \n");
		printf(" -i parameter file used for dpca_importdata. \n");
		printf(" -p peak list file to specify IP and control samples for each peak list. \n");
		printf(" -d full path to the CisGenome bin folder  \n");
		printf(" Usage: \n");
		/* printf("    dpca_peakcalls -i dpca_importdata_parameter.txt -p dpca_peaklist_parameter.txt\n"); */
		printf("    dpca_peakcalls -i dpca_importdata_parameter.txt -p dpca_peaklist_parameter.txt -d /user/cisgenome/bin\n");
		printf("/* ----------------------------- */\n");
		exit(EXIT_SUCCESS);
	}

	iOK = 0;
	pOK = 0;
	dOK = 0;

	ni = 1;
	while(ni < argv)
	{
		if(strcmp(argc[ni], "-i") == 0)
		{
			ni++;
			strcpy(strdPCAParamFile, argc[ni]);
			iOK = 1;
		}
		else if(strcmp(argc[ni], "-p") == 0)
		{
			ni++;
			strcpy(strPeakListParamFile, argc[ni]);
			pOK = 1;
		}
		else if(strcmp(argc[ni], "-d") == 0)
		{
			ni++;
			strcpy(strCisGenomeFolder, argc[ni]);
			AdjustDirectoryPath(strCisGenomeFolder);
			dOK = 1;
		}
		else 
		{
			printf("Error: unknown parameters!\n");
			exit(EXIT_FAILURE);
		}

		ni++;
	}

	if((iOK == 0) || (pOK == 0) /*|| (dOK == 0)*/)
	{
		printf("Error: Input Parameter not correct!\n");
		exit(EXIT_FAILURE);
	}
	else
	{
		nResult = dPCA_PeakCalls_Main(strdPCAParamFile, strPeakListParamFile, strCisGenomeFolder);
	}

	return nResult;
}