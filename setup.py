from setuptools import setup

setup(name='pandata',
      version='0.1',
      description='Download CMU panoptic data.',
      author='Dave Greenwood',
      license='MIT',
      packages=['pandata'],
      zip_safe=False,
      entry_points={'console_scripts': ['panoptic=pandata.cli:main', ]}
      )
