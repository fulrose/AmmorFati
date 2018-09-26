import pandas as pd

from spearmint.utils.database.mongodb import MongoDB
from spearmint.main import load_jobs

# tool_name: 'macs2', 'cisgenome', 'swembl', 'sicer'
def get_optimized_params(tool_name):
    # Database connection
    db = MongoDB(database_address='localhost')
    if not(tool_name == 'macs2' or tool_name == 'cisgenome' or tool_name == 'swembl' or tool_name == 'sicer'):
        dic = {}
        print('incorrect tool name')
        return dic

    jobs = load_jobs(db, tool_name + '_test')

    df = pd.DataFrame()

    # params names of each tools
    macs2_params = ['q', 'm_s', 'm_d']
    cisgenome_params = ['b', 'e', 'w']
    swembl_params = ['x', 'm', 'f']
    sicer_params = ['fs', 'gs', 'w']

    if tool_name == 'macs2':
        params = macs2_params
    elif tool_name == 'cisgenome':
        params = cisgenome_params
    elif tool_name == 'swembl':
        params = swembl_params
    elif tool_name == 'sicer':
        params = sicer_params

    # dict
    res = {}

    for job in jobs:
        df = df.append({params[0]: float(job['params'][params[0]]['values']), params[1]: float(job['params'][params[1]]['values']),
                        params[2]: float(job['params'][params[2]]['values']), 'error_rate': float(job['values']['branin'])}, ignore_index=True)

    df = df.sort_values('error_rate').reset_index(drop=True)

    # print(df)
    #df = df.drop('error_rate', axis=1)

    column_list = df.columns
    for column in column_list:
        res[column] = df[0:1][column][0]
        # print(df[0:1][column][0])

    # return dictionary of params
    return res

print(get_optimized_params('macs2'))
print(get_optimized_params('cisgenome'))
print(get_optimized_params('swembl'))
print(get_optimized_params('sicer'))
