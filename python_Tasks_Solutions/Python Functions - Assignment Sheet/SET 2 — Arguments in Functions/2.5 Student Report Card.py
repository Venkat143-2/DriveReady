'''
Accept a name, any number of marks, and optional details.
report("Priya", 85, 92, 78, 90, section="A", year=2)
Output:
Student : Priya
Section : A
Year    : 2
Marks   : 85, 92, 78, 90
Total   : 345
Average : 86.25
Result  : PASS
Pass mark = average >= 40.
'''
"For alignment we use '''f{value:alignment width}''' <-left align,>->right align,^-->center align"
def report(name,*marks,**details):
    total=sum(marks)
    avg=total/len(marks)
    print(f'{"Student":<10} :',name)
    for k,v in details.items():
        print(f"{k:<10} : {v}")
    print(f'{"Marks":<10} :',','.join(map(str,marks)))
    print(f'{"Total":<10} :',total)
    print(f'{"Average":<10} :',avg)
    print(f'{"Result":<10} :','PASS' if avg>=40 else 'Fail')
report("Priya", 85, 92, 78, 90, section="A", year=2)
