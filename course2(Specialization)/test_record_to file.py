
metric_data = [('Maksim Maksimov', 'father', '36', 'man'),
('Svetlana Maksimova', 'mother', '35', 'woman'),
('Maksimov Vladislav', 'yonger son', '5', 'boy'),
('Maksimov Maksim','older son', '9', 'boy')]


file = '/Users/max/Desktop/education/Test_record.csv'
#with open(file, 'w') as newfile:
file1 = open(file, 'w')
file1.write('Name, Member of family, Age, Sex')
file1.write('\n')
for data in metric_data:
    row_string = '{}, {}, {}, {}'.format(data[0], data[1], (data[2]), data[3])
    #row_string = ','.join([data[0], data[1], (data[2]), data[3]])
    file1.write(row_string)
    file1.write('\n')
file1.close()
