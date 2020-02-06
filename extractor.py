from openpyxl import load_workbook
import pandas as pd
from itertools import islice

def extract_batch(sheet, batchsize):

    data = sheet.values
    cols = next(data)[1:]
    data = list(data)
    idx = [r[0] for r in data]
    data = (islice(r, 1, None) for r in data)
    df = pd.DataFrame(data, index=idx, columns=cols)
    df = df.reset_index()
    df.rename(columns={'index':'length'}, inplace=True)

    df['batchsize'] = batchsize

    print(df)

    return df 

def extract_data(filename):

    wb = load_workbook(filename, data_only=True)

    df = extract_batch(wb['bs1'], 1)
    df = df.append(extract_batch(wb['bs8'], 8))
    df = df.append(extract_batch(wb['bs32'], 32))
    df = df.append(extract_batch(wb['bs64'], 64))
    df = df.append(extract_batch(wb['bs128'], 128))
    print(df)

    return df 

if __name__=='__main__':

    extract_data("v100_for_plot.xlsx")
