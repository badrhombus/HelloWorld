from setuptools import setup, find_packages

setup(
    name='everyone',
    version='0.1.0',
    author='badrhombus',
    author_email='bhall@msn.com',
    description='universal hello world',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my-python-project',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests>=2.25.1',
        'numpy>=1.19.5',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)