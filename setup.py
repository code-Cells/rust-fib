#!/usr/bin/env python

from importlib.metadata import entry_points
from setuptools import dist
dist.Distribution().fetch_build_eggs(['setuptools_rust'])
from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
  name="fib-rs",
  version="0.2",
  rust_extensions=[RustExtension(
    ".fib_rs.fib_rs",
    path="Cargo.toml", binding=Binding.PyO3)
  ],
  packages=["fib_rs"],
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Rust",entry_points={
    'console_scripts': [
      'fib-number = flitton_fib_rs.',
      'fib_number_command',
    ],
  },
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
  ],
  zip_safe=False,
  entry_points={
    'console_scripts': [
        'fib-number = flitton_fib_rs.fib_number_command:fib_number_command',
    ],
  },
)
