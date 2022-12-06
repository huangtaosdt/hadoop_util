from distutils.core import setup
setup(
  name = 'hadoop_util',         # How you named your package folder (MyLib)
  packages = ['hadoop_util'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'hadoop命令行工具python版',   # Give a short description about your library
  author = 'TaoHuang',                   # Type in your name
  author_email = '294319556@qq.com',      # Type in your E-Mail
  url = 'https://github.com/huangtaosdt/hadoop_util',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['HADOOP', 'HDFS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: HDFS Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 2.7',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)