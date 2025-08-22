from setuptools import setup, find_packages

setup(
    name='md2ss14',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A command-line tool to convert Markdown files to SS14 formatted text.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add any dependencies here, for example:
        # 'markdown',
    ],
    entry_points={
        'console_scripts': [
            'md2ss14=__main__:main',
        ],
    },
)