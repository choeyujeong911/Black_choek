import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QImage
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main_box_layout = QVBoxLayout()
        self.game_table_box = QGroupBox("테이블")
        self.info_box_layout = QHBoxLayout()
        self.player_info_box = QGroupBox("플레이어 정보")
        self.game_info_box = QGroupBox("게임 정보")

        self.dealer_playing_box = QGroupBox("딜러")
        self.player_playing_box = QGroupBox("플레이어")
        self.control_playing_box = QGroupBox("게임 컨트롤")

        ## 카드 이미지는 배열로써 GUI에서 정의하지 않습니다.
        ## 백엔드에서 카드 드로우 후, 드로우한 카드에 해당하는 이미지를 그때그때 가져와 사용합니다.
        ## GUI에서는 딜러와 플레이어, 둘 다 카드를 놓을 공간만을 QImage 객체로써 최대 8장의 리스트로 정의합니다.
        self.dealer_card_img = []
        self.player_card_img = []
        for i in range(8):
            self.dealer_card_img.append(QImage())
            self.player_card_img.append(QImage())
        self.dealer_card_img[0] = QImage("./card_img/back.png")

        ## 테이블에 사용될 변수들을 선언합니다.
        self.dealer_hand_layout = QHBoxLayout()
        self.game_status = QTextEdit()
        self.game_status.setReadOnly(True)
        self.game_status.setText(self.game_status.toPlainText() + "> 블랙잭 게임을 시작합니다.\n")
        self.player_hand_layout = QHBoxLayout()
        self.player_score = QLineEdit()
        self.player_betting_sum = QLineEdit()
        self.player_betting_sum.setReadOnly(True)
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
        self.setLayout(self.main_box_layout)
        self.setWindowTitle('BLACKJACK GAME')
        self.setFixedSize(1500, 1125)
        self.setLayout(self.main_box_layout)
        self.set_window_center()
        self.setFont(QFont('SanSerif', 9))

        back_img_path = "back_img.png"
        back_img = QImage(back_img_path)
        back_img = back_img.scaled(QSize(1500, 1115))
        palette = QPalette()
        palette.setBrush(10, QBrush(back_img))
        self.setPalette(palette)
        self.setWindowIcon(QIcon("./chip_img/icon/chip_5.png"))

        self.create_game_table_box()

        self.show()
    def set_window_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def create_game_table_box(self):
        for i in range(8):
            vis_img = QLabel()
            vis_img.setPixmap(QPixmap.fromImage(self.dealer_card_img[i]))
            self.dealer_hand_layout.addWidget(vis_img)
            vis_img = QLabel()
            vis_img.setPixmap(QPixmap.fromImage(self.player_card_img[i]))
            self.player_hand_layout.addWidget(vis_img)

        tmp_horizontal_dealer_layout = QHBoxLayout()
        tmp_horizontal_dealer_layout.addLayout(self.dealer_hand_layout)
        self.dealer_playing_box.setLayout(tmp_horizontal_dealer_layout)

        tmp_horizontal_player_layout = QHBoxLayout()
        tmp_horizontal_player_layout.addLayout(self.player_hand_layout)
        self.player_playing_box.setLayout(tmp_horizontal_player_layout)

        tmp_horizontal_control_layout = QHBoxLayout()
        tmp_vertical_betting_sum_layout = QVBoxLayout()
        tmp_vertical_betting_sum_layout.addWidget(QLabel("> 베팅 금액"), 1)
        tmp_horizontal_betting_sum_layout = QHBoxLayout()
        tmp_horizontal_betting_sum_layout.addWidget(self.player_betting_sum)
        tmp_horizontal_betting_sum_layout.addWidget(QLabel("달러"))
        tmp_vertical_betting_sum_layout.addLayout(tmp_horizontal_betting_sum_layout, 1)
        tmp_betting_sum_box = QGroupBox()
        tmp_betting_sum_box.setLayout(tmp_vertical_betting_sum_layout)
        tmp_betting_sum_box.setStyleSheet("QGroupBox { border: 0; margin-top: 0px; }")

        self.player_control_btn[0].setSizePolicy(self.control_playing_box.sizePolicy().horizontalPolicy(), self.control_playing_box.sizePolicy().verticalPolicy())
        self.player_control_btn[1].setSizePolicy(self.control_playing_box.sizePolicy().horizontalPolicy(), self.control_playing_box.sizePolicy().verticalPolicy())
        self.player_control_btn[2].setSizePolicy(self.control_playing_box.sizePolicy().horizontalPolicy(), self.control_playing_box.sizePolicy().verticalPolicy())

        tmp_horizontal_control_layout.addWidget(self.player_control_btn[0], 2)
        tmp_horizontal_control_layout.addWidget(self.player_control_btn[1], 2)
        tmp_horizontal_control_layout.addWidget(self.player_control_btn[2], 2)
        tmp_horizontal_control_layout.addWidget(self.game_status, 3)
        tmp_horizontal_control_layout.addWidget(tmp_betting_sum_box, 3)
        self.control_playing_box.setLayout(tmp_horizontal_control_layout)

        tmp_vertical_table_layout = QVBoxLayout()
        tmp_vertical_table_layout.addWidget(self.dealer_playing_box, 2)
        tmp_vertical_table_layout.addWidget(self.player_playing_box, 2)
        tmp_vertical_table_layout.addWidget(self.control_playing_box, 1)
        self.game_table_box.setLayout(tmp_vertical_table_layout)

    def create_player_info_box(self):
        print()
    def create_game_info_box(self):
        print()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())