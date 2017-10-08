from sense_hat import SenseHat

def calcAlphaGrade(numGrade):
    alphaGrade = ""
    if numGrade < 50:
        alphaGrade = "F"
    elif numGrade < 53:
        alphaGrade = "D-"
    elif numGrade < 57:
        alphaGrade = "D"
    elif numGrade < 60:
        alphaGrade = "D+"
    elif numGrade < 63:
        alphaGrade = "C-"
    elif numGrade < 67:
        alphaGrade = "C"
    elif numGrade < 70:
        alphaGrade = "C+"
    elif numGrade < 73:
        alphaGrade = "B-"
    elif numGrade < 77:
        alphaGrade = "B"
    elif numGrade < 80:
        alphaGrade = "B+"
    elif numGrade < 85:
        alphaGrade = "A-"
    elif numGrade < 90:
        alphaGrade = "A"
    else:
        alphaGrade = "A+"
    return alphaGrade

def calcNumGrade(poa, pom, pof, a, m, f):
    numGrade = (poa * a + pom * m + pof * f) / 100
    return numGrade

poa = float(input("enter ponderation of assigments"))
pom = float(input("enter ponderation of midterm"))
pof = float(input("enter ponderation of final"))
a = float(input("enter mark for assigments"))
m = float(input("enter mark for midterm"))
f = float(input("enter mark for final"))

numGrade = calcNumGrade(poa, pom, pof, a, m, f)
alphaGrade = calcAlphaGrade(numGrade)
s = SenseHat()

if numGrade > 50:
    s.show_message(alphaGrade + " Congratulations, you passed")