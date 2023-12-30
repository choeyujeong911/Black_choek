import math
import random
import time

# 플레이어의 이름 리스트를 상수로 정의합니다.
LAST_NAME_LIST = ["Kim", "Choe", "Park", "Lee", "Seo", "Jeon"]
MARK_LIST = ["하트", "다이아", "클로버", "스페이드"]
CARD_NAME_LIST = [" ACE", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", " 10", " J", " Q", " K"]

# 게임에 사용될 트럼프 카드 한 세트를 담고있는 클래스입니다.
class CardSet:
    def __init__(self, num: int):
        self.num_of_card_sets = int(num)
        self.total_of_cards = []
        one_set = self.generate_one_set_of_cards()
        for i in range(num): self.total_of_cards.append(one_set)
    def generate_one_set_of_cards(self):
        # 카드 리스트에는 문자열 형태의 숫자와 알파벳이 들어갑니다.
        heart_line = {}
        diamond_line = {}
        clover_line = {}
        spade_line = {}

        # 각 카드 라인을 정의합니다.
        for i in range(13):
            ch = str(i + 1)
            if i == 10:
                score = int(10)
            elif i == 11:
                score = int(10)
            elif i == 12:
                score = int(10)
            # 에이스 카드는 기본적으로 11점을 가집니다. 버스트 확정인 경우 점수는 11점에서 1점으로 내려갑니다.
            elif i == 0:
                score = int(11)
            else:
                score = int(i + 1)
            heart_line[ch] = score
            diamond_line[ch] = score
            clover_line[ch] = score
            spade_line[ch] = score

        cards_one_set = [heart_line, diamond_line, clover_line, spade_line]
        return cards_one_set

# 블랙잭의 딜러를 정의하는 클래스입니다.
class Dealer:
    def __init__(self, name: str, wanna_control: bool):
        self.name = name
        self.controllable = bool(wanna_control)
        self.hand = {}
        self.score = 0
        # NONE, BLACKJACK / BUST, 21
        self.result = "NONE"
        # -, STAY
        self.decision = "-"
        self.ace_get = False
        self.open_card = "Null"
        self.ace_card = "Null"
    def draw_first_cards(self, one_set_of_card: list):
        target_mark_index = int(random.randint(0, 3))
        target_mark_str = str(MARK_LIST[target_mark_index])
        target_mark = one_set_of_card[target_mark_index]    ## 타겟 마크는 한 문양의 카드로만 이루어진 딕셔너리 형태입니다.
        target_card_key = str(random.choice(list(target_mark.keys())))
        target_card_name = CARD_NAME_LIST[int(target_card_key) - 1]
        target_card_value = target_mark.pop(target_card_key)
        if int(target_card_value) == 11:
            self.ace_get = True
        self.hand[str(target_mark_str + target_card_name)] = int(target_card_value)
        self.score += int(target_card_value)
        one_set_of_card[target_mark_index] = target_mark    ## 덱에서 카드가 한 장 빠졌으니, 반영합니다.

        ## 첫 턴이므로 한 장을 더 뽑습니다.
        target_mark_index = int(random.randint(0, 3))
        target_mark_str = str(MARK_LIST[target_mark_index])
        target_mark = one_set_of_card[target_mark_index]  ## 타겟 마크는 한 문양의 카드로만 이루어진 딕셔너리 형태입니다.
        target_card_key = str(random.choice(list(target_mark.keys())))
        target_card_name = CARD_NAME_LIST[int(target_card_key) - 1]
        target_card_value = target_mark.pop(target_card_key)
        if int(target_card_value) == 11:
            self.ace_get = True
            self.ace_card = str(target_mark_str + target_card_name)
        self.hand[str(target_mark_str + target_card_name)] = int(target_card_value)
        self.score += int(target_card_value)
        one_set_of_card[target_mark_index] = target_mark  ## 덱에서 카드가 한 장 빠졌으니, 반영합니다.

        if self.score == 21:
            self.result = "BLACKJACK"
        else:
            ## 총 두 장의 패 중 한 장의 카드를 랜덤으로 골라 공개합니다.
            print("* 딜러의 패 중 한 장을 임의로 공개합니다.")
            self.open_card = random.choice(list(self.hand.keys()))
            print("* 공개된 카드는 {0} 카드입니다.".format(str(self.open_card)))

        return one_set_of_card  ## 카드를 뽑은 후의 덱의 상태를 반환합니다.
    def draw_card(self, one_set_of_card: list):
        if self.decision == "STAY":
            return one_set_of_card  ## 덱에서 카드를 뽑지 않고 그대로 반환합니다.
        target_mark_index = int(random.randint(0, 3))
        target_mark_str = str(MARK_LIST[target_mark_index])
        target_mark = one_set_of_card[target_mark_index]  ## 타겟 마크는 한 문양의 카드로만 이루어진 딕셔너리 형태입니다.
        target_card_key = str(random.choice(list(target_mark.keys())))
        target_card_name = CARD_NAME_LIST[int(target_card_key) - 1]
        target_card_value = target_mark.pop(target_card_key)
        self.hand[str(target_mark_str + target_card_name)] = int(target_card_value)
        self.score += int(target_card_value)
        if int(target_card_value) == 11:
            self.ace_get = True
            self.ace_card = str(target_mark_str + target_card_name)
        one_set_of_card[target_mark_index] = target_mark  ## 덱에서 카드가 한 장 빠졌으니, 반영합니다.

        if self.score >= 17 and self.score < 21:
            self.decision = "STAY"
        elif self.score == 21:
            self.result = "21"
        elif self.score > 21:
            if self.ace_get:
                self.score -= 10
                self.hand[self.ace_card] -= 10
            else:
                self.result = "BUST"

        return one_set_of_card  ## 카드를 뽑은 후의 덱의 상태를 반환합니다.

# 블랙잭의 플레이어 한 명을 정의하는 클래스입니다.
# 프로그램의 확장성을 높이기 위해, 플레이어는 2인 이상 생성이 가능한 형태로 정의합니다.
# 해당 프로그램의 상위호환이 구현될 때까지, 게임은 딜러 대 유저(1대 1) 고정으로 진행됩니다.
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
        self.hand = {}
        if int(play_type) > 2 or int(play_type) < 0:
            if int(play_type) != -1:
                print("Error: No Such Mode !\nField <play_type> should be in list(0, 1, 2)")
        else:
            self.play_type = int(play_type)
        self.controllable = bool(wanna_control)
        self.total_chips = int(total_chips)
        self.score = 0  ## 해당 판의 점수. 판이 바뀔 때마다 0으로 초기화됨.
        self.status = bool(True)    ## 해당 판에서 살았나죽었나. 판이 바뀔 때마다 True로 초기화됨.
        # NONE, BLACKJACK / BUST, 21
        self.result = "NONE"
        # -, HIT, STOP, STAY
        self.decision = "-"
        self.ace_get = False
        self.ace_card = "Null"

        # 판 당 플레이어가 베팅할 고정 칩 개수를 정의합니다.
        # play_typed의 값이 클수록 베팅하는 금액이 커집니다.
        if wanna_control:
            self.sum_of_betting = int(input("한 게임 당 얼마를 베팅하시겠습니까? >> "))
        else:
            self.sum_of_betting = int(10 + (self.play_type * 5))
    def draw_first_cards(self, one_set_of_card: list):
        target_mark_index = int(random.randint(0, 3))
        target_mark_str = str(MARK_LIST[target_mark_index])
        target_mark = one_set_of_card[target_mark_index]  ## 타겟 마크는 한 문양의 카드로만 이루어진 딕셔너리 형태입니다.
        target_card_key = str(random.choice(list(target_mark.keys())))
        target_card_name = CARD_NAME_LIST[int(target_card_key) - 1]
        target_card_value = target_mark.pop(target_card_key)
        if int(target_card_value) == 11:
            self.ace_get = True
            self.ace_card = str(target_mark_str + target_card_name)
        self.hand[str(target_mark_str + target_card_name)] = int(target_card_value)
        self.score += int(target_card_value)
        one_set_of_card[target_mark_index] = target_mark  ## 덱에서 카드가 한 장 빠졌으니, 반영합니다.

        ## 첫 턴이므로 한 장을 더 뽑습니다.
        target_mark_index = int(random.randint(0, 3))
        target_mark_str = str(MARK_LIST[target_mark_index])
        target_mark = one_set_of_card[target_mark_index]  ## 타겟 마크는 한 문양의 카드로만 이루어진 딕셔너리 형태입니다.
        target_card_key = str(random.choice(list(target_mark.keys())))
        target_card_name = CARD_NAME_LIST[int(target_card_key) - 1]
        target_card_value = target_mark.pop(target_card_key)
        if int(target_card_value) == 11:
            self.ace_get = True
            self.ace_card = str(target_mark_str + target_card_name)
        self.hand[str(target_mark_str + target_card_name)] = int(target_card_value)
        self.score += int(target_card_value)
        one_set_of_card[target_mark_index] = target_mark  ## 덱에서 카드가 한 장 빠졌으니, 반영합니다.

        if self.score == 21:
            self.result = "BLACKJACK"

        return one_set_of_card  ## 카드를 뽑은 후의 덱의 상태를 반환합니다.
    def draw_card(self, one_set_of_card: list):
        target_mark_index = int(random.randint(0, 3))
        target_mark_str = str(MARK_LIST[target_mark_index])
        target_mark = one_set_of_card[target_mark_index]  ## 타겟 마크는 한 문양의 카드로만 이루어진 딕셔너리 형태입니다.
        target_card_key = str(random.choice(list(target_mark.keys())))
        target_card_name = CARD_NAME_LIST[int(target_card_key) - 1]
        target_card_value = target_mark.pop(target_card_key)
        self.hand[str(target_mark_str + target_card_name)] = int(target_card_value)
        self.score += int(target_card_value)
        if int(target_card_value) == 11:
            self.ace_get = True
            self.ace_card = str(target_mark_str + target_card_name)
        one_set_of_card[target_mark_index] = target_mark  ## 덱에서 카드가 한 장 빠졌으니, 반영합니다.
        return one_set_of_card  ## 카드를 뽑은 후의 덱의 상태를 반환합니다.

# 블랙잭 게임 전체의 속성을 담은 클래스입니다.
class GameStyle:
    def __init__(self, num_of_mem: int, num_of_set: int, controllable_dealer: bool, debug_mode: bool):
        '''
        게임의 속성을 정의합니다.
        :param num_of_mem: 게임에 참여할 플레이어의 수입니다.
        :param num_of_set: 게임에서 사용할 카드의 세트 개수입니다.
        :param controllable_dealer: 딜러를 조종할 것인지 정합니다.
        :param debug_mode: 일반 게임/개발자를 위한 디버깅 모드를 설정하는 변수입니다. 값이 True일 시, 모든 참여자의 성격과 카드를 열람할 수 있습니다.
        '''
        self.num_of_mem = int(num_of_mem)
        self.num_of_set = int(num_of_set)
        self.debug_mode = bool(debug_mode)

        # 딜러를 생성합니다.
        # 참고: 딜러는 베팅하지 않으므로 플레이어에 포함하지 않습니다.
        print("> > > > > 딜러를 생성중입니다. > > > > >")
        if controllable_dealer:
            dealer_name = str(input("딜러를 조종하는 게임입니다.\n* 딜러의 이름을 입력하십시오. >> "))
        else:
            dealer_name = "Dealer"
        # 유저가 설정한 옵션대로 딜러를 정의합니다.
        self.dealer = Dealer(dealer_name, controllable_dealer)
        print("- - - - - 딜러를 생성했습니다. - - - - -")
        
        # 플레이어 묶음을 생성합니다.
        self.player_list = []
        print("> > > > > 플레이어를 생성중입니다. > > > > >")
        # 플레이어 수만큼 플레이어를 생성합니다.
        for i in range(self.num_of_mem):
            print(">>>>> {0}번째 플레이어를 생성합니다. >>>>>".format(int(i + 1)))
            player = self.do_you_wanna_control()
            self.player_list.append(player)
        print("- - - - - {0}명의 플레이어를 생성했습니다. - - - - -".format(self.num_of_mem))

        # 카드 묶음을 생성합니다.
        self.card_sets = CardSet(num_of_set)
    def do_you_wanna_control(self):
        while True:
            ch = str(input("* 게임에서 이 플레이어를 조종합니까? (Y|N) >> "))
            if ch == "Y" or ch == "y":
                control = True
                play_type = int(-1)
                play_type_str = "당신이 조종 가능"
                player_name = str(input("* 플레이어의 이름을 입력하십시오. >> "))
                start_chips = int(input("* " + player_name + " 이/가 소지할 칩의 개수를 입력하십시오. >> "))
                break
            elif ch == "N" or ch == "n":
                control = False
                play_type = int(random.randint(0, 2))
                style = ["소심", "평범", "대담"]
                play_type_str = "컴퓨터가 조종하며, " + style[play_type]
                player_name = LAST_NAME_LIST.pop(random.randint(0, len(LAST_NAME_LIST) - 1))
                start_chips = 500
                break
            else:
                print("잘못된 응답입니다. 다시 입력하십시오.")
        print("플레이어 {0}의 생성을 완료했습니다.\n{0} 은/는 {1}한 플레이어입니다.\n[칩 {2}개로 시작]".format(player_name, play_type_str, str(start_chips)))
        return Player(player_name, play_type, control, start_chips)

# 블랙잭 게임 한 판을 담은 클래스입니다.
class Game:
    def __init__(self, game_style: GameStyle):
        self.current_status = game_style
        self.current_turn = 0
        self.winner = "NONE"
        self.reason = ""
    def debug_status_of_game(self, go: bool):
        print("[디버그 모드 : {0}]".format(go))
        if go:
            print("[딜러]")
            print("> 핸드 현황 (총 {0}장 보유중)".format(len(self.current_status.dealer.hand)))
            for name in self.current_status.dealer.hand:
                print("\t> {0} 카드".format(name))
            print("> 총점 : {0} 점".format(self.current_status.dealer.score))
            print("> result : {0}".format(self.current_status.dealer.result))
            print("> decision : {0}".format(self.current_status.dealer.decision))
            print("> ace_get : {0}".format(self.current_status.dealer.ace_get))
            print("> open_card : {0}".format(self.current_status.dealer.open_card))
            for player in self.current_status.player_list:
                print("[플레이어 {0}]".format(player.name))
                print("> 핸드 현황 (총 {0}장 보유중)".format(len(player.hand)))
                for name in player.hand:
                    print("\t> {0} 카드".format(name))
                print("> 총점 : {0} 점".format(player.score))
                print("> result : {0}".format(player.result))
                print("> decision : {0}".format(player.decision))
                print("> ace_get : {0}".format(player.ace_get))
            print("*---*---*---*---*---*---*---*---*---*---*---*---*---*")
        else:
            print("[딜러]")
            print("> 핸드 현황 (총 {0}장 보유중)".format(len(self.current_status.dealer.hand)))
            print("\t> {0} 카드 공개됨.".format(self.current_status.dealer.open_card))
            for player in self.current_status.player_list:
                print("\n[플레이어 {0}]".format(player.name))
                print("> 핸드 현황 (총 {0}장 보유중)".format(len(player.hand)))
                for name in player.hand:
                    print("\t> {0} 카드".format(name))
                print("> 총점 : {0} 점".format(player.score))
            print("*---*---*---*---*---*---*---*---*---*---*---*---*---*")
    def start_game(self):
        # n개의 카드 세트들 중, 특정 카드 한 세트의 순서. 플레이어가 바뀔 때마다 한 턴 내에서도 계속 바뀌는 변수.
        target_dec_index = random.randint(0, len(self.current_status.card_sets.total_of_cards) - 1)
        # 임의의 카드 한 세트(하트, 다이아, 스페이드, 클로버)
        target_dec = self.current_status.card_sets.total_of_cards[target_dec_index]
        self.current_status.card_sets.total_of_cards[target_dec_index] = self.current_status.dealer.draw_first_cards(target_dec)
        for player in self.current_status.player_list:
            target_dec_index = random.randint(0, len(self.current_status.card_sets.total_of_cards) - 1)
            target_dec = self.current_status.card_sets.total_of_cards[target_dec_index]
            self.current_status.card_sets.total_of_cards[target_dec_index] = player.draw_first_cards(target_dec)
        print("*---*---*---* 카드 분배가 끝났습니다. 게임 현황을 출력합니다. *---*---*---*")
        self.debug_status_of_game(self.current_status.debug_mode)   # 디버그 모드가 켜져있을 경우, 딜러와 모든 플레이어의 현황을 출력합니다.
    def play_dealer_turn(self):
        if self.current_status.dealer.decision == "STAY":
            return
        else:
            # 드로우할 대상이 될 덱을 임의로 결정합니다.
            target_dec_index = random.randint(0, len(self.current_status.card_sets.total_of_cards) - 1)
            target_dec = self.current_status.card_sets.total_of_cards[target_dec_index]
            self.current_status.card_sets.total_of_cards[target_dec_index] = self.current_status.dealer.draw_card(target_dec)
    def play_player_turn(self, player: Player):
        # 드로우할 대상이 될 덱을 임의로 결정합니다.
        target_dec_index = random.randint(0, len(self.current_status.card_sets.total_of_cards) - 1)
        target_dec = self.current_status.card_sets.total_of_cards[target_dec_index]

        if player.decision == "STAY":
            return player
        else:
            how_about_you = str(input("어떻게 하시겠습니까? (HIT | STOP | STAY) >> "))
            if how_about_you == "HIT" or how_about_you == "hit":
                self.current_status.card_sets.total_of_cards[target_dec_index] = player.draw_card(target_dec)
            elif how_about_you == "STOP" or how_about_you == "stop":
                player.decision = "-"
                return player
            elif how_about_you == "STAY" or how_about_you == "stay":
                player.decision = "STAY"
                return player

        if player.score > 21:
            if player.ace_get:
                player.score -= 10
                player.hand[player.ace_card] -= 10
            else:
                player.result = "BUST"
        elif player.score == 21:
            player.result = "21"

        return player
    def play_main_game(self):
        # 딜러와 플레이어 둘 중 한 쪽이라도 승부가 확정날 때까지 턴을 진행합니다.
        while self.current_status.dealer.result == "NONE" and self.current_status.player_list[0].result == "NONE":
            self.current_turn += 1
            self.play_dealer_turn()
            self.current_status.player_list[0] = self.play_player_turn(self.current_status.player_list[0])
            print("*---*---*---* {0}번째 턴이 끝났습니다. 게임 현황을 출력합니다. *---*---*---*".format(self.current_turn))
            self.debug_status_of_game(self.current_status.debug_mode)   # 디버그 모드가 켜져있을 경우, 딜러와 모든 플레이어의 현황을 출력합니다.
            # 승부는 나지 않았으나 둘 다 스테이한 경우, 게임 결과를 바로 낸 후 게임을 종료합니다.
            if self.current_status.dealer.decision == "STAY" and self.current_status.player_list[0].decision == "STAY":
                self.reason = "딜러와 플레이어 모두 STAY하였으므로, 패를 공개하고 승부를 냅니다.\n"
                if self.current_status.dealer.score == self.current_status.player_list[0].score:
                    self.reason += "딜러와 플레이어의 점수가 " + str(self.current_status.dealer.score) + "점으로 동일하므로, 무승부입니다."
                    return "PUSH"
                elif self.current_status.dealer.score > self.current_status.player_list[0].score:
                    self.reason += "딜러의 점수가 " + str(self.current_status.dealer.score) + "점으로 21에 더 근접하므로, 플레이어의 패배입니다."
                    return "DEALER"
                elif self.current_status.dealer.score < self.current_status.player_list[0].score:
                    self.reason += "플레이어의 점수가 " + str(self.current_status.player_list[0].score) + "점으로 21에 더 근접하므로, 플레이어의 승리입니다."
                    return "PLAYER"
        # 게임 결과를 냅니다.
        if self.current_status.dealer.result == "BUST":
            self.reason = "딜러가 먼저 BUST했습니다. 플레이어의 점수와는 상관없이 플레이어의 승리입니다."
            return "PLAYER"
        elif self.current_status.dealer.result == "21":
            self.reason = "딜러가 먼저 21점을 달성했습니다. 플레이어의 점수와는 상관없이 플레이어의 패배입니다."
            return "DEALER"
        else:
            if self.current_status.player_list[0].result == "BUST":
                self.reason = "플레이어가 먼저 BUST했습니다. 플레이어의 패배입니다."
                return "DEALER"
            elif self.current_status.player_list[0].result == "21":
                self.reason = "플레이어가 먼저 21점을 달성했습니다. 플레이어의 승리입니다."
                return "PLAYER"
            else:
                print("점수 오류입니다. 코드 수정 필요합니다.")
                exit()
                return "ERROR"

    ## 1대 1 게임만을 고려한 플레이입니다.
    def go_blackjack_game(self):
        self.start_game()
        if self.current_status.dealer.result == "BLACKJACK" and self.current_status.player_list[0].result == "BLACKJACK":
            self.winner = "PUSH"
        elif self.current_status.dealer.result == "BLACKJACK" and self.current_status.player_list[0].result == "NONE":
            self.winner = "DEALER"
        elif self.current_status.dealer.result == "NONE" and self.current_status.player_list[0].result == "BLACKJACK":
            self.winner = "PLAYER"
        else:
            while self.winner == "NONE":
                self.winner = self.play_main_game()

    def update_status_of_game(self):
        ## 게임이 끝나면 게임의 결과를 플레이어들의 보유 칩 개수에 반영하여 반환합니다.
        if self.winner == "DEALER":
            self.current_status.player_list[0].total_chips -= self.current_status.player_list[0].sum_of_betting
        elif self.winner == "PLAYER":
            if self.current_status.player_list[0].result == "BLACKJACK":
                self.current_status.player_list[0].total_chips += int(float(self.current_status.player_list[0].sum_of_betting) * 1.5)
            else:
                self.current_status.player_list[0].total_chips += self.current_status.player_list[0].sum_of_betting

        ## 카드에 관련된 변수는 모두 초기화합니다.
        self.current_status.dealer.hand = {}
        self.current_status.dealer.score = 0
        self.current_status.dealer.result = "NONE"
        self.current_status.dealer.decision = "-"
        self.current_status.dealer.ace_get = False
        self.current_status.dealer.open_card = "Null"
        self.current_status.dealer.ace_card = "Null"
        for player in self.current_status.player_list:
            player.hand = {}
            player.score = 0
            player.result = "NONE"
            player.decision = "-"
            player.ace_get = False
            player.ace_card = "Null"

        return self.current_status

if __name__ == '__main__':

    # 설정을 초기화합니다.
    num_of_players = 0
    num_of_games = 0
    num_of_sets = 0
    dealer_control = False
    debug = False

    ## 프로그램을 안내합니다.
    print("*****-----*****-----*****-----*****-----*****")
    print("블랙잭 게임을 1회 이상 진행하는 프로그램입니다.")
    print("한 판이 끝나도 플레이어의 속성은 초기화되지 않습니다.")
    print("설정한 횟수에 도달할 때까지 플레이어들은 보유한 칩을 걸며 게임을 진행합니다.")

    ## 게임의 옵션을 입력받습니다.
    # 플레이어의 수를 입력받습니다.
    while True:
        num_of_players = int(input("* 플레이어의 수(1 ~ 6)를 입력하십시오. >> "))
        if num_of_players >= 1 and num_of_players <= 6:
            break
        else:
            print("잘못된 입력입니다. 다시 입력하십시오.")

    # 진행할 게임의 횟수를 입력받습니다.
    while True:
        num_of_games = int(input("* 몇 판 진행하시겠습니까? (1 ~ 10) >> "))
        if num_of_games >= 1 and num_of_games <= 10:
            break
        else:
            print("잘못된 입력입니다. 다시 입력하십시오.")

    # 사용할 카드의 덱 수를 입력받습니다.
    while True:
        num_of_sets = int(input("* 몇 세트의 카드를 사용하시겠습니까? (1 ~ 6) >> "))
        if num_of_sets >= 1 and num_of_sets <= 6:
            break
        else:
            print("잘못된 입력입니다. 다시 입력하십시오.")

    # 딜러를 조종하는 게임인지 묻습니다.
    while True:
        ch = str(input("* 딜러를 조종합니까? (Y|N) >> "))
        if ch == "Y" or ch == "y":
            dealer_control = True
            break
        else:
            break

    # 디버그 모드를 킬 것인지 묻습니다.
    while True:
        ch = str(input("* 디버그 모드를 킵니까? (Y|N) >> "))
        if ch == "Y" or ch == "y":
            debug = True
            break
        else:
            break

    ## 게임의 옵션을 생성합니다.
    game_style = GameStyle(num_of_players, num_of_sets, dealer_control, debug)
    print("게임을 설정 완료했습니다.")
    print("설정한 횟수만큼 게임을 친행합니다.")
    print("*****-----*****-----*****-----*****-----*****")

    ## 설정한 횟수만큼 게임을 진행합니다.
    for i in range(num_of_games):
        print("\n" * 10)
        print("{0}번째 게임입니다.".format(i + 1))
        game = Game(game_style)
        game.go_blackjack_game()
        game_style = game.update_status_of_game()
        ## 게임이 끝났으면 플레이어들의 칩 보유 현황을 알려줍니다.
        print("{0}번째 게임이 종료되었습니다.".format(i + 1))
        print(game.reason)
        print("*****-----*****-----*****-----*****-----*****")
        print("현재 플레이어가 보유한 칩은 {0}개입니다.".format(game_style.player_list[0].total_chips))