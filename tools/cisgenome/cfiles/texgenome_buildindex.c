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
#include "WorkLib.h"

int menu_texgenome_buildindex(int argv, char **argc);

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
	menu_texgenome_buildindex(argv, argc);

	/* exit */
	exit(EXIT_SUCCESS);
}

int menu_texgenome_buildindex(int argv, char **argc)
{
	char strSampleIndexFile[MED_LINE_LENGTH];
	char strDocIndexFile[MED_LINE_LENGTH];
	char strWordMapFile[MED_LINE_LENGTH];
	char strExportFolder[MED_LINE_LENGTH];

	int ni;
	int sOK;
	int dOK;
	int wOK;
	int oOK;
	int nResult;

	/* ------------------------------- */
	/*     menu_seqclust               */
	/* ------------------------------- */
	if(argv < 1)
	{
		printf("Error: parameter wrong!\n");
		exit(EXIT_FAILURE);
	}
	else if(argv == 1)
	{
		printf("/* ----------------------------- */\n");
		printf("    texgenome_buildindex           \n");
		printf(" -s sample index file \n");
		printf(" -d document index file  \n");
		printf(" -w word map file  \n");
		printf(" -o output folder \n");
		printf(" Example: \n");
		printf("    texgenome_buildindex -s GPL1261_sample_index.txt -d all_doc_index.txt -w tfidf_matrix.txt -o /users/tfidf \n");
		printf("/* ----------------------------- */\n");
		exit(EXIT_SUCCESS);
	}

	sOK = 0;
	dOK = 0;
	wOK = 0;
	oOK = 0;
	
	ni = 1;
	while(ni < argv)
	{
		if(strcmp(argc[ni], "-s") == 0)
		{
			ni++;
			strcpy(strSampleIndexFile, argc[ni]);
			sOK = 1;
		}
		else if(strcmp(argc[ni], "-d") == 0)
		{
			ni++;
			strcpy(strDocIndexFile, argc[ni]);
			dOK = 1;
		}
		else if(strcmp(argc[ni], "-w") == 0)
		{
			ni++;
			strcpy(strWordMapFile, argc[ni]);
			wOK = 1;
		}
		else if(strcmp(argc[ni], "-o") == 0)
		{
			ni++;
			strcpy(strExportFolder, argc[ni]);
			oOK = 1;
		}		
		else 
		{
			printf("Error: unknown parameters!\n");
			exit(EXIT_FAILURE);
		}

		ni++;
	}

	if((sOK == 0) || (dOK == 0) || (wOK == 0) || (oOK == 0))
	{
		printf("Error: Input Parameter not correct!\n");
		exit(EXIT_FAILURE);
	}
	else
	{
		nResult = TexGenome_BuildIndex(strSampleIndexFile, strDocIndexFile, 
						 strWordMapFile, strExportFolder);
	}

	return nResult;
}