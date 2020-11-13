import pymysql
import sys, datetime
import xml.etree.ElementTree as ET
import json
import csv

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

    #플레이어 검색
    def selectPLTeamName(self, value):
        if value == '없음':
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  " FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE TEAM_NAME IS NULL "
            params = ()
        else:
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  " FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE TEAM_NAME= %s "
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPLPosition(self, value):
        if value == '미정':
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                      "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE POSITION IS NULL "
            params = ()
        else:
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE POSITION= %s "
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPLCountry(self, value):
        if value == '대한민국':
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                      "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE NATION IS NULL "
            params = ()
        else:
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE NATION= %s "
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPLUpHeight(self, value):
        if value == '미측정':
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                      "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE HEIGHT IS NULL "
            params = ()
        else:
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE HEIGHT>= %s "
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPLDnHeight(self, value):
        if value == '미측정':
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                      "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE HEIGHT IS NULL "
            params = ()
        else:
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE HEIGHT<= %s "
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPLUpWeight(self, value):
        if value == '미측정':
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE WEIGHT IS NULL "
            params = ()
        else:
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE WEIGHT>= %s "
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPLDnWeight(self, value):
        if value == '미측정':
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE WEIGHT IS NULL "
            params = ()
        else:
            sql = "SELECT PLAYER_ID,PLAYER_NAME,Pl.TEAM_ID TEAM_ID,E_PLAYER_NAME," \
                  "NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT,TEAM_NAME" \
                  "FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
                  "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID WHERE WEIGHT<= %s "
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    #팀 이름 검색
    def selectTeamName(self):
        sql = "SELECT DISTINCT TEAM_NAME FROM player PL LEFT JOIN(SELECT TEAM_NAME,TEAM_ID " \
              "FROM team)AS t ON t.TEAM_ID=PL.TEAM_ID "
        params = ()

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
    def selectPlayerCountry(self):
        sql = "SELECT DISTINCT NATION FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    #키 검색
    def selectPlayerHeight(self):
        sql = "SELECT DISTINCT HEIGHT FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    #몸무게 검색
    def selectPlayerWeight(self):
        sql = "SELECT DISTINCT WEIGHT FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

class FileOutput:
    def readDB_writeCSV(self, players):

        # CSV 화일을 쓰기 모드로 생성
        with open('player.csv', 'w', encoding='utf-8', newline='') as f:
            wr = csv.writer(f)
            columnNames = list(players[0].keys())
            wr.writerow(columnNames)

            # 테이블 내용을 출력
            for rowIDX in range(len(players)):
                row = list(players[rowIDX].values())
                wr.writerow(row)
                # 2007001,정병지,K03,"JEONG, BYUNGJI",,2011,GK,1,,1980-08-04,1,184,77
                # 날짜 변환 기능을 csv 패키지에서 제공함.


    def readDB_writeJSON(self, players):
        for player in players:
            for k, v in player.items():
                if isinstance(v, datetime.date):
                    player[k] = v.strftime('%Y-%m-%d')  # 키가 k인 item의 값 v를 수정
        newDict = dict(Player= players)
        # JSON 화일에 쓰기
        # dump()에 의해 모든 작은 따옴표('')는 큰 따옴표("")로 변환됨
        with open('player.json', 'w', encoding='utf-8') as f:
            json.dump(newDict, f, ensure_ascii=False)

    def readDB_writeXML(self, players):

        # 애트리뷰트 BIRTH_DATE의 값을 MySQL datetime 타입에서 스트링으로 변환함. (CSV에서는 패키지가 변환함.)
        for player in players:
            for k, v in player.items():
                if isinstance(v, datetime.date):
                    player[k] = v.strftime('%Y-%m-%d')  # 키가 k인 item의 값 v를 수정

        newDict = dict(Player = players)

        # XDM 트리 생성
        tableName = list(newDict.keys())[0]
        tableRows = list(newDict.values())[0]

        rootElement = ET.Element('Table')
        rootElement.attrib['name'] = tableName

        for row in tableRows:
            rowElement = ET.Element('Row')
            rootElement.append(rowElement)

            for columnName in list(row.keys()):
                if row[columnName] == None:  # NICKNAME, JOIN_YYYY, NATION 처리
                    rowElement.attrib[columnName] = ''
                else:
                    rowElement.attrib[columnName] = row[columnName]
                if type(row[columnName]) == int:  # BACK_NO, HEIGHT, WEIGHT 처리
                    rowElement.attrib[columnName] = str(row[columnName])

        ET.ElementTree(rootElement).write('player.xml', encoding='utf-8', xml_declaration=True)
