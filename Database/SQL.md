# SQL
Structured Query Language (구조화된 질의 언어)  
: 데이터베이스 시스템에서 자료를 처리하는 용도로 사용되는 구조적 데이터 질의 언어
- DDL (Data Definition Language)
- DML (Data Manipulation Language)
- DCL (Data Control Language)

> 데이터베이스의 데이터를 조회, 추가, 수정, 삭제하기 위해 사용

## 데이터 정의어 (DDL)
: 데이터베이스의 구조를 만들거나 변경하는데 사용되는 언어 (데이터베이스, 테이블 생성 가능)
```sql
# 데이터베이스 추가
CREATE DATABASE 프로젝트명;
```

```sql
# 테이블 추가
CREATE TABLE 테이블명 (
    열이름 데이터_유형 제약조건,
    열이름 데이터_유형 제약조건,
    열이름 데이터_유형 제약조건,
    ...
);
```
- UNSIGNED: 음수가 아닌 양수만 저장 가능
- AUTO_INCREMENT: ID와 같이 유일한 값을 자동 생성할 때 (고유 번호)
- PRIMARY KEY: 테이블의 각 레코드를 유일하게 식별할 수 있는 열 (NULL 허용 X)
- CHECK: 열에 저장될 값을 제한하는 조건
- CURRENT_TIMESTAMP: 현제의 날짜와 시간을 자동으로 입력
  - created_at 열에 많이 사용
  
```sql
# 테이블의 구조 변경
ALTER TABLE 테이블명;

# 새로운 열을 테이블에 추가할 때 (AFTER은 옵션)
ADD 열_이름 데이터_유형 AFTER 기존열_이름

# 데이터 유형을 수정할 때
MODIFY 기존열_이름 새로운_데이터_유형

# 열 삭제
DROP 기존열_이름
```

```sql
# 테이블 삭제
DROP TABLE 테이블명;
```

```sql
# 데이터베이스 확인 (모든 디비)
SHOW DATABASES;

# 데이터베이스 접근
use database_name;

# 테이블 구조 확인 (db_name의 users테이블)
desc database_name.users;
```

## DML
:데이터베이스에 저장된 데이터를 조회, 추가, 수정, 삭제하는데 사용되는 언어

### 데이터 삽입
```sql
# 데이터 삽입
INSERT INTO users (name ,age ,email) VALUES
('John Doe',25,'johndoe@example.com'),
('Jane Smith',30,'janesmith@example.com');
```

### 데이터 조회
```sql
# 데이터 조회
SELECT * FROM users;
```

### 데이터 수정
```sql
# 데이터 수정
UPDATE users SET email = 'newemail@example.com";
```

### 데이터 삭제
```sql
DELETE FROM users WHERE id = 2;
```

## 데이터 제어어 (DCL)
; 사용자에게 권한 부여
### GRANT
```sql
# GRANT : 사용자에게 권한 부여

# @'%' 부분은 이 사용자가 어느 호스트에서든 접속할 수 있음을 의미함.
# %는 모든 호스트를 의미하는 와일드카드임
create user '계정ID'@'%' identified by '계정비밀번호' ;
grant all privileges on DB이름.테이블이름 to '계정ID'@'hostname' with grant option;
flush privileges; # 변경사항을 저장하는 명령어
```
- privileges: 데이터베이스에서 사용자나 사용자 그룹에게 부여된 권한
- option: with grant option은 부여된 권한을 다른 사용자에게 다시 부여할 수 있는 권한을 해당 사용자에게 줌
- flush: flush privileges는 데이터베이스 시스템에 권한 변경사항을 적용하라는 명령

### 권한 취소
```sql
revoke all privileges on shop.* form 'yeon1'@'%';
flush privileges;
```