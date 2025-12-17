/**
 * 百元百鸡问题求解程序
 * 问题描述：公鸡5元一只，母鸡3元一只，小鸡3只1元
 * 用100元买100只鸡，找出所有可能的组合
 */
using System;

namespace HundredChickensProblem
{
    class HundredChickens
    {
        static void Main(string[] args)
        {
            Console.WriteLine("百元百鸡问题求解结果：");
            Console.WriteLine("===================================");
            Console.WriteLine("公鸡数量   母鸡数量   小鸡数量");
            Console.WriteLine();
            
            // 公鸡最多20只（100元/5元=20只）
            for (int rooster = 0; rooster <= 20; rooster++)
            {
                // 母鸡最多33只（100元/3元≈33.33只）
                for (int hen = 0; hen <= 33; hen++)
                {
                    // 计算小鸡数量：总鸡数 - 公鸡数 - 母鸡数
                    int chick = 100 - rooster - hen;
                    
                    // 确保小鸡数量为正数
                    if (chick > 0)
                    {
                        // 计算总花费：公鸡花费 + 母鸡花费 + 小鸡花费
                        // 小鸡3只1元，所以花费为小鸡数量/3
                        // 使用浮点数计算总花费
                        double totalCost = rooster * 5.0 + hen * 3.0 + chick / 3.0;
                        
                        // 如果总花费等于100元（由于浮点数计算，使用近似比较）
                        if (Math.Abs(totalCost - 100.0) < 0.0001)
                        {
                            // 输出符合条件的组合
                            Console.WriteLine($"{rooster,4}         {hen,4}         {chick,4}");
                        }
                    }
                }
            }
            
            Console.WriteLine("===================================");
            Console.ReadKey();
        }
    }
}