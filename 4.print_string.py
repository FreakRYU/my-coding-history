# "안녕하세요"라고 말했습니다. 를 출력한다.
print('"안녕하세요"라고 말했습니다.')

# 만약 큰따옴표 (")를 두번 썼다면, 오류가 났을 것.
# ""와 "라고 말했습니다." 만 문자열로 인식되고, 
# 그 사이에 [안녕하세요]는 문자열로 인식되지 않아 오류가 난 것.

print("\"안녕하세요\"라고 말했습니다.")
# \" : 큰따옴표를 의미한다.

print('\'배가 고픕니다\'라고 생각했습니다.')
# \' : 작은따옴표를 의미한다.

print("안녕하세요\n안녕하세요")
# \n : 줄바꿈을 의미한다.

print("안녕하세요\t안녕하세요")
# \t : 탭을 의미한다.

# 이스케이프 문자(\t)로 탭 사용하기
print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름\t3\t강서구")

# \\ : 역슬래시(\)를 의미한다.
print("\\ \\ \\ \\")

# 매번 줄바꿈 \n을 사용하게 되면, 긴 문단을 처리하기 어렵다.
# 따라서 파이썬은 [여러 줄 문자열] 이라는 기능을 지원한다.
# 그 방법은 큰따옴표 or 작은따옴표 세 번 반복한 기호를 사용.

# 예를 들어서 애국가 1절을 가져와서 적용해보자면...

# 1. 큰따옴표에 그대로 대입
print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세""")

# 2. 문단 자체로 깔끔하게 보이게만 코딩
# 그러나 의도치 않은 줄바꿈 (첫 줄과 마지막 줄이 빈 줄이 생성됨.)
print("""
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
""")

# 3. \를 이용해서 알아보기 쉽고 불필요한 줄바꿈을 없앨 수 있음.
print("""\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세\
""")