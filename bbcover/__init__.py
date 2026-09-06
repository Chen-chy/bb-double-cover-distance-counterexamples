"""Exact convenience tools for the BB double-cover certificates.

The four standalone certificate implementations deliberately do not import this
package. See results/theory/ for the complete hypotheses and proofs.
"""
from .code import BBCode, validate_double_cover
from .bounds import DistanceInterval, cubic_interval
from .examples import get_example, names

__all__ = ["BBCode", "validate_double_cover", "DistanceInterval", "cubic_interval",
           "get_example", "names"]
__version__ = "0.2.1"
