"""
                    导入模块的练习
"""
# 第一种跨文件调用
# import staticmethod_exercise
#
# double_list = [
#     ['00', '01', '02', '03'],
#     ['10', '11', '12', '13'],
#     ['20', '21', '22', '23'],
# ]
# dir_01 = staticmethod_exercise.DirectionOfElements.get_new_position('13', double_list)
# print(dir_01.vector2_x, dir_01.vector2_y)
# dir_01_after_process_1 = (
#     staticmethod_exercise.DirectionOfElements.move(dir_01, staticmethod_exercise.DirectionOfElements.lerg_move_vector,
#                                                    -1, 3, double_list))
# dir_01 = staticmethod_exercise.DirectionOfElements.get_new_position('22', double_list)
# print(dir_01.vector2_x, dir_01.vector2_y)
# dir_01_after_process_2 = (
#     staticmethod_exercise.DirectionOfElements.move(dir_01,
#                                                    staticmethod_exercise.DirectionOfElements.uplo_move_vector,
#                                                    -1, 2, double_list))
# dir_01 = staticmethod_exercise.DirectionOfElements.get_new_position('03', double_list)
# print(dir_01.vector2_x, dir_01.vector2_y)
# dir_01_after_process_3 = (
#     staticmethod_exercise.DirectionOfElements.move(dir_01,
#                                                    staticmethod_exercise.DirectionOfElements.uplo_move_vector,
#                                                    1, 2, double_list))
# print(dir_01_after_process_1, dir_01_after_process_2, dir_01_after_process_3)
# 第二种跨文件调用
# from staticmethod_exercise import DirectionOfElements
# double_list = [
#     ['00', '01', '02', '03'],
#     ['10', '11', '12', '13'],
#     ['20', '21', '22', '23'],
# ]
# dir_01 = DirectionOfElements.get_new_position('13', double_list)
# print(dir_01.vector2_x, dir_01.vector2_y)
# dir_01_after_process_1 = DirectionOfElements.move(dir_01, DirectionOfElements.lerg_move_vector, -1, 3, double_list)
# dir_01 = DirectionOfElements.get_new_position('22', double_list)
# print(dir_01.vector2_x, dir_01.vector2_y)
# dir_01_after_process_2 = DirectionOfElements.move(dir_01, DirectionOfElements.uplo_move_vector, -1, 2, double_list)
# dir_01 = DirectionOfElements.get_new_position('03', double_list)
# print(dir_01.vector2_x, dir_01.vector2_y)
# dir_01_after_process_3 = DirectionOfElements.move(dir_01, DirectionOfElements.uplo_move_vector, 1, 2, double_list)
# print(dir_01_after_process_1, dir_01_after_process_2, dir_01_after_process_3)
# 第三种跨文件调用
from staticmethod_exercise import *
double_list = [
                ['00', '01', '02', '03'],
                ['10', '11', '12', '13'],
                ['20', '21', '22', '23'],
                ]
dir_01 = DirectionOfElements.get_new_position('13', double_list)
print(dir_01.vector2_x, dir_01.vector2_y)
dir_01_after_process_1 = DirectionOfElements.move(dir_01, DirectionOfElements.lerg_move_vector, -1, 3, double_list)
dir_01 = DirectionOfElements.get_new_position('22', double_list)
print(dir_01.vector2_x, dir_01.vector2_y)
dir_01_after_process_2 = DirectionOfElements.move(dir_01, DirectionOfElements.uplo_move_vector, -1, 2, double_list)
dir_01 = DirectionOfElements.get_new_position('03', double_list)
print(dir_01.vector2_x, dir_01.vector2_y)
dir_01_after_process_3 = DirectionOfElements.move(dir_01, DirectionOfElements.uplo_move_vector, 1, 2, double_list)
print(dir_01_after_process_1, dir_01_after_process_2, dir_01_after_process_3)
