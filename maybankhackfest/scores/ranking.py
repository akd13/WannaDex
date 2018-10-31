
# coding: utf-8

# In[1]:


import pandas as pd
import json
import numpy as np
import os


# In[2]:


def path():
    return os.getcwd()

# API to get plain scores
def get_scores():
    df = pd.read_csv('scores/company_data.csv', na_values = ['nm','na'])
    df_extract = df[['Company Name','Sector',
                    'Dividend yld (%) FY-2','Dividend yld (%) FY-1','Dividend yld (%) FY0',
                    'Dividend yld (%) FY1','Dividend yld (%) FY2',
                    'Revenue growth FY-2','Revenue growth FY-1','Revenue growth FY0',
                    'Revenue growth FY1','Revenue growth FY2']]
    X = df_extract.values

    scores = np.zeros((len(X), 1))

    for i, datapoint in enumerate(X):
        score = sum(datapoint[2:])
        if(np.isnan(score)):
            scores[i] = -1000000
        else:
            scores[i] = score
    X = np.hstack((X,scores))
    X_extract = X[:, [0, 1, 12]]

    company_score = {}
    sector_company = {}

    for row in X_extract:
        if(row[0] not in company_score):
            company_score[row[0]] = row[2]

    for row in X_extract:
        if row[1] in sector_company:
            # append the new company to the existing sector
            sector_company[row[1]].append({row[0]:company_score[row[0]]})
        else:
            # create a new array in this slot
            sector_company[row[1]] = [{row[0]:company_score[row[0]]}]

    return json.dumps(sector_company)

def get_scores_columns(list_values):

    df = pd.read_csv("scores/company_data.csv", na_values = ['nm','na'])
    df_extract = df[['Company Name','Sector',
                    'Dividend yld (%) FY-2','Dividend yld (%) FY-1','Dividend yld (%) FY0',
                    'Dividend yld (%) FY1','Dividend yld (%) FY2',
                    'Revenue growth FY-2','Revenue growth FY-1','Revenue growth FY0',
                    'Revenue growth FY1','Revenue growth FY2']]

    X = df_extract.values

    X_nopriority_list = df[['Dividend yld (%) FY-2','Dividend yld (%) FY-1',
                            'Dividend yld (%) FY0','Dividend yld (%) FY1',
                            'Dividend yld (%) FY2','Revenue growth FY-2',
                            'Revenue growth FY-1','Revenue growth FY0',
                            'Revenue growth FY1','Revenue growth FY2']]

    X_nopriority_list = X_nopriority_list.drop(columns=list_values).values #dataframe without the priority values
    X_list = df_extract[list_values].values #dataframe with the priority values
    scores = np.zeros((len(X), 1))

    for i in range(len(X)):
        sum_priority = 2*sum(X_list[i])
        sum_no_priority = sum(X_nopriority_list[i])
        score = sum_priority+sum_no_priority
        if(np.isnan(score)):
            scores[i] = -1000000
        else:
            scores[i] = score

    X = np.hstack((X,scores))
    X_extract = X[:, [0, 1, 12]]

    company_score = {}
    sector_company = {}

    for row in X_extract:
        if(row[0] not in company_score):
            company_score[row[0]] = row[2]

    for row in X_extract:
        if row[1] in sector_company:
            # append the new company to the existing sector
            sector_company[row[1]].append({row[0]:company_score[row[0]]})
        else:
            # create a new array in this slot
            sector_company[row[1]] = [{row[0]:company_score[row[0]]}]

    return json.dumps(sector_company)


