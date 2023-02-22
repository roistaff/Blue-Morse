from setuptools import setup

setup(
    name='blue-morse',
    version='0.2',
    packages=['blue_morse'],
    description='Bluetooth button morse app',
    author='Roi Staff',
    author_email='roistaff1983@gmail.com',
    install_requires=[
        'evdev'
    ],
    entry_points={
        'console_scripts': [
            'blue-morse = blue_morse.blue_morse:autostart',
        ],
    },
)
