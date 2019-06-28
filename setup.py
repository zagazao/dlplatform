from setuptools import setup

setup(name='DLplatform',
      version           = '0.0.5-exp',
      description       = 'A framework to perform large scale experiments with distributed learners',
      url               = '',
      author            = 'Adilova, Kamp, Sicking, Wirtz',
      author_email      = 'tim.wirtz@iais.fraunhofer.de',
      license           = 'tba',
      python_requires     ='>3.5',
      install_requires  = ["keras==2.1.4",
                           "pika==0.11.2",
                           "numpy"],
      packages          = ['DLplatform',
                           'DLplatform/aggregating',
                           'DLplatform/communicating',
                           'DLplatform/dataprovisioning',
                           'DLplatform/learning',
                           'DLplatform/parameters',
                           'DLplatform/synchronizing',
                           'DLplatform/resnet/',
                           'DLplatform/stopping'],
      zip_safe          = False)