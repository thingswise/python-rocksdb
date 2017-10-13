from setuptools import setup
from setuptools import find_packages
from distutils.extension import Extension
import os

try:
    from Cython.Build import cythonize
except ImportError:
    def cythonize(extensions): return extensions
    sources = ['rocksdb/_rocksdb.cpp']
else:
    sources = ['rocksdb/_rocksdb.pyx']

# Set LIBROCKSDB_A to specify the location of librocksdb.a to
# link statically. Librocksdb.a must be compiled with -fPIC

try:
    librocksdb_a = [ os.environ["LIBROCKSDB_A"] ]
    librocksdb_so = []
except KeyError:
    librocksdb_a = []
    librocksdb_so = [ "rocksdb" ]

mod1 = Extension(
    'rocksdb._rocksdb',
    sources,
    extra_compile_args=[
        '-std=c++11',
        '-O3',
        '-Wall',
        '-Wextra',
        '-Wconversion',
        '-fno-strict-aliasing'
    ],
    extra_link_args=[] + librocksdb_a,
    language='c++',
    libraries=[
        # 'rocksdb',
        # 'snappy',
        # 'bz2',
        'z'
    ] + librocksdb_so
)

setup(
    name="python-rocksdb",
    version='0.6.7+tw',
    description="Python bindings for RocksDB",
    keywords='rocksdb',
    author='Ming Hsuan Tu',
    author_email="Use the github issues",
    url="https://github.com/twmht/python-rocksdb",
    license='BSD License',
    install_requires=['setuptools'],
    package_dir={'rocksdb': 'rocksdb'},
    packages=find_packages('.'),
    ext_modules=cythonize([mod1]),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True
)
