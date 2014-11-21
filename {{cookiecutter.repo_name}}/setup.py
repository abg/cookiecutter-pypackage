#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

# http://pytest.org/latest/goodpractises.html#integrating-with-distutils-python-setup-py-test
class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


def find_packages(name):
    path = __import__(name).__path__
    prefix = name + '.'
    walk = __import__('pkgutil').walk_packages(path, name + '.')
    return [name] + [name for _, name, ispkg in walk if ispkg]


def load_requirements(path):
    result = []
    with codecs.open(path, 'r', encoding='utf-8') as fileobj:
        for line in fileobj:
            if line.startswith("#"):
                continue
            result.append(line.rstrip())
    return result


def load_readme():
    with open('README.rst') as fileobj:
        data = fileobj.read()
    with open('HISTORY.rst') as fileobj:
        data += "\n\n" + fileobj.read().replace('.. :changelog:', '')
    return data


requirements = load_requirements('requirements.txt')
test_requirements = load_requirements('test_requirements.txt')
readme = load_readme()


setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages('{{ cookiecutter.repo_name }}'),
    package_dir={'{{ cookiecutter.repo_name }}':
                 '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache License (2.0)",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    cmdclass={
        'test': PyTest,
    },
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        # 'console_scripts': [ 'cmd = mypackage.cli:main' ]
    },
)
