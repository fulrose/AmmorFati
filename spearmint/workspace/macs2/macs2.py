import numpy as np
import math
import subprocess
import os

#dataPath = '/home/coala/Documents/myData/'
#treat = 'Treat_chr1_myTest.bam'
#control = 'Control_chr1_myTest.bam'

treat = os.getenv('treat_bam')
control = os.getenv('control_bam')
labeledData = os.getenv('myLabeled')
MACS2PATH  = os.getenv('MACS2PATH')

import pandas as pd

def file_read(job_id):
    f_name = './temp/test' + str(job_id) + '_peaks.broadPeak'

    label = pd.read_csv(labeledData, sep='\t', header=None)
    result = pd.read_csv(f_name, sep='\t', header=None)

    label.columns = ['a', 'start', 'end', 'label']
    result.columns = ['chr', 'start', 'end', 'score', 'dummy1', 'dummy2', 'dummy3', 'dummy4', 'dummy5']

    label = label.drop(['a'], axis=1)
    result = result.drop(['chr', 'score', 'dummy1', 'dummy2', 'dummy3', 'dummy4', 'dummy5'], axis=1)

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


def macs2(job_id, q, m_min, m_max):

    q_value = q[0]
    mfold_min = m_min[0]
    mfold_max = m_max[0]

    cmd = MACS2PATH + 'macs2 callpeak' 
    cmd += ' -t ' + treat
    cmd += ' -c ' + control
    cmd += ' --outdir ./temp' 
    cmd += ' --broad '
    cmd += ' -f BAM '
    cmd += ' -g hs'
    cmd += ' -n test' + str(job_id)
    cmd += ' -q ' + str(q_value)
    cmd += ' -m ' + str(mfold_min) + ' ' + str(mfold_max)

    subprocess.check_output(cmd, shell=True)

    caculated_rate = error_rate(job_id)
    # caculated_rate = 0.5

    print(caculated_rate)
    #time.sleep(np.random.randint(60))

    cmd_rm = 'rm ./temp/test' + str(job_id) + '*'
    subprocess.check_output(cmd_rm, shell=True)

    return caculated_rate

# Write a function like this called 'main'
def main(job_id, params):
    print 'Anything printed here will end up in the output directory for job #%d' % job_id
    print params
    return macs2(job_id, params['q'], params['m_min'], params['m_max'])
