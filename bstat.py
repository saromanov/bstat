from pymc import DiscreteUniform, Exponential, deterministic, Poisson, Uniform
import numpy as np


early_mean = Exponential('early_mean', beta=1.)
late_mean = Exponential('late_mean', beta=1.)
