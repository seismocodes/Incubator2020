"""
Package for finding LFEs
"""

# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import pkg_resources

# https://github.com/python-poetry/poetry/issues/144#issuecomment-559793020
def get_version():
    try:
        distribution = pkg_resources.get_distribution("lfelib")
    except pkg_resources.DistributionNotFound:
        return "dev"  # or "", or None
        # or try with importib.metadata (py>3.8)
        # or try reading pyproject.toml
    else:
        return distribution.version


__version__ = get_version()

from . import lfe
# lfelib.lfe.findLFEs()
from . import utils
