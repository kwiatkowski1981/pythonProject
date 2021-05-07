transactions = []
positive_transactions = []

with open('transakcje-1.csv', 'r') as input_file:
    for line in input_file:
        transaction = line.strip()
        transactions.append(transaction)
    del transactions[0]
    print(transactions)
    for transaction in transactions:
        if int(transaction.split(',')[-1]) > 0:
            positive_transactions.append(transaction)

print(positive_transactions)


with open('income.txt', 'a') as output_file:
    for transaction in positive_transactions:
        output_file.write(f'{transaction}\n')


result = 0

with open('income.txt', 'r') as handler:
    income_statement = handler.readlines()
    # print(income_statement)
    for line in income_statement:
        values = line.strip().split(',')
        # print(values)
        date, transaction_name, income_value = values
        print(income_value)
        result += int(income_value)

print(f'Podliczenie dochodow. Zarobiłem: {result} erło..')
