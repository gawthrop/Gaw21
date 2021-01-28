import BondGraphTools as bgt
import sympy as sp

def model():
    """ Acausal bond graph ECR.py
    Created by stoichBondGraph at Wed Jan 27 12:34:24 2021

    Usage:
    import ECR; model = ECR.model()
    """

    model = bgt.new(name="ECR")
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

    ### Ce:ecr_C

    ## Component Ce:comp_ecr_C
    K_ecr_C =  sp.symbols('K_ecr_C')
    RT = sp.symbols('RT')
    comp_ecr_C = bgt.new('Ce',name='ecr_C',value={'k':K_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_ecr_C)

    ## Junction 0:comp_ecr_C_jun
    comp_ecr_C_jun = bgt.new('0')
    model.add(comp_ecr_C_jun)

    ## Bond from comp_ecr_C_jun to comp_ecr_C
    bgt.connect(comp_ecr_C_jun,comp_ecr_C)

    ### Ce:ecr_E

    ## Component Ce:comp_ecr_E
    K_ecr_E =  sp.symbols('K_ecr_E')
    RT = sp.symbols('RT')
    comp_ecr_E = bgt.new('Ce',name='ecr_E',value={'k':K_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_ecr_E)

    ## Junction 0:comp_ecr_E_jun
    comp_ecr_E_jun = bgt.new('0')
    model.add(comp_ecr_E_jun)

    ## Bond from comp_ecr_E_jun to comp_ecr_E
    bgt.connect(comp_ecr_E_jun,comp_ecr_E)

    ### Ce:ecr_E0

    ## Component Ce:comp_ecr_E0
    K_ecr_E0 =  sp.symbols('K_ecr_E0')
    RT = sp.symbols('RT')
    comp_ecr_E0 = bgt.new('Ce',name='ecr_E0',value={'k':K_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_ecr_E0)

    ## Junction 0:comp_ecr_E0_jun
    comp_ecr_E0_jun = bgt.new('0')
    model.add(comp_ecr_E0_jun)

    ## Bond from comp_ecr_E0_jun to comp_ecr_E0
    bgt.connect(comp_ecr_E0_jun,comp_ecr_E0)

    ### Ce:ecr_F

    ## Component Ce:comp_ecr_F
    K_ecr_F =  sp.symbols('K_ecr_F')
    RT = sp.symbols('RT')
    comp_ecr_F = bgt.new('Ce',name='ecr_F',value={'k':K_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_ecr_F)

    ## Junction 0:comp_ecr_F_jun
    comp_ecr_F_jun = bgt.new('0')
    model.add(comp_ecr_F_jun)

    ## Bond from comp_ecr_F_jun to comp_ecr_F
    bgt.connect(comp_ecr_F_jun,comp_ecr_F)

    ### Ce:ecr_G

    ## Component Ce:comp_ecr_G
    K_ecr_G =  sp.symbols('K_ecr_G')
    RT = sp.symbols('RT')
    comp_ecr_G = bgt.new('Ce',name='ecr_G',value={'k':K_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_ecr_G)

    ## Junction 0:comp_ecr_G_jun
    comp_ecr_G_jun = bgt.new('0')
    model.add(comp_ecr_G_jun)

    ## Bond from comp_ecr_G_jun to comp_ecr_G
    bgt.connect(comp_ecr_G_jun,comp_ecr_G)
    ### Reactions

    ### Re:ecr_r0

    ## Component Re:comp_ecr_r0
    kappa_ecr_r0 =  sp.symbols('kappa_ecr_r0')
    RT = sp.symbols('RT')
    comp_ecr_r0 = bgt.new('Re',name='ecr_r0',value={'r':kappa_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_ecr_r0)

    ## Junction 1:comp_ecr_r0_junF
    comp_ecr_r0_junF = bgt.new('1')
    model.add(comp_ecr_r0_junF)

    ## Bond from comp_ecr_r0_junF to (comp_ecr_r0,0)
    bgt.connect(comp_ecr_r0_junF,(comp_ecr_r0,0))

    ## Junction 1:comp_ecr_r0_junR
    comp_ecr_r0_junR = bgt.new('1')
    model.add(comp_ecr_r0_junR)

    ## Bond from (comp_ecr_r0,1) to comp_ecr_r0_junR
    bgt.connect((comp_ecr_r0,1),comp_ecr_r0_junR)

    ### Re:ecr_r1

    ## Component Re:comp_ecr_r1
    kappa_ecr_r1 =  sp.symbols('kappa_ecr_r1')
    RT = sp.symbols('RT')
    comp_ecr_r1 = bgt.new('Re',name='ecr_r1',value={'r':kappa_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_ecr_r1)

    ## Junction 1:comp_ecr_r1_junF
    comp_ecr_r1_junF = bgt.new('1')
    model.add(comp_ecr_r1_junF)

    ## Bond from comp_ecr_r1_junF to (comp_ecr_r1,0)
    bgt.connect(comp_ecr_r1_junF,(comp_ecr_r1,0))

    ## Junction 1:comp_ecr_r1_junR
    comp_ecr_r1_junR = bgt.new('1')
    model.add(comp_ecr_r1_junR)

    ## Bond from (comp_ecr_r1,1) to comp_ecr_r1_junR
    bgt.connect((comp_ecr_r1,1),comp_ecr_r1_junR)

    ### Re:ecr_r2

    ## Component Re:comp_ecr_r2
    kappa_ecr_r2 =  sp.symbols('kappa_ecr_r2')
    RT = sp.symbols('RT')
    comp_ecr_r2 = bgt.new('Re',name='ecr_r2',value={'r':kappa_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_ecr_r2)

    ## Junction 1:comp_ecr_r2_junF
    comp_ecr_r2_junF = bgt.new('1')
    model.add(comp_ecr_r2_junF)

    ## Bond from comp_ecr_r2_junF to (comp_ecr_r2,0)
    bgt.connect(comp_ecr_r2_junF,(comp_ecr_r2,0))

    ## Junction 1:comp_ecr_r2_junR
    comp_ecr_r2_junR = bgt.new('1')
    model.add(comp_ecr_r2_junR)

    ## Bond from (comp_ecr_r2,1) to comp_ecr_r2_junR
    bgt.connect((comp_ecr_r2,1),comp_ecr_r2_junR)
    ### Connections

    ### Ce:A to Re:ecr_r1

    ## Bond from comp_A_jun to comp_ecr_r1_junF
    bgt.connect(comp_A_jun,comp_ecr_r1_junF)

    ### Ce:Inh to Re:ecr_r0

    ## Bond from comp_Inh_jun to comp_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_ecr_r0_junF)

    ### Ce:Inh to Re:ecr_r0

    ## Bond from comp_Inh_jun to comp_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_ecr_r0_junF)

    ### Ce:Inh to Re:ecr_r0

    ## Bond from comp_Inh_jun to comp_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_ecr_r0_junF)

    ### Ce:Inh to Re:ecr_r0

    ## Bond from comp_Inh_jun to comp_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_ecr_r0_junF)

    ### Ce:ecr_C to Re:ecr_r2

    ## Bond from comp_ecr_C_jun to comp_ecr_r2_junF
    bgt.connect(comp_ecr_C_jun,comp_ecr_r2_junF)

    ### Ce:ecr_E to Re:ecr_r0

    ## Bond from comp_ecr_E_jun to comp_ecr_r0_junF
    bgt.connect(comp_ecr_E_jun,comp_ecr_r0_junF)

    ### Ce:ecr_E to Re:ecr_r1

    ## Bond from comp_ecr_E_jun to comp_ecr_r1_junF
    bgt.connect(comp_ecr_E_jun,comp_ecr_r1_junF)

    ### Ce:ecr_F to Re:ecr_r1

    ## Bond from comp_ecr_F_jun to comp_ecr_r1_junF
    bgt.connect(comp_ecr_F_jun,comp_ecr_r1_junF)

    ### Re:ecr_r0 to Ce:Act

    ## Bond from comp_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_ecr_r0_junR,comp_Act_jun)

    ### Re:ecr_r0 to Ce:Act

    ## Bond from comp_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_ecr_r0_junR,comp_Act_jun)

    ### Re:ecr_r0 to Ce:Act

    ## Bond from comp_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_ecr_r0_junR,comp_Act_jun)

    ### Re:ecr_r0 to Ce:Act

    ## Bond from comp_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_ecr_r0_junR,comp_Act_jun)

    ### Re:ecr_r2 to Ce:B

    ## Bond from comp_ecr_r2_junR to comp_B_jun
    bgt.connect(comp_ecr_r2_junR,comp_B_jun)

    ### Re:ecr_r1 to Ce:ecr_C

    ## Bond from comp_ecr_r1_junR to comp_ecr_C_jun
    bgt.connect(comp_ecr_r1_junR,comp_ecr_C_jun)

    ### Re:ecr_r2 to Ce:ecr_E

    ## Bond from comp_ecr_r2_junR to comp_ecr_E_jun
    bgt.connect(comp_ecr_r2_junR,comp_ecr_E_jun)

    ### Re:ecr_r0 to Ce:ecr_E0

    ## Bond from comp_ecr_r0_junR to comp_ecr_E0_jun
    bgt.connect(comp_ecr_r0_junR,comp_ecr_E0_jun)

    ### Re:ecr_r2 to Ce:ecr_G

    ## Bond from comp_ecr_r2_junR to comp_ecr_G_jun
    bgt.connect(comp_ecr_r2_junR,comp_ecr_G_jun)

    return model
