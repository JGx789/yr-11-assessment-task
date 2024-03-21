def TestForEqual(S1,S2,S3):# test for equilateral triangle
  if S1==S2==S3:
    print("it is a Equilateral Triangle")
  else:
    print("it is NOT a Equilateral Triangle") 
 
def TestForIsos(S1,S2,S3):# test for isosceles triangle
  if S1==S2!=S3 or S2==S3!=S1 or S1==S3!=S2:
    print("it is a Isosceles Triangle")
  else:
    print("it is NOT a Isosceles Triangle")

def TestforScal(S1,S2,S3):# test for scalene triangle
   if S1!=S2!=S3:
    print("it is a Scalene Triangle")
   else:
    print("it is NOT a Scalene Triangle")


 # start of main program
Side1=input("Enter Side1 Length ")
Side2=input("Enter Side2 Length ")
Side3=input("Enter Side3 Length ")

TestForEqual(Side1,Side2,Side3)# this is the def test for equailateral

TestForIsos(Side1,Side2,Side3)

TestforScal(Side1,Side2,Side3)