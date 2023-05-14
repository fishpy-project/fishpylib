class Table:
    def __init__(self, columns):
        self.settings = {
            'columns':columns,
            'units': None,
            'location': None,
            'species': None
        }
        self.rows = []
        self.settings['columns'].insert(0,'#')

    def __repr__(self):
        sep = '|'
        cell_size = 15

        aligned = [f'{column.upper():^{cell_size}}' for column in self.settings['columns']]
        bar_size = [len(item) for item in aligned]
        print(f'{"FISHPY LIB TABLE: Aaraipama gigas (Aracaju/SE - 2023)":<70}')
        print((sum(bar_size)+4)*'=')
        print(sep.join(aligned))
        print((sum(bar_size)+4)*'-')

        if len(self.rows) == 0:
            print('EMPTY TABLE')

        for row in self.rows:
            aligned = [f'{values:^{cell_size}}' for values in row.values()]
            print(sep.join(aligned))

        print((sum(bar_size)+4)*'=')

    def add_row(self, values, group = False):
        if group == False:
            values.insert(0,len(self.rows))
            try:
                self.rows.append({self.settings['columns'][i]: values[i] for i in range (len(self.settings['columns']))})
            except:
                print(f"ERROR: The row has {len(values)} items and there are {len(self.settings['columns'])} columns in the table.")
        elif group == True:
            for row in values:
                row.insert(0,len(self.rows))
                try:
                    self.rows.append({self.settings['columns'][i]: row[i] for i in range (len(self.settings['columns']))})
                except:
                    print(f"ERROR: The row has {len(row)} items and there are {len(self.settings['columns'])} columns in the table.")
        else:
            print('ERROR: Invalid group parameter value (use True or False)')

    def set_units(self,units):
        units.insert(0, None)
        try:
            self.settings['units'] = {self.settings['columns'][i]: units[i] for i in range (len(self.settings['columns']))}
        except:
            print(f"ERROR: Units has {len(units)} items and there are {len(self.settings['columns'])} columns in the table.")
