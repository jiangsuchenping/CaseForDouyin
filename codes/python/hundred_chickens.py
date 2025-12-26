#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
百元百鸡问题求解程序
<<<<<<< HEAD
问题描述：公鸡5元一只，母鸡3元一只，小鸡3只1元
用100元买100只鸡，找出所有可能的组合
"""

def main():
    print("百元百鸡问题求解结果：")
    print("===================================")
    print("公鸡数量   母鸡数量   小鸡数量")
    print()
    
    # 公鸡最多20只（100元/5元=20只）
    for rooster in range(21):
        # 母鸡最多33只（100元/3元≈33.33只）
        for hen in range(34):
            # 计算小鸡数量：总鸡数 - 公鸡数 - 母鸡数
            chick = 100 - rooster - hen
            
            # 确保小鸡数量为正数
            if chick > 0:
                # 计算总花费：公鸡花费 + 母鸡花费 + 小鸡花费
                # 小鸡3只1元，所以花费为小鸡数量/3
                total_cost = rooster * 5 + hen * 3 + chick / 3
                
                # 如果总花费等于100元（由于浮点数计算，使用近似比较）
                if abs(total_cost - 100) < 0.0001:
                    # 输出符合条件的组合
                    print(f"{rooster:4d}         {hen:4d}         {chick:4d}")
    
    print("===================================")

if __name__ == "__main__":
    main()
=======

问题描述：公鸡5元一只，母鸡3元一只，小鸡3只1元
用100元买100只鸡，找出所有可能的组合

使用说明：
1. 运行脚本：python hundred_chickens.py
2. 查看输出结果，包含所有符合条件的鸡的数量组合
"""

def solve_hundred_chickens():
    """
    求解百元百鸡问题
    
    返回：
        list: 包含所有符合条件的组合，每个组合是(公鸡数量, 母鸡数量, 小鸡数量)的元组
    """
    solutions = []
    
    # 公鸡最多20只（100元/5元=20只）
    for roosters in range(0, 21):
        # 母鸡最多33只（100元/3元≈33.33只）
        for hens in range(0, 34):
            # 计算小鸡数量：总鸡数 - 公鸡数 - 母鸡数
            chicks = 100 - roosters - hens
            
            # 确保小鸡数量为正数
            if chicks > 0:
                # 检查小鸡数量是否能被3整除（因为3只1元）
                if chicks % 3 == 0:
                    # 计算总花费
                    total_cost = roosters * 5 + hens * 3 + chicks / 3
                    
                    # 如果总花费等于100元，记录该组合
                    if total_cost == 100:
                        solutions.append((roosters, hens, chicks))
    
    return solutions

if __name__ == '__main__':
    print('百元百鸡问题求解结果：')
    print('===================================')
    print('公鸡数量   母鸡数量   小鸡数量')
    print()  # 输出空行，增加可读性
    
    solutions = solve_hundred_chickens()
    
    if solutions:
        for roosters, hens, chicks in solutions:
            print(f'{roosters:^9}   {hens:^9}   {chicks:^9}')
    else:
        print('未找到符合条件的组合')
    
    print('===================================')
>>>>>>> origin/main
