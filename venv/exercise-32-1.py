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


