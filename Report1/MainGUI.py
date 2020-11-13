import sys, datetime
from PyQt5.QtWidgets import *
import Report1.DBSearch as DBSearch


#Main window구현
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        self.setWindowTitle("Report")
        self.setGeometry(500, 100, 700, 800)  # 위치, 크기 세팅
        self.TeamnameValue = '사용안함'
        self.PositionValue = '사용안함'
        self.WeightValue = '사용안함'
        self.HeightValue = '사용안함'
        self.CountryValue = '사용안함'
        self.Warning = QMessageBox

        # 기본적으로 필요한 모든 위젯 생성

        # 선수검색 파트====================================================

        # 라벨 모음
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

        # 푸시버튼 모음
        self.ResetBtn = QPushButton("초기화")  # 초기화 버튼
        self.searchBtn = QPushButton("검색")  # 검색 버튼

        # 라디오버튼 모음
        self.HeightUpBtn = QRadioButton("이상", self)  # 키의 이상
        self.HeightDnBtn = QRadioButton("이하", self)  # 키의 이하

        #라디오 버튼 모음2
        self.WeightUpBtn = QRadioButton("이상", self)  # 몸무게의 이상
        self.WeightDnBtn = QRadioButton("이하", self)  # 몸무게의 이하

        # 파일출력 파트 ===================================================

        # 라디오버튼 모음
        self.CsvRdbtn = QRadioButton("CSV", self)  # CSV
        self.JsonRdbtn = QRadioButton("JSON", self)  # JSON
        self.XmlRdbtn = QRadioButton("XML", self)  # XML

        # 푸시버튼 모음
        self.SaveBtn = QPushButton("저장")  # 저장 버튼

        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        #self.tableWidget.resize(1000, 500)

        # 레이아웃 생성 ====================================================

        #선수검색 부분 세팅 ======================================
        self.GroupBox1 = QGroupBox("선수검색") # 선수검색들 묶어둘 녀석
        self.BigLayout = QVBoxLayout(self)
        self.PlLayout1 = QHBoxLayout(self) #선수검색 첫번째줄(팀명~출신국 까지)
        self.PlLayout1.addWidget(self.TeamnameLabel)
        self.PlLayout1.addWidget(self.TeamnameCbbox)
        self.PlLayout1.addWidget(self.PositionLabel)
        self.PlLayout1.addWidget(self.PositionCbbox)
        self.PlLayout1.addWidget(self.CountryLabel)
        self.PlLayout1.addWidget(self.CountryCbbox)

        self.PlLayout2 = QHBoxLayout(self) #선수검색 두번째줄(키~ 몸무게)
        self.HgtGroupBox = QGroupBox()  # 키 이상,이하 체크때문에 나눔
        self.HgtLayout = QHBoxLayout(self)#키 세팅
        self.HgtLayout.addWidget(self.HeightLabel)
        self.HgtLayout.addWidget(self.HeightCbbox)
        self.HgtLayout.addWidget(self.HeightUpBtn)
        self.HgtLayout.addWidget(self.HeightDnBtn)
        self.HgtGroupBox.setLayout(self.HgtLayout)
        self.HeightUpBtn.setChecked(True)

        self.WgtGroupBox= QGroupBox() #몸무게 이상, 이하 체크때문에 나눔
        self.WgtLayout = QHBoxLayout(self)#몸무게 세팅
        self.WgtLayout.addWidget(self.WeightLabel)
        self.WgtLayout.addWidget(self.WeightCbbox)
        self.WgtLayout.addWidget(self.WeightUpBtn)
        self.WgtLayout.addWidget(self.WeightDnBtn)
        self.WgtGroupBox.setLayout(self.WgtLayout)
        self.WeightUpBtn.setChecked(True)

        self.PlLayout2.addWidget(self.HgtGroupBox)
        self.PlLayout2.addWidget(self.WgtGroupBox)

        self.PlInputLayout = QVBoxLayout(self) #선수검색(입력용)
        self.PlInputLayout.addLayout(self.PlLayout1)
        self.PlInputLayout.addLayout(self.PlLayout2)

        self.BtnLayout1 = QHBoxLayout(self) #선수검색 버튼 (리셋)
        self.BtnLayout1.addWidget(self.ResetBtn)
        self.BtnLayout2 = QHBoxLayout(self)
        self.BtnLayout2.addWidget(self.searchBtn) #선수검색 버튼(검색)

        self.PlBtnLayout= QVBoxLayout(self)
        self.PlBtnLayout.addLayout(self.BtnLayout1)
        self.PlBtnLayout.addLayout(self.BtnLayout2)

        self.PlLayer= QHBoxLayout(self)
        self.PlLayer.addLayout(self.PlInputLayout)
        self.PlLayer.addLayout(self.PlBtnLayout)
        self.GroupBox1.setLayout(self.PlLayer)

        self.PLLayout = QHBoxLayout(self)
        self.PLLayout.addWidget(self.GroupBox1)

        #검색된 선수들 출력될 부분 ============================
        self.TableLayout = QHBoxLayout(self) #결과창 나올부분
        self.TableLayout.addWidget(self.tableWidget)

        self.GroupBox2= QGroupBox("파일 출력")

        #파일 출력파트 세팅 ===============================
        self.FlLayout1= QHBoxLayout(self)
        self.FlLayout1.addWidget(self.CsvRdbtn)
        self.FlLayout1.addWidget(self.JsonRdbtn)
        self.FlLayout1.addWidget(self.XmlRdbtn)
        self.FlBtnLayout= QHBoxLayout(self)
        self.FlBtnLayout.addWidget(self.SaveBtn)
        self.CsvRdbtn.setChecked(True)

        self.FLlayer= QHBoxLayout(self)
        self.FLlayer.addLayout(self.FlLayout1)
        self.FLlayer.addLayout(self.FlBtnLayout)
        self.GroupBox2.setLayout(self.FLlayer)

        self.FLLayout = QHBoxLayout(self)
        self.FLLayout.addWidget(self.GroupBox2)

        self.BigLayout.addLayout(self.PLLayout)
        self.BigLayout.addLayout(self.TableLayout)
        self.BigLayout.addLayout(self.FLLayout)

        self.setLayout(self.BigLayout)

        #팀명 콤보박스 내용 추가
        query = DBSearch.DB_Query()

        rows = query.selectTeamName()
        columnName = list(rows[0].keys())[0]
        self.TeamNameitems = ['없음' if row[columnName] == None else row[columnName] for row in rows]
        self.TeamNameitems.sort()
        self.TeamNameitems.insert(0,'사용안함')
        self.TeamnameCbbox.addItems(self.TeamNameitems)
        self.TeamnameCbbox.activated.connect(self.TeamnameCbbox_Activated)

        #포지션 콤보박스 내용추가
        rows = query.selectPlayerPosition()
        columnName = list(rows[0].keys())[0]
        self.Positionitems = ['미정' if row[columnName] == None else row[columnName] for row in rows]
        self.Positionitems.sort()
        self.Positionitems.insert(0, '사용안함')
        self.PositionCbbox.addItems(self.Positionitems)
        self.PositionCbbox.activated.connect(self.PositionCbbox_Activated)

        #출신국 콤보박스 내용추가
        rows = query.selectPlayerCountry()
        columnName = list(rows[0].keys())[0]
        self.Countryitems = ['대한민국' if row[columnName] == None else row[columnName] for row in rows]
        self.Countryitems.sort()
        self.Countryitems.insert(0, '사용안함')
        self.CountryCbbox.addItems(self.Countryitems)
        self.CountryCbbox.activated.connect(self.CountryCbbox_Activated)

        # 키 콤보박스 내용추가
        rows = query.selectPlayerHeight()
        columnName = list(rows[0].keys())[0]
        self.Heightitems = ['미측정' if row[columnName] == None else str(row[columnName]) for row in rows]
        self.Heightitems.sort()
        self.Heightitems.insert(0, '사용안함')
        self.HeightCbbox.addItems(self.Heightitems)
        self.HeightCbbox.activated.connect(self.HeightCbbox_Activated)

        # 몸무게 콤보박스 내용추가
        rows = query.selectPlayerWeight()
        columnName = list(rows[0].keys())[0]
        self.Weightitems = ['미측정' if row[columnName] == None else str(row[columnName]) for row in rows]
        self.Weightitems.sort()
        self.Weightitems.insert(0, '사용안함')
        self.WeightCbbox.addItems(self.Weightitems)
        self.WeightCbbox.activated.connect(self.WeightCbbox_Activated)
        #외형 구현 완료
        self.searchBtn.clicked.connect(self.SearchButton_Clicked)
        self.ResetBtn.clicked.connect(self.ResetButton_Clicked)
        self.SaveBtn.clicked.connect(self.SaveBtn_Clicked)

#==================외형, 클릭 이벤트 정리========================================
    def TeamnameCbbox_Activated(self):
        self.TeamnameValue = self.TeamnameCbbox.currentText()  # TeamNameValue를 통해 선택한 팀명 값을 전달

    def PositionCbbox_Activated(self):
        self.PositionValue = self.PositionCbbox.currentText()  # PositionValue를 통해 선택한 포지션 값을 전달

    def CountryCbbox_Activated(self):
        self.CountryValue = self.CountryCbbox.currentText() #CountryValue를 통해 선택한 출신국 값을 전달

    def HeightCbbox_Activated(self):
        self.HeightValue = self.HeightCbbox.currentText() #HeightValue를 통해 선택한 키 값을 전달

    def WeightCbbox_Activated(self):
        self.WeightValue = self.WeightCbbox.currentText() #WeightValue를 통해 선택한 몸무게 값을 전달

    def ResetButton_Clicked(self):
        self.HeightUpBtn.setChecked(True)
        self.WeightUpBtn.setChecked(True)
        self.TeamnameCbbox.clear()
        self.TeamnameCbbox.addItems(self.TeamNameitems)
        self.PositionCbbox.clear()
        self.PositionCbbox.addItems(self.Positionitems)
        self.CountryCbbox.clear()
        self.CountryCbbox.addItems(self.Countryitems)
        self.HeightCbbox.clear()
        self.HeightCbbox.addItems(self.Heightitems)
        self.WeightCbbox.clear()
        self.WeightCbbox.addItems(self.Weightitems)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

    def SearchButton_Clicked(self):
        # DB 검색문 실행
        query = DBSearch.DB_Query()
        if self.TeamnameValue != '사용안함':
            players = query.selectPLTeamName(self.TeamnameValue)
        elif self.PositionValue != '사용안함':
            players= query.selectPLPosition(self.PositionValue)
        elif self.CountryValue != '사용안함':
            players= query.selectPLCountry(self.CountryValue)
        elif self.HeightValue != '사용안함' and self.HeightUpBtn.isChecked(): #이상으로 검색했는가
            players= query.selectPLUpHeight(self.HeightValue)
        elif self.HeightValue != '사용안함' and self.HeightDnBtn.isChecked(): #이상으로 검색했는가
            players= query.selectPLDnHeight(self.HeightValue)
        elif self.WeightValue != '사용안함' and self.WeightUpBtn.isChecked():
            players= query.selectPLUpWeight(self.WeightValue)
        elif self.WeightValue != '사용안함' and self.WeightDnBtn.isChecked():
            players= query.selectPLDnWeight(self.WeightValue)
        else:
            self.Warning.question(self, 'Warning', "검색할 것을 선택해주세요.", QMessageBox.Yes)
            return

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
                if v == None:  # 파이썬이 DB의 널값을 None으로 변환함.
                    continue  # QTableWidgetItem 객체를 생성하지 않음
                elif isinstance(v, datetime.date):  # QTableWidgetItem 객체 생성
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                else:
                    item = QTableWidgetItem(str(v))
                self.tableWidget.setItem(rowIDX, columnIDX, item)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def SaveBtn_Clicked(self):
        #뭘 검색했는가
        query = DBSearch.DB_Query()
        if self.TeamnameValue != '사용안함':
            players = query.selectPLTeamName(self.TeamnameValue)
        elif self.PositionValue != '사용안함':
            players = query.selectPLPosition(self.PositionValue)
        elif self.CountryValue != '사용안함':
            players = query.selectPLCountry(self.CountryValue)
        elif self.HeightValue != '사용안함' and self.HeightUpBtn.isChecked():  # 이상으로 검색했는가
            players = query.selectPLUpHeight(self.HeightValue)
        elif self.HeightValue != '사용안함' and self.HeightDnBtn.isChecked():  # 이상으로 검색했는가
            players = query.selectPLDnHeight(self.HeightValue)
        elif self.WeightValue != '사용안함' and self.WeightUpBtn.isChecked():
            players = query.selectPLUpWeight(self.WeightValue)
        elif self.WeightValue != '사용안함' and self.WeightDnBtn.isChecked():
            players = query.selectPLDnWeight(self.WeightValue)
        else:
            self.Warning.question(self, 'Warning', "검색할 것을 선택해주세요.", QMessageBox.Yes)
            return

        file = DBSearch.FileOutput()

        if self.CsvRdbtn.isChecked():
            file.readDB_writeCSV(players)
        elif self.JsonRdbtn.isChecked():
            file.readDB_writeJSON(players)
        elif self.XmlRdbtn.isChecked():
            file.readDB_writeXML(players)
        else:
            self.Warning.question(self, 'Warning', "출력방식을 선택해주세요.", QMessageBox.Yes)
            return

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()