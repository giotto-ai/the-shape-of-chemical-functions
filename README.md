Shape of Molecules
============
The application of Machine Learning for biological data is one of the 
most promising and fascinating research direction of AI. In this notebook
we want to give a baseline indication to show how topological data analysis 
tools can be exploited to analyze molecules. More importantly, we show empirically
that shapes matter, in the sense that it is possible to match properties objects with
their shapes. 

The HIV dataset was introduced by the Drug
Therapeutics Program (DTP) AIDS Antiviral Screen, which
tested the ability to inhibit HIV replication for over 40 000
compounds. In the original dataset the chemical compounds were classified
into 3 different classes: confirmed inactive (CI), confirmed active (CA)
and confirmed moderately active (CM). As done in this [paper](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc02664a), 
the two classes CA and CM were grouped into one single class "Active".

Installation
------------

Dependencies
~~~~~~~~~~~~

shape-of-molecules requires:

- Python (>= 3.5)
- scikit-learn (>= 0.21.3)
- NumPy (>= 1.14.0)
- joblib (>= 0.11)

For running the examples jupyter, matplotlib and plotly are required.

User installation
~~~~~~~~~~~~~~~~~

If you already have a working installation of numpy and scipy,
the easiest way to install giotto-learn is using ``pip``   ::

    pip install -U giotto-learn

Documentation
-------------

- HTML documentation (stable release): https://docs.giotto.ai

Contributing
------------

We welcome new contributors of all experience levels. The Giotto
community goals are to be helpful, welcoming, and effective. To learn more about
making a contribution to giotto-learn, please see the `CONTRIBUTING.rst
<https://github.com/giotto-ai/giotto-learn/blob/master/CONTRIBUTING.rst>`_ file.

Developer installation
~~~~~~~~~~~~~~~~~~~~~~~

C++ dependencies:
'''''''''''''''''

-  C++14 compatible compiler
-  CMake >= 3.9
-  Boost >= 1.56

Source code
'''''''''''

You can check the latest sources with the command::

    git clone https://github.com/giotto-ai/giotto-learn.git


To install:
'''''''''''

.. code-block:: bash

   cd giotto-learn
   pip install -e .

From there any change in the library files will be immediately available on your machine.

Testing
~~~~~~~

After installation, you can launch the test suite from outside the
source directory::

    pytest giotto


