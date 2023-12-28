import math
import random
import time

# 블랙잭의 딜러를 정의하는 클래스입니다.
class Dealer:
    def __init__(self):
        print("")

# 블랙잭의 플레이어 한 명을 정의하는 클래스입니다.
class Player:
    def __init__(self, name: str, play_type: int):
        '''
        플레이어의 이름과 플레이 성격을 정의합니다.
        :param name: 플레이어의 이름입니다.
        :param play_type: 게임에 플레이 스타일입니다. 0에서 2 사이의 정수값이며, 숫자가 클 수록 해당 플레이어는 과감한 플레이를 하게 됩니다.
        '''
        self.name = name
        if int(type) > 2 or int(type) < 0:
            print("Error: No Such Mode !\nField <play_type> should be in list(0, 1, 2)")
        else:
            self.play_type = int(play_type)

# 블랙잭 게임 한 판을 플레이하는 주 클래스입니다.
class GamePlay:

    def __init__(self, num_of_mem: int, index_of_me: int, debug_mode: bool):
        '''
        게임의 속성을 정의합니다.
        :param num_of_mem: 게임에 참여할 플레이어의 수입니다.
        :param index_of_me: 컴퓨터가 아닌 사용자가 조작할 플레이어의 인덱스 번호입니다.
        :param debug_mode: 일반 게임/개발자를 위한 디버깅 모드를 설정하는 변수입니다. 값이 True일 시, 모든 참여자의 성격과 카드를 열람할 수 있습니다.
        '''
        self.num_of_mem = int(num_of_mem)
        self.index_of_me = int(index_of_me)
        self.debug_mode = bool(debug_mode)

    def exe_debug_mode(self):
        '''
        턴이 끝날 때마다 모든 참여자의 성격과 카드를 콘솔에 출력합니다.
        일반 게임의 경우 해당 메소드는 작동하지 않습니다.
        :return: void
        '''
        print("")