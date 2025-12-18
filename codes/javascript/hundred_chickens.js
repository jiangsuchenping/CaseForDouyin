/**
 * 百元百鸡问题求解程序
 * 问题描述：公鸡5元一只，母鸡3元一只，小鸡3只1元
 * 用100元买100只鸡，找出所有可能的组合
 */

function solveHundredChickens() {
    console.log("百元百鸡问题求解结果：");
    console.log("===================================");
    console.log("公鸡数量   母鸡数量   小鸡数量");
    console.log();
    
    // 公鸡最多20只（100元/5元=20只）
    for (let rooster = 0; rooster <= 20; rooster++) {
        // 母鸡最多33只（100元/3元≈33.33只）
        for (let hen = 0; hen <= 33; hen++) {
            // 计算小鸡数量：总鸡数 - 公鸡数 - 母鸡数
            const chick = 100 - rooster - hen;
            
            // 确保小鸡数量为正数
            if (chick > 0) {
                // 计算总花费：公鸡花费 + 母鸡花费 + 小鸡花费
                // 小鸡3只1元，所以花费为小鸡数量/3
                const totalCost = rooster * 5 + hen * 3 + chick / 3;
                
                // 如果总花费等于100元（由于浮点数计算，使用近似比较）
                if (Math.abs(totalCost - 100) < 0.0001) {
                    // 输出符合条件的组合
                    console.log(`${rooster.toString().padStart(4)}         ${hen.toString().padStart(4)}         ${chick.toString().padStart(4)}`);
                }
            }
        }
    }
    
    console.log("===================================");
}

// 运行程序
solveHundredChickens();