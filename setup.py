from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req.req_file import parse_requirements
    try: # for pip >= 20.0.2
        from pip._internal.network.session import PipSession
    except:
        from pip._internal.download import PipSession
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession

import locking

from os import path


# Lists of requirements and dependency links which are needed during runtime, testing and setup
install_requires = []
tests_require = []
dependency_links = []

# Inject requirements from requirements.txt into setup.py
requirements_file = parse_requirements(path.join('requirements', 'requirements.txt'), session=PipSession())
for req in requirements_file:
    install_requires.append(str(getattr(req, 'req', getattr(req, 'requirement', None))))
    if hasattr(req, 'link') and req.link:
        dependency_links.append(str(req.link))

# Inject test requirements from requirements_test.txt into setup.py
requirements_test_file = parse_requirements(path.join('requirements', 'requirements_test.txt'), session=PipSession())
for req in requirements_test_file:
    tests_require.append(str(getattr(req, 'req', getattr(req, 'requirement', None))))
    if hasattr(req, 'link') and req.link:
        dependency_links.append(str(req.link))


setup(
    name="django-db-locking",
    version=locking.__version__,
    url='https://github.com/vikingco/django-db-locking/',
    license='BSD',
    description='Database locking',
    long_description=open('README.rst', 'r').read(),
    author='VikingCo',
    author_email='operations@unleashed.be',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={'celery':  ["celery"] },
    tests_require=tests_require,
    dependency_links=dependency_links,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
