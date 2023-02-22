from setuptools import setup

setup(
    name='blue-morse',
    version='0.1',
    packages=['blue_morse'],
    description='Bluetooth button morse app',
    author='Roi Staff',
    author_email='roistaff1983@gmail.com'
    entry_points={
        'console_scripts': [
            'blue-morse = blue_morse.blue_morse:autostart'
        ]
    }
)
