-- 코드를 작성해주세요
#1. 2번 형질을 보유하지 않으면서 1번이나 3번 형질을 보유하기 위해서는, 0101과 & 연산을 했을 때 0이 아니고, 0010과 &연산을 했을 때 0이어야 함
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 5) AND NOT (GENOTYPE & 2);