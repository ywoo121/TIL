`date: 25.02.11`
> '모두의 네트워크'를 기반으로 학습한 내용입니다. 

# Lesson 17. 네트워크 계층의 역할
<img width="369" alt="Image" src="https://github.com/user-attachments/assets/e69f5bd2-22b3-47c3-825e-57347c0d40c9" />

데이터 링크 계층에서는 이더넷 규칙을 기반으로 데이터의 전송을 담당함   
(같은 네트워크에 있는 컴퓨터로는 데이터를 전송할 수 있지만, 인터넷이나 다른 네트워크로는 데이터를 전송할 수 없음)  
➡️ 네트워크 계층: 네트워크 간의 통신을 가능하게 해줌

## 1. 네트워크 간의 연결 구조
- 라우터: 데이터의 목적지가 정해지면 해당 목적지까지 어떤 경로로 가는 것이 좋은지를 알려주는 기능 (라우팅 테이블 존재. 경로 정보를 등록하고 관리)
- IP주소 필요  
  <img width="419" alt="Image" src="https://github.com/user-attachments/assets/4104045c-10c6-4914-aa40-8ba5e71465f8" />
  
  : 어떤 네트워크의 어떤 컴퓨터인지를 구분할 수 있도록 하는 주소
- 라우팅: 목적지 IP주소까지 어떤 경로로 데이터를 보낼지 결정하는 것
  
## 2. IP
네트워크 계층에는 IP(Internet Protocol) 존재
![Image](https://github.com/user-attachments/assets/8c4b4742-30d2-4924-8e29-e03d9d0aba29)
- 네트워크 계층에서 캡슐화할 때 IP헤더를 붙임
- IP헤더에는 '**출발지 IP 주소**'와 '**목적지 IP 주소**'가 포함되어 있음
- IP 프로토콜을 사용하여 캡슐화할 때 데이터에 IP 헤더가 추가되는데, 이렇게 만들어 진 것을 `IP패킷`이라고 함
  
# Lesson 18. IP 주소의 구조
## 1. IP 주소란?
`IP주소`: IP통신에 필요한 고유 주소
- ISP에게 받을 수 있음 (ISP: internet service provider. (예)SKT, KT...)

### IP 버전
**IPv4**
: 32비트로 되어 있어 IP 주소를 약 43억 개 만들 수 있음  
-> IP주소가 부족해지면서 IPv6를 사용하게 됨

**IPv6**
: 128비트로 되어 있어 약 340간 개를 만들 수 있음

### IP주소의 종류
<img width="412" alt="Image" src="https://github.com/user-attachments/assets/1db38112-abec-4b23-8437-8053a4393c20" />  

|공인IP주소|사설IP주소|
|-|-|
|인터넷에 직접 연결되는 컴퓨터나 라우터에 사용|회사나 가정의 랜에 있는 컴퓨터에 사용|
|ISP가 제공|관리자가 할당 or DHCP 기능 사용하여 할당|

> DHCP(Dynamic Host Configuration PRotocol)  
> : IP 주소를 자동으로 할당하는 프로토콜

**IP주소의 구조**  
<img width="446" alt="Image" src="https://github.com/user-attachments/assets/3bed699b-885a-4bea-a59f-dac220e2c4eb" />
- 네트워크 ID: 어떤 네트워크인지
- 호스트 ID: 해당 네트워크의 어느 컴퓨터인지
- => 두 가지가 합쳐져 IP 주소가 되는 것

# Lesson 19. IP 주소의 클래스 구조
## 1. IP 주소 클래스
IPv4 = 32비트  
→ 네트워크 ID 또는 호스트 ID의 크기 변경을 위해 네트워크 크기를 조정할 수 있음  
➡️ **클래스**
|클래스 이름|내용|네트워크ID|호스트ID|
|---|---|---|--|
|A 클래스|대규모 네트워크 주소|8비트|24비트|
|B 클래스|중형 네트워크 주소|16비트|16비트|
|C 클래스|소규모 네트워크 주소|24비트|8비트|
|D 클래스|멀티캐스트 주소|
|E 클래스|연구 및 특수용도 주소|

*일반적으로 A ~ C 클래스 사용

### 클래스와 공인 IP 주소의 범위
|종류|공인 IP 주소의 범위|
|---|---|
|A 클래스|1.0.0.0 ~ 9.255.255.255 / 11.0.0.0 ~ 126.255.255.255|
|B 클래스|128.0.0.0 ~ 172.15.255.255 / 172.32.0.0 ~ 191.255.255.255|
|C 클래스|192.0.0.0 ~ 192.167.255.255 / 192.169.0.0 ~ 223.255.255.255|


### 클래스와 사설 IP 주소의 범위
|종류|공인 IP 주소의 범위|
|---|---|
|A 클래스|10.0.0.0 ~ 10.255.255.255|
|B 클래스|172.16.0.0 ~ 172.31.255.255|
|C 클래스|192.168.0.0 ~ 192.168.255.255|

# Lesson 20. 네트워크 주소와 브로드캐스트 주소의 구조
## 1. 네트워크 주소와 브로드캐스트 주소
→ 특별한 주소로, 컴퓨터나 라우터가 자신의 IP로 사용하면 안되는 주소
<img width="456" alt="Image" src="https://github.com/user-attachments/assets/6115fc9e-0fb8-4716-9f5f-e0165891d49c" />
- 네트워크 주소: 호스트 ID가 0
- 브로드캐스드 주소: 호스트 ID가 255

**네트워크 주소**  
<img width="427" alt="Image" src="https://github.com/user-attachments/assets/19d247bd-9db9-4963-add3-2c94518e84ab" />  
: 전체 네트워크에서 작은 네트워크를 식별하는데 사용
- 호스트 ID가 10진수로 0이면 그 네트워크 전체를 대표하는 주소  
→ 전체 네트워크의 대표 주소


**브로드캐스트 주소**  
<img width="420" alt="Image" src="https://github.com/user-attachments/assets/7cf41faa-3c7c-4918-a0bd-182fc39ec0cd" />  
: 네트워크에 있는 컴퓨터나 장비 모두에게 한 번에 데이터를 전송하는데 사용되는 전용 IP 주소

> ‼️ 네트워크 주소나 브로드캐스트 주소는 컴퓨터에 설정할 수 없다.

# Lesson 21. 서브넷의 구조
## 1. 서브넷
### 서브넷
: 네트워크를 분할함  

<img width="441" alt="Image" src="https://github.com/user-attachments/assets/88fff801-5a20-4dd9-8925-d7a4803b3487" />    

대규모 네트워크를 작은 네트워크로 분할하여 브로드 캐스트로 전송되는 패킷의 범위를 좁힐 수 있음  
(→ IP 주소를 더 효과적으로 활용 가능함)

`서브네팅`: 네트워크를 분할하는 것  
`서브넷`: 분할된 네트워크

### 서브넷팅 방법
: 기존에 네트워크 ID와 호스트 ID로 구성되어 있던 것을 네트워크 ID, 서브넷 ID, 호스트 ID로 나눈다
<img width="431" alt="Image" src="https://github.com/user-attachments/assets/b6a65d51-f88e-441b-bfbe-f02f4ecb51ec" />  

> 호스트ID에서 비트를 빌려 서브넷으로 만들 수 있음

## 2. 서브넷 마스크
IP 주소를 서브넷팅하면 어디까지 네트워크 ID이고 어디부터가 호스트 ID인지 판단하기 어려울 때가 있음  
➡️ `서브넷 마스크`라는 것을 사용

### 서브넷 마스크
: 네트워크 ID와 호스트 ID를 식별하기 위한 값
<img width="423" alt="Image" src="https://github.com/user-attachments/assets/650d463f-4897-491d-b6bb-8e0ee6d8857b" />

- 프리픽스 표기법으로 사용 가능  
  : 서브넷 마스크를 슬래시(/비트 수)로 나타낸 것
  <img width="416" alt="Image" src="https://github.com/user-attachments/assets/d6cd0b82-1f45-4740-8ef2-7a58a2a41890" />
- C클래스 서브넷팅   
  <img width="429" alt="Image" src="https://github.com/user-attachments/assets/49c9c371-ebf6-4c3a-8668-9274ed9e79a6" /> 
  - 프리픽스 표기법: 255.255.255.240/28  
  (C클래스, 24비트 네트워크+4비트 서브넷ID, 4비트 호스트)
# Lesson 22. 라우터의 구조
## 1. 라우터 (Router)
라우터: *네트워크 분리 가능*
<img width="443" alt="Image" src="https://github.com/user-attachments/assets/97b89ae2-501f-4676-93c6-1f27194a9a84" />

스위치: 스위치만 있는 환경에서는 모든 컴퓨터와 스위치가 *동일한 네트워크*에 속함 (허브도 동일)
<img width="439" alt="Image" src="https://github.com/user-attachments/assets/00867cbd-03ff-413e-85a2-555aa5c62bfd" />

### 기본 게이트웨이(Default Gateway)
<img width="456" alt="Image" src="https://github.com/user-attachments/assets/2501af4d-973e-4281-ba0a-7f8fd1e53439" />  

컴퓨터 1이 컴퓨터 6에 접속한다고 가정.  
컴퓨터 1이 다른 ㅔ트워크에 데이터를 전송하려면 라우터의 IP 주소를 설정해야 함.  
➡️ 네트워크의 출입구를 설정하는 것으로 `기본 게이트웨이`라고 함

- 컴퓨터 1은 다른 네트워크로 데이터를 보낼 때 어디로 전송해야 하는지 알지 못함.
- 그래서 네트워크의 출입구를 지정하고 일단 라우터로 데이터를 전송함
- 컴퓨터1은 192.168.1.0/24에 속해있기 때문에 라우터의 IP주소인 192.168.1.1로 설정한 것임
  
> 기본 게이트웨이 + 라우팅이 있어야 컴퓨터 6에 데이터를 보낼 수 있음

## 2. 라우팅
라우팅: 경로 정보를 기반으로 현재의 네트워크에서 다른 네트워크로 최적의 경로를 통해 데이터를 전송  
라우팅 테이블: 경로 정보가 등록되어 있는 테이블

### 경로 정보 등록
- 수동 등록: 소규모 네트워크에 적합
- 자동 등록: 대규모 네트워크에 적합  
  => 라우터 간에 라우팅 정보를 교환하기 위한 프로토콜: `라우팅 프로토콜`   
  (ex. RIP, OSPF, BGP 등)
