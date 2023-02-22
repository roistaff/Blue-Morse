from setuptools import setup

setup(
    name='blue-morse',
    version='0.1',
    packages=['blue_morse'],
    entry_points={
        'console_scripts': [
            'blue-morse = blue_morse.blue_morse:autostart'
        ]
    }
)
