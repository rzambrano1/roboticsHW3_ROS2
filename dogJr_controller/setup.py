from setuptools import find_packages, setup

package_name = 'dogJr_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ric_ml',
    maintainer_email='rzambrano@gmail.com',
    description='Homework 3 - MSML642 Fall 2023 - Ricardo Zambrano',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "draw_circle = dogJr_controller.draw_circle:main",
            "scan_subscriber = dogJr_controller.scan_subscriber:main",
            "car_controller = dogJr_controller.car_controller:main"
        ],
    },
)
