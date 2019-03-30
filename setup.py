from distutils.core import setup

setup(
    name='ApplePy',
    version='0.1',
    description='Apple ][ emulator in Python',
    long_description=open('README.md').read(),
    url='https://github.com/BubaVV/applepy',
    author='James Tauber',
    packages=['applepy', ],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Emulators'
    ]
)
