from setuptools import setup, find_packages

setup(
    name='pymirror',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyqt5'
    ],
    entry_points={
        'console_scripts': [
            'pymirror = pymirror.pymirror:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11.3'
    ],
)
