***
Run
***
.. currentmodule:: pytimeops.run


:func:`main<pytimeops.main>` is the main executable function to pass through the pytimeops workflow.


Example::

    result = pytimeops.main('input.csv', 20, "a note about the metadata", verbose=False)

Overview:

- :func:`main`

.. autofunction:: main



Command line options for running *run.py*:


.. autoprogram:: run:parser
    :prog: run.py

