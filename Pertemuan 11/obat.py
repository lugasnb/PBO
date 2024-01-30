from db import DBConnection as mydb

class obat:

    def __init__(self):
        self.__id=None
        self.__kdobat=None
        self.__nama=None
        self.__berat=None
        self.__bentuk=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def kdobat(self):
        return self.__kdobat

    @kdobat.setter
    def kdobat(self, value):
        self.__kdobat = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def berat(self):
        return self.__berat

    @berat.setter
    def berat(self, value):
        self.__berat = value

    @property
    def bentuk(self):
        return self.__bentuk

    @bentuk.setter
    def bentuk(self, value):
        self.__bentuk = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kdobat, self.__nama, self.__berat, self.__bentuk)
        sql="INSERT INTO obat (kdobat, nama, berat, bentuk) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kdobat, self.__nama, self.__berat, self.__bentuk, id)
        sql="UPDATE obat SET kdobat = %s, nama = %s, berat=%s, bentuk=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykdobat(self, kdobat):
        self.conn = mydb()
        val = (self.__nama, self.__berat, self.__bentuk, kdobat)
        sql="UPDATE obat SET nama = %s, berat=%s, bentuk=%s WHERE kdobat=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM obat WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBykdobat(self, kdobat):
        self.conn = mydb()
        sql="DELETE FROM obat WHERE kdobat='" + str(kdobat) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM obat WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kdobat = self.result[1]
        self.__nama = self.result[2]
        self.__berat = self.result[3]
        self.__bentuk = self.result[4]
        self.conn.disconnect
        return self.result

    def getBykdobat(self, kdobat):
        a=str(kdobat)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM obat WHERE kdobat='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kdobat = self.result[1]
            self.__nama = self.result[2]
            self.__berat = self.result[3]
            self.__bentuk = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kdobat = ''
            self.__nama = ''
            self.__berat = ''
            self.__bentuk = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM obat"
        self.result = self.conn.findAll(sql)
        return self.result

# tampil Data
A = obat()
B = A.getAllData()
print(B)