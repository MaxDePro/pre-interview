file = open('data.csv', 'r')
main_dict = {}
people_list = []
sec_list = []
count = 0
for i in file:
    if i.startswith('country'):
        continue
    sec_list.append(i)

for i in sorted(sec_list):
    lst = i.split(',')
    country = lst[0]
    name = lst[1].rstrip()

    if country in main_dict.keys():
        main_dict[country]['people'] += ', ' + name
        main_dict[country]['count'] += 1
        continue

    main_dict[country] = {
        'people': name,
        'count': 1
    }

print(main_dict)
file.close()
