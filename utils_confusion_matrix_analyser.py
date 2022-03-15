import numpy as np
import pandas as pd
import ast
import matplotlib.pyplot as plt
from sklearn.metrics import auc
from math import sqrt # np.sqrt has limitations

def extract_conf_matrix(x):
    ''' Retrieve the tn, fp, fn and tp from a dictionary (saved as string) '''
    # The dicts are saves as strings, so need to be converted 
    x = ast.literal_eval(x) 
    return x['tn'], x['fp'], x['fn'], x['tp']


# The following formulas are taken from https://en.wikipedia.org/wiki/Confusion_matrix
def TPR(x):
    ''' Calculate TPR'''
    TN, FP, FN, TP = extract_conf_matrix(x)
    if TP+FN == 0:
        return 0
    return TP/(TP+FN)
    
def TNR(x):
    ''' Calculate TNR'''
    TN, FP, FN, TP = extract_conf_matrix(x)
    if TN+FP == 0:
        return 0
    return TN/(TN+FP)

def PPV(x):
    ''' Calculate PPV'''
    TN, FP, FN, TP = extract_conf_matrix(x)
    if TP+FP == 0:
        return 0
    return TP/(TP+FP)

def NPV(x):
    ''' Calculate NPV'''
    TN, FP, FN, TP = extract_conf_matrix(x)
    if TN+FN == 0:
        return 0
    return TN/(TN+FN)

def FNR(x):
    ''' Calculate FNR'''
    return 1 - TPR(x)

def FPR(x):
    '''Calculate FPR'''
    return 1 - TNR(x)

def FDR(x):
    ''' Calculate FDR '''
    return 1 - PPV(x)

def FOR(x):
    ''' Calculate FOR '''
    return 1 - NPV(x)

def PT(x):
    ''' Calculate PT '''
    t = sqrt(TPR(x)*(-TNR(x)+1))+TNR(x)-1
    n = TPR(x)+TNR(x)-1
    return t/n

def TS(x):
    ''' Calculate TS '''
    TN, FP, FN, TP = extract_conf_matrix(x)
    return TP/(TP+FN+FP)

def ACC(x):
    ''' Calculate ACC '''
    TN, FP, FN, TP = extract_conf_matrix(x)
    return (TP+TN)/(TP+TN+FP+FN)

def BA(x):
    ''' Calculate BM '''
    return (TPR(x)+TNR(x))/2

def F1(x):
    ''' Calculate F1 '''
    TN, FP, FN, TP = extract_conf_matrix(x)
    return (2*TP)/(2*TP+FP+FN)

def MCC(x):
    ''' Calculate MCC '''
    TN, FP, FN, TP = extract_conf_matrix(x)
    t = TP*TN-FP*FN
    n = sqrt(float((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)))
    
def FM(x):
    ''' Calculate FM '''
    return sqrt(PPV(x)*TPR(x))

def BM(x):
    ''' Calculate BM '''
    return TPR(x)+TNR(x)-1

def MK(x):
    ''' Calculate MK '''
    return PPV(x)+NPV(x)-1

def create_measurements(edge_algorithm, measurement):
    ''' Apply a measurement (e.g. F1) to an edge algorithm'''
    df = pd.read_csv(f'confusion_matrices/{edge_algorithm}_measures.csv')

    # Drop columns with no confusion matrixes
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.loc[:, ~df.columns.str.contains('Image number name')]
    return df.apply(np.vectorize(measurement))

def plot_ROC_algorithms(list_algorithms, pretty_names):
    ''' Plot a ROC curve and return the ROC AUCs '''
    auc_dict = dict()
    
    # setup plot details
    plt.figure(figsize=(7, 8))
    
    for edge_detector, pretty_name in zip(list_algorithms, pretty_names):
        if len(pd.read_csv(f'confusion_matrices/{edge_detector}_measures.csv').index) != 28800:
            raise Exception(f"The number of rows is incorrect, for {pretty_name}")
        df_temp_FPR = create_measurements(edge_detector, FPR) # x fall-out or false positive rate (FPR)
        df_temp_TPR = create_measurements(edge_detector, TPR) # y sensitivity, recall, hit rate, or true positive rate (TPR)

        # Plot for edge detector
        FPR_list = [np.mean(df_temp_FPR[column]) for column in df_temp_FPR] # x
        TPR_list = [np.mean(df_temp_TPR[column]) for column in df_temp_TPR] # y
        
        temp_auc_val = auc(FPR_list, TPR_list)
        plt.plot(FPR_list, TPR_list, label=f'{pretty_name}, AUC: {temp_auc_val:.4f}')
        auc_dict[edge_detector] = temp_auc_val
        print(f'{pretty_name} is done, AUC={temp_auc_val}', end=", ")
    

    plt.xlabel('False positives')
    plt.ylabel('True positives')
    plt.legend()
    plt.show()
    return auc_dict