import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import statistics


def data_describe(dataset):
    print("Dataset: ")
    print(dataset)

    print("Dataset info: ")
    print(dataset.info())

    print("General info about the dataset: ")
    print(dataset.describe())

    print("Types of every collumn of the dataset: ")
    print(dataset.dtypes)

    print("Check the dataset for null values: ")
    print(dataset.isnull().sum())

def heatmap(dataset):
    # Creating correlation matrix
    dataset_corr = dataset.corr().abs()
    print(dataset_corr)

    sns.heatmap(dataset_corr, cmap='RdYlGn_r', linewidths=0.5, annot=True)
    plt.yticks(rotation= 0)
    plt.xticks(rotation=90)
    # Display the Pharma Sector Heatmap
    plt.show()

def colorbar(dataset):
    print()
    # Displaying a color bar to understand
    # which color represents which range of data
     
    # plt.pcolor(dataset)
    # plt.yticks(np.arange(0.5, len(dataset.index), 1), dataset.index)
    # plt.xticks(np.arange(0.5, len(dataset.columns), 1), dataset.columns)
    # plt.show()
    # for col in dataset.columns[1:-1]:
    #     plt.suptitle(col)
    #     plt.xlabel(col)
    #     plt.ylabel(dataset.columns[-1])
    #     plt.scatter(dataset[col], dataset[dataset.columns[-1]])
    #     plt.show()
    
def boxplot(datasetCols, datasetList):
   
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)

    # Creating axes instance
    bp = ax.boxplot(datasetList, patch_artist = True,
                    notch ='True', vert = 0)

    colors = ['#0000FF', '#00FF00',
            '#FFFF00', '#FF00FF']
    
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B',
                    linewidth = 1.5,
                    linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color ='#8B008B',
                linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='red',
                linewidth = 3)
    
    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(marker ='D',
                color ='#e7298a',
                alpha = 0.5)
        
    # x-axis labels
    ax.set_yticklabels(datasetCols)
    
    # Adding title
    plt.title("Box Plot")
    
    # Removing top axes and right axes
    # ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    plt.show()

def barplotcount(dataset, column_name):
    sns.countplot(x = column_name, data = dataset)
    plt.show()

def data_statistics(table): 

    for col in table.columns:
        print(table[col].dtype)
        if(table[col].dtype != "object"):
            print(col)
            # Finding Mean
            print("\nMean: ", statistics.mean(table[col]))
            
            # Finding Median
            print("Median: ", statistics.median(table[col]))
            
        # Finding Single Mode
        print("Single Mode: ", statistics.mode(table[col]))
            
        # Finding Multiple Modes
        print("Mode: ", statistics.multimode(table[col]))

def scatterplot(dataset):
    sns.set_theme(style="ticks")
    sns.pairplot(dataset, hue="status")
    plt.show()

def du():
    # nulls = {}
    # # account 
    # accounts = pd.read_csv("ficheiros_competicao_dev/account.csv")
    # nulls['account'] = accounts.isna().any(axis=1).sum()
    # # card 
    # cards = pd.read_csv("ficheiros_competicao_dev/card_dev.csv")
    # nulls['card'] = cards.isna().any(axis=1).sum()
    # barplotcount(cards, "type")     
    # # client 
    clients = pd.read_csv("ficheiros_competicao_dev/client.csv")
    # nulls['clients'] = clients.isna().any(axis=1).sum()

    # # disp 
    # disps = pd.read_csv("ficheiros_competicao_dev/disp.csv")
    # nulls['disps'] = disps.isna().any(axis=1).sum()

    # barplotcount(disps, "type")

    # # district 
    districts = pd.read_csv("ficheiros_competicao_dev/district.csv")
    # nulls['district'] = districts.isna().any(axis=1).sum()
    # ax =  districts.plot.bar(x="code ",y="no. of inhabitants")
    # plt.show()
    # # loans 
    loans = pd.read_csv("ficheiros_competicao_dev/loan_dev.csv")
    # lbp = pd.DataFrame({'amount' : loans.amount})
    # boxplot(lbp)
    # nulls['loans'] = loans.isna().any(axis=1).sum()
    # barplotcount(loans, "status")

    # trans 
    trans = pd.read_csv("ficheiros_competicao_dev/trans_dev.csv")

    #BoxPlot trans_dev
    # boxplot(['amount'],[trans['amount']])
    # boxplot(['balance'],[trans['balance']])

    # #BoxPlot loan_dev
    # boxplot(['amount'],[loans['amount']])
    # boxplot(['duration'],[loans['duration']])

    # #BoxPlot client
    # boxplot(['birth_number'],[clients['birth_number']])

    # #BoxPlot disp
    # boxplot()

    #BoxPlot district
    boxplot(['average salary'], [districts['average salary']])
    boxplot(['no. of inhabitants'], [districts['no. of inhabitants']])
   
    # districts[['ola']] = districts[['ola']].apply(pd.to_numeric)  
    # data_trans(districts,'no. of commited crimes \'95', 'int64')

    # boxplot(['no. of commited crimes \'95'], [districts['no. of commited crimes \'95']])

    #BoxPlot account
    # boxplot(['date'],[account['date']])

    # nulls['trans'] = trans.isna().any(axis=1).sum()
    # barplotcount(trans, "type")
    # barplotcount(trans, "operation")
    
    # # heatmap(dataset)
    # dscatter = loans.drop(["loan_id", "account_id", "date"], axis=1)
    # scatterplot(dscatter)

    # #nulls
    # print('Null counts: ')
    # print(nulls)
