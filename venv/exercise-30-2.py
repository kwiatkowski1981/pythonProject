from datetime import date, timedelta, datetime


print("Podaj od i do kiedy pracowałaś/eś i stawkę dzienną: start: dd.mm.yy end: dd.mm.yy stawka dzienna: ")

start = input('Rozpoczęcie pracy: ')
stop = input('zakońćzenie pracy: ')
daily_salary = int(input('Dzienne wynagrodzenie: '))

vat = 1 * 0.23

# start_date = datetime.strptime(start, '%d.%m.%y')
# # print(start_date)
# stop_date = datetime.strptime(stop, '%d.%m.%y')
# # print(stop_date)
# days_worked = stop_date - start_date
# formatted_days_worked = days_worked.days
# # print(days_worked)
# # print(formatted_days_worked)
# total_salary = formatted_days_worked * daily_salary
# print(f'wynagrodzenie netto po przepracowaniu {formatted_days_worked} dni przy stawce {daily_salary} wynosi: \n'
#       f'brutto: {total_salary}zł, \n'
#       f'netto: {total_salary - total_salary * vat}zł.')


def calculate_total_salary(**kwargs):
    start_date = datetime.strptime(start, '%d.%m.%y')
    stop_date = datetime.strptime(stop, '%d.%m.%y')
    days_worked = stop_date - start_date
    formatted_days_worked = days_worked.days
    total_salary = formatted_days_worked * daily_salary
    print(f'wynagrodzenie netto po przepracowaniu {formatted_days_worked} dni przy stawce {daily_salary} wynosi: \n brutto: {total_salary}zł, \n netto: {total_salary - total_salary * vat}zł.')


calculate_total_salary(st=start, sp=stop, ds=daily_salary)
