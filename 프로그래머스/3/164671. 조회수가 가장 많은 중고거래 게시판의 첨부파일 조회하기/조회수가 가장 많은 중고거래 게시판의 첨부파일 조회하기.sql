
# select 첨부파일경로
# where 조회수가 가장 높은 중고거래 게시물
# order by FILE ID DESC

# /home/grep/src/BOARD_ID/FILE_ID+FILE_NAME+FILE_EXT

select concat("/home/grep/src/", f.BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
from USED_GOODS_FILE f join USED_GOODS_BOARD b on f.BOARD_ID=b.BOARD_ID
where b.VIEWS = (select max(VIEWS) from USED_GOODS_BOARD)
order by FILE_ID DESC;
