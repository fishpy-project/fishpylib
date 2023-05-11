import pandas as pd

# Table object
class Table:

    # Table builder
    def __init__(self):
        self.data = pd.DataFrame()
        self.pool = [list(item) for item in self.data.values]

    def __repr__(self):
        if len(self.data) == 0:
            return 'Empty Table'
        else:
            return self.data

    def new_row(self, row_data):
        num_rows = len(self.data.index)
        self.data.loc[num_rows] = row_data
    
    def new_column(self, col_name = None):
        num_cols = len(self.data.columns) + 1
        if col_name is None:
            self.data[f'COL{num_cols}'] = None
        else:
            if type(col_name) == list:
                for item in col_name:
                    self.data[item] = None
            else:
                self.data[col_name.upper()] = None

    def edit_column_name(self, old_name, new_name):
        if old_name in self.data.columns:
            self.data = self.data.rename(columns = {old_name:new_name.upper()})
        else:
            print(f'{old_name} is not in the table')

    def change_headers(self, source):
        if type(source) == list:
            if len(source) == len(self.data.columns):
                self.data.columns = source
            else:
                print('The size of the list of headers are different than the list of old names')
        else:
            print('ERROR: source must be a list type')

    def load_data(self, source):
        for item in source:
            row_size = [len(item)]
        max_col = max(row_size)
        while max_col !=0:
            self.new_column()
            max_col -=1
        if type(source) == list:
            for item in source:
                num_rows = len(self.data.index)
                self.data.loc[num_rows] = item
        else:
            pass

    def add_data(self, source):
        for row in source:
            self.new_row(row)
