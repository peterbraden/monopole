from numpy import complex, complex64, mat, dot, trace, pi, sqrt, mat
from mpmath import ellipk, ellipe
from cmath import exp


c0 = complex(0, 1)
c1 = complex(0, 8)
c2 = complex(0, 2)
c3 = complex(0, 16)
c4 = complex(0, 32)
c5 = complex(0, 24)
c6 = complex(0, 48)
c7 = complex(0, 4)
c8 = complex(0, 12)
c9 = complex(0, -8)
c10 = complex(0, -24)
c11 = complex(0, -16)
c12 = complex(0, -32)
c13 = complex(0, -2)
c14 = complex(0, -48)
c15 = complex(0, -3)
c16 = complex(0, -1)
c17 = complex(0, -4)
c18 = complex(0, -12)
c19 = complex(0, 6)
c20 = complex(0, -6)
c21 = complex(0, 96)
c22 = complex(0, -64)
c23 = complex(0, 64)
c24 = complex(0, 72)
c25 = complex(0, -96)



def ddphis121(zeta, mu, DM, DZ, DDM, DDZ, x, k):


    ex0 = exp(2 * mu[0])
    ex1 = exp(2 * mu[1])
    ex2 = exp(2 * mu[2])
    ex3 = exp(2 * mu[3])
    exm0 = exp(-2 * mu[0])
    exm1 = exp(-2 * mu[1])
    exm2 = exp(-2 * mu[2])
    exm3 = exp(-2 * mu[3])


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

    DS = [None]*2
    DSP = [None]*2
    DSM = [None]*2
    DSPM = [None]*2
    DRP = [None]*3
    DRM = [None]*3
    DRPBAR = [None]*3
    DRMBAR = [None]*3


    p2r = r**2
    p3r = r**3
    p4r = r**4
    p5r = r**5
    p2K = K**2
    p3K = K**3
    p4K = K**4
    p5K = K**5
    p2k1 = k1**2
    p3k1 = k1**3
    p4k1 = k1**4
    p5k1 = k1**5
    p2SP = SP**2
    p3SP = SP**3
    p4SP = SP**4
    p5SP = SP**5
    p2SM = SM**2
    p3SM = SM**3
    p4SM = SM**4
    p5SM = SM**5
    p2x0 = x[0]**2
    p3x0 = x[0]**3
    p4x0 = x[0]**4
    p5x0 = x[0]**5
    p2x1 = x[1]**2
    p3x1 = x[1]**3
    p4x1 = x[1]**4
    p5x1 = x[1]**5
    p2x2 = x[2]**2
    p3x2 = x[2]**3
    p4x2 = x[2]**4
    p5x2 = x[2]**5
    p2zeta0 = zeta[0]**2
    p3zeta0 = zeta[0]**3
    p4zeta0 = zeta[0]**4
    p5zeta0 = zeta[0]**5
    p2zeta1 = zeta[1]**2
    p3zeta1 = zeta[1]**3
    p4zeta1 = zeta[1]**4
    p5zeta1 = zeta[1]**5
    p2zeta2 = zeta[2]**2
    p3zeta2 = zeta[2]**3
    p4zeta2 = zeta[2]**4
    p5zeta2 = zeta[2]**5
    p2zeta3 = zeta[3]**2
    p3zeta3 = zeta[3]**3
    p4zeta3 = zeta[3]**4
    p5zeta3 = zeta[3]**5
    p2ex0 = ex0**2
    p3ex0 = ex0**3
    p4ex0 = ex0**4
    p5ex0 = ex0**5
    p2exm0 = exm0**2
    p3exm0 = exm0**3
    p4exm0 = exm0**4
    p5exm0 = exm0**5
    p2ex1 = ex1**2
    p3ex1 = ex1**3
    p4ex1 = ex1**4
    p5ex1 = ex1**5
    p2exm1 = exm1**2
    p3exm1 = exm1**3
    p4exm1 = exm1**4
    p5exm1 = exm1**5
    p2ex2 = ex2**2
    p3ex2 = ex2**3
    p4ex2 = ex2**4
    p5ex2 = ex2**5
    p2exm2 = exm2**2
    p3exm2 = exm2**3
    p4exm2 = exm2**4
    p5exm2 = exm2**5
    p2ex3 = ex3**2
    p3ex3 = ex3**3
    p4ex3 = ex3**4
    p5ex3 = ex3**5
    p2exm3 = exm3**2
    p3exm3 = exm3**3
    p4exm3 = exm3**4
    p5exm3 = exm3**5



    DS[0] = -4 * (p2K - 4 * p2x0 - 4 * p2x1) ** (-0.1e1 / 0.2e1) * x[0]

    DS[1] = -4 * (p2K - 4 * p2x0 - 4 * p2x1) ** (-0.1e1 / 0.2e1) * x[1]

    DSP[0] = -4 * (x[0] + c0 * x[1]) * (4 * p2x1 + c9 * x[0] * x[1] + p2K - 4 * p2x0) ** (-0.1e1 / 0.2e1)

    DSP[1] = -4 * (c0 * x[0] - x[1]) * (4 * p2x1 + c9 * x[0] * x[1] + p2K - 4 * p2x0) ** (-0.1e1 / 0.2e1)

    DSM[0] = 4 * (c0 * x[1] - x[0]) * (4 * p2x1 + c1 * x[0] * x[1] + p2K - 4 * p2x0) ** (-0.1e1 / 0.2e1)

    DSM[1] = 4 * (x[1] + c0 * x[0]) * (4 * p2x1 + c1 * x[0] * x[1] + p2K - 4 * p2x0) ** (-0.1e1 / 0.2e1)

    DSPM[0] = 4 * (-p2K * k ** 2 * p2k1 + 4 * p2k1 * p2x0 + 4 * p2k1 * p2x1 - 4 * p2x1) ** (-0.1e1 / 0.2e1) * p2k1 * x[0]

    DSPM[1] = 4 * x[1] * (p2k1 - 1) * (-p2K * k ** 2 * p2k1 + 4 * p2k1 * p2x0 + 4 * p2k1 * p2x1 - 4 * p2x1) ** (-0.1e1 / 0.2e1)

    DRP[0] = c9 * p2k1 * p2x1 - 16 * p2k1 * x[0] * x[1] + c2 * p2K * p2k1 + c3 * p2x1 + c10 * p2k1 * p2x0 - 16 * x[0] * x[1] + c3 * p2x2

    DRP[1] = -24 * p2k1 * p2x1 + c11 * p2k1 * x[0] * x[1] - 2 * p2K * p2k1 + 24 * p2x1 - 8 * p2k1 * p2x0 + c4 * x[0] * x[1] + 2 * p2K - 8 * p2x0 - 16 * p2x2

    DRP[2] = -32 * x[1] * x[2] + c4 * x[0] * x[2]

    DRM[0] = c5 * p2k1 * p2x1 - 48 * p2k1 * x[0] * x[1] + c2 * p2K * p2k1 + c11 * p2x1 + c10 * p2k1 * p2x0 + 16 * x[0] * x[1] + c11 * p2x2

    DRM[1] = 24 * p2k1 * p2x1 + c6 * p2k1 * x[0] * x[1] + 2 * p2K * p2k1 - 24 * p2x1 - 24 * p2k1 * p2x0 + c12 * x[0] * x[1] - 2 * p2K + 8 * p2x0 - 16 * p2x2

    DRM[2] = -32 * x[1] * x[2] + c12 * x[0] * x[2]

    DRPBAR[0] = c1 * p2k1 * p2x1 - 16 * p2k1 * x[0] * x[1] + c13 * p2K * p2k1 + c11 * p2x1 + c5 * p2k1 * p2x0 - 16 * x[0] * x[1] + c11 * p2x2

    DRPBAR[1] = -24 * p2k1 * p2x1 + c3 * p2k1 * x[0] * x[1] - 2 * p2K * p2k1 + 24 * p2x1 - 8 * p2k1 * p2x0 + c12 * x[0] * x[1] + 2 * p2K - 8 * p2x0 - 16 * p2x2

    DRPBAR[2] = -32 * x[1] * x[2] + c12 * x[0] * x[2]

    DRMBAR[0] = c10 * p2k1 * p2x1 - 48 * p2k1 * x[0] * x[1] + c13 * p2K * p2k1 + c3 * p2x1 + c5 * p2k1 * p2x0 + 16 * x[0] * x[1] + c3 * p2x2

    DRMBAR[1] = 24 * p2k1 * p2x1 + c14 * p2k1 * x[0] * x[1] + 2 * p2K * p2k1 - 24 * p2x1 - 24 * p2k1 * p2x0 + c4 * x[0] * x[1] - 2 * p2K + 8 * p2x0 - 16 * p2x2

    DRMBAR[2] = -32 * x[1] * x[2] + c4 * x[0] * x[2]

    DDS = [None]*2
    DDSP = [None]*2
    DDSM = [None]*2
    DDSPM = [None]*2
    DDRP = [None]*3
    DDRM = [None]*3
    DDRPBAR = [None]*3
    DDRMBAR = [None]*3

    DDS[0] = -4 * (p2K - 4 * p2x1) * (p2K - 4 * p2x0 - 4 * p2x1) ** (-0.3e1 / 0.2e1)

    DDS[1] = -4 * (p2K - 4 * p2x0) * (p2K - 4 * p2x0 - 4 * p2x1) ** (-0.3e1 / 0.2e1)

    DDSP[0] = -4 * p2K * (4 * p2x1 + c9 * x[0] * x[1] + p2K - 4 * p2x0) ** (-0.3e1 / 0.2e1)

    DDSP[1] = 4 * p2K * (4 * p2x1 + c9 * x[0] * x[1] + p2K - 4 * p2x0) ** (-0.3e1 / 0.2e1)

    DDSM[0] = -4 * p2K * (4 * p2x1 + c1 * x[0] * x[1] + p2K - 4 * p2x0) ** (-0.3e1 / 0.2e1)

    DDSM[1] = 4 * p2K * (4 * p2x1 + c1 * x[0] * x[1] + p2K - 4 * p2x0) ** (-0.3e1 / 0.2e1)

    DDSPM[0] = -4 * p2k1 * (p2K * k ** 2 * p2k1 - 4 * p2k1 * p2x1 + 4 * p2x1) * (-p2K * k ** 2 * p2k1 + 4 * p2k1 * p2x0 + 4 * p2k1 * p2x1 - 4 * p2x1) ** (-0.3e1 / 0.2e1)

    DDSPM[1] = -4 * (p2k1 - 1) * p2k1 * (p2K * k ** 2 - 4 * p2x0) * (-p2K * k ** 2 * p2k1 + 4 * p2k1 * p2x0 + 4 * p2k1 * p2x1 - 4 * p2x1) ** (-0.3e1 / 0.2e1)

    DDRP[0] = -16 * p2k1 * x[1] + c14 * p2k1 * x[0] - 16 * x[1]

    DDRP[1] = -48 * p2k1 * x[1] + c11 * p2k1 * x[0] + 48 * x[1] + c4 * x[0]

    DDRP[2] = -32 * x[1] + c4 * x[0]

    DDRM[0] = -48 * p2k1 * x[1] + c14 * p2k1 * x[0] + 16 * x[1]

    DDRM[1] = 48 * p2k1 * x[1] + c6 * p2k1 * x[0] - 48 * x[1] + c12 * x[0]

    DDRM[2] = -32 * x[1] + c12 * x[0]

    DDRPBAR[0] = -16 * p2k1 * x[1] + c6 * p2k1 * x[0] - 16 * x[1]

    DDRPBAR[1] = -48 * p2k1 * x[1] + c3 * p2k1 * x[0] + 48 * x[1] + c12 * x[0]

    DDRPBAR[2] = -32 * x[1] + c12 * x[0]

    DDRMBAR[0] = -48 * p2k1 * x[1] + c6 * p2k1 * x[0] + 16 * x[1]

    DDRMBAR[1] = 48 * p2k1 * x[1] + c14 * p2k1 * x[0] - 48 * x[1] + c4 * x[0]

    DDRMBAR[2] = -32 * x[1] + c4 * x[0]
