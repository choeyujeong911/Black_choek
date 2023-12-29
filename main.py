import math
import random
import time

# 플레이어의 이름 리스트를 상수로 정의합니다.
LAST_NAME_LIST = ["Kim", "Choe", "Park", "Lee", "Seo", "Jeon"]

# 블랙잭의 딜러를 정의하는 클래스입니다.
class Dealer:
    def __init__(self, name: str, wanna_control: bool):
        self.name = name
        self.controllable = bool(wanna_control)

# 블랙잭의 플레이어 한 명을 정의하는 클래스입니다.
class Player:
    def __init__(self, name: str, play_type: int, wanna_control: bool, total_chips: int):
        '''
        플레이어의 이름과 플레이 성격을 정의합니다.
        :param name: 플레이어의 이름입니다.
        :param play_type: 게임에 플레이 스타일입니다. COM 플레이어의 경우 0에서 2 사이의 정수값을 가지며, 숫자가 클 수록 해당 플레이어는 과감한 플레이를 하게 됩니다. 유저가 직접 조종하는 플레이어의 경우 값이 -1로 고정됩니다.
        :param wanna_control: 유저의 조종 가능 여부입니다.
        :param total_chips: 플레이어가 현재 보유한 칩의 총 개수입니다. 게임을 진행하며 변경될 수 있습니다.
        '''
        self.name = name
        if int(type) > 2 or int(type) < 0:
            print("Error: No Such Mode !\nField <play_type> should be in list(0, 1, 2)")
        else:
            self.play_type = int(play_type)
        self.controllable = bool(wanna_control)
        self.total_chips = int(total_chips)

        # 판 당 플레이어가 베팅할 고정 칩 개수를 정의합니다.
        # play_typed의 값이 클수록 베팅하는 금액이 커집니다.
        if wanna_control:
            self.sum_of_betting = int(input("한 게임 당 얼마를 베팅하시겠습니까? >> "))
        else:
            self.sum_of_betting = int(10 + (self.play_type * 5))


# 블랙잭 게임 전체의 속성을 담은 클래스입니다.
class GameStyle:
    def __init__(self, num_of_mem: int, controllable_dealer: bool, debug_mode: bool):
        '''
        게임의 속성을 정의합니다.
        :param num_of_mem: 게임에 참여할 플레이어의 수입니다.
        :param controllable_dealer: 딜러를 조종할 것인지 정합니다.
        :param debug_mode: 일반 게임/개발자를 위한 디버깅 모드를 설정하는 변수입니다. 값이 True일 시, 모든 참여자의 성격과 카드를 열람할 수 있습니다.
        '''
        self.num_of_mem = int(num_of_mem)
        self.debug_mode = bool(debug_mode)

        # 딜러를 생성합니다.
        # 참고: 딜러는 베팅하지 않으므로 플레이어에 포함하지 않습니다.
        if controllable_dealer:
            dealer_name = str(input("딜러를 조종하는 게임입니다.\n딜러의 이름을 입력하십시오. >> "))
        else:
            dealer_name = "Dealer"
        # 유저가 설정한 옵션대로 딜러를 정의합니다.
        self.dealer = Dealer(dealer_name, controllable_dealer)
        
        # 플레이어 묶음을 생성합니다.
        self.player_list = []
        # 플레이어 수만큼 플레이어를 생성합니다.
        for i in range(self.num_of_mem):
            player = self.do_you_wanna_control()
            self.player_list.append(player)
    def exe_debug_mode(self):
        '''
        턴이 끝날 때마다 모든 참여자의 성격과 카드를 콘솔에 출력합니다.
        일반 게임의 경우 해당 메소드는 작동하지 않습니다.
        :return: void
        '''
        print("")

    def do_you_wanna_control(self):
        while True:
            ch = str(input("게임에서 이 플레이어를 조종합니까? (Y|N) >> "))
            if ch == "Y" or ch == "y":
                control = True
                play_type = int(-1)
                play_type_str = "당신이 조종 가능"
                player_name = str(input("플레이어의 이름을 입력하십시오. >> "))
                start_chips = int(input(player_name + " 이/가 소지할 칩의 개수를 입력하십시오. >> "))
                break
            elif ch == "N" or ch == "n":
                control = False
                play_type = random.randint(0, 3)
                style = ["소심", "평범", "대담"]
                play_type_str = "컴퓨터가 조종하며, " + style[play_type]
                player_name = LAST_NAME_LIST.pop(random.randint(0, len(LAST_NAME_LIST)))
                start_chips = 500
                break
            else:
                print("잘못된 응답입니다. 다시 입력하십시오.")

        print("플레이어 {0}의 생성을 완료했습니다.\n{0} 은/는 {1}한 플레이어입니다.\n[칩 {2}개로 시작]\n".format(player_name, play_type_str, str(start_chips)))
        return Player(player_name, play_type, control, start_chips)

    def WhoIsWinner(self):
        print("")

# 블랙잭 게임 한 판을 담은 클래스입니다.
class Game:
    def __init__(self, game_style: GameStyle):
        self.current_status = game_style
    def update_status_of_players(self):
        ## 게임의 결과를 플레이어들의 보유 칩 개수에 반영하여 반환합니다.
        ## edit
        return self.current_status

if __name__ == '__main__':

    # 설정을 초기화합니다.
    num_of_players = 0
    num_of_games = 0
    dealer_control = False

    ## 프로그램을 안내합니다.
    print("블랙잭 게임을 1회 이상 진행하는 프로그램입니다.")
    print("한 판이 끝나도 플레이어의 속성은 초기화되지 않습니다.")
    print("설정한 횟수에 도달할 때까지 플레이어들은 보유한 칩을 걸며 게임을 진행합니다.")

    ## 게임의 옵션을 입력받습니다.
    # 플레이어의 수를 입력받습니다.
    while True:
        num_of_players = int(input("플레이어의 수(1 ~ 6)를 입력하십시오. >> "))
        if num_of_players >= 1 and num_of_players <= 6:
            break
        else:
            print("잘못된 입력입니다. 다시 입력하십시오.")

    # 진행할 게임의 횟수를 입력받습니다.
    while True:
        num_of_games = int(input("몇 판 진행하시겠습니까? (1 ~ 10) >> "))
        if num_of_games >= 1 and num_of_games <= 10:
            break
        else:
            print("잘못된 입력입니다. 다시 입력하십시오.")

    # 딜러를 조종하는 게임인지 묻습니다.
    while True:
        ch = str(input("딜러를 조종합니까? (Y|N) >> "))
        if ch == "Y" or ch == "y":
            dealer_control = True
            break
        else:
            break
    print("> > > > > 딜러와 플레이어를 생성중입니다. > > > > >")
    ## 게임의 옵션을 생성합니다.
    game_style = GameStyle(num_of_players, dealer_control, False)
    print("게임을 설정 완료했습니다.")
    print("설정한 횟수만큼 게임을 친행합니다.")
    print("*****-----*****-----*****-----*****-----*****")

    ## 설정한 횟수만큼 게임을 진행합니다.
    for i in num_of_games:
        print("{0}번째 게임입니다.".format(i))
        game = Game(game_style)
        game_style = game.update_status_of_players()
        ## 게임이 끝났으면 플레이어들의 칩 보유 현황을 알려줍니다.
        ## edit