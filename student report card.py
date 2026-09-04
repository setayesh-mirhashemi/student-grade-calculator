#-------------------------------------------------
def getNumber ( msg = "Value"  , low = -9e100 , high = 9e100 , jenseDade = int ) :
    while True :
        try :
            x = jenseDade ( input ( msg+" : " ))
            if x >= low and x <= high :
                return x
            else :
                print ("\t Out of Range . Range is [", low , " ~ " , high , "]")
        except :
            print ( "\t invalid input  ... ")
#-------------------------------------------------
def sourceCourseCreator () :
    source = { "riazi":2 , "arabi":4 , "dini":7 , "zaban":3 }
    return source    
#-------------------------------------------------
def getCourse() :
    while True:
        nameDars = input ("Course Name : ")
        if nameDars in source :
            #vahed  = getNumber ( "Unit" , 0 , 8 )
            nomre  = getNumber ( "Mark" , 0 , 20 , float )
            break
        else :
            print ("\t Invalid Course Name ! " )
    return { nameDars : nomre }
#-------------------------------------------------
def getCorseSs() :
    darsha = {}  
    ans = 'y'
    while  ans == 'y' :
        dars = getCourse()
        if not(list(dars.keys())[0] in darsha ):
            darsha[ list(dars.keys())[0] ] = dars[ list(dars.keys())[0]]
        else :
            print ( "\n Course Exist ")
        ans = input ( "\n\t Continue  ? (y|n) : ")
    return  darsha
#-------------------------------------------------
def showKarname ( darsha ) :
    sumGrade = 0
    sumUnit = 0
    print ( "Course" , "Unit" ,"Mark" , "Grade" , sep = "\t" )
    print ("---------------------------------------------")
    for i in  darsha  :
        print ( i , source[i] , darsha[i] , source[i]*darsha[i] , sep = "\t")
        sumGrade += source[i]*darsha[i]
        sumUnit  += source[i]
    print ("---------------------------------------------")
    print ("Sum", sumUnit , "Average" , sumGrade/sumUnit  , sep = "\t")
#-------------------------------------------------
#-----   Main  -----#
source = sourceCourseCreator ()
print (source)
# d = getCorseSs()
d = {'arabi': 12.0, 'riazi': 18.0}
print ( d )
showKarname ( d )
