

print('������������')

prif = '���'

who_animal = input('��� ��� �������? ')

name = input('��� ������ �������? ')

age = int(input('������� ������ �������? '))

# � ���������� ����� ���������� �� ������ "���"

if age == 1:

    prif = '���'

else:

    if age >= 2 and age <= 4:

        prif = '����'

print('���',who_animal,'�� ������ "'+name+'". �������:',age,prif)