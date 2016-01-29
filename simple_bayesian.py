import pymc
import pylab as pl

class Simple1:
    ''' Simple bayesian network
    '''
    def __init__(self, obs):
        self.obs = obs

    def construct(self):
        first = pymc.Bernoulli('F', .6, value=pl.ones(self.obs))
        p_first = pymc.Lambda('p_F', lambda R=R: pl.where(R, .005, .8),doc='Pr[S|R]')
        second = pymc.Bernoulli('S', p_first, value=pl.ones(self.obs))
        p_G = mc.Lambda('p_G', lambda S=S, R=R:pl.where(S, pl.where(R, .99, .9), pl.where(R, .8, 0.)),doc='Pr[G|S,R]')
        G = mc.Bernoulli('G', p_G, value=G_obs, observed=True)


class Simple2:
    ''' Another bayesian network
    '''
    def __init__(self, true_pA, true_pB):
        self.true_pA = true_pA
        self.true_pB = true_pB

    def generate(self, N_A, N_B):
        obsA = pymc.rbernoulli(self.true_pA, N_A)
        obsB = pymc.rbernoulli(self.true_PB, N_B)
