import pymysql

import sys, datetime
from PyQt5.QtWidgets import *

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

#Main window구현
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Report")
        self.setGeometry(200, 200, 1200, 700)  # 위치, 크기 세팅

        # 기본적으로 필요한 모든 위젯 생성

        # 선수검색 파트===================================================
        """
        1) 선수검색이라는 일반 라벨
        2) 팀명 라벨, 팀명용 입력칸, 포지션 라벨, 포지션 입력칸, 출신국 라벨, 출신국 입력칸, 초기화 버튼
        3) 키 라벨, 키용 입력칸, 이상 이하 체크버튼, 몸무게 라벨, 몸무게 입력칸, 이상 이하 체크버튼, 검색 버튼
        4) 선수들 결과창
        """
        # 라벨 모음
        self.MainLabel1 = QLabel("선수검색")  # 선수검색
        self.MainLabel1.move(200, 50)
        self.MainLabel1.resize(100, 20)
        self.TeamnameLabel = QLabel("팀명 : ")  # 팀명
        self.PositionLabel = QLabel("포지션 : ")  # 포지션
        self.CountryLabel = QLabel("출신국 : ")  # 출신국
        self.HeightLabel = QLabel("키 : ")  # 키(height)
        self.WeightLabel = QLabel("몸무게 : ")  # 몸무게

        # 콤보 박스 목록
        self.TeamnameCbbox = QComboBox(self)  # 팀이름 콤보박스
        self.PositionCbbox = QComboBox(self)  # 포지션 콤보박스
        self.CountryCbbox = QComboBox(self)  # 출신국 콤보박스
        self.HeightCbbox = QComboBox(self)  # 키 콤보박스
        self.WeightCbbox = QComboBox(self)  # 몸무게 콤보박스

        """
        콤보박스에 내용물을 추가하는건 for문을 이용하여
        self.Teamname.addItem('~~')식으로 하여 추가한다.
        """

        # 푸시버튼 모음
        self.ResetBtn = QPushButton("초기화")  # 초기화 버튼
        self.searchBtn = QPushButton("검색")  # 검색 버튼

        # 라디오버튼 모음
        self.HeightUpBtn = QRadioButton("이상", self)  # 키의 이상
        self.HeightDnBtn = QRadioButton("이하", self)  # 키의 이하
        self.WeightUpBtn = QRadioButton("이상", self)  # 몸무게의 이상
        self.WeightDnBtn = QRadioButton("이하", self)  # 몸무게의 이하

        # 파일출력 파트 ===================================================
        """
        1) 파일출력이라는 일반 라벨
        2) CSV, JSON, XML 선택 체크 버튼, 저장 버튼
        """

        # 라벨 모음
        self.MainLabel2 = QLabel("파일출력")  # 파일출력

        # 라디오버튼 모음
        self.CsvRdbtn = QRadioButton("CSV", self)  # CSV
        self.JsonRdbtn = QRadioButton("JSON", self)  # JSON
        self.XmlRdbtn = QRadioButton("XML", self)  # XML

        # 푸시버튼 모음
        self.SaveBtn = QPushButton("저장")  # 저장 버튼

        # 콤보박스 설정
        self.comboBox = QComboBox(self)

        # DB 검색문 실행
        query = DB_Query()
        rows = query.selectPlayerPosition()        # rows은 dictionary의 리스트
        # [{'position': 'DF'}, {'position': 'FW'}, {'position': None}, {'position': 'MF'}, {'position': 'GK'}]

        columnName = list(rows[0].keys())[0]
        items = ['없음' if row[columnName] == None else row[columnName] for row in rows]
        self.comboBox.addItems(items)

        # for row in rows:
        #     item = list(row.values()).pop(0)
        #     if item == None:
        #         self.comboBox.addItem('없음')
        #     else:
        #         self.comboBox.addItem(item)

        self.comboBox.move(300, 50)
        self.comboBox.resize(100, 20)
        self.comboBox.activated.connect(self.comboBox_Activated)

        # 푸쉬버튼 설정
        self.pushButton = QPushButton("Search", self)
        self.pushButton.move(600, 50)
        self.pushButton.resize(100, 20)
        self.pushButton.clicked.connect(self.pushButton_Clicked)

        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        self.tableWidget.move(50, 100)
        self.tableWidget.resize(1000, 500)

    def comboBox_Activated(self):

        self.positionValue = self.comboBox.currentText()  # positionValue를 통해 선택한 포지션 값을 전달

    def pushButton_Clicked(self):
        # DB 검색문 실행
        query = DB_Query()
        players = query.selectPlayer(self.positionValue)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(players))
        self.tableWidget.setColumnCount(len(players[0]))
        columnNames = list(players[0].keys())
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for rowIDX in range(len(players)):
            player = players[rowIDX]

            for k, v in player.items():
                columnIDX = columnNames.index(k)

                if v == None:           # 파이썬이 DB의 널값을 None으로 변환함.
                    continue            # QTableWidgetItem 객체를 생성하지 않음
                elif isinstance(v, datetime.date):      # QTableWidgetItem 객체 생성
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                else:
                    item = QTableWidgetItem(str(v))

                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

