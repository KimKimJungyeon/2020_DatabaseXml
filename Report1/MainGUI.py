import sys, datetime
from PyQt5.QtWidgets import *
#import Report1.DBSearch as DBSearch


#Main window구현
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Report")
        self.setGeometry(400, 200, 1100, 800)  # 위치, 크기 세팅

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
        self.WeightUpBtn = QRadioButton("이상", self)  # 몸무게의 이상
        self.WeightDnBtn = QRadioButton("이하", self)  # 몸무게의 이하

        # 파일출력 파트 ===================================================

        # 라디오버튼 모음
        self.CsvRdbtn = QRadioButton("CSV", self)  # CSV
        self.JsonRdbtn = QRadioButton("JSON", self)  # JSON
        self.XmlRdbtn = QRadioButton("XML", self)  # XML

        # 푸시버튼 모음
        self.SaveBtn = QPushButton("저장")  # 저장 버튼
        #self.SaveBtn.clicked.connect(self.pushButton_Clicked)

        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        #self.tableWidget.resize(1000, 500)

        # 레이아웃 생성 ====================================================
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
        self.PlLayout2.addWidget(self.HeightLabel)
        self.PlLayout2.addWidget(self.HeightCbbox)
        self.PlLayout2.addWidget(self.HeightUpBtn)
        self.PlLayout2.addWidget(self.HeightDnBtn)
        self.PlLayout2.addWidget(self.WeightLabel)
        self.PlLayout2.addWidget(self.WeightCbbox)
        self.PlLayout2.addWidget(self.WeightUpBtn)
        self.PlLayout2.addWidget(self.WeightDnBtn)

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

        self.TableLayout = QHBoxLayout(self) #결과창 나올부분
        self.TableLayout.addWidget(self.tableWidget)

        self.GroupBox2= QGroupBox("파일 출력")

        self.FlLayout1= QHBoxLayout(self)
        self.FlLayout1.addWidget(self.CsvRdbtn)
        self.FlLayout1.addWidget(self.JsonRdbtn)
        self.FlLayout1.addWidget(self.XmlRdbtn)
        self.FlBtnLayout= QHBoxLayout(self)
        self.FlBtnLayout.addWidget(self.SaveBtn)

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


    """
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
        self.tableWidget.resizeRowsToContents()"""

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
