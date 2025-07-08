data={
    'name ':['jaggu','raju','mahesh','ramesh'],
    'marks':[23,45,67,89],

}
try:
    h=input('enter the name :')
    print(h,'marks:',data['marks'][data['name '].index(h)])
except ValueError:
    print('student not found')