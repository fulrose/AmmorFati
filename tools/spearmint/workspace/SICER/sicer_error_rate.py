import pandas as pd

def file_read():
    label = pd.read_csv('/_Graduate/errorRate/entire_label_88mb', sep='\t', header=None)
    result = pd.read_csv('/_Graduate/errorRate/island-summary.bed', sep='\t', header=None)

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


def error_rate():
    arr_peak, arr_noPeak, arr_result, totalPeakLength, totalNoPeakLength = file_read()
    peak_score = get_my_score('peak', arr_peak, arr_noPeak, arr_result)
    nopeak_score = get_my_score('noPeak', arr_peak, arr_noPeak, arr_result)
    print('peak(result) - peak(label) matched: ', peak_score, ' /  peak(result) - noPeak(label) matched: ', nopeak_score)
    print('totalPeakLength: ', totalPeakLength, '  /  totalNoPeakLength: ', totalNoPeakLength)
    print('peakScore: ', peak_score / float(totalPeakLength), '  /  noPeakScore: ', nopeak_score / float(totalNoPeakLength))
    return 1 - ((peak_score / float(totalPeakLength)) - (nopeak_score / float(totalNoPeakLength)))

#print('totalPeakLength: ', totalPeakLength, ' /  totalNoPeakLength: ', totalNoPeakLength)
print('score: ', error_rate())
#print(totalPeakLength, totalNoPeakLength, totalNoSeeLength, totalAmbiguousLength)
