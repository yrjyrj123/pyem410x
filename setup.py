from setuptools import setup, find_packages

setup(
    name='pyem410x',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',

    description='A python module for encode & decode Em410x.',
    long_description="A python module for encode & decode Em410x.",

    # The project's main homepage.
    url='https://github.com/yrjyrj123/pyem410x',

    # Author details
    author='yrjyrj123',
    author_email='yrjyrjwp7@hotmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],

    # What does your project relate to?
    keywords='em410x t5577 t55xx rfid id card',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['pyem410x'],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['bitstring'],
)