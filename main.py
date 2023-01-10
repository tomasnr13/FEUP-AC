# import pandas as pd
# import six
# import sys
# import os
# import data_understanding
# import data_preparation
# import matplotlib.pyplot as plt
# sys.modules['sklearn.externals.six'] = six
# import warnings
# warnings.filterwarnings('always')  # "error", "ignore", "always", "default", "module" or "once"
# warnings.filterwarnings('ignore')

# #1 - data understanding 
# data_understanding.du()
# #2 - data preparation
# dataset = data_preparation.data_merge()
# #3 - description

# files_path = "C:/Users/ASUS/Desktop/FEUP/4ano/1Semestre/AC/Projeto-AC/ficheiros_competicao_dev"
# file_list = os.listdir(files_path)

# #for file in file_list:
#     #dataset = pd.read_csv(files_path + "/" + file)

# loans = pd.read_csv("C:/Users/ASUS/Desktop/FEUP/4ano/1Semestre/AC/Projeto-AC/ficheiros_competicao_dev/loan_dev.csv")
# dataset = data_merging.data_merge()


# data_understanding.data_statistics(dataset)
import pandas as pd
import six
import sys
import os
import data_understanding
import data_preparation
import matplotlib.pyplot as plt
sys.modules['sklearn.externals.six'] = six
import warnings
warnings.filterwarnings('always')  # "error", "ignore", "always", "default", "module" or "once"
warnings.filterwarnings('ignore')

#1 - data understanding 
data_understanding.du()
#2 - data preparation
dataset = data_preparation.data_merge()
dataset = data_preparation.ds_clean(dataset)
dataset.to_csv('df.csv')
#3 - description

#4 - prediction