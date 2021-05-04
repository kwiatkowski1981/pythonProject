from datetime import date, timedelta, datetime


today = date.today()
formatted = today.strftime('%d.%m.%Y')
print(f'Dziś jest: {today}')
print(f'Dziś jest: {formatted}')
my_birthday = date(today.year, 4, 21)
formatted_birthday = my_birthday.strftime("%A %d %B %Y")
print(f'Moje urodziny w tym roku: {my_birthday}')
print(f'Moje urodziny w tym roku: {formatted_birthday}')

if my_birthday > today:
    diff = my_birthday - today
    print(f'Do moich urodzin pozostało {diff.days} dni.')
else:
    diff = today - my_birthday
    print(f'Moje urodziny były {diff.days} dni temu.')

my_next_birthday = date(2022, 4, 21)
formatted_next_bnirthday = my_next_birthday.strftime("%A %d %B %Y")
print(formatted_next_bnirthday)
days_left_to_next_birthday = my_next_birthday - today
print(f'Do moich następnych urodzin, które będą: {formatted_next_bnirthday}'
      f' pozostało jeszcze dokładnie {days_left_to_next_birthday.days} dni.')
over_next_year_bth = days_left_to_next_birthday + timedelta(days=365)
print(f"Do urodzin za dwa lata pozostało: {over_next_year_bth} godzin.")

print("\n")

for year in range(1981, 2010):
    birthday = date(year, 4, 21)
    print(f'dzień urodzin to: {birthday.strftime("%Y - %A")}')

print("\n")

for year in range(1986, 2025):
    birthday = date(year, 1, 4)
    print(f'dzień urodzin to: {birthday.strftime("%Y - %A")}')

print("\n")

start = date.today()
diff = timedelta(days=365)
end = start + diff
print(end.strftime('%d.%m.%y'))


event = datetime.now()
print(event.hour)
print(event.minute)
print(event.strftime('%H:%M:%S'))

youre_birthday = input('Podaj datę urodzin w formacie dd.mm.yyyy: ')
d = datetime.strptime(youre_birthday, '%d.%m.%Y')
print(d)
