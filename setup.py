import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='PyppeSnap',
    author='Nat Lee',
    author_email='natlee.work@gmail.com',
    description='Get a snapshot from a website by using Pyppeteer.',
    keywords='pyppeteer, snapshot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/natlee/PyppeSnap',
    project_urls={
        'Documentation': 'https://github.com/natlee/PyppeSnap',
        'Bug Reports': 'https://github.com/natlee/PyppeSnap/issues',
        'Source Code': 'https://github.com/natlee/PyppeSnap',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=['websockets==8.1', 'pyee==6.0.0', 'pyppeteer>=0.0.25'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'pyppesnap=pyppesnap.cli:main'
        ]
    }
)
