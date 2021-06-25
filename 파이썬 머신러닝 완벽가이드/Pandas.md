### Pandas

---

> 데이터 조작 및 분석을 위해 Python 프로그래밍 언어로 작성된 소프트웨어 라이브러리

* 파이썬에서 데이터 처리를 위해 존재하는 가장 인기 있는 라이브러리
* 2차원 데이터 : 가장 이해하기 쉬운 데이터 구조이면서도 효과적으로 데이터를 담을 수 있는 구조
* 넘파이 기반으로 작성되었으며, 넘파이보다 훨씬 유연하고 편리하게 데이터 핸들링을 가능하게 해준다.
* **고수준** API 제공
* 핵심 객체는 **DataFrame**(여러 개의 행과 열로 이루어진 2차원 데이터를 담는 데이터 구조체)
* csv : 칼럼을 '**,**'로 구분한 데이터 및 텍스트 파일, 간혹 '**\\**'도 있음



> 판다스 시작

* pd.read_csv() : 호출 시 파일명 인자로 들어온 파일을 로딩해 DataFrame 객체로 반환한다.
* DataFrame.head() : DataFrame의 맨 앞에 있는 N개의 로우를 반환한다.(디폴트는 5개)
* .shape() : DataFrame의 행과 열 크기를 알 수 있다.
* .info() : 총 데이터 건수와 데이터 타입, Null 건수를 알 수 있다.
* describe() : 칼럼별 숫자형 데이터값의 n-percentile 분포도, 평균값, 최댓값, 최솟값을 나타낸다.
  * count : Not Null인 데이터 건수
  * mean : 전체 데이터의 평균값
  * std : 표준편차
  * 25% : 25 percentile 값
* value_counts() : 데이터의 분포도를 확인하는데 매우 유용한 함수, **지정된 칼럼의 데이터값 건수를 반환**한다.



> DataFrame과 리스트, 딕셔너리, 넘파이 ndarray 상호 변환

* DataFrame은 리스트와 넘파이 ndarray와 다르게 **칼럼명**을 가지고 있다.
* DateFrame을 넘파이 ndarray로 변환하기
  * DataFrame 객체의 values를 이용하기
* DataFrame을 리스트로 변환하기
  * values로 얻은 ndarray에 tolist()를 호출하기
* DataFrame을 딕셔너리로 변환하기
  * DataFrame 객체의 to_dict() 메서드를 호출



> DataFrame의 칼럼 데이터 세트 생성과 수정

* [] 연산자를 이용



> DataFrame 데이터 삭제

* drop()
  * axis=1 : 대부분의 경우 (column 삭제)
  * axis=0 : 이상치 데이터를 삭제하는 경우에 주로 사용(row 삭제)
* inplace
  * False이면 자기 자신의 DataFrame의 데이터는 삭제하지 않으며, 삭제된 결과 DataFrame을 반환한다.
  * True로 설정하면 자신의 DataFrame의 데이터를 삭제
  * inplace=True로 설정한 채로 반환 값을 다시 자신의 DataFrame 객체로 할당하면 안된다.



> Index 객체

* RDBMS의 PK와 유사하게 DataFrame, Series의 레코드를 고유하게 식별하는 객체
* DataFrame, Series에서 Index 객체만 추출하려면 DataFrame.index, Series.index 속성을 통해 가능하다.
* 반환된 Index 객체의 실제 값은 넘파이 1차원 ndarray로 볼 수 있다.
* Index 객체의 values 속성으로 ndarray 값을 알 수 있다.

* ndarray와 유사하게 단일 값 반환 및 슬라이싱 가능하지만 한 번 만들어진 DataFrame 및 Series의 Index 객체는 함부로 변경할 수 없다.
* reset_index() : 새롭게 인덱스를 연속 숫자 형으로 할당하며 기존 인덱스는 index라는 새로운 칼럼명으로 추가한다.
  * 인덱스가 연속된 int 숫자형 데이터가 아닐 경우에 다시 이를 연속 int 숫자형 데이터로 만들 때 주로 사용한다.
  * Series에 reset_index()를 적용하면 Series가 아닌 DataFrame이 반환되니 유의해야 한다.
  * drop=True로 설정하면 기존 인덱스는 새로운 칼럼으로 추가되지 않고 삭제된다.



> 데이터 셀렉션 및 필터링

* DataFrame의 [] 연산자
  * 칼럼만 지정할 수 있는 **칼럼 지정 연산자**
  * 숫자 불가능
    * ex) titanic_df[0] 불가능
  * 판다스의 인덱스 형태로 변환 가능한 표현식은 [] 내에 입력할 수 있다.
    * ex) titanic_df[:2] 가능
  * DataFrame 바로 뒤의 [] 연산자는 넘파이의 []나, Series의 []와는 다르다.
  * DataFrame 바로 뒤의 [] 내 입력 값은 칼럼명을 지정해 칼럼 지정 연산에 사용하거나 불린 인덱스 용도로만 사용해야 한다.
  * DataFrame[:2]와 같은 슬라이싱 연산으로 데이터를 추출하는 방법은 사용하지 않는게 좋다.
  * **<u>DataFrame의 인덱스값은 명칭 기반 인덱싱</u>**
* DataFrame ix[] 연산자
  * 행에 해당하는 위치 지정은 DataFrame의 인덱스 값을 입력해야 한다.
  * 열 위치 지정은 독특하게 칼럼명뿐만 아니라 칼럼의 위치 값 지정도 가능하다.
  * ex) titanic_df.ix[0,'Pclass']
  * **혼돈을 주기 때문에 현재 판다스에서 사라지게 되었다.**
    * 명칭기반 인덱싱인지 위치기반 인덱싱인지 혼선이 있기 때문이다.
* DataFrame iloc[] 연산자
  * **위치 기반 인덱싱**만 허용하기 때문에 행과 열 값으로 integer 또는 integer형의 슬라이싱, 팬시 리스트 값을 입력해줘야 한다.
  * 슬라이싱과 팬시 인덱싱은 제공하나 명확한 위치 기반 인덱싱이 사용되어야 하는 제약으로 인해 불린 인덱싱은 제공하지 않는다.
* DataFrame loc[] 연산자
  * **명칭 기반**으로 데이터를 추출한다.
  * index가 숫자 형일 수 있기 때문에 명칭 기반이라고 무조건 문자열을 입력한다는 선입견을 가지면 안된다.
  * 슬라이싱 기호를 적용하면 (종료 값-1)이 아니라 종료 값까지 포함하는 것을 의미한다.
* 불린 인덱싱
  * ex) titanic_boolean=titanic_df[titanic_df['Age']>60]
  * titanic_boolean 객체 타입은 DataFrame
  * 여러 개의 복합 조건일 때도 가능하다.
    * and : &
    * or : |
    * Not : ~



> 정렬, Aggregation 함수, GroupBy 적용

* DataFrame, Series의 정렬 - sort_values()
  * by : 특정 칼럼을 입력하면 해당 칼럼으로 정렬을 수행한다.
  * ascending=True : 오름차순 정렬
  * inplace=False : DataFrame은 그대로 유지하며 정렬된 DataFrame을 결과로 반환한다.
* Aggregation 함수 적용
  * min(), max(), sum(), count()와 같은 aggregation 함수의 적용은 RDBMS SQL의 aggregation 함수 적용과 유사하다.

* groupby() 적용
  * 사용 시 입력 파라미터 by에 칼럼을 입력하면 대상 칼럼으로 groupby된다.
  * DataFrame에 groupby()를 호출해 반환된 결과에 aggregation 함수를 호출하면 groupby() 대상 칼럼을 제외한 모든 칼럼에 해당 aggregation 함수를 적용한다.



> 결손 데이터 처리하기

* 결손 데이터 : 칼럼에 값이 없는, 즉 Null인 경우를 의미하며, 이를 넘파이의 NaN으로 표시한다.
* NaN 여부를 확인하는 API는 isna()
* NaN 값을 다른 값으로 대체하는 API는 fillna()
  * fillna()를 이용해 반환 값을 다시 받거나 inplace=True 파라미터를 fillna()에 추가해야 실제 데이터 세트 값이 변경된다.



> apply lambda 식으로 데이터 가공