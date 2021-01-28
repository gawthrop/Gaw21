import BondGraphTools as bgt
import sympy as sp

def model():
    """ Acausal bond graph CFM.py
    Created by stoichBondGraph at Wed Jan 27 12:34:40 2021

    Usage:
    import CFM; model = CFM.model()
    """

    model = bgt.new(name="CFM")
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

    ### Ce:Fwd_ecr_C

    ## Component Ce:comp_Fwd_ecr_C
    K_Fwd_ecr_C =  sp.symbols('K_Fwd_ecr_C')
    RT = sp.symbols('RT')
    comp_Fwd_ecr_C = bgt.new('Ce',name='Fwd_ecr_C',value={'k':K_Fwd_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_Fwd_ecr_C)

    ## Junction 0:comp_Fwd_ecr_C_jun
    comp_Fwd_ecr_C_jun = bgt.new('0')
    model.add(comp_Fwd_ecr_C_jun)

    ## Bond from comp_Fwd_ecr_C_jun to comp_Fwd_ecr_C
    bgt.connect(comp_Fwd_ecr_C_jun,comp_Fwd_ecr_C)

    ### Ce:Fwd_ecr_E

    ## Component Ce:comp_Fwd_ecr_E
    K_Fwd_ecr_E =  sp.symbols('K_Fwd_ecr_E')
    RT = sp.symbols('RT')
    comp_Fwd_ecr_E = bgt.new('Ce',name='Fwd_ecr_E',value={'k':K_Fwd_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_Fwd_ecr_E)

    ## Junction 0:comp_Fwd_ecr_E_jun
    comp_Fwd_ecr_E_jun = bgt.new('0')
    model.add(comp_Fwd_ecr_E_jun)

    ## Bond from comp_Fwd_ecr_E_jun to comp_Fwd_ecr_E
    bgt.connect(comp_Fwd_ecr_E_jun,comp_Fwd_ecr_E)

    ### Ce:Fwd_ecr_E0

    ## Component Ce:comp_Fwd_ecr_E0
    K_Fwd_ecr_E0 =  sp.symbols('K_Fwd_ecr_E0')
    RT = sp.symbols('RT')
    comp_Fwd_ecr_E0 = bgt.new('Ce',name='Fwd_ecr_E0',value={'k':K_Fwd_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_Fwd_ecr_E0)

    ## Junction 0:comp_Fwd_ecr_E0_jun
    comp_Fwd_ecr_E0_jun = bgt.new('0')
    model.add(comp_Fwd_ecr_E0_jun)

    ## Bond from comp_Fwd_ecr_E0_jun to comp_Fwd_ecr_E0
    bgt.connect(comp_Fwd_ecr_E0_jun,comp_Fwd_ecr_E0)

    ### Ce:Fwd_ecr_F

    ## Component Ce:comp_Fwd_ecr_F
    K_Fwd_ecr_F =  sp.symbols('K_Fwd_ecr_F')
    RT = sp.symbols('RT')
    comp_Fwd_ecr_F = bgt.new('Ce',name='Fwd_ecr_F',value={'k':K_Fwd_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_Fwd_ecr_F)

    ## Junction 0:comp_Fwd_ecr_F_jun
    comp_Fwd_ecr_F_jun = bgt.new('0')
    model.add(comp_Fwd_ecr_F_jun)

    ## Bond from comp_Fwd_ecr_F_jun to comp_Fwd_ecr_F
    bgt.connect(comp_Fwd_ecr_F_jun,comp_Fwd_ecr_F)

    ### Ce:Fwd_ecr_G

    ## Component Ce:comp_Fwd_ecr_G
    K_Fwd_ecr_G =  sp.symbols('K_Fwd_ecr_G')
    RT = sp.symbols('RT')
    comp_Fwd_ecr_G = bgt.new('Ce',name='Fwd_ecr_G',value={'k':K_Fwd_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_Fwd_ecr_G)

    ## Junction 0:comp_Fwd_ecr_G_jun
    comp_Fwd_ecr_G_jun = bgt.new('0')
    model.add(comp_Fwd_ecr_G_jun)

    ## Bond from comp_Fwd_ecr_G_jun to comp_Fwd_ecr_G
    bgt.connect(comp_Fwd_ecr_G_jun,comp_Fwd_ecr_G)

    ### Ce:Rev_ecr_C

    ## Component Ce:comp_Rev_ecr_C
    K_Rev_ecr_C =  sp.symbols('K_Rev_ecr_C')
    RT = sp.symbols('RT')
    comp_Rev_ecr_C = bgt.new('Ce',name='Rev_ecr_C',value={'k':K_Rev_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_Rev_ecr_C)

    ## Junction 0:comp_Rev_ecr_C_jun
    comp_Rev_ecr_C_jun = bgt.new('0')
    model.add(comp_Rev_ecr_C_jun)

    ## Bond from comp_Rev_ecr_C_jun to comp_Rev_ecr_C
    bgt.connect(comp_Rev_ecr_C_jun,comp_Rev_ecr_C)

    ### Ce:Rev_ecr_E

    ## Component Ce:comp_Rev_ecr_E
    K_Rev_ecr_E =  sp.symbols('K_Rev_ecr_E')
    RT = sp.symbols('RT')
    comp_Rev_ecr_E = bgt.new('Ce',name='Rev_ecr_E',value={'k':K_Rev_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_Rev_ecr_E)

    ## Junction 0:comp_Rev_ecr_E_jun
    comp_Rev_ecr_E_jun = bgt.new('0')
    model.add(comp_Rev_ecr_E_jun)

    ## Bond from comp_Rev_ecr_E_jun to comp_Rev_ecr_E
    bgt.connect(comp_Rev_ecr_E_jun,comp_Rev_ecr_E)

    ### Ce:Rev_ecr_E0

    ## Component Ce:comp_Rev_ecr_E0
    K_Rev_ecr_E0 =  sp.symbols('K_Rev_ecr_E0')
    RT = sp.symbols('RT')
    comp_Rev_ecr_E0 = bgt.new('Ce',name='Rev_ecr_E0',value={'k':K_Rev_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_Rev_ecr_E0)

    ## Junction 0:comp_Rev_ecr_E0_jun
    comp_Rev_ecr_E0_jun = bgt.new('0')
    model.add(comp_Rev_ecr_E0_jun)

    ## Bond from comp_Rev_ecr_E0_jun to comp_Rev_ecr_E0
    bgt.connect(comp_Rev_ecr_E0_jun,comp_Rev_ecr_E0)

    ### Ce:Rev_ecr_F

    ## Component Ce:comp_Rev_ecr_F
    K_Rev_ecr_F =  sp.symbols('K_Rev_ecr_F')
    RT = sp.symbols('RT')
    comp_Rev_ecr_F = bgt.new('Ce',name='Rev_ecr_F',value={'k':K_Rev_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_Rev_ecr_F)

    ## Junction 0:comp_Rev_ecr_F_jun
    comp_Rev_ecr_F_jun = bgt.new('0')
    model.add(comp_Rev_ecr_F_jun)

    ## Bond from comp_Rev_ecr_F_jun to comp_Rev_ecr_F
    bgt.connect(comp_Rev_ecr_F_jun,comp_Rev_ecr_F)

    ### Ce:Rev_ecr_G

    ## Component Ce:comp_Rev_ecr_G
    K_Rev_ecr_G =  sp.symbols('K_Rev_ecr_G')
    RT = sp.symbols('RT')
    comp_Rev_ecr_G = bgt.new('Ce',name='Rev_ecr_G',value={'k':K_Rev_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_Rev_ecr_G)

    ## Junction 0:comp_Rev_ecr_G_jun
    comp_Rev_ecr_G_jun = bgt.new('0')
    model.add(comp_Rev_ecr_G_jun)

    ## Bond from comp_Rev_ecr_G_jun to comp_Rev_ecr_G
    bgt.connect(comp_Rev_ecr_G_jun,comp_Rev_ecr_G)
    ### Reactions

    ### Re:Fwd_ecr_r0

    ## Component Re:comp_Fwd_ecr_r0
    kappa_Fwd_ecr_r0 =  sp.symbols('kappa_Fwd_ecr_r0')
    RT = sp.symbols('RT')
    comp_Fwd_ecr_r0 = bgt.new('Re',name='Fwd_ecr_r0',value={'r':kappa_Fwd_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_Fwd_ecr_r0)

    ## Junction 1:comp_Fwd_ecr_r0_junF
    comp_Fwd_ecr_r0_junF = bgt.new('1')
    model.add(comp_Fwd_ecr_r0_junF)

    ## Bond from comp_Fwd_ecr_r0_junF to (comp_Fwd_ecr_r0,0)
    bgt.connect(comp_Fwd_ecr_r0_junF,(comp_Fwd_ecr_r0,0))

    ## Junction 1:comp_Fwd_ecr_r0_junR
    comp_Fwd_ecr_r0_junR = bgt.new('1')
    model.add(comp_Fwd_ecr_r0_junR)

    ## Bond from (comp_Fwd_ecr_r0,1) to comp_Fwd_ecr_r0_junR
    bgt.connect((comp_Fwd_ecr_r0,1),comp_Fwd_ecr_r0_junR)

    ### Re:Fwd_ecr_r1

    ## Component Re:comp_Fwd_ecr_r1
    kappa_Fwd_ecr_r1 =  sp.symbols('kappa_Fwd_ecr_r1')
    RT = sp.symbols('RT')
    comp_Fwd_ecr_r1 = bgt.new('Re',name='Fwd_ecr_r1',value={'r':kappa_Fwd_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_Fwd_ecr_r1)

    ## Junction 1:comp_Fwd_ecr_r1_junF
    comp_Fwd_ecr_r1_junF = bgt.new('1')
    model.add(comp_Fwd_ecr_r1_junF)

    ## Bond from comp_Fwd_ecr_r1_junF to (comp_Fwd_ecr_r1,0)
    bgt.connect(comp_Fwd_ecr_r1_junF,(comp_Fwd_ecr_r1,0))

    ## Junction 1:comp_Fwd_ecr_r1_junR
    comp_Fwd_ecr_r1_junR = bgt.new('1')
    model.add(comp_Fwd_ecr_r1_junR)

    ## Bond from (comp_Fwd_ecr_r1,1) to comp_Fwd_ecr_r1_junR
    bgt.connect((comp_Fwd_ecr_r1,1),comp_Fwd_ecr_r1_junR)

    ### Re:Fwd_ecr_r2

    ## Component Re:comp_Fwd_ecr_r2
    kappa_Fwd_ecr_r2 =  sp.symbols('kappa_Fwd_ecr_r2')
    RT = sp.symbols('RT')
    comp_Fwd_ecr_r2 = bgt.new('Re',name='Fwd_ecr_r2',value={'r':kappa_Fwd_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_Fwd_ecr_r2)

    ## Junction 1:comp_Fwd_ecr_r2_junF
    comp_Fwd_ecr_r2_junF = bgt.new('1')
    model.add(comp_Fwd_ecr_r2_junF)

    ## Bond from comp_Fwd_ecr_r2_junF to (comp_Fwd_ecr_r2,0)
    bgt.connect(comp_Fwd_ecr_r2_junF,(comp_Fwd_ecr_r2,0))

    ## Junction 1:comp_Fwd_ecr_r2_junR
    comp_Fwd_ecr_r2_junR = bgt.new('1')
    model.add(comp_Fwd_ecr_r2_junR)

    ## Bond from (comp_Fwd_ecr_r2,1) to comp_Fwd_ecr_r2_junR
    bgt.connect((comp_Fwd_ecr_r2,1),comp_Fwd_ecr_r2_junR)

    ### Re:Rev_ecr_r0

    ## Component Re:comp_Rev_ecr_r0
    kappa_Rev_ecr_r0 =  sp.symbols('kappa_Rev_ecr_r0')
    RT = sp.symbols('RT')
    comp_Rev_ecr_r0 = bgt.new('Re',name='Rev_ecr_r0',value={'r':kappa_Rev_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_Rev_ecr_r0)

    ## Junction 1:comp_Rev_ecr_r0_junF
    comp_Rev_ecr_r0_junF = bgt.new('1')
    model.add(comp_Rev_ecr_r0_junF)

    ## Bond from comp_Rev_ecr_r0_junF to (comp_Rev_ecr_r0,0)
    bgt.connect(comp_Rev_ecr_r0_junF,(comp_Rev_ecr_r0,0))

    ## Junction 1:comp_Rev_ecr_r0_junR
    comp_Rev_ecr_r0_junR = bgt.new('1')
    model.add(comp_Rev_ecr_r0_junR)

    ## Bond from (comp_Rev_ecr_r0,1) to comp_Rev_ecr_r0_junR
    bgt.connect((comp_Rev_ecr_r0,1),comp_Rev_ecr_r0_junR)

    ### Re:Rev_ecr_r1

    ## Component Re:comp_Rev_ecr_r1
    kappa_Rev_ecr_r1 =  sp.symbols('kappa_Rev_ecr_r1')
    RT = sp.symbols('RT')
    comp_Rev_ecr_r1 = bgt.new('Re',name='Rev_ecr_r1',value={'r':kappa_Rev_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_Rev_ecr_r1)

    ## Junction 1:comp_Rev_ecr_r1_junF
    comp_Rev_ecr_r1_junF = bgt.new('1')
    model.add(comp_Rev_ecr_r1_junF)

    ## Bond from comp_Rev_ecr_r1_junF to (comp_Rev_ecr_r1,0)
    bgt.connect(comp_Rev_ecr_r1_junF,(comp_Rev_ecr_r1,0))

    ## Junction 1:comp_Rev_ecr_r1_junR
    comp_Rev_ecr_r1_junR = bgt.new('1')
    model.add(comp_Rev_ecr_r1_junR)

    ## Bond from (comp_Rev_ecr_r1,1) to comp_Rev_ecr_r1_junR
    bgt.connect((comp_Rev_ecr_r1,1),comp_Rev_ecr_r1_junR)

    ### Re:Rev_ecr_r2

    ## Component Re:comp_Rev_ecr_r2
    kappa_Rev_ecr_r2 =  sp.symbols('kappa_Rev_ecr_r2')
    RT = sp.symbols('RT')
    comp_Rev_ecr_r2 = bgt.new('Re',name='Rev_ecr_r2',value={'r':kappa_Rev_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_Rev_ecr_r2)

    ## Junction 1:comp_Rev_ecr_r2_junF
    comp_Rev_ecr_r2_junF = bgt.new('1')
    model.add(comp_Rev_ecr_r2_junF)

    ## Bond from comp_Rev_ecr_r2_junF to (comp_Rev_ecr_r2,0)
    bgt.connect(comp_Rev_ecr_r2_junF,(comp_Rev_ecr_r2,0))

    ## Junction 1:comp_Rev_ecr_r2_junR
    comp_Rev_ecr_r2_junR = bgt.new('1')
    model.add(comp_Rev_ecr_r2_junR)

    ## Bond from (comp_Rev_ecr_r2,1) to comp_Rev_ecr_r2_junR
    bgt.connect((comp_Rev_ecr_r2,1),comp_Rev_ecr_r2_junR)
    ### Connections

    ### Ce:A to Re:Fwd_ecr_r1

    ## Bond from comp_A_jun to comp_Fwd_ecr_r1_junF
    bgt.connect(comp_A_jun,comp_Fwd_ecr_r1_junF)

    ### Ce:Act to Re:Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_Rev_ecr_r0_junF)

    ### Ce:Act to Re:Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_Rev_ecr_r0_junF)

    ### Ce:Act to Re:Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_Rev_ecr_r0_junF)

    ### Ce:Act to Re:Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_Rev_ecr_r0_junF)

    ### Ce:B to Re:Rev_ecr_r1

    ## Bond from comp_B_jun to comp_Rev_ecr_r1_junF
    bgt.connect(comp_B_jun,comp_Rev_ecr_r1_junF)

    ### Ce:Inh to Re:Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_Fwd_ecr_r0_junF)

    ### Ce:Fwd_ecr_C to Re:Fwd_ecr_r2

    ## Bond from comp_Fwd_ecr_C_jun to comp_Fwd_ecr_r2_junF
    bgt.connect(comp_Fwd_ecr_C_jun,comp_Fwd_ecr_r2_junF)

    ### Ce:Fwd_ecr_E to Re:Fwd_ecr_r0

    ## Bond from comp_Fwd_ecr_E_jun to comp_Fwd_ecr_r0_junF
    bgt.connect(comp_Fwd_ecr_E_jun,comp_Fwd_ecr_r0_junF)

    ### Ce:Fwd_ecr_E to Re:Fwd_ecr_r1

    ## Bond from comp_Fwd_ecr_E_jun to comp_Fwd_ecr_r1_junF
    bgt.connect(comp_Fwd_ecr_E_jun,comp_Fwd_ecr_r1_junF)

    ### Ce:Fwd_ecr_F to Re:Fwd_ecr_r1

    ## Bond from comp_Fwd_ecr_F_jun to comp_Fwd_ecr_r1_junF
    bgt.connect(comp_Fwd_ecr_F_jun,comp_Fwd_ecr_r1_junF)

    ### Ce:Rev_ecr_C to Re:Rev_ecr_r2

    ## Bond from comp_Rev_ecr_C_jun to comp_Rev_ecr_r2_junF
    bgt.connect(comp_Rev_ecr_C_jun,comp_Rev_ecr_r2_junF)

    ### Ce:Rev_ecr_E to Re:Rev_ecr_r0

    ## Bond from comp_Rev_ecr_E_jun to comp_Rev_ecr_r0_junF
    bgt.connect(comp_Rev_ecr_E_jun,comp_Rev_ecr_r0_junF)

    ### Ce:Rev_ecr_E to Re:Rev_ecr_r1

    ## Bond from comp_Rev_ecr_E_jun to comp_Rev_ecr_r1_junF
    bgt.connect(comp_Rev_ecr_E_jun,comp_Rev_ecr_r1_junF)

    ### Ce:Rev_ecr_F to Re:Rev_ecr_r1

    ## Bond from comp_Rev_ecr_F_jun to comp_Rev_ecr_r1_junF
    bgt.connect(comp_Rev_ecr_F_jun,comp_Rev_ecr_r1_junF)

    ### Re:Rev_ecr_r2 to Ce:A

    ## Bond from comp_Rev_ecr_r2_junR to comp_A_jun
    bgt.connect(comp_Rev_ecr_r2_junR,comp_A_jun)

    ### Re:Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:Fwd_ecr_r2 to Ce:B

    ## Bond from comp_Fwd_ecr_r2_junR to comp_B_jun
    bgt.connect(comp_Fwd_ecr_r2_junR,comp_B_jun)

    ### Re:Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:Fwd_ecr_r1 to Ce:Fwd_ecr_C

    ## Bond from comp_Fwd_ecr_r1_junR to comp_Fwd_ecr_C_jun
    bgt.connect(comp_Fwd_ecr_r1_junR,comp_Fwd_ecr_C_jun)

    ### Re:Fwd_ecr_r2 to Ce:Fwd_ecr_E

    ## Bond from comp_Fwd_ecr_r2_junR to comp_Fwd_ecr_E_jun
    bgt.connect(comp_Fwd_ecr_r2_junR,comp_Fwd_ecr_E_jun)

    ### Re:Fwd_ecr_r0 to Ce:Fwd_ecr_E0

    ## Bond from comp_Fwd_ecr_r0_junR to comp_Fwd_ecr_E0_jun
    bgt.connect(comp_Fwd_ecr_r0_junR,comp_Fwd_ecr_E0_jun)

    ### Re:Fwd_ecr_r2 to Ce:Fwd_ecr_G

    ## Bond from comp_Fwd_ecr_r2_junR to comp_Fwd_ecr_G_jun
    bgt.connect(comp_Fwd_ecr_r2_junR,comp_Fwd_ecr_G_jun)

    ### Re:Rev_ecr_r1 to Ce:Rev_ecr_C

    ## Bond from comp_Rev_ecr_r1_junR to comp_Rev_ecr_C_jun
    bgt.connect(comp_Rev_ecr_r1_junR,comp_Rev_ecr_C_jun)

    ### Re:Rev_ecr_r2 to Ce:Rev_ecr_E

    ## Bond from comp_Rev_ecr_r2_junR to comp_Rev_ecr_E_jun
    bgt.connect(comp_Rev_ecr_r2_junR,comp_Rev_ecr_E_jun)

    ### Re:Rev_ecr_r0 to Ce:Rev_ecr_E0

    ## Bond from comp_Rev_ecr_r0_junR to comp_Rev_ecr_E0_jun
    bgt.connect(comp_Rev_ecr_r0_junR,comp_Rev_ecr_E0_jun)

    ### Re:Rev_ecr_r2 to Ce:Rev_ecr_G

    ## Bond from comp_Rev_ecr_r2_junR to comp_Rev_ecr_G_jun
    bgt.connect(comp_Rev_ecr_r2_junR,comp_Rev_ecr_G_jun)

    return model
