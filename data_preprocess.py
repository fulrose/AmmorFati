import sys
import subprocess

argc = len(sys.argv)

treat           = sys.argv[1]
control         = sys.argv[2]
bamPath         = sys.argv[3]
cisgenomePath   = sys.argv[4]

print '----------------------------------------'
print 'Data Preprocessing'
print '----------------------------------------'
print 'Treat file : ', treat
print 'Control file :', control
print '----------------------------------------'
print ''

try:
    #Treat file processing
    print 'Filtering(slicing) the Treat file...'

    cmd_filter = bamPath + 'bamtools filter'
    cmd_filter += ' -in '      + treat  
    cmd_filter += ' -out '     + treat[:-4] + '_filtered.bam'
    cmd_filter += ' -region '  + 'chr1:40000000..41000000'

    #print cmd_filter
    output = subprocess.call(cmd_filter, shell=True)

    print ''

    if (output != 0) :
        raise exception('Treat filtering error..')

    print 'Convert the bam to bed...'
    cmd_convert = bamPath + 'bamtools convert'
    cmd_convert += ' -format ' + 'bed'  
    cmd_convert += ' -in '  + treat[:-4] + '_filtered.bam'
    cmd_convert += ' -out ' + treat[:-4] + '_filtered.bed'
    
    #print cmd_convert
    output = subprocess.call(cmd_convert, shell=True)

    if (output != 0) :
        raise exception('Treat converting error..')

    print ''
    print 'Treat is Done !!'
    print '----------------------------------------'
    print ''

    #Control file processing
    print 'Filtering(slicing) the Control file...'

    cmd_filter = bamPath + 'bamtools filter'
    cmd_filter += ' -in '      + control  
    cmd_filter += ' -out '     + control[:-4] + '_filtered.bam'
    cmd_filter += ' -region '  + 'chr1:40000000..41000000'

    #print cmd_filter
    output = subprocess.call(cmd_filter, shell=True)

    print ''

    if (output != 0) :
        raise exception('Control filtering error..')

    print 'Convert the bam to bed...'
    cmd_convert = bamPath + 'bamtools convert'
    cmd_convert += ' -format ' + 'bed'  
    cmd_convert += ' -in '  + control[:-4] + '_filtered.bam'
    cmd_convert += ' -out ' + control[:-4] + '_filtered.bed'
    
    #print cmd_convert
    output = subprocess.call(cmd_convert, shell=True)

    if (output != 0) :
        raise exception('Control converting error..')
    print ''
    print 'Control is Done !!'
    print '----------------------------------------'
    print 'Generate aln for cisgenome...'

    cmd_bed2aln = cisgenomePath + 'file_bed2aln'
    cmd_bed2aln += ' -i ' + treat[:-4] + '_filtered.bed'
    cmd_bed2aln += ' -o ' + treat[:-4] + '_filtered.aln'

    output = subprocess.call(cmd_bed2aln, shell=True)
    
    if (output != 0) :
        raise exception('Treat aln generating error..')

    cmd_bed2aln = cisgenomePath + 'file_bed2aln'
    cmd_bed2aln += ' -i ' + control[:-4] + '_filtered.bed'
    cmd_bed2aln += ' -o ' + control[:-4] + '_filtered.aln'

    output = subprocess.call(cmd_bed2aln, shell=True)
 
    if (output != 0) :
        raise exception('Control aln generating error..')
  
    print 'Generating aln is done !!'
    print '----------------------------------------'
    print ''
except Exception as e:
    print 'Error: ', e
    sys.exit()

finally:
    print 'BAM done!'


