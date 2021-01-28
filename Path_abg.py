import BondGraphTools as bgt
import sympy as sp

def model():
    """ Acausal bond graph Path.py
    Created by stoichBondGraph at Wed Jan 27 12:34:26 2021

    Usage:
    import Path; model = Path.model()
    """

    model = bgt.new(name="Path")
    ### Species

    ### Ce:I1

    ## Component Ce:comp_I1
    K_I1 =  sp.symbols('K_I1')
    RT = sp.symbols('RT')
    comp_I1 = bgt.new('Ce',name='I1',value={'k':K_I1,'R':RT,'T':1},library='BioChem')
    model.add(comp_I1)

    ## Junction 0:comp_I1_jun
    comp_I1_jun = bgt.new('0')
    model.add(comp_I1_jun)

    ## Bond from comp_I1_jun to comp_I1
    bgt.connect(comp_I1_jun,comp_I1)

    ### Ce:I2

    ## Component Ce:comp_I2
    K_I2 =  sp.symbols('K_I2')
    RT = sp.symbols('RT')
    comp_I2 = bgt.new('Ce',name='I2',value={'k':K_I2,'R':RT,'T':1},library='BioChem')
    model.add(comp_I2)

    ## Junction 0:comp_I2_jun
    comp_I2_jun = bgt.new('0')
    model.add(comp_I2_jun)

    ## Bond from comp_I2_jun to comp_I2
    bgt.connect(comp_I2_jun,comp_I2)

    ### Ce:P

    ## Component Ce:comp_P
    K_P =  sp.symbols('K_P')
    RT = sp.symbols('RT')
    comp_P = bgt.new('Ce',name='P',value={'k':K_P,'R':RT,'T':1},library='BioChem')
    model.add(comp_P)

    ## Junction 0:comp_P_jun
    comp_P_jun = bgt.new('0')
    model.add(comp_P_jun)

    ## Bond from comp_P_jun to comp_P
    bgt.connect(comp_P_jun,comp_P)

    ### Ce:S

    ## Component Ce:comp_S
    K_S =  sp.symbols('K_S')
    RT = sp.symbols('RT')
    comp_S = bgt.new('Ce',name='S',value={'k':K_S,'R':RT,'T':1},library='BioChem')
    model.add(comp_S)

    ## Junction 0:comp_S_jun
    comp_S_jun = bgt.new('0')
    model.add(comp_S_jun)

    ## Bond from comp_S_jun to comp_S
    bgt.connect(comp_S_jun,comp_S)
    ### Reactions

    ### Re:r1

    ## Component Re:comp_r1
    kappa_r1 =  sp.symbols('kappa_r1')
    RT = sp.symbols('RT')
    comp_r1 = bgt.new('Re',name='r1',value={'r':kappa_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_r1)

    ## Junction 1:comp_r1_junF
    comp_r1_junF = bgt.new('1')
    model.add(comp_r1_junF)

    ## Bond from comp_r1_junF to (comp_r1,0)
    bgt.connect(comp_r1_junF,(comp_r1,0))

    ## Junction 1:comp_r1_junR
    comp_r1_junR = bgt.new('1')
    model.add(comp_r1_junR)

    ## Bond from (comp_r1,1) to comp_r1_junR
    bgt.connect((comp_r1,1),comp_r1_junR)

    ### Re:r2

    ## Component Re:comp_r2
    kappa_r2 =  sp.symbols('kappa_r2')
    RT = sp.symbols('RT')
    comp_r2 = bgt.new('Re',name='r2',value={'r':kappa_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_r2)

    ## Junction 1:comp_r2_junF
    comp_r2_junF = bgt.new('1')
    model.add(comp_r2_junF)

    ## Bond from comp_r2_junF to (comp_r2,0)
    bgt.connect(comp_r2_junF,(comp_r2,0))

    ## Junction 1:comp_r2_junR
    comp_r2_junR = bgt.new('1')
    model.add(comp_r2_junR)

    ## Bond from (comp_r2,1) to comp_r2_junR
    bgt.connect((comp_r2,1),comp_r2_junR)

    ### Re:r3

    ## Component Re:comp_r3
    kappa_r3 =  sp.symbols('kappa_r3')
    RT = sp.symbols('RT')
    comp_r3 = bgt.new('Re',name='r3',value={'r':kappa_r3,'R':RT,'T':1},library='BioChem')
    model.add(comp_r3)

    ## Junction 1:comp_r3_junF
    comp_r3_junF = bgt.new('1')
    model.add(comp_r3_junF)

    ## Bond from comp_r3_junF to (comp_r3,0)
    bgt.connect(comp_r3_junF,(comp_r3,0))

    ## Junction 1:comp_r3_junR
    comp_r3_junR = bgt.new('1')
    model.add(comp_r3_junR)

    ## Bond from (comp_r3,1) to comp_r3_junR
    bgt.connect((comp_r3,1),comp_r3_junR)
    ### Connections

    ### Ce:I1 to Re:r2

    ## Bond from comp_I1_jun to comp_r2_junF
    bgt.connect(comp_I1_jun,comp_r2_junF)

    ### Ce:I2 to Re:r3

    ## Bond from comp_I2_jun to comp_r3_junF
    bgt.connect(comp_I2_jun,comp_r3_junF)

    ### Ce:S to Re:r1

    ## Bond from comp_S_jun to comp_r1_junF
    bgt.connect(comp_S_jun,comp_r1_junF)

    ### Re:r1 to Ce:I1

    ## Bond from comp_r1_junR to comp_I1_jun
    bgt.connect(comp_r1_junR,comp_I1_jun)

    ### Re:r2 to Ce:I2

    ## Bond from comp_r2_junR to comp_I2_jun
    bgt.connect(comp_r2_junR,comp_I2_jun)

    ### Re:r3 to Ce:P

    ## Bond from comp_r3_junR to comp_P_jun
    bgt.connect(comp_r3_junR,comp_P_jun)

    return model
