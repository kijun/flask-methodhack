"""
Flask-MethodHack
----------------

Description goes here...

Links
`````

* `documentation <http://packages.python.org/Flask-MethodHack>`_
* `development version
  <http://github.com/USERNAME/REPOSITORY/zipball/master#egg=Flask-MethodHack-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-MethodHack',
    version='0.1',
    url='<enter URL here>',
    license='BSD',
    author='kijun',
    author_email='your-email-here@example.com',
    description='<enter short description here>',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
