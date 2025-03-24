## 트랜잭션?

: DBMS 또는 유사한 시스템에서 상호작용의 단위 (하나의 논리적인 작업 단위)

특징

- Atomic
- Consistent
- Isolation
- Durability

연산

- 롤백
- 커밋

⇒ 그럼 Spring에서는 이 트랜잭션 처리를 어떻게 하는가?

## @Transactional

스프링에서는 트랜잭션 처리를 위해 선언적 트랜잭션을 사용한다.

@Transactional 과 같이 어노테이션 방식으로 이를 지원한다. 

Spring에서 데이터 작업의 실행단위를 명시하기 위해 사용한다고 볼 수 있다. 

클래스 / 메서드 위에 **@Transactional** 을 붙이면 AOP(관점지향프로그래밍)를 통해 타겟이 상속하고 있는 인터페이스 또는 타겟을 상속한 **프록시 객체**가 생성된다. 이때 프록시 객체의 메소드를 호출하면 타겟 메소드 전 후로 트랜잭션 처리를 수행한다.

### 필요한 이유

// 가독성 높고

유지보수 좋다

### 작동

트랜잭션의 경우, 트랜잭션의 시작과 연산 종료 시의 커밋 과정이 필요하므로, 프록시(트랜잭션 AOP)를 생성해 해당 메서드의 앞뒤에 트랜잭션의 시작과 끝을 추가하는 것이다.

또한, 스프링 컨테이너는 **트랜잭션 범위의 영속성 컨텍스트 전략**을 기본으로 사용한다.

서비스 클래스에서 @Transactional을 사용할 경우, 해당 코드 내의 메서드를 호출할 때 영속성 컨텍스트가 생긴다는 뜻이다. 영속성 컨텍스트는 트랜잭션 AOP가 트랜잭션을 시작할 때 생겨나고, 메서드가 종료되어 트랜잭션 AOP가 트랜잭션을 커밋할 경우 영속성 컨텍스트가 flush되면서 해당 내용이 반영된다. 

이후 영속성 컨텍스트 역시 종료되는 것이다. 

// 이 말이 1차 캐시가 사라진다는 거냐

![Image](https://github.com/user-attachments/assets/4c973292-5009-44c8-ad96-80cc137981df)

### 동작 원리

**AOP** (관점지향 프로그래밍)

spring은 @Transactional을 보고 AOP 기반 프록시 객체를 만든다. 

스프링 AOP는 프록시 패턴을 기반으로 동작. 클라이언트가 객체를 사용할 때, 스프링 컨테이너는 대상 객체 대신 프록시 객체를 제공.

⇒ 코드의 재사용성과 모듈성이 확장

- AOP 주요 개념
    - **Aspect**: Advice + PointCut로 AOP의 기본 모듈
    - **Advice**: Target에 제공할 부가 기능을 담고 있는 모듈
    - **Target**: Advice이 부가 기능을 제공할 대상 (Advice가 적용될 비즈니스 로직)
    - **JointPoint**: Advice가 적용될 위치
        - 메서드 진입 지점, 생성자 호출 시점, 필드에서 값을 꺼내올 때 등 다양한 시점에 적용 가능
    - **PointCut**: Target을 지정하는 정규 표현식
    
    ⇒ 역할과 책임을 명확하게 분리함
    
    advice: 부가기능 로직만 담당
    
    pointcut: 대상인지 확인하는 필터 역할만 담당
    

**Proxy**

AOP를 구현하는 기술 중 하나, 대상 객체에 대한 접근을 제어하고 추가 기능을 수행하기 위해 사용

프록시를 통해 실제 객체를 감싸고 클라이언트가 이게 진짜인지 가짜인지 모르게하면서 추가적인 기능을 제공할 수 있음

- [Proxy 객체가 만들어지는 방법]
    1. JDK Dynamic Proxy
        
        인터페이스를 상속받아 프록시 객체 생성
        
        ```java
        public interface MyService {
            void doSomething();
        }
        ```
        
        ```java
        @Service
        public class MyServiceImpl implements MyService {
        	@Transactional 
        	public void doSomething() {
        		System.out.println("실제 로직 실행");
        	}
        }
        ```
        
        ⇒ @Tranactional이 적용되면 spring은 MyServiceImpl으ㅢ 프록시 객체 생성. doSomething을 호출하면 프록시가 먼저 실행되면서 트랜잭션 관리를 함
        
    2. CGLIB 
        
        클래스 기반 프록시
        
        클래스 자체를 상속하여 프록시 생성
        
        : 자식 클래스를 만들어 원래 클래스의 메서드를 오버라이딩
        
![Image](https://github.com/user-attachments/assets/4c973292-5009-44c8-ad96-80cc137981df)

1. @Transactional 적용시점: Bean 후처리 과정
    
    Spring Application이 시작할 때, 컨테이너는 각 Bean을 생성하고 BeanPostProcessor 단계에서 @Transactional 등 AOP 관련 어노테이션이 붙은 Bean을 스캔함
    
    Spring 컨테이너는 `BeanFactoryPostProcessor`와 `AnnotationTransactionAttributeSource`를 이용해 `@Transactional`을 감지하고, **프록시 객체를 생성하여 스프링 컨테이너에 등록**한다.
    
2. Caller에서 AOP 프록시를 탄다. 이때 타겟을 호출하지는 않고, 프록시를 호출한다.
    - Caller: 앱 내부/외부에서 메서드를 호출하는 주체 (@Autowired로 주입받은 객체의 메소드를 호출할 때, 실제로는 그 객체의 “프록시”가 호출된다. )
    
3. 그 AOP 프록시는 Advisor를 호출한다. 
    
    @Transactional이 있으므로 이 메서드는 트랜잭션이 필요하다. 시작해달라고 한다.
    
    DB연결잡고, Auto-commit 조정하는 방식으로 실제 트랜잭션이 시작된다.
    
    → 이때 @Transactional의 세부 설정이 반영됨 (propagation, isolation 등)
    
    - Transaction Advisor: @Transactional을 해석하고 시작/커밋/롤백을 관리하는 관리자.
    
    Custom Advisor가 있다면, 트랜잭션 Advisor 실행 전후로 동작한다. 
    
    - CustomAdvisor: 별도로 만든 AOP설정이 있다면, TransactionAdvisor 앞뒤로 끼어들어 동작하는 추가적인 어드바이저

1. 실제 메서드 실행 (Targer Method)
    
    모든 Advisor들이 실행 전에 해야할 일을 마치면 실제 Target 객체의 메서드가 실행됨
    
    이때 비즈니스 로직이 수행되고, DB접근 (쿼리)도 @Transactional 경계 안에서 진행됨
    
    - 예외 발생 → 롤백 발생 가능
    - 오류 없음 → 커밋 단계로 넘어갈 수 있음

1. 메서드 실행 결과 반환
    
    메서드 실행이 완료되면, 다시 CustomAdvisor→TransactionAdvisor 순으로 돌아옴 
    
    - 각 advisor의 after 파트 실행 가능
    
    TransactionalAdvisor는 롤백 / 커밋할지 최종판단하여 진행
    
    - JPA 사용 시 flush() 실행 후 실제 커밋 수행
    - 커밋 완료되면 트랜잭션 종료 후 Connection 반환
    - 롤백 시에는 영속성 컨텍스트 초기화
    
    모든 처리가 끝나면 결과값을 AOP Proxy가 caller에게 반환함
    

### 주의점

- **내부 호출**을 하면 트랜잭션이 걸리지 않음
    
    반드시 **프록시 객체**를 거쳐야 트랜잭션 AOP 적용
    
    ```java
    @Service
    public class dkdkdkdService {
    @Transactional
    public void methodA{
    methodB;
    }
    
    @Transactional
    public void methodB{
     methodB
    }
    ```