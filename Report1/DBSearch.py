import pymysql
import sys, datetime

#DB 접근
class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='wjddus427', db='kleague', charset='utf8')

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:     # dictionary based cursor
                cursor.execute(sql, params)
                tuples = cursor.fetchall()
                return tuples
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

    def updateExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='wjddus427', db=db, charset='utf8')

        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Query:
    # 모든 검색문은 여기에 각각 하나의 메소드로 정의

    # 팀 이름 검색
    def selectTeam(self, value):
        if value == '없음':
            sql = "SELECT * FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE TEAM_NAME= NULL "
            params = ()
        else:
            sql = "SELECT * FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE TEAM_NAME= %s "
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectTeamName(self):
        sql = "SELECT DISTINCT TEAM_NAME FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
              "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID "
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    #선수 검색
    def selectPlayer(self, value):
        if value == '없음':
            sql = "SELECT * FROM player WHERE position IS NULL"
            params = ()
        else:
            sql = "SELECT * FROM player WHERE position = %s"
            params = (value)         # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    #포지션 검색
    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    #출신국 검색
    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    #키 검색
    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    #몸무게 검색
    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

class DB_Update:
    # 모든 갱신문은 여기에 각각 하나의 메소드로 정의
    def insertPlayer(self, player_id, player_name, team_id, position):
        sql = "INSERT INTO player (player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
        params = (player_id, player_name, team_id, position)

        util = DB_Utils()
        util.updateExecutor(db="kleague", sql=sql, params=params)