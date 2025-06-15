# src/my_robot_pkg/setup.py

import os
from glob import glob
from setuptools import setup, find_packages

# ----------------------------------------------------------------
# ★★★ 1. 패키지 이름 변수를 새로운 이름으로 수정합니다. ★★★
# ----------------------------------------------------------------
package_name = 'my_robot_pkg'

# ----------------------------------------------------------------
# setup() 함수: 패키지에 대한 모든 정보를 colcon에 제공
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
    # 'test' 폴더를 제외한 모든 파이썬 패키지를 자동으로 찾습니다.
    packages=find_packages(exclude=['test']),
    
    # --- 데이터 파일 설정 ---
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        
        # package.xml 파일 포함
        ('share/' + package_name, ['package.xml']),
        
        # launch 폴더 안의 모든 .launch.py 파일을 자동으로 포함
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],

    # --- 의존성 및 테스트 설정 ---
    install_requires=['setuptools'],
    zip_safe=True,
    tests_require=['pytest'],

    # --- 실행 파일(노드) 등록 ---
    #
    # ★★★ 2. 실행 명령어의 경로도 새로운 패키지 이름으로 수정합니다. ★★★
    # 형식: '실행명령어 = 패키지이름.파이썬파일:main함수'
    #
    entry_points={
        'console_scripts': [
            'talker = my_robot_pkg.talker:main',
            'listener = my_robot_pkg.listener:main',
        ],
    },
)
