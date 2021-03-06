# This file contains some section data extracted from the CRM (Common Research 
# Model) wing geometry. This is used to build the transonic wing geometry example.
def CRMlinear(Epsilon):
    XRoot = [1,
    0.9497,
    0.8992,
    0.8487,
    0.798,
    0.7474,
    0.6967,
    0.646,
    0.5953,
    0.5445,
    0.4938,
    0.443,
    0.3922,
    0.3414,
    0.2906,
    0.2398,
    0.189,
    0.1382,
    0.0878,
    0.0384,
    0,
    0.0381,
    0.0863,
    0.136,
    0.1864,
    0.2371,
    0.2881,
    0.3394,
    0.3907,
    0.442,
    0.4931,
    0.5441,
    0.595,
    0.6457,
    0.6964,
    0.7469,
    0.7974,
    0.8478,
    0.8983,
    0.949,
    1]
    
    ZRoot = [0.0014,
    0.0088,
    0.0145,
    0.0195,
    0.024,
    0.0282,
    0.032,
    0.0353,
    0.0382,
    0.0408,
    0.0431,
    0.0453,
    0.0471,
    0.0488,
    0.05,
    0.0505,
    0.0499,
    0.0472,
    0.0412,
    0.0293,
    0,
    -0.0314,
    -0.0488,
    -0.0616,
    -0.0716,
    -0.0794,
    -0.0847,
    -0.0873,
    -0.0874,
    -0.085,
    -0.0807,
    -0.0748,
    -0.0678,
    -0.06,
    -0.0516,
    -0.0428,
    -0.0334,
    -0.0238,
    -0.0144,
    -0.0063,
    -0.0009]
    
    XTip = [1,
    0.9502,
    0.9001,
    0.85,
    0.7998,
    0.7496,
    0.6993,
    0.6489,
    0.5985,
    0.548,
    0.4975,
    0.447,
    0.3965,
    0.346,
    0.2956,
    0.2451,
    0.1948,
    0.1445,
    0.0944,
    0.0446,
    0,
    0.0436,
    0.0935,
    0.1437,
    0.194,
    0.2444,
    0.2949,
    0.3454,
    0.3959,
    0.4464,
    0.4969,
    0.5473,
    0.5977,
    0.6479,
    0.6981,
    0.7483,
    0.7985,
    0.8487,
    0.8991,
    0.9496,
    1]
    
    ZTip = [0.0028,
    0.0112,
    0.0178,
    0.024,
    0.0299,
    0.0353,
    0.04,
    0.0439,
    0.0469,
    0.049,
    0.0502,
    0.0505,
    0.0499,
    0.0484,
    0.0462,
    0.0431,
    0.0392,
    0.0342,
    0.028,
    0.0195,
    0,
    -0.0207,
    -0.0287,
    -0.0346,
    -0.0391,
    -0.0424,
    -0.0446,
    -0.0456,
    -0.0454,
    -0.0441,
    -0.0416,
    -0.0381,
    -0.0337,
    -0.0285,
    -0.0228,
    -0.0168,
    -0.0108,
    -0.0055,
    -0.0015,
    0.0003,
    -0.0019]
    
    i = -1
    
    x = []
    z = []
    
    for XR in XRoot:
        i = i + 1
        ZR = ZRoot[i]
        XT = XTip[i]
        ZT = ZTip[i]
        list.append(x, XR*(1-Epsilon)+XT*Epsilon)
        list.append(z, ZR*(1-Epsilon)+ZT*Epsilon)

    return x, z