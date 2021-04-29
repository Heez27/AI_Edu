import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from Kiwoom import *
import time

form_class = uic.loadUiType("pytrader.ui")[0] # pytrader.ui 실행

class MyWindow(QMainWindow, form_class):
    # QMainWindow: QWidget 상속하는 클래스(위젯 사용할 수 있도록), form_class: pytrader.ui
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.kiwoom = Kiwoom() # Kiwoom 인스턴스 생성
        self.kiwoom.comm_connect() # 로그인

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.timer2 = QTimer(self)
        self.timer2.start(1000 *10)
        self.timer2.timeout.connect(self.timeout2)

        accouns_num = int(self.kiwoom.get_login_info("ACCOUNT_CNT")) # 보유계좌 갯수 (ex. 2)
        accounts = self.kiwoom.get_login_info("ACCNO") # 구분자 ';'로 연결된 보유계좌 목록을 반환 (ex. 8165088111;8753740831;)

        accounts_list = accounts.split(';')[0:accouns_num] # 계좌번호를 리스트로 저장
        self.comboBox.addItems(accounts_list) # 계좌번호를 comboBox에 넣음

        self.lineEdit.textChanged.connect(self.code_changed) # 종목코드 입력시
        self.pushButton.clicked.connect(self.send_order) # [현금주문] 버튼 누를시
        self.pushButton_2.clicked.connect(self.check_balance) # [조회] 버튼 누를시

    def code_changed(self):
        code = self.lineEdit.text() # 변경된 종목코드 text 받아서
        name = self.kiwoom.get_master_code_name(code) # 종목코드에 맞는 종목명을 받아옴
        self.lineEdit_2.setText(name) # 종목명 보여줌

    def send_order(self):
        order_type_lookup = {'신규매수': 1, '신규매도': 2, '매수취소': 3, '매도취소': 4}
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        account = self.comboBox.currentText() # 계좌번호
        order_type = self.comboBox_2.currentText() # 신규매수/신규매도/매수취소/매도취소
        code = self.lineEdit.text() # 종목코드
        hoga = self.comboBox_3.currentText() # 지정가/시장가
        num = self.spinBox.value() # 수량
        price = self.spinBox_2.value() # 가격

        self.kiwoom.send_order("send_order_req", "0101", account, order_type_lookup[order_type], code, num, price, hoga_lookup[hoga], "")

    def timeout(self): # 화면 왼쪽 아래에 서버 연결 여부와 현재시간 출력
        current_time = QTime.currentTime()
        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간: " + text_time

        state = self.kiwoom.get_connect_state()
        if state == 1:
            state_msg = "서버 연결 중"
        else:
            state_msg = "서버 미 연결 중"

        self.statusbar.showMessage(state_msg + " | " + time_msg)

    def timeout2(self): # 실시간 계좌정보 조회 여부
        if self.checkBox.isChecked():
            self.check_balance()

    def check_balance(self): # 계좌정보 조회
        self.kiwoom.reset_opw00018_output()
        account_number = self.kiwoom.get_login_info("ACCNO")
        account_number = account_number.split(';')[0]

        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 0, "2000")

        while self.kiwoom.remained_data:
            time.sleep(0.2)
            self.kiwoom.set_input_value("계좌번호", account_number)
            self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 2, "2000")

        # opw00001
        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00001_req", "opw00001", 0, "2000")

        # balance
        item = QTableWidgetItem(self.kiwoom.d2_deposit)
        item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tableWidget.setItem(0, 0, item)

        for i in range(1, 6):
            item = QTableWidgetItem(self.kiwoom.opw00018_output['single'][i - 1])
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
            self.tableWidget.setItem(0, i, item)

        self.tableWidget.resizeRowsToContents()

        # Item list
        item_count = len(self.kiwoom.opw00018_output['multi'])
        self.tableWidget_2.setRowCount(item_count)

        for j in range(item_count):
            row = self.kiwoom.opw00018_output['multi'][j]
            for i in range(len(row)):
                item = QTableWidgetItem(row[i])
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.tableWidget_2.setItem(j, i, item)

        self.tableWidget_2.resizeRowsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv) # QApplication 클래스에 대한 인스턴스 생성 후, app이라는 변수로 바인딩
                                # app은 GUI 프로그램을 전반적으로 제어하는 역할을 함
    myWindow = MyWindow()
    myWindow.show()
    app.exec_() # 이벤트 루프에 진입으로 프로그램 종료되지 않게함