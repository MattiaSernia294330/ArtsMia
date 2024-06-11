from database.DB_connect import DBConnect
from model.Opera import Opera
from model.Collegamento import Collegamento

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllObject():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                from objects o """
        cursor.execute(query)
        for row in cursor:
            result.append(Opera(row["object_id"], row["classification"], row["object_name"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT eo1.object_id as object_id1,  eo2.object_id as object_id2 
            from exhibition_objects eo1, exhibition_objects eo2
            where eo2.exhibition_id = eo1.exhibition_id and eo2.object_id != eo1.object_id"""
        query_prof="""SELECT eo1.object_id as object_id1,  eo2.object_id as object_id2 
            from exhibition_objects eo1, exhibition_objects eo2
            where eo2.exhibition_id = eo1.exhibition_id and eo2.object_id > eo1.object_id
            group by eo1.object_id,eo2.object_id"""
        cursor.execute(query)
        for row in cursor:
            result.append(Collegamento(row["object_id1"],row["object_id2"]))
        cursor.close()
        conn.close()
        return result

