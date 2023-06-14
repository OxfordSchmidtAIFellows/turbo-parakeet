[![Style tests (flake8)](https://github.com/OxfordSchmidtAIFellows/turbo-parakeet/actions/workflows/style-test.yml/badge.svg)](https://github.com/OxfordSchmidtAIFellows/turbo-parakeet/actions/workflows/style-test.yml)
[![Unit tests](https://github.com/OxfordSchmidtAIFellows/turbo-parakeet/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/OxfordSchmidtAIFellows/turbo-parakeet/actions/workflows/unit-tests.yml)
[![Documentation Status](https://readthedocs.org/projects/turbo-parakeet/badge/?version=latest)](https://turbo-parakeet.readthedocs.io/en/latest/?badge=latest)

# turbo-parakeet
Find the main documentation here: https://turbo-parakeet.readthedocs.io/en/latest/

# What is turbo-parakeet?

This repository contains a python package **pytimeops**: a pipeline for cleaning, processing and clustering time-series data.

## Installation

To install the latest repository version, type:

```
$ git clone https://github.com/OxfordSchmidtAIFellows/turbo-parakeet.git
$ cd turbo-parakeet
$ pip install -e .[dev/docs]
```

## License

turbo-parakeet is fully open source. For more information about its license, see [LICENSE](https://github.com/OxfordSchmidtAIFellows/turbo-parakeet/LICENSE.md).

## Input format

The **pytimeops** package assumes the data you want to analyse is formatted in a certain way:
- a ```.csv``` file
- each row in the file corresponds to 1 time series measurement of a particular experiment.
- the M+C+T columns are ordered thus:
  - first M columns contain metadata describing the experimental setup and input specimen: e.g. the animal ID, sensillum, sugar, concentration.
  - next C=1 column contains the measurement channel used to obtain the time series data for the experiment: e.g. the neuron response being measured (GRN)
  - final T columns contain the values of the measurement for each time bin, ordered by increasing time.

In this way, we can correctly extract the measurements for all channels, and the associated metadata for each experiment.
