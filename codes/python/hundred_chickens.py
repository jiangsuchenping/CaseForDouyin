#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
百元百鸡问题求解程序
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