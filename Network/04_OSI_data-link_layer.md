`date: 25.02.10`
> '모두의 네트워크'를 기반으로 학습한 내용입니다. 
# Lesson 12. 데이터 링크 계층의 역할과 이더넷
## 1. 데이터 링크 계층의 역할
데이터링크 계층: **네트워크 장비 간에 신호를 주고 받는 규칙**을 정하는 계층
- 랜에서 데이터를 정상적으로 주고받기 위해 필요함
- 일반적으로 많이 사용되는 규칙: `이더넷(ethernet)`

### 2. 이더넷
- 허브와 같은 장비에 연결된 컴퓨터와 데이터를 주고받을 때 사용

    <details>    <summary> <strong> 허브의 특징</strong> </summary>
    <br>
    <img width="451" alt="Image" src="https://github.com/user-attachments/assets/f73f9a24-f705-411f-b54a-fd61aa7399c7" />     

    약해지거나 파형이 뭉그러진 전기 신호를 복원, 해당 전기 신호를 전달받은 포트를 제외한 나머지 포트에 전달
    - 허브를 사용하는 랜 환경에서는 특정한 컴퓨터 한 대에 데이터를 보내려고 해도 다른 모든 컴퓨터에 전기 신호가 전달됨. 
    </details>
<br>

- 데이터에 목적지 정보를 추가해서 보내고 목적지 이외의 컴퓨터는 데이터를 받더라도 무시하게 되어있음

- `충돌` (collision): 컴퓨터 여러 대가 동시에 데이터를 보내면 데이터들이 서로 부딪힐 수 있음
  
➡️ 이더넷은 **여러 컴퓨터가 동시에 데이터를 전송해도 충돌이 일어나지 않는 구조**로 되어 있음
  - 이더넷에서 시점을 늦추는 방법: `CSMA/CD`
    > CSMA/CD (Carrier Sense Multiple Access with Collision Detection. 반송파 감지 다중 접속 및 충돌 탐지)
    > - CS: 데이터를 보래녀로 하는 컴퓨터가 케이블에 신호가 흐르고 있는지 아닌지를 확인한다
    > - MA: 케이블에 데이터가 흐르고 있지 않다면 데이터를 보내도 좋다
    > - CD: 충돌이 발생하고 있는지를 확인한다.
    > - 요즘에는 효율이 좋지 않아 거의 사용하지 않음

<br>

# Lesson 13. MAC 주소의 구조
## 1. MAC 주소
랜 카드: 비트열 (0, 1) -> 전기 신호  
이런 랜 카드에는 `MAC 주소` (= 물리주소)라는 번호가 정해져 있음 

### **MAC 주소**
- 전 세계에 *유일한 번호*로 할당
- 48비트 숫자로 구성
  - 앞 24비트: 랜 카드를 만든 제조사 번호
  - 뒤 24비트: 제조사가 랜 카드에 붙인 일련번호
    ```bash
    00-23-AE-D9-7A-9A
    \ 제조사/ \일련번호 /
    ```
  
### **이더넷 헤더**
OSI의 데이터링크 계층, TCP/IP 모델의 네트워크 계층에서는 **이더넷 헤더**와 **트레일러**를 붙임
- **이더넷 헤더**: 목적지 MAC 주소 (6바이트) + 출발지 MAC 주소 (6바이트) + 유형 (2바이트)
  - 이더넷 유형: 이더넷으로 전송되는 상위계층 프로토콜의 종류
    |유형번호|프로토콜|
    |---|---|
    |0800|IPv4|
    |0806|ARP|
    |8035|RARP|
    |814C|SNMP over Ethernet|
    |86DD|IPv6|

### **트레일러**
트레일러 = `FCS` (Frame Check Solution)  
: 데이터 전송 도중에 오류가 발생하는지 확인하는 용도로 사용

> 이더넷 헤더 + 트레일러 => 프레임
> - 네트워크를 통해 프레임이 전송됨

# Lesson 14. 스위치의 구조
## 1. MAC 주소 케이블
### 스위치
: 스위치: 데이터 링크 계층에서 동작
(= 레이어 2 스위치, 스위칭 허브)


- 스위치 내부에 MAC 주소 테이블 존재
  - MAC 주소 테이블 (= 브리지 테이블)  
  : 스위치의 포트 번호와 해당 포트에 연결되어 있는 컴퓨터의 MAC 주소가 등록되는 데이터베이스
- MAC 주소 학습 기능  
  - 스위치의 전원을 켠 상태에서는 아직 MAC 주소 테이블에 아무것도 등록되어 있지 않음
  - 컴퓨터에서 프레임이라는 데이터가 전송되면 MAC 주소 테이블을 확인
  - 출발지 MAC 주소가 등록되어 있지 않으면 MAC 주소를 포트와 함께 저장

### 플러딩
플러딩(Flooding): 송신포트 이외의 포트에 데이터가 전송되는 데이터 전송
<img width="443" alt="Image" src="https://github.com/user-attachments/assets/742b0282-0140-488a-93c9-0c2f898e6b5d" />  

- 목적지 MAC 주소가 저장되어 있지 않으면 무분별하게 모든 포트에 데이터 전송이 된다.
- 목적지 MAC 주소가 저장되어 있으면? 목적지에만 데이터가 전송된다. 
<aside>

    💡 MAC 주소 필터링
    : MAC 주소를 기준으로 목적지를 선택하는 것
    -> 이것으로 불필요한 데이터를 네트워크에 전송하지 않게 됨.
</aside>

# Lesson 15. 데이터가 케이블에서 충돌하지 않는 구조
## 1. 전이중 통신과 반이중 통신
### **전이중 통신 방식**
: 데이터의 송수신을 <u>동시에</u> 통신하는 방식  
➡️ 데이터를 동시에 전송해도 충돌이 발생하지 않음  
(ex. 랜 케이블, 스위치)  
<img width="446" alt="Image" src="https://github.com/user-attachments/assets/db25a61d-c86c-4762-acd4-c3af53101a99" /><img width="432" alt="Image" src="https://github.com/user-attachments/assets/3fd04fc3-e285-4f6e-9e49-a9c7947ece7b" />

### **반이중 통신 방식**
: 회선 하나로 송신과 수신을 번갈아가면서 통신하는 방식  
➡️ 데이터를 동시에 전송하면 <u>충돌</u> 발생  
(ex. 더미 허브)
<img width="452" alt="Image" src="https://github.com/user-attachments/assets/84eb9786-bebd-4e40-9e00-065e80b138c3" />

## 2. 충돌 도메인
충돌 도메인: 충돌이 발생할 때 그 영향이 미치는 범위  
충돌 도메인의 범위가 넓을 수록 네트워크가 지연됨

- 허브: 연결되어 있는 컴퓨터 전체가 하나의 충돌 도메인이 됨 (충돌의 영향이 모든 컴퓨터에 미침)
  <img width="419" alt="Image" src="https://github.com/user-attachments/assets/7cff41d1-3922-4d94-b017-a1440aece24d" />
- 스위치: 전이중 통신 방식이므로 충돌 도메인의 범위가 좁음
    <img width="436" alt="Image" src="https://github.com/user-attachments/assets/c3e7dd83-6558-4928-99af-44bc6ff1e81c" />

# Lesson 16. 이더넷의 종류와 특징
## 1. 이더넷 규격
이더넷은 케이블 종류나 통신 속도에 따라 다양한 규격으로 종류함
![Image](https://github.com/user-attachments/assets/8ce4668f-7bf7-4813-92c9-a84866e7d211) 
```bash
10BASE-T    //예시
```
- `10`: 통신속도 (-> 10Mbps)
- `BASE`: 전송방식 (-> BASEBAND: 펄스 신호에 의한 디지털 전송 방식)
- `T`: 케이블 종류