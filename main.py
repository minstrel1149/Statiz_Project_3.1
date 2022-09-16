import sys
import statiz_3_background as stb

year = sys.argv[1]

statiz_crawling = stb.Statiz()
statiz_crawling.export_excel(year)

print('Process Done!')


# __init__()의 경우 year라는 위치 전달인자가 없다는 문제 발생
# → record_site 및 kt_site를 클래스 바깥으로 이동 후 재시도
# → name 'year' is not defined 문제 발생
# → background 파일에 sys.argv 삽입
# → selenium driver는 열리는데 lmxl not found, please install it 문제 발생