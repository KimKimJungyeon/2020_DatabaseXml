import sys, datetime
from PyQt5.QtWidgets import *
import pymysql

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Report")
        self.setGeometry(200, 200, 800, 800) #위치, 크기 세팅

        # 기본적으로 필요한 모든 위젯 생성

        # 선수검색 파트===================================================
        """
        1) 선수검색이라는 일반 라벨
        2) 팀명 라벨, 팀명용 입력칸, 포지션 라벨, 포지션 입력칸, 출신국 라벨, 출신국 입력칸, 초기화 버튼
        3) 키 라벨, 키용 입력칸, 이상 이하 체크버튼, 몸무게 라벨, 몸무게 입력칸, 이상 이하 체크버튼, 검색 버튼
        4) 선수들 결과창
        """
        #라벨 모음
        self.MainLabel1= QLabel("선수검색") #선수검색
        self.TeamnameLabel= QLabel("팀명 : ") #팀명
        self.PositionLabel = QLabel("포지션 : ") #포지션
        self.CountryLabel = QLabel("출신국 : ") #출신국
        self.HeightLabel = QLabel("키 : ") #키(height)
        self.WeightLabel = QLabel("몸무게 : ") #몸무게

        #콤보 박스 목록
        self.TeamnameCbbox = QComboBox(self) #팀이름 콤보박스
        self.PositionCbbox = QComboBox(self)  # 포지션 콤보박스
        self.CountryCbbox = QComboBox(self)  # 출신국 콤보박스
        self.HeightCbbox = QComboBox(self)  # 키 콤보박스
        self.WeightCbbox = QComboBox(self)  # 몸무게 콤보박스

        """
        콤보박스에 내용물을 추가하는건 for문을 이용하여
        self.Teamname.addItem('~~')식으로 하여 추가한다.
        """

        #푸시버튼 모음
        self.ResetBtn = QPushButton("초기화") #초기화 버튼
        self.searchBtn = QPushButton("검색") #검색 버튼

        #라디오버튼 모음
        self.HeightUpBtn = QRadioButton("이상", self) #키의 이상
        self.HeightDnBtn = QRadioButton("이하", self) #키의 이하
        self.WeightUpBtn = QRadioButton("이상", self) #몸무게의 이상
        self.WeightDnBtn = QRadioButton("이하", self) #몸무게의 이하

        # 파일출력 파트 ===================================================
        """
        1) 파일출력이라는 일반 라벨
        2) CSV, JSON, XML 선택 체크 버튼, 저장 버튼
        """

        #라벨 모음
        self.MainLabel2 = QLabel("파일출력")  # 파일출력

        # 라디오버튼 모음
        self.CsvRdbtn = QRadioButton("CSV", self)  #CSV
        self.JsonRdbtn = QRadioButton("JSON", self)  #JSON
        self.XmlRdbtn = QRadioButton("XML", self)  #XML

        # 푸시버튼 모음
        self.SaveBtn = QPushButton("저장")  # 저장 버튼

        # 레이아웃 생성, 위젯 연결, 레이아웃 설정
        Layout = QVBoxLayout()

        Layout.addWidget(self.pushButton1)
        Layout.addWidget(self.pushButton2)
        Layout.addWidget(self.label)

        self.setLayout(Layout)

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()