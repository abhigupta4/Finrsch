import pymysql as PyMySQL

db = PyMySQL.connect("localhost","arafin_test","&gR^Fh-?)Tn(","arafin_edgar", charset="utf8" )
cursor = db.cursor()

def add_to_db(tablename,url,q,t1,t2,t3,date,exclink,tp,yr):
    cursor.execute("""CREATE TABLE IF NOT EXISTS `%s`(
    id int auto_increment not null primary key,
    Link VARCHAR(255) default null,
    Quarter INT(5) default 0,
    U_Text LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    S_Text LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    T_Text LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    F_date VARCHAR(255),
    Financials varchar(255),
    F_Type varchar(255),
    Year varchar(255)
    )""" % tablename)
    db.commit()
    print("adding")
    cursor.execute("""insert into `%s` (Link,Quarter,U_Text,S_Text,T_Text,F_date,Financials,F_Type,Year) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s")""" %
                   (tablename,url,q,db.escape_string(t1),db.escape_string(t2),db.escape_string(t3),date,exclink,tp,yr))
    db.commit()
