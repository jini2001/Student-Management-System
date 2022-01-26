import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid Integer primary key autoincrement,name text,duration text,charges text,description text)")
    con.commit()
  
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll Integer primary key autoincrement,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid Integer primary key autoincrement,roll text,name text,course text,marks text,full_marks text,per text)")
    con.commit()

    con.close()

create_db()