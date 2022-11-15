from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()





setup(
    name = 'GToolGenerator',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['GTool'],
    version = '1.6',
    license = 'MIT',
    description = 'Generate cards with useful data from different applications (for now only GitHub) and insert them in your web/app or wherever you want c: (API APP) 🎯',
    author = 'ElHaban3ro',
    author_email = 'habanferd@gmail.com',
    url = 'https://github.com/ElHaban3ro/ConvTool',
    keywords = 'GitHub, Generator, Target, Pillow',
    classifiers = [
        'Programming Language :: Python :: 3.10'
    ],
    install_requires=['requests', 'Pillow', 'beatifulsoup4', 'lxml', 'Flask']
)