import pyodbc

class accessdbclient(object):
    """Microsoft access database client"""
    def __init__(self):
        __connectionString = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=path\database.accdb;'
        self.connection = pyodbc.connect(__connectionString)
        self.cursor = self.connection.cursor()
        return

    def getbmk(self):
        sql_query = """SELECT avgn, avge, avgz
                       FROM benchmark
                       WHERE id = 10"""
        self.cursor.execute(sql_query)
        results = self.cursor.fetchall()
        self.connection.close()
        return results

    def getRD_All(self, pid):
        sql_query = """SELECT rdate, r1n, r1e, r1z, r2n, r2e, r2z, r3n, r3e, r3z
                       FROM %s""";
        self.cursor.execute(sql_query %(pid))
        results = self.cursor.fetchall()
        self.connection.close()
        return results

    def getCD_All(self, pid):
        sql_query = """SELECT rdate, avgn, avge, avgz, ddn, dde, ddz
                       FROM %s""";
        self.cursor.execute(sql_query %(pid))
        results = self.cursor.fetchall()
        self.connection.close()
        return results

    def getRD_Day(self, pid, get_date):
        sql_query = """SELECT rdate, r1n, r1e, r1z, r2n, r2e, r2z, r3n, r3e, r3z
                       FROM %s 
                       WHERE YEAR(rdate) = ? AND MONTH(rdate) = ? AND DAY(rdate) = ?""";
        self.cursor.execute(sql_query %(pid), get_date.year, get_date.month, get_date.day)
        results = self.cursor.fetchall()
        self.connection.close()
        return results

    def getCD_Day(self, pid, get_date):
        sql_query = """SELECT rdate, avgn, avge, avgz, ddn, dde, ddz
                       FROM %s
                       WHERE YEAR(rdate) = ? AND MONTH(rdate) = ? AND DAY(rdate) = ?""";
        self.cursor.execute(sql_query %(pid), get_date.year, get_date.month, get_date.day )
        results = self.cursor.fetchall()
        self.connection.close()
        return results

    def getRD_Month(self, pid, get_date):
        sql_query = """SELECT * 
                       FROM %s 
                       WHERE YEAR(rdate) = ? AND MONTH(rdate) = ?""";
        self.cursor.execute(sql_query %(pid), get_date.year, get_date.month)
        results = self.cursor.fetchall()
        self.connection.close()
        return results

    def getCD_Month(self, pid, get_date):
        sql_query = """SELECT rdate, avgn, avge, avgz, ddn, dde, ddz 
                       FROM %s 
                       WHERE YEAR(rdate) = ? AND MONTH(rdate) = ?"""
        self.cursor.execute(sql_query %(pid), get_date.year, get_date.month)
        results = self.cursor.fetchall()
        self.connection.close()
        return results

    def getRD_Year(self, pid, get_date):
        sql_query = """SELECT * 
                       FROM %s 
                       WHERE YEAR(rdate) = ?"""
        self.cursor.execute(sql_query %(pid), get_date.year )
        results = self.cursor.fetchall()
        self.connection.close()
        return results

    def getCD_Year(self, pid, get_date):
        sql_query = """SELECT rdate, avgn, avge, avgz, ddn, dde, ddz 
                       FROM %s 
                       WHERE YEAR(rdate) = ?"""
        self.cursor.execute(sql_query %(pid), get_date.year)
        results = self.cursor.fetchall()
        self.connection.close()
        return results

    def addCD(self, pid, data_tuple, rdate):
        sql_query = """UPDATE %s 
                       SET avgn=?, avge=?, avgz=?, ddn=?, dde=?, ddz=? 
                       WHERE rdate = ?"""
        self.cursor.execute(sql_query %(pid), data_tuple)
        self.cursor.commit()