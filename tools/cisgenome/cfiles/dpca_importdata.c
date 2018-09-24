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

int menu_dpca_importdata(int argv, char **argc);

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
	menu_dpca_importdata(argv, argc);

	/* exit */
	exit(EXIT_SUCCESS);
}

int menu_dpca_importdata(int argv, char **argc)
{
	char strParamFile[LINE_LENGTH];
	int nResult;

	/* ------------------------------- */
	/*    menu_dpca_importdata         */
	/* ------------------------------- */
	if(argv != 2)
	{
		printf("/* ----------------------------- */\n");
		printf("    dpca_importdata                \n");
		printf(" Usage: \n");
		printf("    dpca_importdata parameterfile.txt \n");
		printf("/* ----------------------------- */\n");
		exit(EXIT_SUCCESS);
	}

	strcpy(strParamFile, argc[1]);
	nResult = dPCA_ImportData_Main(strParamFile);

	return nResult;
}