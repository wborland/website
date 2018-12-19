import boto3
import db

def queryAll(query):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()
    all = cursor.fetchall()

    conn.close()
    cursor.close()

    return all

def queryOne(query):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()
    one = cursor.fetchone()

    conn.close()
    cursor.close()
    
    return one


def getAdmin():

    out = list()
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(id) FROM website.intern")
    out.append(cursor.fetchone())

    cursor.execute("SELECT COUNT(id) FROM website.intern where had_interview = 1")
    out.append(cursor.fetchone())

    conn.close()
    cursor.close()

    return out

def addEntry(name, file, position):
    conn = db.conn()

    cursor = conn.cursor()
    cursor.execute(""" INSERT INTO `website`.`intern` (`name`, `file`, `position`) VALUES (%s, %s, %s);""", [name, file, position])

    conn.commit()
    conn.close()


def updateStatusNum(id, type):
    conn = db.conn()
    cursor = conn.cursor()
    
    if type == "1":
        cursor.execute("""update website.intern set status_num = """ + type + """, had_interview = 1 where id = """ + id)
    else:
        cursor.execute("""update website.intern set status_num = """ + type + """ where id = """ + id)

    conn.commit()
    conn.close()


def updateStatus(id, status):
    conn = db.conn()

    cursor = conn.cursor()
    cursor.execute("""update website.intern set status = \"""" + status + """\" where id = """ + id)

    conn.commit()
    conn.close()
