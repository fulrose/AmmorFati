import numpy as np
import math
import subprocess

dataPath = '/home/coala/Documents/myData/'
treat = 'Treat_chr1_myTest.bed'
control = 'Control_chr1_myTest.bed'
swemblPath = '/home/coala/Documents/swembl/'

import pandas as pd

def file_read(job_id):
    label = pd.read_csv('labeled_0912', sep='\t', header=None)

    tmp_file = open('swembl_test', 'r')
    swembl_result = open('swembl_result', 'w')

    lines = tmp_file.readlines()
    for line in lines:
        if line[0] == 'c':
            swembl_result.write(line)
    tmp_file.close()
    swembl_result.close()

    label = pd.read_csv('labeled_0912', sep='\t', header=None)
    result = pd.read_csv('swembl_result', sep='\t', header=None)

    label.columns = ['a', 'start', 'end', 'label']
    result.columns = ['Region', 'start', 'End', 'Count', 'Length', 'Unique pos.', 'Score', 'Ref. count', 'Max. Coverage', 'Summit', 'P value']

    label = label.drop(['a'], axis=1)
    result = result.drop(['Region', 'Count', 'Length', 'Unique pos.', 'Score', 'Ref. count', 'Max. Coverage', 'Summit', 'P value'], axis=1)

    print(result)

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

                res += (get_min(arr_label[j][1], arr_result[i][1]) - get_max(arr_label[j][0], arr_result[i][0]))

            elif flag_start:
                break

    return res


def error_rate(job_id):
    arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength = file_read(job_id)
    peak_score = get_my_score('peak', arr_peak, arr_noPeak, arr_result)
    nopeak_score = get_my_score('noPeak', arr_peak, arr_noPeak, arr_result)
    print('peak(result) - peak(label) matched: ', peak_score, ' /  peak(result) - noPeak(label) matched: ', nopeak_score)
    print('totalPeakLength: ', totalPeakLength, '  /  totalNoPeakLength: ', totalNoPeakLength)
    print('peakScore: ', peak_score / float(totalPeakLength), '  /  noPeakScore: ', nopeak_score / float(totalNoPeakLength))

    rate = (peak_score / float(totalPeakLength)) - (nopeak_score / float(totalNoPeakLength))
    return 1 - rate


def swembl(job_id, f, x, m):

    frag_length = f[0]
    penalty_ref = x[0]
    min_readCnt = m[0]

    # cmd = 'macs2 callpeak -t ' + dataPath + treat + ' -c ' + dataPath + control + ' --broad -f BAM -g hs -n test'
    cmd = swemblPath + 'SWEMBL -i ' + dataPath + treat + ' -r ' + dataPath + control + ' -B -o swembl_test'
    cmd += ' -f ' + str(frag_length)
    cmd += ' -x ' + str(penalty_ref)
    cmd += ' -m ' + str(min_readCnt)

    subprocess.check_output(cmd, shell=True)

    caculated_rate = error_rate(job_id)
    # caculated_rate = 0.5

    print 'Result = %f' % caculated_rate
    #time.sleep(np.random.randint(60))
    return caculated_rate

# Write a function like this called 'main'
def main(job_id, params):
    print 'Anything printed here will end up in the output directory for job #%d' % job_id
    print params
    return swembl(job_id, params['f'], params['x'], params['m'])
