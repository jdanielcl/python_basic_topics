def ageEvaluation(age):
    if age<0:
        raise TypeError("Negative value")
    else:
        print(age)

ageEvaluation(-1)