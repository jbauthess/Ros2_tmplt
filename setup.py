from setuptools import find_packages, setup

package_name = 'tmplt_py'

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
    maintainer='timdev',
    maintainer_email='jean-baptiste.authesserre.ext@safrangroup.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "basic = tmplt_py.basic_node:main",
            "publisher = tmplt_py.publisher_node:main",
            "subscriber = tmplt_py.subscriber_node:main",
            "server = tmplt_py.server_node:main",
            "client = tmplt_py.client_node:main"
        ],
    },
)
