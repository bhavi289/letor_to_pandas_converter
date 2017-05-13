# Letor-to-Pandas-Converter for Microsoft's Learning to Rank (LETOR) Dataset

Get the data & descriptions here: https://www.microsoft.com/en-us/research/project/mslr/

Letor_Converter takes the original .txt files as input, removes string patterns from the values to convert them to fully numeric values embedded a neat pandas dataframe and renames columns accordingly.


##Usage

conv = Letor_Converter('/home/user/letor/Fold1/train.txt')
df_train_fold1 = conv.convert()
