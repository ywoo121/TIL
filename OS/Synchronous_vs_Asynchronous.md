## 1. 정의
<img width="1040" alt="Image" src="https://github.com/user-attachments/assets/9e1c8098-6795-4334-9daf-98514524cb4d" />  

### **동기(Synchronous)**
: 함수 호출 시 결과가 반환될 때까지 기다리는 처리 방식  
![Image](https://github.com/user-attachments/assets/572bbe3e-423d-49e4-ac7c-8c40f9483700)
- 직렬적으로 태스크 수행
- 태스크는 순차적으로 실행되며, 어떤 작업이 수행 중이면 다음 태스크는 대기


### **비동기(Asynchronous)**
: 함수 호출과 결과 반환 사이에 다른 작업을 수행할 수 있는 처리 방식  
![Image](https://github.com/user-attachments/assets/6ab8c974-851d-42fb-8465-4414137591b3)
- 병렬적으로 태스크 수행
- 즉, 태스크가 종료되지 않은 상태라 하더라도 대기하지 않고 즉시 다음 태스크 실행
- Task1이 실행되는 시간 동안 Task2를 할 수 있으므로 자원을 효율적으로 사용 가능
- 이때, 비동기 요청시 응답 후 처리할 '콜백 함수'를 함께 알려준다. 따라서 해당 태스크가 완료되었을 때, '콜백 함수'가 호출됨
> 현재 작업과 다음 작업이 `순서`대로 진행되는가의 차이


### 비동기의 성능 이점
![Image](https://github.com/user-attachments/assets/470e9519-7ebf-4c27-8c35-5e3aa0a5025f)
비동기 방식: I/O 작업과 같은 느린 작업이 발생할 때, 기다리지 않고 다른 작업을 처리하면서 동시에 처리하여 멀티 작업을 진행할 수 있음

➡️ 전반적인 시스템 성능 향상에 도움을 줌

## 2. 사용 이유
**동기**  
: 실행 순서 보장, 프로그램의 흐름을 이해하고 디버깅하기 쉬움

**비동기**  
: 시스템 자원의 비효율적 사용을 줄이고, 대기 시간 없이 여러 작업을 병렬으로 처리할 수 있음


## 3. 사용 방법
### 동기
: API 호출이나 함수 실행 시 결과를 바로 반환받음
```js
function doWorkSync() {
    const start = Date.now();
    while (Date.now() < start + 1000);
    console.log('동기 작업 완료');
}

console.log('작업 시작');
doWorkSync();
console.log('다음 작업');
```
```bash
작업 완료
동기 작업 완료
다음 작업
```
`doWorkSync()` 가 호출되면 `doWorkSync()`에게 제어권이 넘겨짐  
`doWorkSync()` 종료될 때까지 대기  
종류 이후 다음 작업 실행

### 비동기
: 콜백함수, Promise, async/await 등을 활용하여 결과를 나중에 받음, 동시에 여러 작업 가능
```js
function doWorkAsync() {
    setTimeout(() => {
        console.log('비동기 작업 완료');
    }, 1000); 
}

console.log('작업 시작');
doWorkAsync(); 
console.log('다음 작업');
```
```bash
작업 시작
다음 작업
비동기 작업 완료
```
`doWorkAsync` 에게 제어권을 넘겨 실행 후 즉시 제어권 반환  
`doWorkAsync` 가 작업이 끝났다고 통보  
제어권은 현재 진행중인 작업이 있을 경우 해당 작업을 끝내고 `doWorkAsync` 결과에 대한 작업을 진행  