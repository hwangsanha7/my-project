# src/my_robot_pkg/setup.py

import os
from glob import glob
from setuptools import setup

package_name = 'my_robot_pkg'

setup(
    name=package_name,
    version='0.0.1',
    # ★★★★★ packages 항목을 다시 명시적으로 지정합니다. ★★★★★
    # find_packages() 대신, 우리 패키지의 이름(폴더명)을 직접 리스트에 넣어줍니다.
    # 이렇게 하면 colcon이 패키지의 위치를 절대 헷갈리지 않습니다.
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
            # ★★★ entry_points의 형식도 패키지 이름으로 시작해야 합니다. ★★★
            'talker = my_robot_pkg.talker:main',
            'listener = my_robot_pkg.listener:main',
        ],
    },
)
