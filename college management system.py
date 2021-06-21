import mysql.connector as mysql

db= mysql.connect(host="localhost", user="root", password="", database="college")
command_handler= db.cursor(buffered=True)


def teacher_session():
     while 1:
          print("")
          print("teacher menu")
          print("1. mark student register")
          print("2. view register")
          print("3. logout")

          user_option = input(str("option: "))
          if user_option == "1":
               print("")
               print("Mark student register")
               command_handler.execute(" SELECT username FROM users WHERE privilege = 'student' ")
               records = command_handler.fetchall()
               date = input(str("Date: DD/MM/YYYY: "))
               for record in records:
                    record = str(record).replace("'","")
                    record = str(record).replace(",","")
                    record = str(record).replace("(","")
                    record = str(record).replace(")","")
                    # present | absent | late
                    status = input(str("Status for" + str(record) + "P/A/L : "))
                    query_vals= (str(record),date,status)
                    command_handler.execute("INSERT INTO attendance (username, date, status) VALUES(%s,%s,%s)",query_vals)
                    db.commit()
                    print(record + "marked as" + status)
          elif user_option =="2":
               print("")
               print("Viewing all student registers")
               command_handler.execute("SELECT username, date, status FROM attendance")
               records= command_handler.fetchall()
               print(" Displaying all regsters")
               for record in records:
                    print(record)
          elif user_option =="3":
               break
          else:
               print("no valid option is selected")

def student_session(username):
     while 1:
          print("")
          print("student menu")
          print("")
          print("1. view register")
          print("2. download register")
          print("3. logout")

          user_option = input(str("option: "))
          if user_option =="1":
               print("displaying register")
               username = (str(username),)
               command_handler.execute("SELECT date, username, status FROM attendance WHERE username =%s", username)
               records = command_handler.fetchall()
               for record in records:
                    print(record)
          elif user_option == "2":
               print("downloading register")
               username = (str(username),)
               command_handler.execute("SELECT date, username, status FROM attendance WHERE username =%s", username)
               records = command_handler.fetchall()
               for record in records:
                    with open("C:/Users/DELL EXCLUSIVE STORE/Desktop/register.txt", "w") as f:
                         f.write(str(records)+ "\n")
                    f.close()
               print(" all records saved")
          
          elif user_option == "3":
               break
          else:
               print("no valid option is selected")



def admin_session():
     while 1:
          print("")
          print("admin menu")
          print("1. register new student")
          print("2. register new teacher")
          print("3. delete existing student")
          print("4. delete existing teacher")
          print("5. logout")
          
          user_option = input(str("option: "))
          if user_option == "1":
               print("")
               print("register new student")
               username = input(str("Student username: "))
               password = input(str("Student password: "))
               query_vals= (username, password)
               command_handler.execute("INSERT INTO users (username, password, privilege) VALUES (%s, %s,'student')",query_vals)
               db.commit()
               print(username + " has been registered as a student")
          elif user_option =="2":
               print("")
               print("register new teacher")
               username = input(str("Teacher username: "))
               password = input(str("Teacher password: "))
               query_vals= (username, password)
               command_handler.execute("INSERT INTO users (username, password, privilege) VALUES (%s, %s,'teacher')",query_vals)
               db.commit()
               print(username + " has been registered as a teacher")
          elif user_option == "3":
               print("")
               print("delete existing student account")
               username = input(str("Student username: "))
               query_vals = (username, "student")
               command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ", query_vals)
               db.commit()
               if command_handler.rowcount <1:
                    print("user not found")
               else:
                    print(username+"has been deleted")
          elif user_option == "4":
               print("")
               print("delete existing teacher account")
               username = input(str("teacher username: "))
               query_vals = (username, "teacher")
               command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ", query_vals)
               db.commit()
               if command_handler.rowcount <1:
                    print("user not found")
               else:
                    print(username+"has been deleted")
          elif user_option =="5":
               break
          else:
               print("no valid option selected")

def auth_student():
     print("")
     print("student login")
     print("")
     username = input(str("Username: "))
     password = input(str("Password: "))
     query_vals =(username, password, "student")
     command_handler.execute("SELECT username FROM users WHERE username = %s AND password = %s AND privilege = %s", query_vals)
     if command_handler.rowcount <=0:
          print("inavlid login details")
     else:
          student_session(username)


def auth_teacher():
     print("")
     print("teacher login")
     print("")
     username = input(str("Username: "))
     password = input(str("Password: "))
     query_vals =(username, password)
     command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege ='teacher' ",query_vals)
     if command_handler.rowcount <=0:
          print("login not recognised")
     else:
          teacher_session()

def auth_admin():
     print("")
     print("admin login")
     print("")
     username = input(str("Username: "))
     password = input(str("Password: "))
     if username== "admin":
          if password=="password":
               admin_session()
          else:
               print("incorrect password")
     else:
          print("login details not recognised")

def main():
    while 1:
        print("welcome to college system")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")

        user_option= input(str("option: "))

        if user_option == "1":
             auth_student()
        elif user_option == "2":
             auth_teacher()
        elif user_option == "3":
             auth_admin()
        else:
            print("no valid option is selected here")


main()