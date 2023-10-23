import pandas as pd


FILE = 'costs.csv'
PERSONS = ['name0','name1','name2']


class Cbd:
    def __init__(self, csv_file) -> None:
        self.df = pd.read_csv(csv_file)
        self.df = self.df.drop(columns=['item','date','comment'])
    
    def payers(self):
        return self.df['payer'].unique()
    
    def expenses_per_person(self, person):
        return self.df[self.df['payer'] == person]['amount'].sum()
    
    def costs_per_person(self, person):
        return self.df[[person,'amount','units']].dropna().\
            apply(lambda x: x[person] * x['amount'] / x['units'], axis=1).sum()
            
    def balance_per_person(self, person):
        return self.expenses_per_person(person) - self.costs_per_person(person)


def main():
    cbd = Cbd(csv_file=FILE)
    
    print('Balances for persons:')
    
    for person in PERSONS:
        balance = cbd.balance_per_person(person)
        print('{person}: {balance}'.format(person=person, balance=balance))
    
    
if __name__ == '__main__':
    main()
