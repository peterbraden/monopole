from numpy import complex, complex64, mat, dot, trace, pi, sqrt, mat
from mpmath import ellipk, ellipe
from cmath import exp


def grams(zeta, mu, x, k):

    K = complex64(ellipk(k**2))

    E = complex64(ellipe(k**2))

    cm= (2*E-K)/K

    k1 = sqrt(1-k**2)

    xp = x[0]+complex(0,1)*x[1]
    xm = x[0]-complex(0,1)*x[1]
    S =  sqrt(K**2-4*xp*xm)
    SP = sqrt(K**2-4*xp**2)
    SM = sqrt(K**2-4*xm**2)
    SPM = sqrt(-k1**2*(K**2*k**2-4*xm*xp)+(xm-xp)**2)
    R = 2*K**2*k1**2-S**2-8*x[2]**2
    RM = complex(0,1)*SM**2*(xm*(2*k1**2-1)+xp)-(16*complex(0,1))*xm*x[2]**2
    RP = complex(0,1)*SM**2*(xp*(2*k1**2-1)+xm)+(16*complex(0,1))*xp*x[2]**2
    RMBAR=-complex(0,1)*SP**2*( xp*(2*k1**2-1)+xm ) +16*complex(0,1)*xp*x[2]**2
    RPBAR=-complex(0,1)*SP**2*( xm*(2*k1**2-1)+xp ) -16*complex(0,1)*xm*x[2]**2
    r=sqrt(x[0]**2+x[1]**2+x[2]**2)

    return mat([[(complex(0, -1) * (-exp(2 * mu[2]) + exp(2 * mu[1])) * zeta[0] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[0] ** 3 - R / zeta[0] ** 2 + complex(0, 12) * xm * x[2] / zeta[0] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[0]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[2] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[0] - (-x[0] + complex(0, -1) * x[1]) / zeta[0] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[0]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[0] - x[2] / zeta[0] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[2] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[0] + complex(0, 2) * pi - 2 * mu[2])) / K ** 2 / (-RMBAR / zeta[0] ** 3 + 2 * R * x[2] / zeta[0] ** 2 + RPBAR / zeta[0] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (exp(2 * mu[2]) - exp(2 * mu[0])) * zeta[1] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[1] ** 3 - R / zeta[1] ** 2 + complex(0, 12) * xm * x[2] / zeta[1] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[1]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[2] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[1] - (-x[0] + complex(0, -1) * x[1]) / zeta[1] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[1]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[1] - x[2] / zeta[1] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[2] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[1] + complex(0, 2) * pi - 2 * mu[2])) / K ** 2 / (-RMBAR / zeta[1] ** 3 + 2 * R * x[2] / zeta[1] ** 2 + RPBAR / zeta[1] - x[2] * (SM ** 2 + SP ** 2))) * (exp(-2 * mu[0]) - exp(-2 * mu[3])) + (complex(0, -1) * (-exp(2 * mu[1]) + exp(2 * mu[0])) * zeta[2] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[2] ** 3 - R / zeta[2] ** 2 + complex(0, 12) * xm * x[2] / zeta[2] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[2]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[3] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[2] - (-x[0] + complex(0, -1) * x[1]) / zeta[2] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[2]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[2] - x[2] / zeta[2] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[3] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[2] - 2 * mu[3])) / K ** 2 / (-RMBAR / zeta[2] ** 3 + 2 * R * x[2] / zeta[2] ** 2 + RPBAR / zeta[2] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (-exp(2 * mu[2]) + exp(2 * mu[1])) * zeta[0] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[0] ** 3 - R / zeta[0] ** 2 + complex(0, 12) * xm * x[2] / zeta[0] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[0]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[3] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[0] - (-x[0] + complex(0, -1) * x[1]) / zeta[0] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[0]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[0] - x[2] / zeta[0] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[3] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[0] + complex(0, 2) * pi - 2 * mu[3])) / K ** 2 / (-RMBAR / zeta[0] ** 3 + 2 * R * x[2] / zeta[0] ** 2 + RPBAR / zeta[0] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (exp(2 * mu[2]) - exp(2 * mu[0])) * zeta[1] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[1] ** 3 - R / zeta[1] ** 2 + complex(0, 12) * xm * x[2] / zeta[1] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[1]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[3] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[1] - (-x[0] + complex(0, -1) * x[1]) / zeta[1] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[1]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[1] - x[2] / zeta[1] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[3] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[1] + complex(0, 2) * pi - 2 * mu[3])) / K ** 2 / (-RMBAR / zeta[1] ** 3 + 2 * R * x[2] / zeta[1] ** 2 + RPBAR / zeta[1] - x[2] * (SM ** 2 + SP ** 2))) * (-exp(-2 * mu[0]) + exp(-2 * mu[2])) + (complex(0, -1) * (-exp(2 * mu[1]) + exp(2 * mu[0])) * zeta[2] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[2] ** 3 - R / zeta[2] ** 2 + complex(0, 12) * xm * x[2] / zeta[2] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[2]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[0] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[2] - (-x[0] + complex(0, -1) * x[1]) / zeta[2] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[2]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[2] - x[2] / zeta[2] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[0] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[2] + complex(0, -2) * pi - 2 * mu[0])) / K ** 2 / (-RMBAR / zeta[2] ** 3 + 2 * R * x[2] / zeta[2] ** 2 + RPBAR / zeta[2] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (exp(2 * mu[2]) - exp(2 * mu[0])) * zeta[1] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[1] ** 3 - R / zeta[1] ** 2 + complex(0, 12) * xm * x[2] / zeta[1] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[1]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[0] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[1] - (-x[0] + complex(0, -1) * x[1]) / zeta[1] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[1]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[1] - x[2] / zeta[1] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[0] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[1] - 2 * mu[0])) / K ** 2 / (-RMBAR / zeta[1] ** 3 + 2 * R * x[2] / zeta[1] ** 2 + RPBAR / zeta[1] - x[2] * (SM ** 2 + SP ** 2))) * (exp(-2 * mu[3]) - exp(-2 * mu[2])),(complex(0, -1) * (-exp(2 * mu[2]) + exp(2 * mu[1])) * zeta[0] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[0] ** 3 - R / zeta[0] ** 2 + complex(0, 12) * xm * x[2] / zeta[0] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[0]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[2] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[0] - (-x[0] + complex(0, -1) * x[1]) / zeta[0] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[0]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[0] - x[2] / zeta[0] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[2] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[0] + complex(0, 2) * pi - 2 * mu[2])) / K ** 2 / (-RMBAR / zeta[0] ** 3 + 2 * R * x[2] / zeta[0] ** 2 + RPBAR / zeta[0] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (exp(2 * mu[2]) - exp(2 * mu[0])) * zeta[1] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[1] ** 3 - R / zeta[1] ** 2 + complex(0, 12) * xm * x[2] / zeta[1] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[1]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[2] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[1] - (-x[0] + complex(0, -1) * x[1]) / zeta[1] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[1]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[1] - x[2] / zeta[1] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[2] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[1] + complex(0, 2) * pi - 2 * mu[2])) / K ** 2 / (-RMBAR / zeta[1] ** 3 + 2 * R * x[2] / zeta[1] ** 2 + RPBAR / zeta[1] - x[2] * (SM ** 2 + SP ** 2))) * (exp(-2 * mu[1]) - exp(-2 * mu[0])) + (complex(0, -1) * (-exp(2 * mu[1]) + exp(2 * mu[0])) * zeta[2] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[2] ** 3 - R / zeta[2] ** 2 + complex(0, 12) * xm * x[2] / zeta[2] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[2]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[0] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[2] - (-x[0] + complex(0, -1) * x[1]) / zeta[2] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[2]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[2] - x[2] / zeta[2] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[0] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[2] + complex(0, -2) * pi - 2 * mu[0])) / K ** 2 / (-RMBAR / zeta[2] ** 3 + 2 * R * x[2] / zeta[2] ** 2 + RPBAR / zeta[2] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (exp(2 * mu[2]) - exp(2 * mu[0])) * zeta[1] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[1] ** 3 - R / zeta[1] ** 2 + complex(0, 12) * xm * x[2] / zeta[1] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[1]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[0] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[1] - (-x[0] + complex(0, -1) * x[1]) / zeta[1] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[1]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[1] - x[2] / zeta[1] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[0] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[1] - 2 * mu[0])) / K ** 2 / (-RMBAR / zeta[1] ** 3 + 2 * R * x[2] / zeta[1] ** 2 + RPBAR / zeta[1] - x[2] * (SM ** 2 + SP ** 2))) * (exp(-2 * mu[2]) - exp(-2 * mu[1])) + (complex(0, -1) * (-exp(2 * mu[1]) + exp(2 * mu[0])) * zeta[2] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[2] ** 3 - R / zeta[2] ** 2 + complex(0, 12) * xm * x[2] / zeta[2] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[2]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[1] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[2] - (-x[0] + complex(0, -1) * x[1]) / zeta[2] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[2]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[2] - x[2] / zeta[2] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[1] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[2] + complex(0, -2) * pi - 2 * mu[1])) / K ** 2 / (-RMBAR / zeta[2] ** 3 + 2 * R * x[2] / zeta[2] ** 2 + RPBAR / zeta[2] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (-exp(2 * mu[2]) + exp(2 * mu[1])) * zeta[0] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[0] ** 3 - R / zeta[0] ** 2 + complex(0, 12) * xm * x[2] / zeta[0] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[0]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[1] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[0] - (-x[0] + complex(0, -1) * x[1]) / zeta[0] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[0]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[0] - x[2] / zeta[0] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[1] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[0] - 2 * mu[1])) / K ** 2 / (-RMBAR / zeta[0] ** 3 + 2 * R * x[2] / zeta[0] ** 2 + RPBAR / zeta[0] - x[2] * (SM ** 2 + SP ** 2))) * (-exp(-2 * mu[2]) + exp(-2 * mu[0]))],[(complex(0, -1) * (exp(2 * mu[0]) - exp(2 * mu[2])) * zeta[3] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[3] ** 3 - R / zeta[3] ** 2 + complex(0, 12) * xm * x[2] / zeta[3] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[3]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[2] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[3] - (-x[0] + complex(0, -1) * x[1]) / zeta[3] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[3]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[3] - x[2] / zeta[3] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[2] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[3] - 2 * mu[2])) / K ** 2 / (-RMBAR / zeta[3] ** 3 + 2 * R * x[2] / zeta[3] ** 2 + RPBAR / zeta[3] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (-exp(2 * mu[3]) + exp(2 * mu[2])) * zeta[0] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[0] ** 3 - R / zeta[0] ** 2 + complex(0, 12) * xm * x[2] / zeta[0] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[0]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[2] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[0] - (-x[0] + complex(0, -1) * x[1]) / zeta[0] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[0]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[0] - x[2] / zeta[0] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[2] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[0] + complex(0, 2) * pi - 2 * mu[2])) / K ** 2 / (-RMBAR / zeta[0] ** 3 + 2 * R * x[2] / zeta[0] ** 2 + RPBAR / zeta[0] - x[2] * (SM ** 2 + SP ** 2))) * (exp(-2 * mu[0]) - exp(-2 * mu[3])) + (complex(0, -1) * (-exp(2 * mu[0]) + exp(2 * mu[3])) * zeta[2] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[2] ** 3 - R / zeta[2] ** 2 + complex(0, 12) * xm * x[2] / zeta[2] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[2]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[3] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[2] - (-x[0] + complex(0, -1) * x[1]) / zeta[2] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[2]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[2] - x[2] / zeta[2] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[3] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[2] - 2 * mu[3])) / K ** 2 / (-RMBAR / zeta[2] ** 3 + 2 * R * x[2] / zeta[2] ** 2 + RPBAR / zeta[2] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (-exp(2 * mu[3]) + exp(2 * mu[2])) * zeta[0] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[0] ** 3 - R / zeta[0] ** 2 + complex(0, 12) * xm * x[2] / zeta[0] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[0]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[3] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[0] - (-x[0] + complex(0, -1) * x[1]) / zeta[0] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[0]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[3] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[3] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[0] - x[2] / zeta[0] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[3] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[0] + complex(0, 2) * pi - 2 * mu[3])) / K ** 2 / (-RMBAR / zeta[0] ** 3 + 2 * R * x[2] / zeta[0] ** 2 + RPBAR / zeta[0] - x[2] * (SM ** 2 + SP ** 2))) * (-exp(-2 * mu[0]) + exp(-2 * mu[2])) + (complex(0, -1) * (-exp(2 * mu[0]) + exp(2 * mu[3])) * zeta[2] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[2] ** 3 - R / zeta[2] ** 2 + complex(0, 12) * xm * x[2] / zeta[2] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[2]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[0] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[2] - (-x[0] + complex(0, -1) * x[1]) / zeta[2] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[2]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[2] - x[2] / zeta[2] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[0] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[2] + complex(0, -2) * pi - 2 * mu[0])) / K ** 2 / (-RMBAR / zeta[2] ** 3 + 2 * R * x[2] / zeta[2] ** 2 + RPBAR / zeta[2] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (exp(2 * mu[0]) - exp(2 * mu[2])) * zeta[3] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[3] ** 3 - R / zeta[3] ** 2 + complex(0, 12) * xm * x[2] / zeta[3] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[3]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[0] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[3] - (-x[0] + complex(0, -1) * x[1]) / zeta[3] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[3]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[3] - x[2] / zeta[3] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[0] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[3] + complex(0, -2) * pi - 2 * mu[0])) / K ** 2 / (-RMBAR / zeta[3] ** 3 + 2 * R * x[2] / zeta[3] ** 2 + RPBAR / zeta[3] - x[2] * (SM ** 2 + SP ** 2))) * (exp(-2 * mu[3]) - exp(-2 * mu[2])),(complex(0, -1) * (exp(2 * mu[0]) - exp(2 * mu[2])) * zeta[3] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[3] ** 3 - R / zeta[3] ** 2 + complex(0, 12) * xm * x[2] / zeta[3] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[3]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[2] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[3] - (-x[0] + complex(0, -1) * x[1]) / zeta[3] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[3]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[3] - x[2] / zeta[3] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[2] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[3] - 2 * mu[2])) / K ** 2 / (-RMBAR / zeta[3] ** 3 + 2 * R * x[2] / zeta[3] ** 2 + RPBAR / zeta[3] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (-exp(2 * mu[3]) + exp(2 * mu[2])) * zeta[0] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[0] ** 3 - R / zeta[0] ** 2 + complex(0, 12) * xm * x[2] / zeta[0] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[0]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[2] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[0] - (-x[0] + complex(0, -1) * x[1]) / zeta[0] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[0]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[2] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[2] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[0] - x[2] / zeta[0] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[2] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[0] + complex(0, 2) * pi - 2 * mu[2])) / K ** 2 / (-RMBAR / zeta[0] ** 3 + 2 * R * x[2] / zeta[0] ** 2 + RPBAR / zeta[0] - x[2] * (SM ** 2 + SP ** 2))) * (exp(-2 * mu[1]) - exp(-2 * mu[0])) + (complex(0, -1) * (-exp(2 * mu[0]) + exp(2 * mu[3])) * zeta[2] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[2] ** 3 - R / zeta[2] ** 2 + complex(0, 12) * xm * x[2] / zeta[2] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[2]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[0] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[2] - (-x[0] + complex(0, -1) * x[1]) / zeta[2] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[2]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[2] - x[2] / zeta[2] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[0] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[2] + complex(0, -2) * pi - 2 * mu[0])) / K ** 2 / (-RMBAR / zeta[2] ** 3 + 2 * R * x[2] / zeta[2] ** 2 + RPBAR / zeta[2] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (exp(2 * mu[0]) - exp(2 * mu[2])) * zeta[3] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[3] ** 3 - R / zeta[3] ** 2 + complex(0, 12) * xm * x[2] / zeta[3] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[3]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[0] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[3] - (-x[0] + complex(0, -1) * x[1]) / zeta[3] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[3]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[0] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[0] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[3] - x[2] / zeta[3] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[0] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[3] + complex(0, -2) * pi - 2 * mu[0])) / K ** 2 / (-RMBAR / zeta[3] ** 3 + 2 * R * x[2] / zeta[3] ** 2 + RPBAR / zeta[3] - x[2] * (SM ** 2 + SP ** 2))) * (exp(-2 * mu[2]) - exp(-2 * mu[1])) + (complex(0, -1) * (-exp(2 * mu[0]) + exp(2 * mu[3])) * zeta[2] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[2] ** 3 - R / zeta[2] ** 2 + complex(0, 12) * xm * x[2] / zeta[2] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[2]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[1] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[2] - (-x[0] + complex(0, -1) * x[1]) / zeta[2] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[2]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[2] - x[2] / zeta[2] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[1] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[2] + complex(0, -2) * pi - 2 * mu[1])) / K ** 2 / (-RMBAR / zeta[2] ** 3 + 2 * R * x[2] / zeta[2] ** 2 + RPBAR / zeta[2] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (exp(2 * mu[0]) - exp(2 * mu[2])) * zeta[3] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[3] ** 3 - R / zeta[3] ** 2 + complex(0, 12) * xm * x[2] / zeta[3] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[3]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[1] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[3] - (-x[0] + complex(0, -1) * x[1]) / zeta[3] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[3]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[3] - x[2] / zeta[3] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[1] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[3] + complex(0, -2) * pi - 2 * mu[1])) / K ** 2 / (-RMBAR / zeta[3] ** 3 + 2 * R * x[2] / zeta[3] ** 2 + RPBAR / zeta[3] - x[2] * (SM ** 2 + SP ** 2)) + complex(0, -1) * (-exp(2 * mu[3]) + exp(2 * mu[2])) * zeta[0] * SP ** 2 * (complex(0, 4) * x[2] * xp / zeta[0] ** 3 - R / zeta[0] ** 2 + complex(0, 12) * xm * x[2] / zeta[0] + SM ** 2) * ((-x[2] + complex(0, 1) * (-x[0] + complex(0, -1) * x[1]) / zeta[0]) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, -1) * x[1]) ** 2) * zeta[1] - (x[0] + complex(0, -1) * x[1]) * x[2]) + (complex(0, -1) * x[2] / zeta[0] - (-x[0] + complex(0, -1) * x[1]) / zeta[0] ** 2) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 - 0.3e1 / 0.2e1 * x[2] ** 2) + (-x[0] + complex(0, 1) * x[1] + complex(0, 1) * x[2] / zeta[0]) * (-(K ** 2 / 8 - (x[0] + complex(0, 1) * x[1]) ** 2 / 2) / zeta[1] ** 2 + complex(0, -2) * (x[0] + complex(0, 1) * x[1]) * x[2] / zeta[1] + K ** 2 * (-2 * k ** 2 + 1) / 8 + (x[0] + complex(0, -1) * x[1]) * (x[0] + complex(0, 1) * x[1]) - x[2] ** 2 / 2) + (complex(0, 1) * (complex(0, 1) * x[1] - x[0]) / zeta[0] - x[2] / zeta[0] ** 2) * (complex(0, 0.1e1 / 0.4e1) * (K ** 2 - 4 * (x[0] + complex(0, 1) * x[1]) ** 2) / zeta[1] - (x[0] + complex(0, 1) * x[1]) * x[2])) * (1 - exp(2 * mu[0] - 2 * mu[1])) / K ** 2 / (-RMBAR / zeta[0] ** 3 + 2 * R * x[2] / zeta[0] ** 2 + RPBAR / zeta[0] - x[2] * (SM ** 2 + SP ** 2))) * (-exp(-2 * mu[2]) + exp(-2 * mu[0]))]])