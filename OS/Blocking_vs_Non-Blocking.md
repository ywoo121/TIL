```date: 25.02.06```
## 1. 정의
![Image](https://github.com/user-attachments/assets/c84d2509-191e-4fe3-bcca-7cd26b2a34a1)
### 블로킹 (Blocking)
: 현재 실행 중인 작업이 완료될 때까지 다음 작업을 기다리는 방식  
A함수가 B함수를 호출하면, 제어권을 A가 호출한 B함수에 넘겨준다

1. A함수가 B함수를 호출하면 B에게 제어권을 넘긴다.
2. 제어권을 넘겨받은 B는 열심히 함수를 실행한다. A는 B에게 제어권을 넘겨주었기 때문에 함수 실행을 잠시 멈춘다.
3. B함수는 실행이 끝나면 자신을 호출한 A에게 제어권을 돌려준다.

### 논블로킹 (Non-Blocking)
: 현재 실행 중인 작업의 완료를 기다리지 않고 다음 작업을 실행하는 방식    
A함수가 B함수를 호출해도 제어권은 그대로 자신이 가지고 있는다.


> 현재 작업이 다른 작업의 실행을 `차단`하는가의 차이

## 2. 사용 이유
**블로킹**  
: 작업의 완료와 순차적 실행을 보장하여 프로그램의 실행 흐름을 쉽게 관리하기 위해서

**논블로킹**  
: 시스템 자원의 효율적 사용 비동기적 작업 처리를 통해 프로그램의 반응성과 처리 능력을 향상시키기 위해서

## 3. 사용 방법
### 블로킹
![Image](https://github.com/user-attachments/assets/0628aef7-4f0d-4ac9-95f5-de4045239350)  
```js
const fs = require('fs');
const data = fs.readFileSync('./file_path');
console.log('파일 읽기 완료', data);
```
- `fs.readFileSync` 호출시 제어권이 파일 시스템(fs)에게 전달됨.
    - 제어권이 넘어 갔기 때문에, 그동안 다른 작업을 수행할수 없음 ⇒ `Block`
- 파일 읽기가 완료되면 `fs.readFileSync` 가 제어권을 반환
    - 제어권이 반환 되었기 때문에 그 다음 작업 진행이 가능.

### 논블로킹
![Image](https://github.com/user-attachments/assets/770d48a8-e909-472c-bdfc-bc45acc61fc0)  
```js
const fs = require('fs');

fs.readFile('./file_path', (err, data) => {
	if(err) return err;
	console.log('파일 읽기 완료', data);
})
```
- `.readFile` 호출시 제어권을 넘겨 실행후 즉시 제어권 반환
    - 제어권을 반환 받았기 때문에 다른 작업 수행이 가능 ⇒ Non-Block
- 파일 읽기가 완료 되면 `fs.readFile` 에 등록된 `callback` 을 호출.

---
## ✅ 블로킹/논블로킹, 동기/비동기 정리
<aside>

**[동기 / 비동기] → `완료` 가 중요한 느낌?**
- 동기 : `완료` 따짐
  - 함수를 호출하면, 그 함수가 ‘완전히’ 끝날 때까지 제어권(실행 흐름)이 ‘호출된 함수’ 쪽에 머무른다.
  - 함수가 종료(결과 반환)되면, 제어권이 ‘다시’ 호출한 곳으로 돌아온다.
  1. A → B 호출 (B 실행, 제어권 B)
  2. A는 B의 실행이 끝나고 리턴값과 제어권을 넘겨줄 때까지 대기해야
  3. B의 실행이 완료되면 제어권을 A에게로 넘겨주고 A가 실행됨
- 비동기: `완료` 따지지 않음
  - 호출 시점에는 즉시(매우 빨리) 제어권을 원래 호출부(A)에게 돌려준다.
  - 완료 시점에(나중에) “콜백, 이벤트, Promise/Future 등”으로 결과를 알려준다.
  1. A → B 호출 (B 실행, 제어권: A로 개빨리 돌아옴)
  2. 비동기는 완료를 따지지 않음으로 A도 계속 실행됨

**[블로킹 / 논블로킹] → 말 그대로 `차단`** 

: 차단을 위해 제어권을 넘기냐 아니냐의 관점? 

- 블로킹: 차단하기 위해 제어권을 완전히 넘김
    1. A → B 호출 (B 실행, 제어권: B)
    2. B에게 제어권이 완전히 넘어갔으므로 A는 block된다.
    3. B의 실행이 다 끝난 후 제어권이 A한테로 반환. 그때 A 실행 가능
- 논블로킹: 차단하지 않으므로 제어권을 실행할 때 줬다가 바로 다시 돌려받음
    1. A → B 호출 (B 실행, 제어권: A)
    2. A가 계속 제어권을 가지고 있기 때문에 B호출 이후에도 A 계속 실행
</aside>

![Image](https://github.com/user-attachments/assets/ad5fe608-b4c8-4c6d-8cc0-71e194753612)

### 1. Sync-Blocking
![Image](https://github.com/user-attachments/assets/c19491f9-4204-43cd-9fb3-0f2037a7132d)
- Sync: A는 B를 호출하고 B의 완료(리턴값)이 반환되어야 함 => A 대기
- Blocking: B가 실행을 완료하여 제어권 & 리턴값을 돌려줄 때까지 대기
  
### 2. Sync-NonBlocking
![Image](https://github.com/user-attachments/assets/7109527c-8fff-410b-afaa-4f6e64df969e)
- Sync: 동기이므로 A는 B의 리턴값 필요함. B 실행 중 함수 실행 완료되었는지 지속적으로 물어봄
- NonBlocking: 제어권은 A한테 있음
  
### 3. Async-Blocking
![Image](https://github.com/user-attachments/assets/2a2b8d66-10d1-449f-9d3a-4b5678697a7c)
- Async: B와 상관없이 제어권은 일단 A
- Blocking: 그럼에도 불구하고, A는 B에게 제어권을 넘김  
=> A함수는 자신과 관련 없는 B의 작업이 끝날 때까지 기다려야 함 

### 4. Async-NonBlocking
![Image](https://github.com/user-attachments/assets/edc8039f-ba32-40b0-9a1f-27c730ee8bb7)
- Async: 제어권은 A한테 있고, B함수를 호출할 때 콜백함수 같이
- NonBlocking: 제어권은 계속 A한테