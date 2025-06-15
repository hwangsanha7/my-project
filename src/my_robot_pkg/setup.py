# src/my_robot_pkg/setup.py

import os
from glob import glob
from setuptools import setup

package_name = 'my_robot_pkg'

setup(
    name=package_name,
    version='0.0.1',
    # ★★★★★ 이 부분이 핵심입니다 ★★★★★
    # 'my_robot_pkg' 패키지 안에 있는 모든 파이썬 패키지를 찾으라고 명시합니다.
    # find_packages()를 사용하지 않고, 실제 Python 모듈이 있는 폴더 이름을 직접 지정합니다.
    # 만약 talker.py, listener.py가 my_robot_pkg 폴더 바로 아래 있다면,
    # 이 설정은 colcon에게 "my_robot_pkg 라는 이름의 파이썬 패키지를 찾아라" 라고 알려줍니다.
    packages=[package_name],
    
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@email.com',
    description='My custom robot package for autonomous driving project.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_robot_pkg.talker:main',
            'listener = my_robot_pkg.listener:main',
        ],
    },
)
