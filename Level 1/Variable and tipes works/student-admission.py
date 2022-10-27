# application -> University -> approve

# INPUT
# # DATA 
UNIVERSITY_MARK      =7.0     #float
student_SCHOOL_MARK  =3.0    #float

UNIVERSITY_contract  =10000 #int/year
student_MONEY        =10000

student_DAD_HAS_CONN = False
#LOGIC
#!!!! OPERATOR PRECEDENCE 1 + 2 * 3
approved = student_SCHOOL_MARK >= UNIVERSITY_MARK\
                     or\
                     student_MONEY >= UNIVERSITY_contract\
                     or\
                     student_DAD_HAS_CONN ==False
#OUTPUT
print( "Will the student be approved? ", approved )