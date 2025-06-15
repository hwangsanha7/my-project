# ROS2 Python Project Framework

이 저장소는 **ROS2 Humble과 Python을 사용하는 모든 프로젝트**를 위한 고성능 개발 프레임워크 템플릿입니다.
전문적인 개발 환경을 위해, 코드 품질 검사와 빌드/테스트를 자동화하는 CI/CD 파이프라인이 기본적으로 설정되어 있습니다. 이 템플릿을 사용하면, 어떤 ROS2 프로젝트든 초기 설정의 고통 없이 즉시 핵심 로직 개발에 집중할 수 있습니다.

---

## ✨ 주요 특징

*   **자동화된 코드 검증 (CI):** Pull Request를 생성할 때마다 GitHub Actions가 자동으로 코드 스타일(Pylint)을 검사하고, `colcon`을 이용해 빌드 및 단위 테스트를 실행합니다.
*   **표준화된 개발 환경:** 모든 팀원이 동일한 규칙과 환경에서 개발하여 "제 컴퓨터에서는 잘 됐는데요?"와 같은 문제를 원천적으로 방지합니다.
*   **개발 효율성 극대화:** 개발자는 기계가 할 수 있는 반복적인 검증 작업에서 해방되어, 오직 창의적인 로직 개발에만 집중할 수 있습니다.
      
# ROS2 Python Project Framework

이 저장소는 **ROS2 Humble과 Python을 사용하는 모든 프로젝트**를 위한 고성능 개발 프레임워크 템플릿입니다.
전문적인 개발 환경을 위해, 코드 품질 검사와 빌드/테스트를 자동화하는 CI/CD 파이프라인이 기본적으로 설정되어 있습니다. 이 템플릿을 사용하면, 어떤 ROS2 프로젝트든 초기 설정의 고통 없이 즉시 핵심 로직 개발에 집중할 수 있습니다.

---

## ✨ 주요 특징

*   **자동화된 코드 검증 (CI):** Pull Request를 생성할 때마다 GitHub Actions가 자동으로 코드 스타일(Pylint)을 검사하고, `colcon`을 이용해 빌드 및 단위 테스트를 실행합니다.
*   **표준화된 개발 환경:** 모든 팀원이 동일한 규칙과 환경에서 개발하여 "제 컴퓨터에서는 잘 됐는데요?"와 같은 문제를 원천적으로 방지합니다.
*   **개발 효율성 극대화:** 개발자는 기계가 할 수 있는 반복적인 검증 작업에서 해방되어, 오직 창의적인 로직 개발에만 집중할 수 있습니다.
*   **고속 CI 파이프라인:** ROS 의존성 캐싱을 적용하여, 두 번째 실행부터는 CI/CD 실행 시간을 1~2분 내외로 단축했습니다.

---

## 🚀 시작하기 (Getting Started)

이 프레임워크를 사용하여 당신의 ROS2 프로젝트 개발을 시작하는 방법은 매우 간단합니다.

### 1. 저장소 포크 (Fork) 또는 템플릿으로 사용

*   **Fork:** 이 저장소의 오른쪽 위에 있는 **[Fork]** 버튼을 눌러 당신의 개인 GitHub 계정으로 그대로 복사해 가세요.
*   **Use this template:** (저장소 설정에서 템플릿으로 지정했다면) **[Use this template]** 버튼을 눌러 이 구조를 기반으로 새로운 저장소를 생성하세요.

### 2. 로컬 컴퓨터에 복제 (Clone)

당신이 생성한 저장소를 로컬 컴퓨터로 다운로드합니다.

# 'your-github-id'와 'your-repo-name'을 당신의 정보로 바꿔주세요.
git clone https://github.com/your-github-id/your-repo-name.git
cd your-repo-name

    

IGNORE_WHEN_COPYING_START
Use code with caution. Markdown
IGNORE_WHEN_COPYING_END
3. 핵심 폴더에서 개발 시작

이제 여러분이 신경 쓸 폴더는 딱 두 곳뿐입니다.

    핵심 로직 코드 작성:

        위치: src/my_robot_pkg/my_robot_pkg/

        설명: 여러분의 모든 Python 노드 파일(talker.py, motor_controller.py 등)을 이곳에 작성하고 저장하세요.

    단위 테스트 코드 작성:

        위치: src/my_robot_pkg/test/

        설명: 여러분이 만든 기능이 약속대로 작동하는지 검증하기 위한 테스트 코드를 이곳에 test_로 시작하는 파일명으로 작성하세요.

 Use code with caution. Markdown
IGNORE_WHEN_COPYING_END
3. 핵심 폴더에서 개발 시작

이제 여러분이 신경 쓸 폴더는 딱 두 곳뿐입니다.

    핵심 로직 코드 작성:

        위치: src/my_robot_pkg/my_robot_pkg/

        설명: 여러분의 모든 Python 노드 파일(talker.py, motor_controller.py 등)을 이곳에 작성하고 저장하세요.

    단위 테스트 코드 작성:

        위치: src/my_robot_pkg/test/

        설명: 여러분이 만든 기능이 약속대로 작동하는지 검증하기 위한 테스트 코드를 이곳에 test_로 시작하는 파일명으로 작성하세요.

🛠️ 프로젝트 맞춤 설정 (Customization)

이 프레임워크를 당신의 프로젝트에 맞게 수정하는 방법입니다.
1. 패키지 이름 변경하기

현재 기본 패키지 이름은 my_robot_pkg입니다. 만약 drone_control 같은 다른 이름으로 바꾸고 싶다면, 아래 파일들에서 my_robot_pkg를 당신의 새 패키지 이름으로 모두 변경해주세요.

    src/ 폴더 안의 폴더 이름 (my_robot_pkg)

    package.xml

    setup.py

    .github/workflows/ci.yml

2. 새로운 Python 라이브러리 추가하기

    requirements.txt 파일을 열고, 필요한 라이브러리 이름(예: pandas)을 새로운 줄에 추가하고 저장합니다.

3. 새로운 실행 노드(Node) 추가하기

    src/my_robot_pkg/setup.py 파일을 열고, entry_points 섹션의 console_scripts 리스트에 당신의 노드를 추가합니다.

이 프레임워크가 여러분의 개발 과정을 더 즐겁고 효율적으로 만들어 주기를 바랍니다.
궁금한 점이 있다면 언제든지 저에게 물어보세요!
