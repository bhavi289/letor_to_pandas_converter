import pandas as pd


class Converter(object):
    
    def __init__(self, path):
        self._path = path
        
    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, p):
        self._path = p
        
    def _load_file(self, path):
        df = pd.read_csv(str(self._path), sep=" ", header=None)
        return df
        
    def _drop_col(self, df):
        '''
        Arguments:
            df: pandas dataframe object
        Return:
            df: original df with last column dropped (parsing leftover as data set as trailing space for each sample)
        '''
        #df.drop(df.columns[-1], axis=1, inplace=True)
        return df.drop(df.columns[-1], axis=1)
    
    def _split_colon(self, df):
        '''
        Arguments:
            df: pandas dataframe object
        Return:
            df: original df with string pattern ':' removed; columns named appropriately
        '''
        for col in range(1,len(df.columns)):
            df.loc[:,col] = df.loc[:,col].apply(lambda x: str(x).split(':')[1])
        df.columns = ['rel', 'qid'] + [str(x) for x in range(1,len(df.columns)-1)] # renaming cols
        return df
    
    def convert(self):
        df_raw = self._load_file(self._path)
        df_drop = self._drop_col(df_raw)
        return self._split_colon(df_drop)
        
    
    

