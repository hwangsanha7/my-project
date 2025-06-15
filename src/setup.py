# setup.py (수정 후)
from setuptools import setup
import os
from glob import glob

package_name = 'picar_pkg'

setup(
    name=package_name,
    version='0.0.0',
    # ★★★★★ 이 부분이 핵심입니다 ★★★★★
    # 'packages' 대신 'py_modules'를 사용합니다.
    # 이것은 'picar_pkg' 폴더에서 .py로 끝나는 모든 파일을 모듈로 취급하라는 의미입니다.
    py_modules=[
        'talker',
        'listener'
    ],
    # ... (다른 설정들)
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (고급) launch 파일을 포함시키려면 이 부분을 추가합니다.
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@email.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # '실행명령어 = 파이썬파일:main함수' 형식으로 등록합니다.
            'talker = talker:main',
            'listener = listener:main',
        ],
    },
)
