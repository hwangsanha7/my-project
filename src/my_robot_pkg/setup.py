# src/my_robot_pkg/setup.py

import os
from glob import glob
from setuptools import setup, find_packages

# ----------------------------------------------------------------
# 1. 패키지 이름 정의
# ----------------------------------------------------------------
# 이 변수 하나만 바꾸면, 아래의 모든 경로와 이름이 자동으로 변경됩니다.
package_name = 'my_robot_pkg'

# ----------------------------------------------------------------
# 2. setup() 함수: 패키지에 대한 모든 정보를 colcon에 제공
# ----------------------------------------------------------------
setup(
    # --- 기본 정보 ---
    name=package_name,
    version='0.0.1',
    description='My custom robot package for autonomous driving project.',
    license='Apache License 2.0',
    
    # --- 작성자 정보 ---
    maintainer='Your Name',
    maintainer_email='your_email@email.com',

    # --- 패키지 및 모듈 설정 ---
    #
    # find_packages() 함수는 이 폴더(my_robot_pkg)를 패키지로 인식하고,
    # 그 안의 모든 파이썬 모듈(.py 파일)을 자동으로 찾아줍니다.
    # 'test' 폴더는 테스트 전용이므로 패키지에서 제외합니다.
    packages=find_packages(exclude=['test']),
    
    # --- 데이터 파일 설정 ---
    #
    # 소스 코드가 아닌 다른 파일들(설정, 런치 파일 등)을
    # 설치 폴더에 함께 복사하도록 지시합니다.
    data_files=[
        # ament_index: colcon이 이 패키지를 찾을 수 있도록 등록
        # ★★★ 이전 실패 원인이었던 부분을 package_name 변수를 사용하도록 수정했습니다. ★★★
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        
        # package.xml: 패키지의 메타 정보를 포함
        ('share/' + package_name, ['package.xml']),
        
        # launch 폴더 자동화: 'launch' 폴더 안의 모든 '.launch.py' 파일을 자동으로 포함
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],

    # --- 의존성 및 테스트 설정 ---
    install_requires=['setuptools'],
    zip_safe=True,
    tests_require=['pytest'],

    # --- 실행 파일(노드) 등록 ---
    #
    # 'console_scripts'는 'ros2 run <패키지명> <실행명령어>'를 가능하게 합니다.
    # 형식: '실행명령어 = 패키지이름.파이썬파일:main함수'
    #
    # ★★★ 새로운 실행 노드를 추가할 때마다 이 리스트에 한 줄을 추가해야 합니다. ★★★
    entry_points={
        'console_scripts': [
            'talker = my_robot_pkg.talker:main',
            'listener = my_robot_pkg.listener:main',
        ],
    },
)
