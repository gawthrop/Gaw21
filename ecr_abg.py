import BondGraphTools as bgt
import sympy as sp

def model():
    """ Acausal bond graph ecr.py
    Created by stoichBondGraph at Wed Jan 27 12:34:22 2021

    Usage:
    import ecr; model = ecr.model()
    """

    model = bgt.new(name="ecr")
    ### Species

    ### Ce:A

    ## Component Ce:comp_A
    K_A =  sp.symbols('K_A')
    RT = sp.symbols('RT')
    comp_A = bgt.new('Ce',name='A',value={'k':K_A,'R':RT,'T':1},library='BioChem')
    model.add(comp_A)

    ## Junction 0:comp_A_jun
    comp_A_jun = bgt.new('0')
    model.add(comp_A_jun)

    ## Bond from comp_A_jun to comp_A
    bgt.connect(comp_A_jun,comp_A)

    ### Ce:Act

    ## Component Ce:comp_Act
    K_Act =  sp.symbols('K_Act')
    RT = sp.symbols('RT')
    comp_Act = bgt.new('Ce',name='Act',value={'k':K_Act,'R':RT,'T':1},library='BioChem')
    model.add(comp_Act)

    ## Junction 0:comp_Act_jun
    comp_Act_jun = bgt.new('0')
    model.add(comp_Act_jun)

    ## Bond from comp_Act_jun to comp_Act
    bgt.connect(comp_Act_jun,comp_Act)

    ### Ce:B

    ## Component Ce:comp_B
    K_B =  sp.symbols('K_B')
    RT = sp.symbols('RT')
    comp_B = bgt.new('Ce',name='B',value={'k':K_B,'R':RT,'T':1},library='BioChem')
    model.add(comp_B)

    ## Junction 0:comp_B_jun
    comp_B_jun = bgt.new('0')
    model.add(comp_B_jun)

    ## Bond from comp_B_jun to comp_B
    bgt.connect(comp_B_jun,comp_B)

    ### Ce:C

    ## Component Ce:comp_C
    K_C =  sp.symbols('K_C')
    RT = sp.symbols('RT')
    comp_C = bgt.new('Ce',name='C',value={'k':K_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_C)

    ## Junction 0:comp_C_jun
    comp_C_jun = bgt.new('0')
    model.add(comp_C_jun)

    ## Bond from comp_C_jun to comp_C
    bgt.connect(comp_C_jun,comp_C)

    ### Ce:E

    ## Component Ce:comp_E
    K_E =  sp.symbols('K_E')
    RT = sp.symbols('RT')
    comp_E = bgt.new('Ce',name='E',value={'k':K_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_E)

    ## Junction 0:comp_E_jun
    comp_E_jun = bgt.new('0')
    model.add(comp_E_jun)

    ## Bond from comp_E_jun to comp_E
    bgt.connect(comp_E_jun,comp_E)

    ### Ce:E0

    ## Component Ce:comp_E0
    K_E0 =  sp.symbols('K_E0')
    RT = sp.symbols('RT')
    comp_E0 = bgt.new('Ce',name='E0',value={'k':K_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_E0)

    ## Junction 0:comp_E0_jun
    comp_E0_jun = bgt.new('0')
    model.add(comp_E0_jun)

    ## Bond from comp_E0_jun to comp_E0
    bgt.connect(comp_E0_jun,comp_E0)

    ### Ce:F

    ## Component Ce:comp_F
    K_F =  sp.symbols('K_F')
    RT = sp.symbols('RT')
    comp_F = bgt.new('Ce',name='F',value={'k':K_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_F)

    ## Junction 0:comp_F_jun
    comp_F_jun = bgt.new('0')
    model.add(comp_F_jun)

    ## Bond from comp_F_jun to comp_F
    bgt.connect(comp_F_jun,comp_F)

    ### Ce:G

    ## Component Ce:comp_G
    K_G =  sp.symbols('K_G')
    RT = sp.symbols('RT')
    comp_G = bgt.new('Ce',name='G',value={'k':K_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_G)

    ## Junction 0:comp_G_jun
    comp_G_jun = bgt.new('0')
    model.add(comp_G_jun)

    ## Bond from comp_G_jun to comp_G
    bgt.connect(comp_G_jun,comp_G)

    ### Ce:Inh

    ## Component Ce:comp_Inh
    K_Inh =  sp.symbols('K_Inh')
    RT = sp.symbols('RT')
    comp_Inh = bgt.new('Ce',name='Inh',value={'k':K_Inh,'R':RT,'T':1},library='BioChem')
    model.add(comp_Inh)

    ## Junction 0:comp_Inh_jun
    comp_Inh_jun = bgt.new('0')
    model.add(comp_Inh_jun)

    ## Bond from comp_Inh_jun to comp_Inh
    bgt.connect(comp_Inh_jun,comp_Inh)
    ### Reactions

    ### Re:r0

    ## Component Re:comp_r0
    kappa_r0 =  sp.symbols('kappa_r0')
    RT = sp.symbols('RT')
    comp_r0 = bgt.new('Re',name='r0',value={'r':kappa_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_r0)

    ## Junction 1:comp_r0_junF
    comp_r0_junF = bgt.new('1')
    model.add(comp_r0_junF)

    ## Bond from comp_r0_junF to (comp_r0,0)
    bgt.connect(comp_r0_junF,(comp_r0,0))

    ## Junction 1:comp_r0_junR
    comp_r0_junR = bgt.new('1')
    model.add(comp_r0_junR)

    ## Bond from (comp_r0,1) to comp_r0_junR
    bgt.connect((comp_r0,1),comp_r0_junR)

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
    ### Connections

    ### Ce:A to Re:r1

    ## Bond from comp_A_jun to comp_r1_junF
    bgt.connect(comp_A_jun,comp_r1_junF)

    ### Ce:C to Re:r2

    ## Bond from comp_C_jun to comp_r2_junF
    bgt.connect(comp_C_jun,comp_r2_junF)

    ### Ce:E to Re:r0

    ## Bond from comp_E_jun to comp_r0_junF
    bgt.connect(comp_E_jun,comp_r0_junF)

    ### Ce:E to Re:r1

    ## Bond from comp_E_jun to comp_r1_junF
    bgt.connect(comp_E_jun,comp_r1_junF)

    ### Ce:F to Re:r1

    ## Bond from comp_F_jun to comp_r1_junF
    bgt.connect(comp_F_jun,comp_r1_junF)

    ### Ce:Inh to Re:r0

    ## Bond from comp_Inh_jun to comp_r0_junF
    bgt.connect(comp_Inh_jun,comp_r0_junF)

    ### Re:r0 to Ce:Act

    ## Bond from comp_r0_junR to comp_Act_jun
    bgt.connect(comp_r0_junR,comp_Act_jun)

    ### Re:r2 to Ce:B

    ## Bond from comp_r2_junR to comp_B_jun
    bgt.connect(comp_r2_junR,comp_B_jun)

    ### Re:r1 to Ce:C

    ## Bond from comp_r1_junR to comp_C_jun
    bgt.connect(comp_r1_junR,comp_C_jun)

    ### Re:r2 to Ce:E

    ## Bond from comp_r2_junR to comp_E_jun
    bgt.connect(comp_r2_junR,comp_E_jun)

    ### Re:r0 to Ce:E0

    ## Bond from comp_r0_junR to comp_E0_jun
    bgt.connect(comp_r0_junR,comp_E0_jun)

    ### Re:r2 to Ce:G

    ## Bond from comp_r2_junR to comp_G_jun
    bgt.connect(comp_r2_junR,comp_G_jun)

    return model
