# Statiz_Project_3.1 - 개인 프로젝트
[2022년 9월 진행]
스탯티즈 사이트 "시즌기록실"에서 시즌 내 데이터를 가져오는 코드
- 타격 - 기본(모든 내용 포함)
- 타격 - 확장(기본에서의 중복 내용 제외)
- 투구 - 기본(모든 내용 포함)
- 투구 - 확장(기본에서의 중복 내용 제외)
- 투구 - 구종구사(포심 혹은 투심 최고구속 포함)

### 변경 사항
- 스탯티즈에 상세 데이터가 존재하는 2015년 ~ 2022년 데이터 수집
- 이전 버전에서 구분이 불가능했던 KIA / KT 구분 진행
- 크롤링 연습을 위해 진행했던 BeautifulSoup 대신 Pandas의 read_html 활용
- Jupiter Notebook으로 연습 후 .py 파일로 생성
- git bash 실행 및 sys.argv 활용하여 원하는 년도 정리 가능하도록 구성

### 고려 및 습득 사항
- 클래스에서 @property 데코레이터의 적절한 사용 → 속성이냐 메서드냐
- 인스턴스 메서드의 적절한 활용이 아직 어려움 → 지역함수 / 람다식으로 대체
- 같은 성격 및 한 번에 처리되어야 한다면 하나의 속성으로 지정할 필요
- openpyxl에서 셀 배경색 지정하는 것은 PatternFill을 활용
- 새로운 형식 및 내용 변경은 생각보다 시간이 오래 걸리나, 새로이 습득하는 것도 존재

### 향후 리팩토링 및 기능 추가 사항
1. 2014 - 현재까지 전체 내용들을 하나의 엑셀로 정리할 수 있는 파일 생성
2. sys.argv가 main 파일에만 적용될 수 있도록 코드 수정
     - record_site 및 kt_site가 클래스 안 메서드로 움직이게끔 변환
     - @property를 통해 속성으로 정의된 내용을 메서드로 변환
     - __init__에서 별도의 빈 리스트들 생성(타격기본, 타격확장, 투수기본, 투수확장, 투수구속)
     - hit_basic 등의 메서드가 return 값을 반환하는 함수가 아님
        - __init__에서 설정된 빈 리스트에 값을 추가하도록 설정
3. 2014 - 현재가 아닌 값을 입력할 경우 예외가 발생하도록 수정
4. 기타 리팩토링 사항 발견 및 수정