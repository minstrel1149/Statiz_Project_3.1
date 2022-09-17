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
# jupyter notebook 환경에서 새로 시도 중.. 클래스 메서드 활용이 제대로 안되고 있는듯. 임시방편으로라도 지역함수로 사용하면 어떨까?
# 클래스 메서도 활용 문제는 아닌듯. 일단 지역함수로 전환하고 두 개로 나눠진 속성을 하나로 합침
# jupyter notebook 상에서는 클래스 형태로 구현 완료