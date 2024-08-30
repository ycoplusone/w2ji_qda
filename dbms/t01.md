> ## [데이터베이스 인덱스의 오해와 진실](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52409)  
> 결합인덱스 : 2개 이상의 컬럼으로 인덱스를 구성한 경우
>> 1. 인덱스를 구성한 컬럼 순서대로 "=" 조건이 들어가야한다.   
>> 2. 결합인덱스를 구성할경우 "일자" 같은 컬럼은 후행에 자리 잡도록 인덱스를 구성해야 한다.  
>> 3. 결합인덱스를 구성할 경우 분포도가 나쁜 컬럼을 선행에 넣는것이 유리하다.  
>> #### - 공통적으로 사용하는 필수 조건절 컬럼을 우선.  
>> #### - "=" 조건의 컬럼을 다른 연사자 컬럼보다 우선한다.
>> #### - 대분류 , 중분류 , 소분류 컬럼순으로 구성한다.  
>> #### - 조건 정보 컬럼은 순서 정보 컬럼보다 우선한다.  
***
> ## [쉬운 것이 올바른 것이다. ‘인덱스 끝장리뷰’ (상)](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52402)
>> - 인덱스 대상 후보 컬럼 선정 기준
>> 1. 분포도가 좋은 컬럼 : 
>>> - 식별가능한 데이터 분포비율이 낮은것이 좋은 컬럼이다.  데이터의 분포도가 1% 이상이면 인덱스 효율성이 낮다.  
>> 2. 갱신(update)이 자주 발생하지 않는 컬럼.  
>>> - 갱신이 발생하는 컬럼의 경우 결합인덱스에서 후행에 넣는것이 바람직하다.  
>> 3. 조건절에서 자주 사용되는 컬럼.  
>>> - ![그림](https://dataonair.or.kr/publishing/img/knowledge/column_img_1434.jpg).  
>>> - 위 그림에서 처럼 조합과 빈도로 산출한다.    
>>> - 결합인덱스 = 컬럼3 + 컬럼4 + 컬럼6 + 컬럼7 순으로 생성하는것이 효율적이다.
>> 4. 조인의 연결고리에 사용되는 컬럼.  
>>> 오라클 쿼리에서 테이블간의 관계를 연결해주는 조인의 방법은 다음과 같이 3가지가 있다.    
>>> - nested loop join : 온라인 쿼리에서 90% 이상을 차지, 조인절에 인덱스가 반드시 있어야 한다.
>>> - sort merge join : 거의 발견할 수 없다. 조인절에 인덱스가 반드시 있어야 하는것은 아니다.  
>>> - Hash join : 배치쿼리에서 30% 이상을 차지, 조인절에 인덱스가 반드시 있어야하는것은 아니다.  
>>> ![인덱스 생성 이미지](https://dataonair.or.kr/publishing/img/knowledge/column_img_1435.jpg)
>>> 1번 위치에 인덱스를 생성할 경우 : 주문 테이블에서 고객 테이블로 접근(조인연결).  
>>> 2번 위치에 인덱스를 생성할 경우 : 고객 테이블에서 주문 테이블로 접근(조인연결).  
>>> 1번, 2번 위치에 모두다 있을 경우 : 오라클에서 통계 정보를 바탕으로 테이블간 방향을 결정.  
>>> 1번,2번 위치에 모두다 없을 경우 :  sort merge join 방식이나 Hash join 방식으로 플랜이 결정.  
>> 5. sort 발생을 제거하는 컬럼.  
>>> 하나의 테이블에 인덱스가 많으면 많을 수록 부하가 점점 증가 하듯이 결합인덱스도 컬럼 수가 많으면 부하가 점점 증가한다.  
>>> 결합인덱스에 조건절 컬럼 이외에 order by 절 컬럼을 추가할 때 발생하는 인덱스 부하와 추가하지 않때 sort 부하를 비교해 결정한다.  
>>> 쿼리의 조건에 과 ORDER BY 까지 확인해서 결합인덱스를 생성한다.  
***  
> ## [쉬운 것이 올바른 것이다. ‘인덱스 끝장리뷰’ (하)](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52396)
>> - 인덱스 수는 적정해야 한다.  
>>> 1. 코드성 테이블: 필요한 만큼 인덱스 생성 가능(인덱스 경합이 발생하지 않도록 주의).  
>>>> - 마스터 테이블 같은경우 필요한 만큼 생성한다, 단 인덱스 경합이 발생할수 있으므로 주의하자.  
>>> 2. 처리성 테이블 : 최소한으로 사용(대용량 테이블이라면 가능한 적게).  
>>>> - core 테이블 같은 경우 인덱스는 최소한으로 한다, 빈번한 cud가 발생 하나 인덱스를 최소화 한다.  
>>> 3. 집계성 테이블 : 필요한 만큼 적정하게 사용.  
>>>> - dw테이블을 의미한다 .  
>>>> - 데이터 집계 처리에 대한 부담보다는 조회에  비중이 있는 테이블이므로 인덱스가 많아도 무방하다.  
>>> 4. 로그성 테이블 : 필요 없음(필요에 따라서 하나 정도는 존재할수도 있음).  
>>>> - 시간정보에 대한 인덱스 정도면 충분하다.  
>> ***
>> - 해당 테이블에 인덱스가 너무 많다면, 인덱스 생성 여부를 결정하는 요소가 될수있다.  
>>> 1. 쿼리 구동 시간이 낮인지 밤인지에 따라서 인덱스 생성 여루ㅂ를 결정할수 있다(온라인, 배치).  
>>> 2. 누가 사용하는지에 따라서 인덱스 생성 여부를 결정 할수 있다(담당자 , 관리자, 사장).  
>>> 3. 얼마나 많이 구동되는지에 따라서 인덱스 생성 여부를 결정할 수 있다.  
>>> 4. 소형 테이블인 경우 인덱스는 있어야 한다.  
>> ***  
>> - 인덱스는 위치정보와 순서정보로 구성됐다.  
>> - 조건절에 사용하는 인덱스와 조인절에 사용하는 인덱스.  
>>> 1. 1:n 관계의 테이블 조인에서는 오히려 접근 범위가 커지기도한다.  
>>> 2. 쿼리에서는 조건절 인덱스가 최초로 접근하는 테이블을 결정한다.  
>>> 3. join 하는 테이블에 인덱스가 없는것이 where 하는 기준테이블에 인덱스 없는것보다 성능에 문제를 발생시킬수 있다.  
>> - 인덱스 생성/삭제 시 고려사항 : 인덱스는 만들때나 삭제할때 언제나 신중하게 접근하는것이 필요하다.  
>> 1. 신규 인덱스 생성하기 전에 유사 인덱스가 존재하는지 확인한다.  
>>> - 유사한 인덱스끼리 경합이 발생할 수도 있고, 기존 쿼리의 플랜이 변동하여 성능상에 문제가 발생할수 있다.  
>> 2. 신규인덱스 생성하기전에 index split을 유발하지 않는지 확인한다.  
>>> - 인덱스 분류 작업이 한곳으로 집중되어서, 동일한 leaf block에 대해 과도한 split이 발생한다면 성능상의 문제가 발생한다. Reverse index를 이용해서 해결한다.  
>> 3. 신규인덱스 생성하기 전에 CBO 방식에서의 통계정보가 최신인지 확인한다.  
>>> - 통계정보와 실제 데이터의 차이가 현저하기 발생하면 인덱를 이용하지 못할수 있다.  
>> 4. 기존 인덱스 삭제하기 전에 사용하지 않는 미사용 인덱스인지 반드시 확인한다.  
>>> - dba 입장에서 어디서 사용되는지 확실할수 없기때문에 삭제는 엄청 부담스럽다.  
>> - 결합 인덱스의 컬럼 순서 결정방법 : 결합인덱스를 만들때 컬럼의 순서 결정이 가장 중요하다.  
>>> 1. 공통적으로 사용하는 필수 조건절 컬럼을 우선한다.  
>>> 2. '=' 조건의 컬럼을 다른 연산자 컬럼 보다 우선한다.  
>>> 3. 대분류 중분류 소분류 컬럼 순으로 구성한다.  
>>> 4. 위치(조건) 정보 컬럼은 순서(sort) 정보 컬럼보다 우선한다.  
***
> ## [누구도 알려주지 않았던 ‘오라클 인덱스 생성도’의 비밀](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52389)
>> ※ 어머니 심부름 : 두부가게와 쌀가게 => 무거운 쌀은 나중에 가벼운곳 부터 처리한다.  
>> ※ 인덱스 생성도의 기본 규칙 : 실선은 inner join 또는 조건절 , 점선은 outer join , ●인덱스있음 ,○인덱스없음.  
>> ※ 인덱스 생성도에 대한 이해.  
>>> - CBO(Cost Based Optimizer) 방식은 오라클이 주도적으로 처리 하는것 처럼 보이지만 실제로는 수동적인 역할만한다.  
>>> - 통계정보를 기준으로 최소의 비용으로 플랜을 보여주는것뿐이다(현재 dlive dw의 통계정보는 갱신하지 않는다 하여 CBO를 믿을수 없다).  
>>> - 인덱스 생성은 항상 목적지 컬럼에 생성되어 있어야 한다.  
>>> - /*+ LEADING( 순서 테이블 들 )*/ 해당 구문으로 테이블 로드 순서를 정할수 있다.  
>>> ![예제1](https://dataonair.or.kr/publishing/img/knowledge/column_img_1505.jpg)  
>>> ![예제2](https://dataonair.or.kr/publishing/img/knowledge/column_img_1506.jpg)  
>>> ![예제3](https://dataonair.or.kr/publishing/img/knowledge/column_img_1507.jpg)  
>>> ![예제4](https://dataonair.or.kr/publishing/img/knowledge/column_img_1508.jpg)  
>>> ![예제5](https://dataonair.or.kr/publishing/img/knowledge/column_img_1509.jpg)  
***  
> ## [누구도 알려주지 않았던 ‘오라클 쿼리 작성의 비법’](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52385)  
>> ※ 공정무역과 공정여행 그리고 공정쿼리.  
>>> - 공정쿼리 : 어느 누가 보더라도 쉽게 빠르게 쿼리의 의미를 전달 할수 있다.  
>> ※ 무엇을(데이터조회결과에 대해서 집중) + 어떻게(과정에 집중한다) = 공정쿼리.  
>>> - 공정쿼리로 작성한 쿼리에서는 쿼리의 결과뿐 아니라, 생성해야 할 인덱스 정보와 접근되어야할 플랜정보까지 모두 알수 있다.  
>>> ![공정쿼리= 무엇을(What) + 어떻게(How)](https://dataonair.or.kr/publishing/img/knowledge/column_img_1519.jpg)  
>> ※ 나막사 주부의 심부름 메모지.  
>>> - ![나막사 주부가 남편에게 남겨 놓은 메모](https://dataonair.or.kr/publishing/img/knowledge/column_img_1520.jpg).  
>>> - ![메모지에 적힌 순서에 따라 나막사 주부의 남편이 매장을 방문한 경로](https://dataonair.or.kr/publishing/img/knowledge/column_img_1521.jpg).  
>> ※ 나계획 주부의 심부름 메모지.  
>>> ![나계획 주부가 남편에게 남겨 놓은 메모](https://dataonair.or.kr/publishing/img/knowledge/column_img_1522.jpg).  
>>> ![메모지에 적힌 순서에 따라 나계획 주부의 남편이 매장을 방문한 경로](https://dataonair.or.kr/publishing/img/knowledge/column_img_1523.jpg).  
>> ※ 공정쿼리! 반드시 이렇게 작성하라.  
>>> - ![인덱스 생성도](https://dataonair.or.kr/publishing/img/knowledge/column_img_1524.jpg).  
>>> - ![나신입 사원이 작성한 쿼리](https://dataonair.or.kr/publishing/img/knowledge/column_img_1525.jpg).  
>>> - ![나신입 사원이 작성한 쿼리와 인덱스 생성도](https://dataonair.or.kr/publishing/img/knowledge/column_img_1526.jpg).  
>> ※ 공정쿼리를 작성하기에 앞서 다음 3가지 공정쿼리 작성규칙을 이해하자.  
>>> 1. from 절에 나열할 테이블 순서는 인덱스 생성도의 테이블 접근 순서와 동일하다.  
>>> 2. 조인절의 접근 방향은 인덱스 생성도의 조인절 접근 방향과 동일하다.  
>>> 3. 조건절의 순서는 인덱스 생성도의 테이블 접근 순서에 따른 조건절 순서와 동일하다.  
>>> ![나신입 사원이 작성한 쿼리를 공정쿼리로 재작성](https://dataonair.or.kr/publishing/img/knowledge/column_img_1527.jpg)  
>>> ![*나신입 사원이 작성한 쿼리와 재작성한 공정쿼리의 비교*](https://dataonair.or.kr/publishing/img/knowledge/column_img_1528.jpg)
***
> ## [ 퀴리 최적화 및 튜닝을 위한 오라클 공정쿼리 작성법](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52380)  
>> ※ 배낭여행 스마트앱 만들기.  
>>> 가. 첫 진입 포지션을 잘 선정해야 한다.  
>>> 나. 진입 이후 그 다음 포지션 선정 시 가까운 거리에 있는 작은 숫자를 우선해 선택한다.  
>>> 다. 한번 지나간 경로는 다시 지나가지 않게 경로를 선택한다(중첩 경로 지양).  
>> ※ 오라클 CBO방식과 통계정보.  
>>> - 오라클 CBO 방식에서 비용이란 물리적인 비용이 아니라 논리적인 비용을 의마한다.  
>>> - 논리적인 비용이란 어떤 근거로 비용이 산출되었는지 명확하게 알수 없다.  
>>> - 오라클에서 명시적으로 비용 산출 계산 방식을 공개하지 않는다는 말과 동일하다.  
>> ※ 테이블 접근 순서 규칙 1:진입형 테이블을 결정하라.  
>>> - 쿼리의 조건중 가장 선택도가 좋은 컬럼의 테이블을 최초 진입형 테이블로 결정한다.  
>>> ![교원평가 테이블](https://dataonair.or.kr/publishing/img/knowledge/column_img_1540.jpg)  
>>> ![테이블접근순서도](https://dataonair.or.kr/publishing/img/knowledge/column_img_1541.jpg)  
>>> - 인덱스 생성도와 공정쿼리 재작성하기  
>>> ![인덱스 생성 포인트](https://dataonair.or.kr/publishing/img/knowledge/column_img_1550.jpg)  
>>> ![공정 쿼리 재작성](https://dataonair.or.kr/publishing/img/knowledge/column_img_1551.jpg)  
***
> ## [만능 쿼리와 한 방 쿼리](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52375)
>> ※ 만능 쿼리에 대한 이해.  
>>> 입력 변수 값에 따라서 쿼리의 조건이 변경되는 쿼리를 통칭함.   
>>> ![동적 쿼리와 만능 쿼리에 대한 간단한 예제](https://dataonair.or.kr/publishing/img/knowledge/column_img_1563.jpg).  
>> ※ 한방쿼리에 대한 이해.  
>>> ![간단한 한방 쿼리의 예제](https://dataonair.or.kr/publishing/img/knowledge/column_img_1564.jpg).  
***
> ## [오라클 옵티마이저 ‘CBO와 RBO’ 이해하기](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52368)
>> ※ CBO방식과 RBO 방식  
>>> ![RBO방식과 CBO방식](https://dataonair.or.kr/publishing/img/knowledge/column_img_1582.jpg)  
>>> ![옵티마이저와 통계정보 그리고 실행계획](https://dataonair.or.kr/publishing/img/knowledge/column_img_1583.jpg)  
***
> ## [재미있는 DB 이야기 ‘60갑자와 쿼리’](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52366)
>> 특별한 내용없다.  
***
> ## [그림으로 배우는 ‘오라클 조인의 방식’ 이야기](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52359)  
>> ※ 조인이란 무엇인가.  
>>> - NESTED LOOP JOIN : 순차적 루프에 의한 접근 방식 , 소량의 데이터 처리에 적합.  
>>> - SORT MERGE JOIN : 정렬을 통한 접근방식, 거의 사용하지 않는 방식. 
>>> - HASH JOIN : 해지 함수를 이용한 접근방식, 대량의 데이터 처리에 적합. 
>> ※ NESTED LOOP JOIN   
>>> 테이블 간 조인을 순차적으로 수행한다,  테이블 간 접근 순서가 매우 중요하고, 선행 테이블의 처리 범위가 작아야 한다, 조인절의 목적지 컬럼에 반드시 인덱스가 존재해야한다.  
>>> 1. 고객 테이블에서 이름이 홍길동인 고객을 구한다(선행테이블 결정).  
>>> 2. 홍길동 고객의 수만큼 순차적으로 주문 테이블을 고객번호 컬럼으로 접근한다(순차적 접근).  
>>> 3. 주문 테이블에서 주문일자가 '20240708' 인 정보만 필터한다.  
>> ※ Hash Join  
>>> 대량의 데이터 처리에 유리하다, nl 조인의 처리 범위가 부담스럽거나 sort merge join 의 sort 가 부담스러울때 사용한다, 메모리에 해시 테이블을 생성하고 해시 함수를 이용해 연산 조인을 함에 따른 cpu사용이 증가할수 있으므로 조회빈도가 높은 온라인 프로그램에 적합하다.  
>>> - ![hash 예제](https://dataonair.or.kr/publishing/img/knowledge/column_img_1613.png).  
>>> - hash join 에서는 작언 테이블을 먼저 접근하는것이 성능면에서 더 좋다.  
>>> - 해시 테이블 구성 작업에 부하가 많이 발생하기 때문이다.  
>>> - 작은 테이블에 접근해  hash함수로 해시 테이블을 생성하고, 이후 큰 테이블에 접근해 hash함수를 통해 순차적으로 해시 테이블로 접근한다.  
>> ※ Nested loop join 장점.  
>>> - 부분범위 처리에 적합.  
>>> - 소량 데이터 처리에 적합.  
>>> - 온라인 프로그램에 적합.  
>>> - 일반적으로 흔하게 발생.  
>>> - 온라인 쿼리 약 90% 분포.  
>>> - 테이블 접근 순서가 중요.  
>>> - 조인절에 인덱스 필수.  
>>> - 순차적 접근.  
>> ※ Hash Join.  
>>> - 전체범위 처리에 적합.  
>>> - 대량 데이터 처리에 적합.  
>>> - 배치 프로그램에 적합.  
>>> - 대량 집계 작업 때 발생.  
>>> - 배치 쿼리 약 50% 분포.  
>>> - 작은 테이블로 해쉬 구성.  
>>> - 메모리 크기에 영향.  
>>> - Hash함수 이용한 접근.  
***
> ## [반드시 알아야 하는 오라클 힌트절 7가지](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52344)
>> ※ 힌트절이란 무엇인가.  
>>> 1. ordered from 절에 나열된 테이블 순서대로 접근한다.         => 접근 순서
>>> 2. leading 테이블 접근 순서를 명시적으로 표시한다.            => 접근 순서
>>> 3. USE_NL NESTED LOOP JOIN 방식으로 조인하도록 유도한다.     => 접근방법
>>> 4. USE_HASH HASH JOIN 방식으로 조인하도록 유도한다.          => 접근방법
>>> 5. INDEX 인덱스를 통한 ACCESS PATH 유도한다.                => 자원 할당 부분
>>> 6. FULL 테이블을 FULL SCAN 한다.                           => 자원 할당 부분
>>> 7. PARALLEL 병렬 처리를 통해서 성능을 높인다.                => 자원 할당 부분  
***
> ## [오라클 플랜을 보는 법](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52341)
>> ACCESS FULL : 고객 테이블 FULL SCAN(전체 접근).  
>> Cost=633K : 633,000 비용발생(논리적 비용 = IO + MEM + CPU + NET + …).  
>> Card=42M : 42,000,000건(접근하는 레코드 수).  
>> Bytes=15G : 15,000,000,000(42,000,000 * 1 ROW의 총 길이).  
>>> 1. 해당 쿼리에 대한 적절한 인덱스가 존재하지 않는 경우로써 필요한 인덱스를 생성함으로써 해결 가능하다.  
>>> 2. 인덱스는 존재하지만 부정확한 통계정보로 인하여 인덱스를 타지 않는 경우로써 최신의 통계 정보를 구성하거나 힌트절을 사용해 해결할 수 있다.  
>>> 3. 테이블 FULL SCAN하는것이 인덱스를 통해 랜덤 엑세스보다 유리한 경우로써, 데이터 조회 범위가 커서 인덱스를 사용하는것이 별로 효용성이 없다.  
***
> ## [개발자들의 영원한 숙제 ‘NULL 이야기’](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52319)  
>> ※ INDEX 에서의 NULL.  
>>> 1. NULL 회피전략이다. NULL 대신 대체값을 찾는다, 날짜의 경우 99991231 같은 공백은 추천하지 않는다 함수 사용시 오류 발생.  
>>> 2. 함수기반 인덱스를 이용하는것이다. 인덱스는 NULL값을 보관하지 않지만 함수기반 인덱스는 함수를 이용해 변환값을 보관하기 때문이다.  
***
> ## [알면 유용한 오라클 기능 ‘GATHER_PLAN_STATISTICS’](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52301)  
>> - SELECT /*+ GATHER_PLAN_STATISTICS */ * FROM 인사 WHERE 사용자명 = ‘이슬기’; .  
>> - SELECT * FROM TABLE(dbms_xplan.display_cursor(null,null,'ALLSTATS LAST')); .  
>> - 해석.  
>>> - Starts => 
오퍼레이션을 수행한 횟수를 의미한다. Starts * E-Rows 의 값이 A-Rows 값과 비슷하다면, 통계정보의 예측 Row 수와 실제 실행 결과에 따른 실제 Row 수가 유사함을 알 수 있다. 만약 >>> 값에 큰 차이가 있다면 통계정보가 실제의 정보를 제대로 반영하지 못했다고 생각할 수 있다. 이로 인해 오라클의 Optimizer가 잘못된 실행 계획을 수립할 수도 있음을 염두에 둬야 한다.  
>>> - E-Rows (Estimated Rows) => 
 통계정보에 근거한 예측 Row 수를 의미한다. 통계정보를 갱신할수록 값이 매번 다를 수 있으며, 대부분의 DB 운영에서는 통계정보를 수시로 갱신하지 않으므로 해당 값에 큰 의미를 둘 필요는 없다. 하지만 E-Rows 값과 A-Rows 값이 현격하게 차이가 있다면 오라클이 잘못된 실행 계획을 세울 수도 있음을 인지해야 하며 통계정보 생성을 검토해 보아야 한다.  
>>> - A-Rows (Actual Rows) =>
쿼리 실행 결과에 따른 실제 Row 수를 의미한다. 우리는 A-Rows 에서 중요한 여러 정보를 추정 할 수 있다. 이에 대한 부분은 이번 연재에서 계속 설명이 이어진다(이번 호 문제 부분에서).  
>>> - A-Time (Actual Elapsed Time) => 
쿼리 실행 결과에 따른 실제 수행 시간을 의미한다. 하지만 실행 시점의 여러 상황이 늘 가변적이고 또한 메모리에 올라온 Block의 수에 따라서 수행 시간이 달라지므로 해당 값에 큰 의미를 둘 필요는 없다.  
>>> - Buffers (Logical Reads) => 
논리적인 Get Block 수를 의미한다. 해당 값은 오라클 옵티마이저가 일한 총량을 의미하므로, 튜닝을 진행할 때 필자가 가장 중요하게 생각하는 요소 중 하나다.  
>>> - Reads (Physical Reads) => 
물리적인 Get Block 수를 의미한다. 동일한 쿼음이 아닌 경우에는 값이 0인 것을 보면 알 수 있듯이 메모리에서 읽어온 Block은 제외된다. 해당 값에 큰 의미를 둘 필요는 없다.  
***
> ## [알면 유용한 오라클 기능들](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52285)  
>> ※ COMMIT 이전의 상태로 되돌리는 기능 FLASHBACK.  
select * from v$parameter where name = 'db_flashback_retention_target‘

조회된 value 값은 분 단위 시간을 의미한다. 제한된 설정 시간 내에서 우리는 다음과 같은 쿼리를 사용하여 과거 시점의 데이터를 조회하거나 원복할 수 있다.

-- 1시간전 시점의 고객 테이블을 조회하는 쿼리
SELECT * FROM 고객 AS OF TIMESTAMP (SYSTIMESTAMP - INTERVAL ‘1’ HOUR)

-- 20분전 시점의 고객 테이블을 조회하는 쿼리
SELECT * FROM 고객 AS OF TIMESTAMP (SYSTIMESTAMP - INTERVAL ‘20’ MINUTE)

-- 2015년 01월 10일 10시 20분 시점의 고객 테이블을 조회하는 쿼리
SELECT * FROM 고객 AS OF TIMESTAMP TO_DATE(‘201501101020’, ‘YYYYMMDDHH24MI’)

-- 30분전 시점의 고객 테이블을 조회하는 쿼리
SELECT * FROM 고객 AS OF TIMESTAMP SYSDATE - 30 / (24 * 60)
만약 사용 권한이 없다면 DBA에게 요청하여 DBMS_FLASHBACK 패키지에 대한 EXECUTE 권한을 부여받아야 한다.

만약 20분 전에서 10분 전 사이에 삭제된 레코드를 원복하고 싶다면, 다음과 같은 쿼리 구문을 사용하면 된다.

INSERT INTO 고객
SELECT * FROM 고객 AS OF TIMESTAMP (SYSTIMESTAMP - INTERVAL ‘20’ MINUTE)
MINUS
SELECT * FROM 고객 AS OF TIMESTAMP (SYSTIMESTAMP - INTERVAL ‘10’ MINUTE)

또한 특정 시점에 존재했던 레코드를 조회해 새로운 테이블을 생성-추가할 수도 있다.

CREATE TABLE 고객_BACKUP
AS
SELECT * FROM 고객 AS OF TIMESTAMP TO_DATE(‘201501101020’, ‘YYYYMMDDHH24MI’)
***
> ## [오라클 DICTIONARY를 활용한 DB툴 프로그램 ‘FreeSQL’](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52273)
>> ※ Oracle DICTIONARY.  
사용자 소유의 모든 오브젝트 정보를 알고자 한다면 다음과 같이 조회 하면 된다.
SELECT * FROM USER_OBJECTS

사용자 소유의 테이블 정보를 알고자 한다면 다음과 같이 조회한다.
SELECT * FROM USER_TABLES

현재 시점의 세션 정보를 알고자 한다면 다음과 같이 조회한다.
SELECT * FROM V$SESSION

그렇다면 이와 같은 DB 시스템 정보를 제공하는 수많은 딕셔너리는 어떻게 알 수 있을까 바로 다음과 같이 조회하면 된다.

SELECT * FROM DICTIONARY
혹은
SELECT * FROM DICT
ALL_* : 현재 오라클에 접속한 사용자가 접근 가능한 모든 정보들에 대한 딕셔너리
USER_* : 현재 오라클에 접속한 사용자가 소유하고 있는 모든 정보들에 대한 딕셔너리
DBA_* : 관리자 계정으로 접속한 사용자가 조회 가능한 모든 정보들에 대한 딕셔너리
V$* : Dynamic Performance View라고도 하며, DBA의 모니터링에 많이 이용되는 딕셔너리
***
> ## [이제는 말할 수 있다: 주식 자동매매 프로그램(상)](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52255).  
> ## [이제는 말할 수 있다: 주식 자동매매 프로그램(하)](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52242).  
> ## [개발자들이 자주 접하는 오라클 에러 메세지](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52226).  
>> - “ORA-00001 : 유일성 제약조건에 위배됩니다.“.  
>> - “ORA-00942 : 테이블 또는 뷰가 존재하지 않습니다.”.  
>> - “ORA-00904 : 열명이 부적합합니다.“.  
>> - “ORA-01017 : 유효하지 않는 사용자/패스워드에 의한 접근을 제한합니다.“.  
>> - “ORA-01722 : 수치가 부적합합니다.“.  
>> - “ORA-01555 : 스냅샷이 너무 오래 되었습니다. (롤벡 세그먼트가 너무 작습니다)”.  
>> - “ORA-00911 : 문자가 부적합합니다.“.  
>> - “ORA-12541 : 리스너가 존재하지 않습니다.“.  
>> - “ORA-03113 : 통신 채널에 EOF가 있습니다.“.  
>> - “ORA-01476 : 제수가 0 입니다.“.  
> ## [ 재미있는 DB 이야기 ‘사라진 날짜를 찾아라’](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52221)  
> ## [오라클 랜덤 함수와 사용자 정의 함수](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52213)  
> ## [그림으로 배우는 ‘공정쿼리와 인덱스 생성도’](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52204)  
> ## [이병국의 개발자를 위한 DB 이야기: 디폴트 세팅의 함정과 오라클 파라미터](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52187)  
> ## [오라클 운반 최소 단위 BLOCK](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52149)  
>> OS Block → Oracle Block → Extent → Segment → Tablespace → Database  
>> SELECT VALUE FROM V$PARAMETER WHERE NAME = ‘db_block_size’  
>> ※ 오라클 블록의 크기와 OLTP & OLAP.  
>>> OLTP(Online Transaction Processing): 일반적인 업무 처리에 적합(현황 처리가 목적, Block Size↓)  
>>> OLAP(Online Analytical processing): 분석을 위한 통계에 적합(미래 예측이 목적, Block Size↑)  
>>> 데이터베이스 성능에 영향을 미치는 파라미터로 한번의 i/o로 운반할수 있는 블록수 => SELECT VALUE FROM V$PARAMETER WHERE NAME = ‘db_file_multiblock_read_count‘ 
>> ※ 오라클 블록과 Row Chaining & Row Migration.  
> ## [이병국의 개발자를 위한 DB 이야기(30회) : DB 엔지니어의 가볍게 읽는 세상 이야기](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52118)
> ## [이병국의 개발자를 위한 DB 이야기: 튜닝(31회) : 개발자를 위한 DB 튜닝 실전(1편)](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52103)
> ## [이병국의 개발자를 위한 DB 이야기: 튜닝(32회) : 개발자를 위한 튜닝 실전(2편)](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52095)  