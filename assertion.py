def compute_avg(marks):
    '''computes the avg of marks
      marks cannot be empty'''
    assert len(marks) >0,"average undefined"
    sum=0.0
    for m in marks:
        sum=sum+m
    return sum/len(marks)
print(compute_avg([]))

#python allows u to erase all the assert programes
#by passing -O or -OO option to pythonintepretor
#(python -O script.py)
# print(assert 5/0 > 0)
