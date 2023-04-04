import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="salary",
  auth_plugin='mysql_native_password'
)
n=int(input("1.employeedetailscreation 2.incrementupdation 3.viewdetails "))
if(n==1):
    ch=1
    while(ch==1):
        empcode=int(input("enter employee code"))
        name=input("enter emp name")
        sal=input("enter emp salary")
        month=input("enter salaried month")
        mycursor=mydb.cursor()
        sql="insert into list(empcode,name,month,salary)values(%s,%s,%s,%s)"
        val=(empcode,name,month,sal)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor = mydb.cursor()
        sql = "insert into details(empcode,name,month,sal)values(%s,%s,%s,%s)"
        val = (empcode,name,month,sal)
        mycursor.execute(sql,val)
        mydb.commit()
        ch=int(input("1.continue 2.exit"))
elif(n==3):
    empcode=int(input("enter employee code"))
    mycursor=mydb.cursor()
    sql="select salary from list where empcode='{}'".format(empcode)
    mycursor.execute(sql)
    myresult=mycursor.fetchone()
    for x in myresult:
        salary=x
    print("your current salary is",salary)
else:
    empcode=int(input("enter your empcode"))
    name=input("enter your name")
    month=input("enter your salary month")
    mycursor=mydb.cursor()
    sql = "select salary from list where empcode='{}'".format(empcode)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    for x in myresult:
        salary = x

    if(salary<=10000):
        inc=(2*salary)/100
        sal=inc+salary
    elif(salary>10001)and(salary<=20000):
        inc=(5*salary)/100
        sal=inc+salary
    else:
        inc=(10*salary)/100
        sal=inc+salary

    mycursor=mydb.cursor()
    sql="insert into details(empcode,name,month,sal)values(%s,%s,%s,%s)"
    val=(empcode,name,month,sal)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor=mydb.cursor()
    sql="update list set salary='{}'where empcode='{}'".format(sal,empcode)
    mycursor.execute(sql)
    mydb.commit()

