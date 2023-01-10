import pandas as pd

def data_merge(p=True):
    account = pd.read_csv("ficheiros_competicao_dev/account.csv")
    cards = pd.read_csv("ficheiros_competicao_dev/card_dev.csv")
    clients = pd.read_csv("ficheiros_competicao_dev/client.csv")
    disps = pd.read_csv("ficheiros_competicao_dev/disp.csv")
    districts = pd.read_csv("ficheiros_competicao_dev/district.csv")
    loans = pd.read_csv("ficheiros_competicao_dev/loan_dev.csv")
    trans = pd.read_csv("ficheiros_competicao_dev/trans_dev.csv")

    dataset = account.rename({'frequency' : 'frequency_account', 'date' : 'date_of_creation'}, axis=1)

    dataset = dataset.merge(loans, how='outer') 
    dataset.drop('loan_id', inplace=True, axis=1)
    dataset = dataset.rename({'date' : 'date_of_loan', 'duration' : 'duration_loan', 'payments' : 'payments_loan', 'status' : 'status_loan'}, axis=1)

    dataset = dataset.merge(pd.DataFrame(trans.groupby('account_id').size(), columns=['n.of trans']), left_on='account_id', right_index=True, how="outer")
    dataset = dataset.merge(pd.DataFrame(trans[trans['operation']=='credit in cash'].groupby('account_id').size(), columns=['op credit cash']), right_index=True, left_on='account_id', how="outer")
    dataset = dataset.merge(pd.DataFrame(trans[trans['operation']=='credit card withdrawal'].groupby('account_id').size(), columns=['op cc withdrawal']), right_index=True, left_on='account_id', how="outer")
    dataset = dataset.merge(pd.DataFrame(trans[trans['operation']=='withdrawal in cash'].groupby('account_id').size(), columns=['op withdrawal cash']), right_index=True, left_on='account_id', how="outer")
    dataset = dataset.merge(pd.DataFrame(trans[trans['operation']=='collection from another bank'].groupby('account_id').size(), columns=['op collection bank']), right_index=True, left_on='account_id', how="outer")
    dataset = dataset.merge(pd.DataFrame(trans[trans['operation']=='remittance to another bank'].groupby('account_id').size(), columns=['op remittance bank']), right_index=True, left_on='account_id', how="outer")
    # dataset = dataset.rename({'amount_x' : 'amount_loan', 'amount_y' : 'amount_trans', 'date' : 'date_trans', 'account' : 'account partner'}, axis=1)
    dataset = dataset.merge(pd.DataFrame(trans.groupby('account_id').amount.mean()).rename(columns={'amount':'avg trans amount'}), right_index=True, left_on='account_id', how="outer")
    dataset = dataset.merge(pd.DataFrame(trans.groupby('account_id').balance.mean()).rename(columns={'balance':'avg trans balance'}), right_index=True, left_on='account_id', how="outer")

    dataset = dataset.merge(disps,  how='outer')
    dataset = dataset.rename({'type' : 'disp_type'}, axis=1)
    
    dataset = dataset.merge(cards, how='outer')
    dataset = dataset.rename({'type' : 'card_type'}, axis=1)
    dataset.drop('disp_id', inplace=True, axis=1)

    dataset = dataset.merge(clients, left_on="client_id", right_on="client_id", how='outer') 
    dataset = dataset.rename({'district_id_x' : 'district_id_account', 'district_id_y' : 'district_id_client'}, axis=1)
    dataset = dataset.merge(districts, left_on = "district_id_client", right_on="district_id", how='outer' )
    dataset.drop("district_id", inplace=True, axis=1)  

    if(p):
        print(dataset.columns.tolist())
        print(len(dataset))
        print(dataset.head())

    data_trans(districts,'no. of commited crimes \'95', 'int64')

    #aggregate loans by dispositions(client + account\)
    #aggregate dispositions by clients

    # print(df.groups)
    # print(df.first())

    return dataset

def nulls(dataset, jcolumns):
    for col in jcolumns:
        if(col in dataset.columns.tolist()):
            for row in range(0,len(dataset)):
                if dataset.iloc[row][col] is None:
                    dataset.drop(row, axis=0, inplace=True)
        else:
            print('Error: column ' + col + ' does not exist in dataset')
    dataset.fillna(0) 
    return dataset


def outliers(dataset):
    print()


def data_trans(dataset, attribute, type):
    dataset[attribute] = pd.to_numeric(dataset[attribute], errors='coerce').fillna(0).astype(type)

def add_features(dataset):
    print()

def ds_clean(dataset):
    dataset = nulls(dataset, ['account_id','client_id', 'card_id', 'name '])
    return dataset
