# 파이프라인
소프트웨어 개발의 전 과정을 **자동화**하여 코드 변경 사항이 개발 환경에서 프로덕션 환경까지 빠르고 안전하게 이동할 수 있도록 하는 일련의 프로세스

## 파이프라인의 개념
1. 코드 커밋
2. 빌드
3. 테스트: 유닛, 통합, 기능, 정적 코드 분석 등 다양한 테스트 포람
4. 배포: 스테이징 / 프로덕션 환경에 제공
5. 모니터링 및 피드백: 배포된 어플리케이션의 상태 모니터링, 문제가 발생하면 즉시 알림을 통해 개발자에게 피드백을 제공함

## 단계적 파이프라인 구성 예제
ex. Jenkins
```Groovy

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // GitHub에서 코드 가져오기
                git 'https://github.com/user/repo.git'
            }
        }

        stage('Build') {
            steps {
                // 빌드 명령 실행 (예: Maven, Gradle, npm)
                sh 'npm install'
                sh 'npm run build'
            }
        }

        stage('Test') {
            steps {
                // 테스트 명령 실행
                sh 'npm test'
            }
        }

        stage('Staging Deployment') {
            when {
                branch 'main'
            }
            steps {
                // 스테이징 환경에 배포
                sh 'scp -r ./build user@staging-server:/path/to/deploy'
            }
        }

        stage('Production Deployment') {
            when {
                branch 'main'
                beforeAgent true
                environment name: 'DEPLOY_PRODUCTION', value: 'true'
            }
            steps {
                // 프로덕션 환경에 배포 (수동 승인 필요)
                input message: '프로덕션 배포를 승인하시겠습니까?', ok: '승인'
                sh 'scp -r ./build user@production-server:/path/to/deploy'
            }
        }
    }

    post {
        always {
            // 성공이든 실패든 로그 남기기
            archiveArtifacts artifacts: '**/build.log', allowEmptyArchive: true
        }
        success {
            // 성공 시 알림
            mail to: 'team@example.com',
                 subject: "성공: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                 body: "배포가 성공적으로 완료되었습니다. 링크: ${env.BUILD_URL}"
        }
        failure {
            // 실패 시 알림
            mail to: 'team@example.com',
                 subject: "실패: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                 body: "배포가 실패했습니다. 링크: ${env.BUILD_URL}"
        }
    }
}


```

### 2. **파이프라인 단계 설명**

1. **Checkout**:
    - **설명**: 버전 관리 시스템(GitHub)에서 최신 코드를 가져옵니다.
    - **목적**: 최신 코드를 파이프라인에서 사용할 수 있도록 준비합니다.
2. **Build**:
    - **설명**: 가져온 코드를 빌드합니다. 이 단계에서는 애플리케이션을 컴파일하고, 필요한 라이브러리나 종속성을 설치합니다.
    - **목적**: 실행 가능한 애플리케이션 아티팩트를 생성합니다.
3. **Test**:
    - **설명**: 빌드된 코드에 대해 자동화된 테스트를 실행합니다. 여기서는 `npm test` 명령어를 통해 유닛 테스트가 실행됩니다.
    - **목적**: 코드의 품질과 기능이 예상대로 동작하는지 확인합니다.
    - 필요에 따라 **보안 스캔(SAST, DAST)**, **정적 분석**, **코드 린팅** 등을 함께 실행하여 품질과 보안을 강화할 수 있습니다.
4. **Staging Deployment**:
    - **설명**: 테스트가 통과된 코드를 스테이징 서버에 배포합니다. 이 단계는 `main` 브랜치에 커밋된 코드에 대해서만 실행됩니다.
    - **목적**: 프로덕션 환경에 배포하기 전에, 실제 환경과 유사한 스테이징 환경에서 코드를 검증합니다.
5. **Production Deployment**:
    - **설명**: 스테이징 환경에서 검증된 코드를 프로덕션 서버에 배포합니다. 이 단계는 수동 승인이 필요합니다.
    - **목적**: 최종적으로 사용자에게 제공될 애플리케이션을 배포합니다.
6. **Post Actions**:
    - **설명**: 배포가 완료된 후, 결과를 저장하고 팀에 알림을 보냅니다. 성공 여부에 따라 알림 내용이 다릅니다.
    - **목적**: 배포 기록을 남기고, 팀에 현재 상태를 공유합니다.

### 3. **수동 승인 단계**

- **Production Deployment** 단계에서 `input` 단계가 사용되어, Jenkins 파이프라인이 이 시점에서 일시 정지하고, 사용자의 수동 승인을 기다립니다.
- 승인된 후에야 프로덕션 배포가 진행되며, 이를 통해 실수나 버그로 인한 문제를 최소화할 수 있습니다.

## 결론
소프트웨어 개발과 배포 과정에


## 파이프라인 관리
1. 다양한 환경 분리
   : 개발, 스테이징, QA, 프로덕션 등 여러 환경을 동시에 운영하는 경운는 많지 않음

2. 컨테이너
항상 동일한 환경에서 어플리케이션 실행 가능 (격리)

3. 멀티 브랜치 파이프라인
4. Secrets 및 민감 정보 관리
5. 자동화된 롤백