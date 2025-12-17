/*
百元百鸡问题求解程序 - T-SQL版本
问题描述：公鸡5元一只，母鸡3元一只，小鸡3只1元
用100元买100只鸡，找出所有可能的组合
*/

-- 创建存储过程
go
CREATE PROCEDURE dbo.SolveHundredChickens
AS
BEGIN
    SET NOCOUNT ON;
    
    -- 创建临时表存储结果
    CREATE TABLE #ChickenResults (
        Rooster INT,    -- 公鸡数量
        Hen INT,        -- 母鸡数量
        Chick INT       -- 小鸡数量
    );
    
    DECLARE @rooster INT = 0;   -- 公鸡数量
    DECLARE @hen INT = 0;       -- 母鸡数量
    DECLARE @chick INT = 0;     -- 小鸡数量
    DECLARE @totalCost FLOAT;   -- 总花费
    
    -- 公鸡最多20只（100元/5元=20只）
    WHILE @rooster <= 20
    BEGIN
        -- 重置母鸡数量
        SET @hen = 0;
        
        -- 母鸡最多33只（100元/3元≈33.33只）
        WHILE @hen <= 33
        BEGIN
            -- 计算小鸡数量：总鸡数 - 公鸡数 - 母鸡数
            SET @chick = 100 - @rooster - @hen;
            
            -- 确保小鸡数量为正数
            IF @chick > 0
            BEGIN
                -- 计算总花费：公鸡花费 + 母鸡花费 + 小鸡花费
                -- 小鸡3只1元，所以花费为小鸡数量/3
                SET @totalCost = @rooster * 5.0 + @hen * 3.0 + @chick / 3.0;
                
                -- 如果总花费等于100元（由于浮点数计算，使用近似比较）
                IF ABS(@totalCost - 100.0) < 0.0001
                BEGIN
                    -- 将结果插入临时表
                    INSERT INTO #ChickenResults (Rooster, Hen, Chick)
                    VALUES (@rooster, @hen, @chick);
                END;
            END;
            
            -- 增加母鸡数量
            SET @hen = @hen + 1;
        END;
        
        -- 增加公鸡数量
        SET @rooster = @rooster + 1;
    END;
    
    -- 输出结果
    SELECT 
        '百元百鸡问题求解结果：' AS [标题]
    UNION ALL
    SELECT '==================================='
    UNION ALL
    SELECT '公鸡数量   母鸡数量   小鸡数量'
    UNION ALL
    SELECT ''
    UNION ALL
    SELECT 
        RIGHT('    ' + CAST(Rooster AS VARCHAR(4)), 4) + '         ' +
        RIGHT('    ' + CAST(Hen AS VARCHAR(4)), 4) + '         ' +
        RIGHT('    ' + CAST(Chick AS VARCHAR(4)), 4)
    FROM #ChickenResults
    UNION ALL
    SELECT ''
    UNION ALL
    SELECT '===================================';
    
    -- 清理临时表
    DROP TABLE #ChickenResults;
END;
go

-- 执行存储过程
go
EXEC dbo.SolveHundredChickens;
go

-- 删除存储过程（可选）
-- DROP PROCEDURE dbo.SolveHundredChickens;
go