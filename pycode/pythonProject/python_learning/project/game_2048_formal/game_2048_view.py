"""
                        2048界面视图层
"""
from game_2048_bll import *
import os


class Game2048View:
    def __init__(self):
        self.__game_core_controller = GameCoreController()

    def main(self):
        """
                程序主入口
        """
        while True:
            self.__start_game()
            if not self.__update():
                break

    def __start_game(self):
        """
                游戏开始时初始化界面
        """
        self.__game_core_controller.game_list_clear()
        self.__game_core_controller.random_num_produce()
        self.__game_core_controller.random_num_produce()

    def __update(self):
        """
                游戏进程更新
        :return: bool
        """
        while True:
            self.__game_situation_display()
            if self.__game_core_controller.is_continue():
                if self.__move():
                    self.__game_core_controller.random_num_produce()
            else:
                print('游戏结束')
                return Game2048View.__restart_game()

    def __move(self):
        """
                游戏移动获取并调用
        :return: bool
        """
        dir_diction = {'w': DirectionModel.Up,
                       'a': DirectionModel.LEFT,
                       's': DirectionModel.DOWN,
                       'd': DirectionModel.RIGHT
                       }
        direction = None
        re = self.__input_and_judge(direction, msg_input='请输入wasd:>', judge_func=lambda item: item in dir_diction)
        return self.__game_core_controller.move(dir_diction[re[0]])

    @staticmethod
    def __restart_game():
        """
                    游戏是否重新开始
        """
        choice = None
        re = Game2048View.__input_and_judge(choice, msg_input='请输入yes or no:>',
                                            judge_func=lambda item: item in ('yes', 'no'))
        if re[0] == 'yes':
            return True
        else:
            print('感谢游玩')
            return False

    def __game_situation_display(self):
        """
                游戏进程打印
        """
        os.system('cls')
        for line in self.__game_core_controller.game_list:
            for cuber in line:
                print(cuber, end=' ')
            print()

    @staticmethod
    def __input_and_judge(*args, msg_input, msg_warning='请输入正确内容', judge_func):
        """
                输入内容获取以及非法判断器
        :param args: 需要用户input内容
        :param msg_input: 输入内容的信息提示
        :param msg_warning: 错误输入内容的信息提示
        :param judge_func: 函数，有一个判断内容作为参数，返回bool，判断方法
        :return: input内容所在的元组
        """
        re = list(args)
        for i in range(len(re)):
            while True:
                re[i] = input(f'{msg_input}')
                if judge_func(re[i]):
                    break
                else:
                    print(f'{msg_warning}')
        return tuple(re)
