import sys
import subprocess
import os

def convert_region(string):
    sp = string.split('_')

    for i in range(1, 4):
        sp[i] = sp[i].replace('K', '000')
        sp[i] = sp[i].replace('M', '000000')
        sp[i] = sp[i].replace('B', '000000000')

    return sp[1] + ':' + sp[2] + ".." + sp[3]

treat           = sys.argv[1]
control         = sys.argv[2]
bamPath         = sys.argv[3]
chipPath        = sys.argv[4]
train_region    = sys.argv[5]
test_region     = sys.argv[6]
cisgenomePath   = os.getenv('CISGENOMEPATH')

print 'Data Preprocessing'
print '----------------------------------------'
print 'Treat file : ', treat
print 'Control file :', control

print 'Train labeled data region : ',convert_region(train_region)
print 'Test labeled data region : ', convert_region(test_region)
print '----------------------------------------'
print ''

try:
    #Treat file processing
    print 'Filtering(slicing) the Treat file about train region...'

    cmd_filter = bamPath + 'bamtools filter'
    cmd_filter += ' -in '     + treat
    cmd_filter += ' -out '    + treat[:-4] + '_filtered_train.bam'
    #cmd_filter += ' -region ' + train_chrNum + ':' + str(train_chrStart) + '..' + str(train_chrEnd)
    cmd_filter += ' -region ' + convert_region(train_region)

    #print cmd_filter
    output = subprocess.call(cmd_filter, shell=True)

    print ''

    if (output != 0) :
        raise exception('Treat filtering error..')

    print 'Filtering(slicing) the Treat file about test region...'

    cmd_filter = bamPath + 'bamtools filter'
    cmd_filter += ' -in '     + treat
    cmd_filter += ' -out '    + treat[:-4] + '_filtered_test.bam'
    #cmd_filter += ' -region ' + train_chrNum + ':' + str(train_chrStart) + '..' + str(train_chrEnd)
    cmd_filter += ' -region ' + convert_region(test_region)

    #print cmd_filter
    output = subprocess.call(cmd_filter, shell=True)

    print ''

    if (output != 0) :
        raise exception('Treat filtering error..')

    print 'Convert treat_train the bam to bed...'
    cmd_convert = bamPath + 'bamtools convert'
    cmd_convert += ' -format ' + 'bed'
    cmd_convert += ' -in '  + treat[:-4] + '_filtered_train.bam'
    cmd_convert += ' -out ' + treat[:-4] + '_filtered_train.bed'

    #print cmd_convert
    output = subprocess.call(cmd_convert, shell=True)
    print ''

    if (output != 0) :
        raise exception('Treat converting error..')

    print 'Convert treat_test the bam to bed...'
    cmd_convert = bamPath + 'bamtools convert'
    cmd_convert += ' -format ' + 'bed'
    cmd_convert += ' -in '  + treat[:-4] + '_filtered_test.bam'
    cmd_convert += ' -out ' + treat[:-4] + '_filtered_test.bed'

    #print cmd_convert
    output = subprocess.call(cmd_convert, shell=True)

    if (output != 0) :
        raise exception('Treat converting error..')

    print ''
    print 'Treat is Done !!'
    print '----------------------------------------'
    print ''

    #Control file processing
    print 'Filtering(slicing) the Control file about train region...'

    cmd_filter = bamPath + 'bamtools filter'
    cmd_filter += ' -in '     + control
    cmd_filter += ' -out '    + control[:-4] + '_filtered_train.bam'
    #cmd_filter += ' -region ' + train_chrNum + ':' + str(train_chrStart) + '..' + str(train_chrEnd)
    cmd_filter += ' -region ' + convert_region(train_region)

    #print cmd_filter
    output = subprocess.call(cmd_filter, shell=True)

    print ''

    if (output != 0) :
        raise exception('Control filtering error..')

    print 'Filtering(slicing) the Control file about test region...'

    cmd_filter = bamPath + 'bamtools filter'
    cmd_filter += ' -in '     + control
    cmd_filter += ' -out '    + control[:-4] + '_filtered_test.bam'
    #cmd_filter += ' -region ' + train_chrNum + ':' + str(train_chrStart) + '..' + str(train_chrEnd)
    cmd_filter += ' -region ' + convert_region(test_region)

    #print cmd_filter
    output = subprocess.call(cmd_filter, shell=True)

    print ''

    if (output != 0) :
        raise exception('Control filtering error..')

    print 'Convert control_train the bam to bed...'
    cmd_convert = bamPath + 'bamtools convert'
    cmd_convert += ' -format ' + 'bed'
    cmd_convert += ' -in '  + control[:-4] + '_filtered_train.bam'
    cmd_convert += ' -out ' + control[:-4] + '_filtered_train.bed'

    #print cmd_convert
    output = subprocess.call(cmd_convert, shell=True)
    print ''

    if (output != 0) :
        raise exception('Control converting error..')

    print 'Convert control_test the bam to bed...'
    cmd_convert = bamPath + 'bamtools convert'
    cmd_convert += ' -format ' + 'bed'
    cmd_convert += ' -in '  + control[:-4] + '_filtered_test.bam'
    cmd_convert += ' -out ' + control[:-4] + '_filtered_test.bed'

    #print cmd_convert
    output = subprocess.call(cmd_convert, shell=True)

    if (output != 0) :
        raise exception('Treat converting error..')

    print ''
    print 'Control is Done !!'
    print '----------------------------------------'
    print ''

    print '----------------------------------------'
    print 'Generate aln for cisgenome...'
    print cisgenomePath

    cmd_bed2aln = cisgenomePath + 'file_bed2aln'
    cmd_bed2aln += ' -i ' + treat[:-4] + '_filtered_train.bed'
    cmd_bed2aln += ' -o ' + treat[:-4] + '_filtered_train.aln'

    print cmd_bed2aln

    output = subprocess.call(cmd_bed2aln, shell=True)

    if (output != 0) :
        raise exception('Treat aln generating error..')

    cmd_bed2aln = cisgenomePath + 'file_bed2aln'
    cmd_bed2aln += ' -i ' + control[:-4] + '_filtered_train.bed'
    cmd_bed2aln += ' -o ' + control[:-4] + '_filtered_train.aln'

    output = subprocess.call(cmd_bed2aln, shell=True)

    if (output != 0) :
        raise exception('Control aln generating error..')

    cmd_bed2aln = cisgenomePath + 'file_bed2aln'
    cmd_bed2aln += ' -i ' + treat[:-4] + '_filtered_test.bed'
    cmd_bed2aln += ' -o ' + treat[:-4] + '_filtered_test.aln'

    output = subprocess.call(cmd_bed2aln, shell=True)

    if (output != 0) :
        raise exception('Treat aln generating error..')

    cmd_bed2aln = cisgenomePath + 'file_bed2aln'
    cmd_bed2aln += ' -i ' + control[:-4] + '_filtered_test.bed'
    cmd_bed2aln += ' -o ' + control[:-4] + '_filtered_test.aln'

    output = subprocess.call(cmd_bed2aln, shell=True)

    if (output != 0) :
        raise exception('Control aln generating error..')


    cmd_filelist = 'echo "'
    cmd_filelist += control[:-4] + '_filtered_train.bed\t0\n'
    cmd_filelist += treat[:-4] + '_filtered_train.bed\t1"'
    cmd_filelist += ' > ' + chipPath + 'cisgenome_train_list.txt'

    output = subprocess.call(cmd_filelist, shell=True)

    cmd_filelist = 'echo "'
    cmd_filelist += control[:-4] + '_filtered_test.bed\t0\n'
    cmd_filelist += treat[:-4] + '_filtered_test.bed\t1"'
    cmd_filelist += ' > ' + chipPath + 'cisgenome_test_list.txt'

    output = subprocess.call(cmd_filelist, shell=True)

    print 'Generating aln is done !!'
    print '----------------------------------------'
    print ''
except Exception as e:
    print 'Error: ', e
    sys.exit()

finally:
    print 'BAM done!'
