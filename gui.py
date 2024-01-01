import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.main_box_layout = QVBoxLayout()
        self.game_table_box = QGroupBox("테이블")
        self.info_box_layout = QHBoxLayout()
        self.player_info_box = QGroupBox("플레이어 정보")
        self.game_info_box = QGroupBox("게임 정보")

        # 셋 다 Horizon 레이아웃으로 설정할 것.
        self.dealer_playing_box = QGroupBox("딜러")
        self.player_playing_box = QGroupBox("플레이어")
        self.control_playing_box = QGroupBox("게임 컨트롤")

        ## 테이블에 사용될 변수들을 선언합니다.
        self.dealer_hand_layout = QHBoxLayout()
        self.dealer_status = QLineEdit()
        self.player_hand_layout = QHBoxLayout()
        self.player_score = QLineEdit()
        self.player_betting_sum = QLineEdit()
        self.player_control_btn = [QPushButton("HIT"), QPushButton("STOP"), QPushButton("STAY")]

        ## 플레이어 정보에 사용될 변수들을 선언합니다.
        self.player_name = QLineEdit()
        self.sum_of_chips = QLineEdit()
        self.num_of_chip = []
        for i in range(8):
            self.num_of_chip.append(QLineEdit())
        self.chip_info_btn = QPushButton("칩 정보")

        ## 게임 정보에 사용될 변수들을 선언합니다.
        self.num_of_dec = QSpinBox()
        self.num_of_dec.setRange(1, 6)
        self.player_betting_chips = []
        for i in range(8):
            self.player_betting_chips.append(QSpinBox)
        self.playing_start_btn = [QPushButton("초기화"), QPushButton("시작")]

        self.info_box_layout.addWidget(self.player_info_box, 2)
        self.info_box_layout.addWidget(self.game_info_box, 3)

        self.main_box_layout.addWidget(self.game_table_box, 11)
        self.main_box_layout.addLayout(self.info_box_layout, 4)

        self.init_UI()
    def init_UI(self):
        self.setWindowTitle('BLACKJACK GAME')
        self.setFixedSize(1000, 750)
        self.setLayout(self.main_box_layout)
        self.set_window_center()
        self.setFont(QFont('SanSerif', 9))

        self.create_game_table_box()

        self.show()
    def set_window_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def create_game_table_box(self):
        tmp_horizontal_dealer_layout = QHBoxLayout()
        tmp_horizontal_dealer_layout.addLayout(self.dealer_hand_layout, 3)
        tmp_horizontal_dealer_layout.addWidget(self.dealer_status, 1)
        self.dealer_playing_box.setLayout(tmp_horizontal_dealer_layout)

        tmp_horizontal_player_layout = QHBoxLayout()
        tmp_horizontal_player_layout.addLayout(self.player_hand_layout)
        self.player_playing_box.setLayout(tmp_horizontal_player_layout)

        tmp_horizontal_control_layout = QHBoxLayout()
        tmp_vertical_betting_sum_layout = QVBoxLayout()
        tmp_vertical_betting_sum_layout.addWidget(QLabel("> 베팅 금액"), 1)
        tmp_vertical_betting_sum_layout.addWidget(self.player_betting_sum, 1)
        tmp_betting_sum_box = QGroupBox()
        tmp_betting_sum_box.setLayout(tmp_vertical_betting_sum_layout)

        self.player_control_btn[0].setSizePolicy(self.control_playing_box.sizePolicy().horizontalPolicy(), self.control_playing_box.sizePolicy().verticalPolicy())
        self.player_control_btn[1].setSizePolicy(self.control_playing_box.sizePolicy().horizontalPolicy(), self.control_playing_box.sizePolicy().verticalPolicy())
        self.player_control_btn[2].setSizePolicy(self.control_playing_box.sizePolicy().horizontalPolicy(), self.control_playing_box.sizePolicy().verticalPolicy())

        tmp_horizontal_control_layout.addWidget(self.player_control_btn[0], 2)
        tmp_horizontal_control_layout.addWidget(self.player_control_btn[1], 2)
        tmp_horizontal_control_layout.addWidget(self.player_control_btn[2], 2)
        tmp_horizontal_control_layout.addWidget(tmp_betting_sum_box, 1)
        self.control_playing_box.setLayout(tmp_horizontal_control_layout)

        tmp_grid_table_layout = QGridLayout()
        tmp_grid_table_layout.addWidget(self.dealer_playing_box, 0, 0)
        tmp_grid_table_layout.addWidget(self.player_playing_box, 1, 0)
        tmp_grid_table_layout.addWidget(self.control_playing_box, 2, 0)
        tmp_grid_table_layout.setRowStretch(0, 2)
        tmp_grid_table_layout.setRowStretch(1, 2)
        tmp_grid_table_layout.setRowStretch(2, 1)
        self.game_table_box.setLayout(tmp_grid_table_layout)

    def create_player_info_box(self):
        print()
    def create_game_info_box(self):
        print()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())