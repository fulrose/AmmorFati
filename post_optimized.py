import os
import sys
import subprocess

#from AmmorFati.spearmint.spearmint.get_hyper import get_optimized_params

treat_test_bam      = os.getenv('treat_test_bam')
control_test_bam    = os.getenv('control_test_bam')
treat_test_bed      = os.getenv('treat_test_bed')
control_test_bed    = os.getenv('control_test_bed')
CISGENOMELIST       = os.getenv('cisgenome_test_list')
testLabeled         = os.getenv('testLabeled')

MACS2PATH = os.getenv('MACS2PATH')
SWEMBLPATH = os.getenv('SWEMBLPATH')
SICERPATH = os.getenv('SICERPATH')
CISGENOMEPATH = os.getenv('CISGENOMEPATH')

SPEARMINTPATH = os.getenv('SPEARMINTPATH')


import pandas as pd

def macs_file_read():
    label = pd.read_csv(testLabeled, sep='\t', header=None)
    result = pd.read_csv('./temp/macs/optimized_peaks.narrowPeak', sep='\t', header=None)

    label.columns = ['a', 'start', 'end', 'label']
    result.columns = ['chr', 'start', 'end', 'dummy1', 'dummy2', 'dummy3', 'dummy4', 'dummy5', 'dummy6', 'dummy7']

    label = label.drop(['a'], axis=1)
    result = result.drop(['chr', 'dummy1', 'dummy2', 'dummy3', 'dummy4', 'dummy5', 'dummy6', 'dummy7'], axis=1)

    # print(result)

    label_peak = pd.DataFrame(columns=['start', 'end'])
    label_noPeak = pd.DataFrame(columns=['start', 'end'])

    totalNoSeeLength = 0
    totalLength = 0
    totalPeakLength = 0
    totalNoPeakLength = 0
    totalAmbiguousLength = 0

    for row_num, row in label.iterrows():
        if row['label'] == 'peak':
            label_peak = label_peak.append({'start': row['start'], 'end': row['end']}, ignore_index=True)
            totalPeakLength += (row['end'] - row['start'])
        elif row['label'] == 'noPeak':
            label_noPeak = label_noPeak.append({'start': row['start'], 'end': row['end']}, ignore_index=True)
            totalNoPeakLength += (row['end'] - row['start'])
        else:
            totalNoSeeLength += (row['end'] - row['start'])

        if row_num == 0:
            totalLength = -row['start']
        elif row_num == len(label) - 1:
            totalLength += row['end']

    totalAmbiguousLength = totalLength - totalPeakLength - totalNoSeeLength
    arr_peak = label_peak.values
    arr_noPeak = label_noPeak.values
    arr_result = result.values

    return arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength

def cisgenome_file_read():
    label = pd.read_csv(testLabeled, sep='\t', header=None)
    result = pd.read_csv('./temp/cisgenome/optimized_peak.cod', sep='\t', header=0)

    label.columns = ['a', 'start', 'end', 'label']

    label = label.drop(['a'], axis=1)
    result = result.drop(['#rank','chromosome','strand','peak_length','FDR','left_peakboundary','right_peakboundary','peak_summit',
                          'bound_center','bound_width','maxT','maxT_pos','max_log2FC','maxFC_pos','minuslog10_minPoisP','minPoisP_pos'], axis=1)


    label_peak = pd.DataFrame(columns=['start', 'end'])
    label_noPeak = pd.DataFrame(columns=['start', 'end'])

    totalNoSeeLength = 0
    totalLength = 0
    totalPeakLength = 0
    totalNoPeakLength = 0
    totalAmbiguousLength = 0

    for row_num, row in label.iterrows():
        if row['label'] == 'peak':
            label_peak = label_peak.append({'start': row['start'], 'end': row['end']}, ignore_index=True)
            totalPeakLength += (row['end'] - row['start'])
        elif row['label'] == 'noPeak':
            label_noPeak = label_noPeak.append({'start': row['start'], 'end': row['end']}, ignore_index=True)
            totalNoPeakLength += (row['end'] - row['start'])
        else:
            totalNoSeeLength += (row['end'] - row['start'])

        if row_num == 0:
            totalLength = -row['start']
        elif row_num == len(label) - 1:
            totalLength += row['end']

    totalAmbiguousLength = totalLength - totalPeakLength - totalNoSeeLength
    arr_peak = label_peak.values
    arr_noPeak = label_noPeak.values
    arr_result = result.values

    return arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength

def swembl_file_read():
    label = pd.read_csv(testLabeled, sep='\t', header=None)
    result = pd.DataFrame(columns=["start", "end"])
    tmp_file = open('./temp/swembl/optimized.bed', 'r')

    lines = tmp_file.readlines()
    for line in lines:
        if line[0] == 'c':
            list_ = line.split()
            result = result.append({'start': int(list_[1]), 'end': int(list_[2])}, ignore_index=True)
    tmp_file.close()

    label.columns = ['a', 'start', 'end', 'label']
    label = label.drop(['a'], axis=1)

    label_peak = pd.DataFrame(columns=['start', 'end'])
    label_noPeak = pd.DataFrame(columns=['start', 'end'])

    totalNoSeeLength = 0
    totalLength = 0
    totalPeakLength = 0
    totalNoPeakLength = 0
    totalAmbiguousLength = 0

    for row_num, row in label.iterrows():
        if row['label'] == 'peak':
            label_peak = label_peak.append({'start': row['start'], 'end': row['end']}, ignore_index=True)
            totalPeakLength += (row['end'] - row['start'])
        elif row['label'] == 'noPeak':
            label_noPeak = label_noPeak.append({'start': row['start'], 'end': row['end']}, ignore_index=True)
            totalNoPeakLength += (row['end'] - row['start'])
        else:
            totalNoSeeLength += (row['end'] - row['start'])

        if row_num == 0:
            totalLength = -row['start']
        elif row_num == len(label) - 1:
            totalLength += row['end']

    totalAmbiguousLength = totalLength - totalPeakLength - totalNoSeeLength
    arr_peak = label_peak.values
    arr_noPeak = label_noPeak.values
    arr_result = result.values

    return arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength

def sicer_file_read():
    label = pd.read_csv(testLabeled, sep='\t', header=None)
    result = pd.read_csv('./temp/sicer/optimized.bed', sep='\t', header=None)

    label.columns = ['a', 'start', 'end', 'label']
    result.columns = ['chr', 'start', 'end', 'dummy1', 'dummy2', 'dummy3', 'dummy4', 'dummy5']

    label = label.drop(['a'], axis=1)
    result = result.drop(['chr', 'dummy1', 'dummy2', 'dummy3', 'dummy4', 'dummy5'], axis=1)

    # print(result)

    label_peak = pd.DataFrame(columns=['start', 'end'])
    label_noPeak = pd.DataFrame(columns=['start', 'end'])

    totalNoSeeLength = 0
    totalLength = 0
    totalPeakLength = 0
    totalNoPeakLength = 0
    totalAmbiguousLength = 0

    for row_num, row in label.iterrows():
        if row['label'] == 'peak':
            label_peak = label_peak.append({'start': row['start'], 'end': row['end']}, ignore_index=True)
            totalPeakLength += (row['end'] - row['start'])
        elif row['label'] == 'noPeak':
            label_noPeak = label_noPeak.append({'start': row['start'], 'end': row['end']}, ignore_index=True)
            totalNoPeakLength += (row['end'] - row['start'])
        else:
            totalNoSeeLength += (row['end'] - row['start'])

        if row_num == 0:
            totalLength = -row['start']
        elif row_num == len(label) - 1:
            totalLength += row['end']

    totalAmbiguousLength = totalLength - totalPeakLength - totalNoSeeLength
    arr_peak = label_peak.values
    arr_noPeak = label_noPeak.values
    arr_result = result.values

    return arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength

def is_overlap(label_start, label_end, result_start, result_end):
    if (label_start < result_end < label_end or label_start < result_start < label_end or
            result_start < label_end < result_end or result_start < label_start < result_end):
        return True
    else:
        return False

def get_min(a, b):
    return b if a > b else a

def get_max(a, b):
    return a if a > b else b

def get_my_score(_label, arr_peak, arr_noPeak, arr_result):
    if _label == 'peak':
        arr_label = arr_peak
    else:
        arr_label = arr_noPeak

    label_length = len(arr_label)
    result_length = len(arr_result)

    res = 0

    for i in range(result_length):
        flag_start = False
        for j in range(label_length):
            if is_overlap(arr_label[j][0], arr_label[j][1], arr_result[i][0], arr_result[i][1]):
                if not flag_start:
                    flag_start = True

                overlap_start = get_max(arr_label[j][0], arr_result[i][0])
                overlap_end = get_min(arr_label[j][1], arr_result[i][1])
                overlap_ratio = float(overlap_end - overlap_start) / float(arr_label[j][1] - arr_label[j][0])

                if _label == 'peak':
                    if 0.3 <= overlap_ratio < 0.5:
                        res += int((arr_label[j][1] - arr_label[j][0]) * 0.6)
                    elif 0.5 <= overlap_ratio < 0.7:
                        res += int((arr_label[j][1] - arr_label[j][0]) * 0.8)
                    elif overlap_ratio >= 0.7:
                        res += (arr_label[j][1] - arr_label[j][0])
                    else:
                        res += (get_min(arr_label[j][1], arr_result[i][1]) - get_max(arr_label[j][0], arr_result[i][0]))
                else:
                    res += (get_min(arr_label[j][1], arr_result[i][1]) - get_max(arr_label[j][0], arr_result[i][0]))

            elif flag_start:
                break

    return res

#####################################################################################################################
def all_tool_error_rate():
    res = {}

    arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength = macs_file_read()
    peak_score = get_my_score('peak', arr_peak, arr_noPeak, arr_result)
    nopeak_score = get_my_score('noPeak', arr_peak, arr_noPeak, arr_result)
    res['macs_error_rate'] = 1 - ((peak_score / float(totalPeakLength)) - (nopeak_score / float(totalNoPeakLength)))

    arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength = cisgenome_file_read()
    peak_score = get_my_score('peak', arr_peak, arr_noPeak, arr_result)
    nopeak_score = get_my_score('noPeak', arr_peak, arr_noPeak, arr_result)
    res['cisgenome_error_rate'] = 1 - ((peak_score / float(totalPeakLength)) - (nopeak_score / float(totalNoPeakLength)))

    arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength = swembl_file_read()
    peak_score = get_my_score('peak', arr_peak, arr_noPeak, arr_result)
    nopeak_score = get_my_score('noPeak', arr_peak, arr_noPeak, arr_result)
    res['swembl_error_rate'] = 1 - ((peak_score / float(totalPeakLength)) - (nopeak_score / float(totalNoPeakLength)))

    arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength = sicer_file_read()
    peak_score = get_my_score('peak', arr_peak, arr_noPeak, arr_result)
    nopeak_score = get_my_score('noPeak', arr_peak, arr_noPeak, arr_result)
    res['sicer_error_rate'] = 1 - ((peak_score / float(totalPeakLength)) - (nopeak_score / float(totalNoPeakLength)))

    return res

import json

cmd = 'python ' + SPEARMINTPATH + 'get_hyper.py'
output = subprocess.check_output(cmd, shell=True)

res = json.loads(output)


macs_params = res['macs']
q_value = macs_params['q'] #float
mfold_start = int(float(macs_params['m_s'])) #int
mfold_delta = int(float(macs_params['m_d'])) #int

sicer_params = res['sicer']
genome_size = sicer_params['gs'] #float
window_size = int(float(sicer_params['w'])) #int
frag_size = int(float(sicer_params['fs'])) #int

swembl_params = res['swembl']
frag_length = int(float(swembl_params['f'])) # int
penalty_ref = swembl_params['x'] #float
min_readCnt = int(float(swembl_params['m'])) #int

cisgenome_params = res['cisgenome']
binSize = int(float(cisgenome_params['b'])) #int
windowSize = int(float(cisgenome_params['w'])) #int
ext_length = int(float(cisgenome_params['e'])) #int

print 'macs : ', macs_params
print 'sicer : ', sicer_params
print 'swembl : ', swembl_params
print 'cisgenome: ',cisgenome_params

# MACS
cmd = MACS2PATH + 'macs2 callpeak'
cmd += ' -t ' + treat_test_bam
cmd += ' -c ' + control_test_bam
cmd += ' --outdir ./temp/macs/'
cmd += ' -f BAM '
cmd += ' -g hs'
cmd += ' -n optimized'
cmd += ' -q ' + str(q_value)
cmd += ' -m ' + str(mfold_start) + ' ' + str(mfold_start + mfold_delta)

output = subprocess.call(cmd, shell=True)

# SICER
cmd = 'python2 ' + SICERPATH + 'SICER.py'
cmd += ' -t '   + treat_test_bam
cmd += ' -c '   + control_test_bam
cmd += ' -gs '  + str(genome_size)
cmd += ' -w '   + str(window_size)
cmd += ' -fs '  + str(frag_size)
cmd += ' > '    + './temp/sicer/optimized.bed'

output = subprocess.call(cmd, shell=True)

# SWEMBL
cmd = SWEMBLPATH + 'SWEMBL'
cmd += ' -i ' + treat_test_bed
cmd += ' -r ' + control_test_bed
cmd += ' -B '
cmd += ' -o ' + './temp/swembl/optimized.bed'
cmd += ' -f ' + str(frag_length)
cmd += ' -x ' + str(penalty_ref)
cmd += ' -m ' + str(min_readCnt)

output = subprocess.call(cmd, shell=True)

# CISGENOME
cmd = CISGENOMEPATH + 'seqpeak'
cmd += ' -i ' + CISGENOMELIST
cmd += ' -d ./temp/cisgenome/'
cmd += ' -o optimized'
cmd += ' -b ' + str(binSize)
cmd += ' -w ' + str(windowSize)
cmd += ' -e ' + str(ext_length)

output = subprocess.call(cmd, shell=True)

# LOG
cmd = 'echo "'
cmd += str(all_tool_error_rate()) + '\n\n'
cmd += 'macs optimized param: ' + str(macs_params) + '\n'
cmd += 'sicer optimized param: ' + str(sicer_params) + '\n'
cmd += 'swembl optimized param: ' + str(swembl_params) + '\n'
cmd += 'cisgenome optimized param: ' + str(cisgenome_params) + '\n'
cmd += '" > post_optimized.log'

output = subprocess.call(cmd, shell=True)



print all_tool_error_rate()
