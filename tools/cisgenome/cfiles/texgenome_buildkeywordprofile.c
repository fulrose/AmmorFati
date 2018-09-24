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

int menu_texgenome_buildkeywordprofile(int argv, char **argc);

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
	menu_texgenome_buildkeywordprofile(argv, argc);

	/* exit */
	exit(EXIT_SUCCESS);
}

int menu_texgenome_buildkeywordprofile(int argv, char **argc)
{
	char strSampleIndexFile[MED_LINE_LENGTH];
	char strDictionaryFolder[MED_LINE_LENGTH];
	char strKeywordFile[MED_LINE_LENGTH];
	char strOutputFile[MED_LINE_LENGTH];
	int nScoreType = 0;

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
		printf("   texgenome_buildkeywordprofile   \n");
		printf(" -s sample index file \n");
		printf(" -d dictionary folder  \n");
		printf(" -w key word file. Each line is a combined key word such as stem cell \n");
		printf(" -wt key word score type. 0 (default): add; 1: multiply. \n");
		printf(" -o output file \n");
		printf(" Example: \n");
		printf("    texgenome_buildkeywordprofile -s GPL1261_sample_index.txt -d /users/tfidf -w keyword_list.txt -wt 1 -o keyword_profile.txt\n");
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
			strcpy(strDictionaryFolder, argc[ni]);
			dOK = 1;
		}
		else if(strcmp(argc[ni], "-w") == 0)
		{
			ni++;
			strcpy(strKeywordFile, argc[ni]);
			wOK = 1;
		}
		else if(strcmp(argc[ni], "-wt") == 0)
		{
			ni++;
			nScoreType = atoi(argc[ni]);
		}
		else if(strcmp(argc[ni], "-o") == 0)
		{
			ni++;
			strcpy(strOutputFile, argc[ni]);
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
		nResult = TexGenome_BuildKeywordProfile(strSampleIndexFile, strDictionaryFolder, 
					strKeywordFile, strOutputFile, nScoreType);
	}

	return nResult;
}