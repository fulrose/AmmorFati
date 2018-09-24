#! /bin/sh

gcc -c ./cfiles/AffyLib.c -o ./obj/AffyLib.o
gcc -c ./cfiles/GenomeLib.c -o ./obj/GenomeLib.o
gcc -c ./cfiles/MathLib.c -o ./obj/MathLib.o
gcc -c ./cfiles/MatrixLib.c -o ./obj/MatrixLib.o
gcc -c ./cfiles/MicroarrayLib.c -o ./obj/MicroarrayLib.o
gcc -c ./cfiles/MotifLib.c -o ./obj/MotifLib.o
gcc -c ./cfiles/RandomLib.c -o ./obj/RandomLib.o
gcc -c ./cfiles/SequenceLib.c -o ./obj/SequenceLib.o
gcc -c ./cfiles/StringLib.c -o ./obj/StringLib.o
gcc -c ./cfiles/Alignment.c -o ./obj/Alignment.o
gcc -c ./cfiles/PhysicalNetworkLib.c -o ./obj/PhysicalNetworkLib.o
gcc -c ./cfiles/WorkLib.c -o ./obj/WorkLib.o
gcc -c ./cfiles/FlexModuleInterface.c -o ./obj/FlexModuleInterface.o
gcc -c ./cfiles/TilingArrayLib.c -o ./obj/TilingArrayLib.o
gcc -c ./cfiles/HTSequencingLib.c -o ./obj/HTSequencingLib.o
gcc -c ./cfiles/GSCALib.c -o ./obj/GSCALib.o

gcc -c ./cfiles/file_bed2cod.c -o ./obj/file_bed2cod.o
gcc -o ./bin/file_bed2cod ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/file_bed2cod.o -lm
gcc -c ./cfiles/file_cod2bed.c -o ./obj/file_cod2bed.o
gcc -o ./bin/file_cod2bed ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/file_cod2bed.o -lm
gcc -c ./cfiles/file_eland2aln.c -o ./obj/file_eland2aln.o
gcc -o ./bin/file_eland2aln ./obj/file_eland2aln.o
gcc -c ./cfiles/file_eland2aln_v2.c -o ./obj/file_eland2aln_v2.o
gcc -o ./bin/file_eland2aln_v2 ./obj/file_eland2aln_v2.o
gcc -c ./cfiles/file_bowtie2aln.c -o ./obj/file_bowtie2aln.o
gcc -o ./bin/file_bowtie2aln ./obj/file_bowtie2aln.o
gcc -c ./cfiles/file_bed2aln.c -o ./obj/file_bed2aln.o
gcc -o ./bin/file_bed2aln ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/file_bed2aln.o -lm

gcc -c ./cfiles/genome_encode.c -o ./obj/genome_encode.o
gcc -o ./bin/genome_encode ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_encode.o -lm
gcc -c ./cfiles/genome_conservebg.c -o ./obj/genome_conservebg.o
gcc -o ./bin/genome_conservebg ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_conservebg.o -lm
gcc -c ./cfiles/genome_conservecs.c -o ./obj/genome_conservecs.o
gcc -o ./bin/genome_conservecs ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_conservecs.o -lm
gcc -c ./cfiles/genome_footprint.c -o ./obj/genome_footprint.o
gcc -o ./bin/genome_footprint ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_footprint.o -lm
gcc -c ./cfiles/genome_csgetdistn.c -o ./obj/genome_csgetdistn.o
gcc -o ./bin/genome_csgetdistn ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_csgetdistn.o -lm
gcc -c ./cfiles/genome_codephastcons.c -o ./obj/genome_codephastcons.o
gcc -o ./bin/genome_codephastcons ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_codephastcons.o -lm
gcc -c ./cfiles/genome_codephastcons_v2.c -o ./obj/genome_codephastcons_v2.o
gcc -o ./bin/genome_codephastcons_v2 ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_codephastcons_v2.o -lm
gcc -c ./cfiles/genome_getseq.c -o ./obj/genome_getseq.o
gcc -o ./bin/genome_getseq ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_getseq.o -lm
gcc -c ./cfiles/genome_getseqcs.c -o ./obj/genome_getseqcs.o
gcc -o ./bin/genome_getseqcs ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_getseqcs.o -lm
gcc -c ./cfiles/genome_getmaskedseq.c -o ./obj/genome_getmaskedseq.o
gcc -o ./bin/genome_getmaskedseq ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_getmaskedseq.o -lm
gcc -c ./cfiles/genome_getmaskedreg.c -o ./obj/genome_getmaskedreg.o
gcc -o ./bin/genome_getmaskedreg ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_getmaskedreg.o -lm
gcc -c ./cfiles/genome_getseq_c.c -o ./obj/genome_getseq_c.o
gcc -o ./bin/genome_getseq_c ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_getseq_c.o -lm
gcc -c ./cfiles/genome_getseqcs_c.c -o ./obj/genome_getseqcs_c.o
gcc -o ./bin/genome_getseqcs_c ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_getseqcs_c.o -lm
gcc -c ./cfiles/genome_getmaskedseq_c.c -o ./obj/genome_getmaskedseq_c.o
gcc -o ./bin/genome_getmaskedseq_c ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_getmaskedseq_c.o -lm
gcc -c ./cfiles/genome_getmaskedreg_c.c -o ./obj/genome_getmaskedreg_c.o
gcc -o ./bin/genome_getmaskedreg_c ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_getmaskedreg_c.o -lm
gcc -c ./cfiles/genome_codingCDS.c -o ./obj/genome_codingCDS.o
gcc -o ./bin/genome_codingCDS ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_codingCDS.o -lm
gcc -c ./cfiles/genome_getcsgcsummary.c -o ./obj/genome_getcsgcsummary.o
gcc -o ./bin/genome_getcsgcsummary ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_getcsgcsummary.o -lm
gcc -c ./cfiles/genome_regioncssummary.c -o ./obj/genome_regioncssummary.o
gcc -o ./bin/genome_regioncssummary ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_regioncssummary.o -lm
gcc -c ./cfiles/genome_regionextend.c -o ./obj/genome_regionextend.o
gcc -o ./bin/genome_regionextend ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_regionextend.o -lm
gcc -c ./cfiles/genome_fastaseqmask.c -o ./obj/genome_fastaseqmask.o
gcc -o ./bin/genome_fastaseqmask ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_fastaseqmask.o -lm
gcc -c ./cfiles/genome_hash.c -o ./obj/genome_hash.o
gcc -o ./bin/genome_hash ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/genome_hash.o -lm

gcc -c ./cfiles/fasta_soft2hardmask.c -o ./obj/fasta_soft2hardmask.o
gcc -o ./bin/fasta_soft2hardmask ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/fasta_soft2hardmask.o -lm

gcc -c ./cfiles/refgene_encode.c -o ./obj/refgene_encode.o
gcc -o ./bin/refgene_encode ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_encode.o -lm
gcc -c ./cfiles/refgene_pickspeciesspecific.c -o ./obj/refgene_pickspeciesspecific.o
gcc -o ./bin/refgene_pickspeciesspecific ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_pickspeciesspecific.o -lm
gcc -c ./cfiles/refgene_gettssaround.c -o ./obj/refgene_gettssaround.o
gcc -o ./bin/refgene_gettssaround ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_gettssaround.o -lm
gcc -c ./cfiles/refgene_getmultiortholog.c -o ./obj/refgene_getmultiortholog.o
gcc -o ./bin/refgene_getmultiortholog ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_getmultiortholog.o -lm
gcc -c ./cfiles/refgene_getmultiortholog1way.c -o ./obj/refgene_getmultiortholog1way.o
gcc -o ./bin/refgene_getmultiortholog1way ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_getmultiortholog1way.o -lm
gcc -c ./cfiles/refgene_getmultiorthologtssaround.c -o ./obj/refgene_getmultiorthologtssaround.o
gcc -o ./bin/refgene_getmultiorthologtssaround ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_getmultiorthologtssaround.o -lm
gcc -c ./cfiles/refgene_getmultiorthologtssaroundexonmasked.c -o ./obj/refgene_getmultiorthologtssaroundexonmasked.o
gcc -o ./bin/refgene_getmultiorthologtssaroundexonmasked ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_getmultiorthologtssaroundexonmasked.o -lm
gcc -c ./cfiles/refgene_getnearestgene.c -o ./obj/refgene_getnearestgene.o
gcc -o ./bin/refgene_getnearestgene ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_getnearestgene.o -lm
gcc -c ./cfiles/refgene_getaffy.c -o ./obj/refgene_getaffy.o
gcc -o ./bin/refgene_getaffy ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_getaffy.o -lm
gcc -c ./cfiles/refgene_getmatchedcontrol.c -o ./obj/refgene_getmatchedcontrol.o
gcc -o ./bin/refgene_getmatchedcontrol ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_getmatchedcontrol.o -lm
gcc -c ./cfiles/refgene_getlocationsummary.c -o ./obj/refgene_getlocationsummary.o
gcc -o ./bin/refgene_getlocationsummary ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refgene_getlocationsummary.o -lm

gcc -c ./cfiles/refflat_encode.c -o ./obj/refflat_encode.o
gcc -o ./bin/refflat_encode ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refflat_encode.o -lm
gcc -c ./cfiles/reflocus_createmap.c -o ./obj/reflocus_createmap.o
gcc -o ./bin/reflocus_createmap ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/reflocus_createmap.o -lm
gcc -c ./cfiles/reflocus_getneighborgenes.c -o ./obj/reflocus_getneighborgenes.o
gcc -o ./bin/reflocus_getneighborgenes ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/reflocus_getneighborgenes.o -lm
gcc -c ./cfiles/reflocus_assignvalue.c -o ./obj/reflocus_assignvalue.o
gcc -o ./bin/reflocus_assignvalue ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/reflocus_assignvalue.o -lm

gcc -c ./cfiles/refexon_createmap.c -o ./obj/refexon_createmap.o
gcc -o ./bin/refexon_createmap ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refexon_createmap.o -lm
gcc -c ./cfiles/refmicroarray_createmap.c -o ./obj/refmicroarray_createmap.o
gcc -o ./bin/refmicroarray_createmap ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refmicroarray_createmap.o -lm
gcc -c ./cfiles/refflex_getmultiortholog.c -o ./obj/refflex_getmultiortholog.o
gcc -o ./bin/refflex_getmultiortholog ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refflex_getmultiortholog.o -lm
gcc -c ./cfiles/refflex_getmultiortholog1way.c -o ./obj/refflex_getmultiortholog1way.o
gcc -o ./bin/refflex_getmultiortholog1way ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/refflex_getmultiortholog1way.o -lm

gcc -c ./cfiles/affy_bar2txt.c -o ./obj/affy_bar2txt.o
gcc -o ./bin/affy_bar2txt ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/affy_bar2txt.o -lm
gcc -c ./cfiles/affy_bar2wig.c -o ./obj/affy_bar2wig.o
gcc -o ./bin/affy_bar2wig ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/affy_bar2wig.o -lm

gcc -c ./cfiles/powexpress.c -o ./obj/powexpress.o
gcc -o ./bin/powexpress ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/powexpress.o -lm
gcc -c ./cfiles/powexpressloc.c -o ./obj/powexpressloc.o
gcc -o ./bin/powexpressloc ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/powexpressloc.o -lm
gcc -c ./cfiles/powexpress_getspecificprobe.c -o ./obj/powexpress_getspecificprobe.o
gcc -o ./bin/powexpress_getspecificprobe ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/powexpress_getspecificprobe.o -lm
gcc -c ./cfiles/powexpress_getnrprobe.c -o ./obj/powexpress_getnrprobe.o
gcc -o ./bin/powexpress_getnrprobe ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/powexpress_getnrprobe.o -lm

gcc -c ./cfiles/tileprobe_buildmodel.c -o ./obj/tileprobe_buildmodel.o
gcc -o ./bin/tileprobe_buildmodel ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_buildmodel.o -lm
gcc -c ./cfiles/tileprobe_buildmodel_v2.c -o ./obj/tileprobe_buildmodel_v2.o
gcc -o ./bin/tileprobe_buildmodel_v2 ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_buildmodel_v2.o -lm
gcc -c ./cfiles/tileprobe_buildmodel_hmmt.c -o ./obj/tileprobe_buildmodel_hmmt.o
gcc -o ./bin/tileprobe_buildmodel_hmmt ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_buildmodel_hmmt.o -lm
gcc -c ./cfiles/tileprobe_buildmodel_hmmb.c -o ./obj/tileprobe_buildmodel_hmmb.o
gcc -o ./bin/tileprobe_buildmodel_hmmb ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_buildmodel_hmmb.o -lm
gcc -c ./cfiles/tileprobe_buildmodel_hmmm.c -o ./obj/tileprobe_buildmodel_hmmm.o
gcc -o ./bin/tileprobe_buildmodel_hmmm ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_buildmodel_hmmm.o -lm
gcc -c ./cfiles/tileprobe_buildmodel_hmmw.c -o ./obj/tileprobe_buildmodel_hmmw.o
gcc -o ./bin/tileprobe_buildmodel_hmmw ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_buildmodel_hmmw.o -lm
gcc -c ./cfiles/tileprobe_huberdata.c -o ./obj/tileprobe_huberdata.o
gcc -o ./bin/tileprobe_huberdata ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_huberdata.o -lm

gcc -c ./cfiles/tileprobe_norm.c -o ./obj/tileprobe_norm.o
gcc -o ./bin/tileprobe_norm ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_norm.o -lm
gcc -c ./cfiles/tileprobe_peak.c -o ./obj/tileprobe_peak.o
gcc -o ./bin/tileprobe_peak ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_peak.o -lm
gcc -c ./cfiles/tileprobe_mat.c -o ./obj/tileprobe_mat.o
gcc -o ./bin/tileprobe_mat ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_mat.o -lm
gcc -c ./cfiles/tileprobe_buildbarmodel.c -o ./obj/tileprobe_buildbarmodel.o
gcc -o ./bin/tileprobe_buildbarmodel ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_buildbarmodel.o -lm
gcc -c ./cfiles/tileprobe_barnorm.c -o ./obj/tileprobe_barnorm.o
gcc -o ./bin/tileprobe_barnorm ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_barnorm.o -lm
gcc -c ./cfiles/tileprobe_buildbarmodel_v2.c -o ./obj/tileprobe_buildbarmodel_v2.o
gcc -o ./bin/tileprobe_buildbarmodel_v2 ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_buildbarmodel_v2.o -lm
gcc -c ./cfiles/tileprobe_resample.c -o ./obj/tileprobe_resample.o
gcc -o ./bin/tileprobe_resample ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tileprobe_resample.o -lm

gcc -c ./cfiles/tilemap.c -o ./obj/tilemap.o
gcc -o ./bin/tilemap ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/tilemap.o -lm
gcc -c ./cfiles/tilemap_norm.c -o ./obj/tilemap_norm.o
gcc -o ./bin/tilemap_norm ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/tilemap_norm.o -lm
gcc -c ./cfiles/tilemap_importaffy.c -o ./obj/tilemap_importaffy.o
gcc -o ./bin/tilemap_importaffy ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/tilemap_importaffy.o -lm
gcc -c ./cfiles/tilemap_extract.c -o ./obj/tilemap_extract.o
gcc -o ./bin/tilemap_extract ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/tilemap_extract.o -lm
gcc -c ./cfiles/tilemapv2_importaffy.c -o ./obj/tilemapv2_importaffy.o
gcc -o ./bin/tilemapv2_importaffy ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tilemapv2_importaffy.o -lm
gcc -c ./cfiles/tilemapv2.c -o ./obj/tilemapv2.o
gcc -o ./bin/tilemapv2 ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tilemapv2.o -lm
gcc -c ./cfiles/tilemapv2_regioninfo.c -o ./obj/tilemapv2_regioninfo.o
gcc -o ./bin/tilemapv2_regioninfo ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tilemapv2_regioninfo.o -lm
gcc -c ./cfiles/tilemapv2_regioninfo_integral.c -o ./obj/tilemapv2_regioninfo_integral.o
gcc -o ./bin/tilemapv2_regioninfo_integral ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tilemapv2_regioninfo_integral.o -lm
gcc -c ./cfiles/tilemapv2_txt2bar.c -o ./obj/tilemapv2_txt2bar.o
gcc -o ./bin/tilemapv2_txt2bar ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tilemapv2_txt2bar.o -lm
gcc -c ./cfiles/tilemapv2_quantilenorm.c -o ./obj/tilemapv2_quantilenorm.o
gcc -o ./bin/tilemapv2_quantilenorm ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/tilemapv2_quantilenorm.o -lm

gcc -c ./cfiles/hts_aln2uniq.c -o ./obj/hts_aln2uniq.o
gcc -o ./bin/hts_aln2uniq ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_aln2uniq.o -lm
gcc -c ./cfiles/hts_aln2window.c -o ./obj/hts_aln2window.o
gcc -o ./bin/hts_aln2window ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_aln2window.o -lm
gcc -c ./cfiles/hts_aln2bar.c -o ./obj/hts_aln2bar.o
gcc -o ./bin/hts_aln2bar ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_aln2bar.o -lm
gcc -c ./cfiles/hts_alnshift2bar.c -o ./obj/hts_alnshift2bar.o
gcc -o ./bin/hts_alnshift2bar ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_alnshift2bar.o -lm
gcc -c ./cfiles/hts_aln2barv2.c -o ./obj/hts_aln2barv2.o
gcc -o ./bin/hts_aln2barv2 ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_aln2barv2.o -lm
gcc -c ./cfiles/hts_aln2winbar.c -o ./obj/hts_aln2winbar.o
gcc -o ./bin/hts_aln2winbar ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_aln2winbar.o -lm
gcc -c ./cfiles/hts_windowsummary.c -o ./obj/hts_windowsummary.o
gcc -o ./bin/hts_windowsummary ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_windowsummary.o -lm
gcc -c ./cfiles/hts_windowsummaryv2.c -o ./obj/hts_windowsummaryv2.o
gcc -o ./bin/hts_windowsummaryv2 ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_windowsummaryv2.o -lm
gcc -c ./cfiles/hts_windowsummary_2sample.c -o ./obj/hts_windowsummary_2sample.o
gcc -o ./bin/hts_windowsummary_2sample ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_windowsummary_2sample.o -lm
gcc -c ./cfiles/hts_windowsummaryv2_2sample.c -o ./obj/hts_windowsummaryv2_2sample.o
gcc -o ./bin/hts_windowsummaryv2_2sample ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_windowsummaryv2_2sample.o -lm
gcc -c ./cfiles/hts_peakdetector.c -o ./obj/hts_peakdetector.o
gcc -o ./bin/hts_peakdetector ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_peakdetector.o -lm
gcc -c ./cfiles/hts_peakdetector_2sample.c -o ./obj/hts_peakdetector_2sample.o
gcc -o ./bin/hts_peakdetector_2sample ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_peakdetector_2sample.o -lm
gcc -c ./cfiles/hts_peakdetectorv2.c -o ./obj/hts_peakdetectorv2.o
gcc -o ./bin/hts_peakdetectorv2 ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_peakdetectorv2.o -lm
gcc -c ./cfiles/hts_peakdetectorv2_2sample.c -o ./obj/hts_peakdetectorv2_2sample.o
gcc -o ./bin/hts_peakdetectorv2_2sample ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_peakdetectorv2_2sample.o -lm
gcc -c ./cfiles/hts_createrepeatfilter.c -o ./obj/hts_createrepeatfilter.o
gcc -o ./bin/hts_createrepeatfilter ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_createrepeatfilter.o -lm
gcc -c ./cfiles/hts_filterrepeatreads.c -o ./obj/hts_filterrepeatreads.o
gcc -o ./bin/hts_filterrepeatreads ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_filterrepeatreads.o -lm
gcc -c ./cfiles/hts_collectreads.c -o ./obj/hts_collectreads.o
gcc -o ./bin/hts_collectreads ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_collectreads.o -lm
gcc -c ./cfiles/hts_collectprofile.c -o ./obj/hts_collectprofile.o
gcc -o ./bin/hts_collectprofile ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_collectprofile.o -lm
gcc -c ./cfiles/hts_countreads4refgene.c -o ./obj/hts_countreads4refgene.o
gcc -o ./bin/hts_countreads4refgene ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_countreads4refgene.o -lm
gcc -c ./cfiles/hts_selectreads.c -o ./obj/hts_selectreads.o
gcc -o ./bin/hts_selectreads ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/hts_selectreads.o -lm


gcc -c ./cfiles/cnv_aln2window.c -o ./obj/cnv_aln2window.o
gcc -o ./bin/cnv_aln2window ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/cnv_aln2window.o -lm
gcc -c ./cfiles/cnv_repeat2window.c -o ./obj/cnv_repeat2window.o
gcc -o ./bin/cnv_repeat2window ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/cnv_repeat2window.o -lm

gcc -c ./cfiles/rnaseq_countgeneread.c -o ./obj/rnaseq_countgeneread.o
gcc -o ./bin/rnaseq_countgeneread ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/rnaseq_countgeneread.o -lm

gcc -c ./cfiles/seqclust_seg.c -o ./obj/seqclust_seg.o
gcc -o ./bin/seqclust_seg ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/seqclust_seg.o -lm
gcc -c ./cfiles/seqclust_count.c -o ./obj/seqclust_count.o
gcc -o ./bin/seqclust_count ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/seqclust_count.o -lm
gcc -c ./cfiles/seqclust.c -o ./obj/seqclust.o
gcc -o ./bin/seqclust ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/seqclust.o -lm
gcc -c ./cfiles/seqclust_dp.c -o ./obj/seqclust_dp.o
gcc -o ./bin/seqclust_dp ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/seqclust_dp.o -lm

gcc -c ./cfiles/seqpeak.c -o ./obj/seqpeak.o
gcc -o ./bin/seqpeak ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/seqpeak.o -lm
gcc -c ./cfiles/seqpeak_iponly.c -o ./obj/seqpeak_iponly.o
gcc -o ./bin/seqpeak_iponly ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/seqpeak_iponly.o -lm
gcc -c ./cfiles/seqpca.c -o ./obj/seqpca.o
gcc -o ./bin/seqpca ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/seqpca.o -lm
gcc -c ./cfiles/dpca_importdata.c -o ./obj/dpca_importdata.o
gcc -o ./bin/dpca_importdata ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/dpca_importdata.o -lm
gcc -c ./cfiles/dpca.c -o ./obj/dpca.o
gcc -o ./bin/dpca ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/dpca.o -lm
gcc -c ./cfiles/dpca_peakcalls.c -o ./obj/dpca_peakcalls.o
gcc -o ./bin/dpca_peakcalls ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/dpca_peakcalls.o -lm
gcc -c ./cfiles/dpca_peakfilter.c -o ./obj/dpca_peakfilter.o
gcc -o ./bin/dpca_peakfilter ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/dpca_peakfilter.o -lm


gcc -c ./cfiles/network_shortestpath.c -o ./obj/network_shortestpath.o
gcc -o ./bin/network_shortestpath ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/FlexModuleInterface.o ./obj/network_shortestpath.o -lm
gcc -c ./cfiles/network_createortholognet.c -o ./obj/network_createortholognet.o
gcc -o ./bin/network_createortholognet ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/FlexModuleInterface.o ./obj/network_createortholognet.o -lm
gcc -c ./cfiles/network_getsubnet.c -o ./obj/network_getsubnet.o
gcc -o ./bin/network_getsubnet ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/FlexModuleInterface.o ./obj/network_getsubnet.o -lm
gcc -c ./cfiles/network_bind2entrez.c -o ./obj/network_bind2entrez.o
gcc -o ./bin/network_bind2entrez ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/FlexModuleInterface.o ./obj/network_bind2entrez.o -lm

gcc -c ./cfiles/motifmap_consensusscan.c -o ./obj/motifmap_consensusscan.o
gcc -o ./bin/motifmap_consensusscan ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_consensusscan.o -lm
gcc -c ./cfiles/motifmap_consensusscan_genome.c -o ./obj/motifmap_consensusscan_genome.o
gcc -o ./bin/motifmap_consensusscan_genome ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_consensusscan_genome.o -lm
gcc -c ./cfiles/motifmap_matrixscan.c -o ./obj/motifmap_matrixscan.o
gcc -o ./bin/motifmap_matrixscan ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_matrixscan.o -lm
gcc -c ./cfiles/motifmap_matrixscan_genomebg.c -o ./obj/motifmap_matrixscan_genomebg.o
gcc -o ./bin/motifmap_matrixscan_genomebg ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_matrixscan_genomebg.o -lm
gcc -c ./cfiles/motifmap_matrixscan_genome.c -o ./obj/motifmap_matrixscan_genome.o
gcc -o ./bin/motifmap_matrixscan_genome ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_matrixscan_genome.o -lm
gcc -c ./cfiles/motifmap_matrixintegrate_genome.c -o ./obj/motifmap_matrixintegrate_genome.o
gcc -o ./bin/motifmap_matrixintegrate_genome ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_matrixintegrate_genome.o -lm
gcc -c ./cfiles/motifmap_multiplematrixscan_genome.c -o ./obj/motifmap_multiplematrixscan_genome.o
gcc -o ./bin/motifmap_multiplematrixscan_genome ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_multiplematrixscan_genome.o -lm
gcc -c ./cfiles/motifmap_matrixscan_group.c -o ./obj/motifmap_matrixscan_group.o
gcc -o ./bin/motifmap_matrixscan_group ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_matrixscan_group.o -lm
gcc -c ./cfiles/motifmap_getsitearound.c -o ./obj/motifmap_getsitearound.o
gcc -o ./bin/motifmap_getsitearound ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_getsitearound.o -lm
gcc -c ./cfiles/motifmap_getsitearoundcs.c -o ./obj/motifmap_getsitearoundcs.o
gcc -o ./bin/motifmap_getsitearoundcs ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_getsitearoundcs.o -lm
gcc -c ./cfiles/motifmap_countkmer.c -o ./obj/motifmap_countkmer.o
gcc -o ./bin/motifmap_countkmer ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_countkmer.o -lm
gcc -c ./cfiles/motifmap_matrixscan_genome_enrich.c -o ./obj/motifmap_matrixscan_genome_enrich.o
gcc -o ./bin/motifmap_matrixscan_genome_enrich ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_matrixscan_genome_enrich.o -lm
gcc -c ./cfiles/motifmap_consensusscan_genome_enrich.c -o ./obj/motifmap_consensusscan_genome_enrich.o
gcc -o ./bin/motifmap_consensusscan_genome_enrich ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_consensusscan_genome_enrich.o -lm
gcc -c ./cfiles/motifmap_matrixscan_genome_summary.c -o ./obj/motifmap_matrixscan_genome_summary.o
gcc -o ./bin/motifmap_matrixscan_genome_summary ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_matrixscan_genome_summary.o -lm
gcc -c ./cfiles/motifmap_consensusscan_genome_summary.c -o ./obj/motifmap_consensusscan_genome_summary.o
gcc -o ./bin/motifmap_consensusscan_genome_summary ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_consensusscan_genome_summary.o -lm
gcc -c ./cfiles/motifmap_filter_genome.c -o ./obj/motifmap_filter_genome.o
gcc -o ./bin/motifmap_filter_genome ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_filter_genome.o -lm
gcc -c ./cfiles/motifmap_matrixscan_genome_getcutoff.c -o ./obj/motifmap_matrixscan_genome_getcutoff.o
gcc -o ./bin/motifmap_matrixscan_genome_getcutoff ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_matrixscan_genome_getcutoff.o -lm
gcc -c ./cfiles/motifmap_getcluster.c -o ./obj/motifmap_getcluster.o
gcc -o ./bin/motifmap_getcluster ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/motifmap_getcluster.o -lm


gcc -c ./cfiles/flexmodule.c -o ./obj/flexmodule.o
gcc -c ./cfiles/FlexModuleInterface_anchordist.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule_anchordist ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/FlexModuleInterface_motif.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule_motif ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/FlexModuleInterface_tnum.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule_tnum ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/FlexModuleInterface_oneeach.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule_oneeach ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/FlexModuleInterface_moreeach.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule_moreeach ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/FlexModuleInterface_tnumrelax.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule_tnumrelax ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/FlexModuleInterface_oneeachrelax.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule_oneeachrelax ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/FlexModuleInterface_moreeachrelax.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule_moreeachrelax ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/FlexModuleInterface_tworeverse.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule_tworeverse ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/FlexModuleInterface.c -o ./obj/FlexModuleInterface.o
gcc -o ./bin/flexmodule ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule.o -lm
gcc -c ./cfiles/flexmodule_bgfit.c -o ./obj/flexmodule_bgfit.o
gcc -o ./bin/flexmodule_bgfit ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/flexmodule_bgfit.o -lm

gcc -c ./cfiles/malign_blasthit.c -o ./obj/malign_blasthit.o
gcc -o ./bin/malign_blasthit ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/malign_blasthit.o -lm
gcc -c ./cfiles/malign_motifmap.c -o ./obj/malign_motifmap.o
gcc -o ./bin/malign_motifmap ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/malign_motifmap.o -lm
gcc -c ./cfiles/malign_genome_prepareortholog.c -o ./obj/malign_genome_prepareortholog.o
gcc -o ./bin/malign_genome_prepareortholog ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/malign_genome_prepareortholog.o -lm
gcc -c ./cfiles/malign_genome_blasthit.c -o ./obj/malign_genome_blasthit.o
gcc -o ./bin/malign_genome_blasthit ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/malign_genome_blasthit.o -lm
gcc -c ./cfiles/malign_modulemap.c -o ./obj/malign_modulemap.o
gcc -o ./bin/malign_modulemap ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/malign_modulemap.o -lm
gcc -c ./cfiles/malign_countkmer.c -o ./obj/malign_countkmer.o
gcc -o ./bin/malign_countkmer ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/malign_countkmer.o -lm
gcc -c ./cfiles/malign_generatemotifaln.c -o ./obj/malign_generatemotifaln.o
gcc -o ./bin/malign_generatemotifaln ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/malign_generatemotifaln.o -lm

gcc -c ./cfiles/work_esclusgetrefflat.c -o ./obj/work_esclusgetrefflat.o
gcc -o ./bin/work_esclusgetrefflat ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/work_esclusgetrefflat.o -lm
gcc -c ./cfiles/work_esgetpromoter.c -o ./obj/work_esgetpromoter.o
gcc -o ./bin/work_esgetpromoter ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/work_esgetpromoter.o -lm
gcc -c ./cfiles/work_shhmbtest.c -o ./obj/work_shhmbtest.o
gcc -o ./bin/work_shhmbtest ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/Alignment.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/work_shhmbtest.o -lm

gcc -c ./cfiles/texgenome_buildindex.c -o ./obj/texgenome_buildindex.o
gcc -o ./bin/texgenome_buildindex ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/GSCALib.o ./obj/texgenome_buildindex.o -lm
gcc -c ./cfiles/texgenome_buildkeywordprofile.c -o ./obj/texgenome_buildkeywordprofile.o
gcc -o ./bin/texgenome_buildkeywordprofile ./obj/AffyLib.o ./obj/GenomeLib.o ./obj/MathLib.o ./obj/MatrixLib.o ./obj/MicroarrayLib.o ./obj/MotifLib.o ./obj/RandomLib.o ./obj/SequenceLib.o ./obj/StringLib.o ./obj/PhysicalNetworkLib.o ./obj/WorkLib.o ./obj/FlexModuleInterface.o ./obj/TilingArrayLib.o ./obj/HTSequencingLib.o ./obj/GSCALib.o ./obj/texgenome_buildkeywordprofile.o -lm


g++ -O3 -m64 -o ./bin/tablesorter ./cpp/tablesorter.cpp
g++ -O3 -m64 -o ./bin/tablesorter_str ./cpp/tablesorter_str.cpp
g++ -g  -Wall -o ./bin/region_overlap ./cpp/region_overlap.cpp