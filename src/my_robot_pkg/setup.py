from setuptools import find_packages, setup

package_name = 'my_robot_pkg'

setup(
    name=package_name,
    version='0.0.0',
    # packages=[package_name], # find_packages()를 사용하면 더 좋습니다.
    packages=find_packages(exclude=['test']), # 'test' 폴더는 패키지에 포함하지 않음
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # '실행파일_이름 = 패키지폴더.파이썬파일:main' 형식
            'talker = my_robot_pkg.talker_node:main',
            'listener = my_robot_pkg.listener_node:main',
        ],
    },
)
