import BondGraphTools as bgt
import sympy as sp

def model():
    """ Acausal bond graph PI.py
    Created by stoichBondGraph at Wed Jan 27 12:35:26 2021

    Usage:
    import PI; model = PI.model()
    """

    model = bgt.new(name="PI")
    ### Species

    ### Ce:I_Fwd_ecr_C

    ## Component Ce:comp_I_Fwd_ecr_C
    K_I_Fwd_ecr_C =  sp.symbols('K_I_Fwd_ecr_C')
    RT = sp.symbols('RT')
    comp_I_Fwd_ecr_C = bgt.new('Ce',name='I_Fwd_ecr_C',value={'k':K_I_Fwd_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Fwd_ecr_C)

    ## Junction 0:comp_I_Fwd_ecr_C_jun
    comp_I_Fwd_ecr_C_jun = bgt.new('0')
    model.add(comp_I_Fwd_ecr_C_jun)

    ## Bond from comp_I_Fwd_ecr_C_jun to comp_I_Fwd_ecr_C
    bgt.connect(comp_I_Fwd_ecr_C_jun,comp_I_Fwd_ecr_C)

    ### Ce:I_Fwd_ecr_E

    ## Component Ce:comp_I_Fwd_ecr_E
    K_I_Fwd_ecr_E =  sp.symbols('K_I_Fwd_ecr_E')
    RT = sp.symbols('RT')
    comp_I_Fwd_ecr_E = bgt.new('Ce',name='I_Fwd_ecr_E',value={'k':K_I_Fwd_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Fwd_ecr_E)

    ## Junction 0:comp_I_Fwd_ecr_E_jun
    comp_I_Fwd_ecr_E_jun = bgt.new('0')
    model.add(comp_I_Fwd_ecr_E_jun)

    ## Bond from comp_I_Fwd_ecr_E_jun to comp_I_Fwd_ecr_E
    bgt.connect(comp_I_Fwd_ecr_E_jun,comp_I_Fwd_ecr_E)

    ### Ce:I_Fwd_ecr_E0

    ## Component Ce:comp_I_Fwd_ecr_E0
    K_I_Fwd_ecr_E0 =  sp.symbols('K_I_Fwd_ecr_E0')
    RT = sp.symbols('RT')
    comp_I_Fwd_ecr_E0 = bgt.new('Ce',name='I_Fwd_ecr_E0',value={'k':K_I_Fwd_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Fwd_ecr_E0)

    ## Junction 0:comp_I_Fwd_ecr_E0_jun
    comp_I_Fwd_ecr_E0_jun = bgt.new('0')
    model.add(comp_I_Fwd_ecr_E0_jun)

    ## Bond from comp_I_Fwd_ecr_E0_jun to comp_I_Fwd_ecr_E0
    bgt.connect(comp_I_Fwd_ecr_E0_jun,comp_I_Fwd_ecr_E0)

    ### Ce:I_Fwd_ecr_F

    ## Component Ce:comp_I_Fwd_ecr_F
    K_I_Fwd_ecr_F =  sp.symbols('K_I_Fwd_ecr_F')
    RT = sp.symbols('RT')
    comp_I_Fwd_ecr_F = bgt.new('Ce',name='I_Fwd_ecr_F',value={'k':K_I_Fwd_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Fwd_ecr_F)

    ## Junction 0:comp_I_Fwd_ecr_F_jun
    comp_I_Fwd_ecr_F_jun = bgt.new('0')
    model.add(comp_I_Fwd_ecr_F_jun)

    ## Bond from comp_I_Fwd_ecr_F_jun to comp_I_Fwd_ecr_F
    bgt.connect(comp_I_Fwd_ecr_F_jun,comp_I_Fwd_ecr_F)

    ### Ce:I_Fwd_ecr_G

    ## Component Ce:comp_I_Fwd_ecr_G
    K_I_Fwd_ecr_G =  sp.symbols('K_I_Fwd_ecr_G')
    RT = sp.symbols('RT')
    comp_I_Fwd_ecr_G = bgt.new('Ce',name='I_Fwd_ecr_G',value={'k':K_I_Fwd_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Fwd_ecr_G)

    ## Junction 0:comp_I_Fwd_ecr_G_jun
    comp_I_Fwd_ecr_G_jun = bgt.new('0')
    model.add(comp_I_Fwd_ecr_G_jun)

    ## Bond from comp_I_Fwd_ecr_G_jun to comp_I_Fwd_ecr_G
    bgt.connect(comp_I_Fwd_ecr_G_jun,comp_I_Fwd_ecr_G)

    ### Ce:I_Rev_ecr_C

    ## Component Ce:comp_I_Rev_ecr_C
    K_I_Rev_ecr_C =  sp.symbols('K_I_Rev_ecr_C')
    RT = sp.symbols('RT')
    comp_I_Rev_ecr_C = bgt.new('Ce',name='I_Rev_ecr_C',value={'k':K_I_Rev_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Rev_ecr_C)

    ## Junction 0:comp_I_Rev_ecr_C_jun
    comp_I_Rev_ecr_C_jun = bgt.new('0')
    model.add(comp_I_Rev_ecr_C_jun)

    ## Bond from comp_I_Rev_ecr_C_jun to comp_I_Rev_ecr_C
    bgt.connect(comp_I_Rev_ecr_C_jun,comp_I_Rev_ecr_C)

    ### Ce:I_Rev_ecr_E

    ## Component Ce:comp_I_Rev_ecr_E
    K_I_Rev_ecr_E =  sp.symbols('K_I_Rev_ecr_E')
    RT = sp.symbols('RT')
    comp_I_Rev_ecr_E = bgt.new('Ce',name='I_Rev_ecr_E',value={'k':K_I_Rev_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Rev_ecr_E)

    ## Junction 0:comp_I_Rev_ecr_E_jun
    comp_I_Rev_ecr_E_jun = bgt.new('0')
    model.add(comp_I_Rev_ecr_E_jun)

    ## Bond from comp_I_Rev_ecr_E_jun to comp_I_Rev_ecr_E
    bgt.connect(comp_I_Rev_ecr_E_jun,comp_I_Rev_ecr_E)

    ### Ce:I_Rev_ecr_E0

    ## Component Ce:comp_I_Rev_ecr_E0
    K_I_Rev_ecr_E0 =  sp.symbols('K_I_Rev_ecr_E0')
    RT = sp.symbols('RT')
    comp_I_Rev_ecr_E0 = bgt.new('Ce',name='I_Rev_ecr_E0',value={'k':K_I_Rev_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Rev_ecr_E0)

    ## Junction 0:comp_I_Rev_ecr_E0_jun
    comp_I_Rev_ecr_E0_jun = bgt.new('0')
    model.add(comp_I_Rev_ecr_E0_jun)

    ## Bond from comp_I_Rev_ecr_E0_jun to comp_I_Rev_ecr_E0
    bgt.connect(comp_I_Rev_ecr_E0_jun,comp_I_Rev_ecr_E0)

    ### Ce:I_Rev_ecr_F

    ## Component Ce:comp_I_Rev_ecr_F
    K_I_Rev_ecr_F =  sp.symbols('K_I_Rev_ecr_F')
    RT = sp.symbols('RT')
    comp_I_Rev_ecr_F = bgt.new('Ce',name='I_Rev_ecr_F',value={'k':K_I_Rev_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Rev_ecr_F)

    ## Junction 0:comp_I_Rev_ecr_F_jun
    comp_I_Rev_ecr_F_jun = bgt.new('0')
    model.add(comp_I_Rev_ecr_F_jun)

    ## Bond from comp_I_Rev_ecr_F_jun to comp_I_Rev_ecr_F
    bgt.connect(comp_I_Rev_ecr_F_jun,comp_I_Rev_ecr_F)

    ### Ce:I_Rev_ecr_G

    ## Component Ce:comp_I_Rev_ecr_G
    K_I_Rev_ecr_G =  sp.symbols('K_I_Rev_ecr_G')
    RT = sp.symbols('RT')
    comp_I_Rev_ecr_G = bgt.new('Ce',name='I_Rev_ecr_G',value={'k':K_I_Rev_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Rev_ecr_G)

    ## Junction 0:comp_I_Rev_ecr_G_jun
    comp_I_Rev_ecr_G_jun = bgt.new('0')
    model.add(comp_I_Rev_ecr_G_jun)

    ## Bond from comp_I_Rev_ecr_G_jun to comp_I_Rev_ecr_G
    bgt.connect(comp_I_Rev_ecr_G_jun,comp_I_Rev_ecr_G)

    ### Ce:P_Fwd_ecr_C

    ## Component Ce:comp_P_Fwd_ecr_C
    K_P_Fwd_ecr_C =  sp.symbols('K_P_Fwd_ecr_C')
    RT = sp.symbols('RT')
    comp_P_Fwd_ecr_C = bgt.new('Ce',name='P_Fwd_ecr_C',value={'k':K_P_Fwd_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Fwd_ecr_C)

    ## Junction 0:comp_P_Fwd_ecr_C_jun
    comp_P_Fwd_ecr_C_jun = bgt.new('0')
    model.add(comp_P_Fwd_ecr_C_jun)

    ## Bond from comp_P_Fwd_ecr_C_jun to comp_P_Fwd_ecr_C
    bgt.connect(comp_P_Fwd_ecr_C_jun,comp_P_Fwd_ecr_C)

    ### Ce:P_Fwd_ecr_E

    ## Component Ce:comp_P_Fwd_ecr_E
    K_P_Fwd_ecr_E =  sp.symbols('K_P_Fwd_ecr_E')
    RT = sp.symbols('RT')
    comp_P_Fwd_ecr_E = bgt.new('Ce',name='P_Fwd_ecr_E',value={'k':K_P_Fwd_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Fwd_ecr_E)

    ## Junction 0:comp_P_Fwd_ecr_E_jun
    comp_P_Fwd_ecr_E_jun = bgt.new('0')
    model.add(comp_P_Fwd_ecr_E_jun)

    ## Bond from comp_P_Fwd_ecr_E_jun to comp_P_Fwd_ecr_E
    bgt.connect(comp_P_Fwd_ecr_E_jun,comp_P_Fwd_ecr_E)

    ### Ce:P_Fwd_ecr_E0

    ## Component Ce:comp_P_Fwd_ecr_E0
    K_P_Fwd_ecr_E0 =  sp.symbols('K_P_Fwd_ecr_E0')
    RT = sp.symbols('RT')
    comp_P_Fwd_ecr_E0 = bgt.new('Ce',name='P_Fwd_ecr_E0',value={'k':K_P_Fwd_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Fwd_ecr_E0)

    ## Junction 0:comp_P_Fwd_ecr_E0_jun
    comp_P_Fwd_ecr_E0_jun = bgt.new('0')
    model.add(comp_P_Fwd_ecr_E0_jun)

    ## Bond from comp_P_Fwd_ecr_E0_jun to comp_P_Fwd_ecr_E0
    bgt.connect(comp_P_Fwd_ecr_E0_jun,comp_P_Fwd_ecr_E0)

    ### Ce:P_Fwd_ecr_F

    ## Component Ce:comp_P_Fwd_ecr_F
    K_P_Fwd_ecr_F =  sp.symbols('K_P_Fwd_ecr_F')
    RT = sp.symbols('RT')
    comp_P_Fwd_ecr_F = bgt.new('Ce',name='P_Fwd_ecr_F',value={'k':K_P_Fwd_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Fwd_ecr_F)

    ## Junction 0:comp_P_Fwd_ecr_F_jun
    comp_P_Fwd_ecr_F_jun = bgt.new('0')
    model.add(comp_P_Fwd_ecr_F_jun)

    ## Bond from comp_P_Fwd_ecr_F_jun to comp_P_Fwd_ecr_F
    bgt.connect(comp_P_Fwd_ecr_F_jun,comp_P_Fwd_ecr_F)

    ### Ce:P_Fwd_ecr_G

    ## Component Ce:comp_P_Fwd_ecr_G
    K_P_Fwd_ecr_G =  sp.symbols('K_P_Fwd_ecr_G')
    RT = sp.symbols('RT')
    comp_P_Fwd_ecr_G = bgt.new('Ce',name='P_Fwd_ecr_G',value={'k':K_P_Fwd_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Fwd_ecr_G)

    ## Junction 0:comp_P_Fwd_ecr_G_jun
    comp_P_Fwd_ecr_G_jun = bgt.new('0')
    model.add(comp_P_Fwd_ecr_G_jun)

    ## Bond from comp_P_Fwd_ecr_G_jun to comp_P_Fwd_ecr_G
    bgt.connect(comp_P_Fwd_ecr_G_jun,comp_P_Fwd_ecr_G)

    ### Ce:P_Rev_ecr_C

    ## Component Ce:comp_P_Rev_ecr_C
    K_P_Rev_ecr_C =  sp.symbols('K_P_Rev_ecr_C')
    RT = sp.symbols('RT')
    comp_P_Rev_ecr_C = bgt.new('Ce',name='P_Rev_ecr_C',value={'k':K_P_Rev_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Rev_ecr_C)

    ## Junction 0:comp_P_Rev_ecr_C_jun
    comp_P_Rev_ecr_C_jun = bgt.new('0')
    model.add(comp_P_Rev_ecr_C_jun)

    ## Bond from comp_P_Rev_ecr_C_jun to comp_P_Rev_ecr_C
    bgt.connect(comp_P_Rev_ecr_C_jun,comp_P_Rev_ecr_C)

    ### Ce:P_Rev_ecr_E

    ## Component Ce:comp_P_Rev_ecr_E
    K_P_Rev_ecr_E =  sp.symbols('K_P_Rev_ecr_E')
    RT = sp.symbols('RT')
    comp_P_Rev_ecr_E = bgt.new('Ce',name='P_Rev_ecr_E',value={'k':K_P_Rev_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Rev_ecr_E)

    ## Junction 0:comp_P_Rev_ecr_E_jun
    comp_P_Rev_ecr_E_jun = bgt.new('0')
    model.add(comp_P_Rev_ecr_E_jun)

    ## Bond from comp_P_Rev_ecr_E_jun to comp_P_Rev_ecr_E
    bgt.connect(comp_P_Rev_ecr_E_jun,comp_P_Rev_ecr_E)

    ### Ce:P_Rev_ecr_E0

    ## Component Ce:comp_P_Rev_ecr_E0
    K_P_Rev_ecr_E0 =  sp.symbols('K_P_Rev_ecr_E0')
    RT = sp.symbols('RT')
    comp_P_Rev_ecr_E0 = bgt.new('Ce',name='P_Rev_ecr_E0',value={'k':K_P_Rev_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Rev_ecr_E0)

    ## Junction 0:comp_P_Rev_ecr_E0_jun
    comp_P_Rev_ecr_E0_jun = bgt.new('0')
    model.add(comp_P_Rev_ecr_E0_jun)

    ## Bond from comp_P_Rev_ecr_E0_jun to comp_P_Rev_ecr_E0
    bgt.connect(comp_P_Rev_ecr_E0_jun,comp_P_Rev_ecr_E0)

    ### Ce:P_Rev_ecr_F

    ## Component Ce:comp_P_Rev_ecr_F
    K_P_Rev_ecr_F =  sp.symbols('K_P_Rev_ecr_F')
    RT = sp.symbols('RT')
    comp_P_Rev_ecr_F = bgt.new('Ce',name='P_Rev_ecr_F',value={'k':K_P_Rev_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Rev_ecr_F)

    ## Junction 0:comp_P_Rev_ecr_F_jun
    comp_P_Rev_ecr_F_jun = bgt.new('0')
    model.add(comp_P_Rev_ecr_F_jun)

    ## Bond from comp_P_Rev_ecr_F_jun to comp_P_Rev_ecr_F
    bgt.connect(comp_P_Rev_ecr_F_jun,comp_P_Rev_ecr_F)

    ### Ce:P_Rev_ecr_G

    ## Component Ce:comp_P_Rev_ecr_G
    K_P_Rev_ecr_G =  sp.symbols('K_P_Rev_ecr_G')
    RT = sp.symbols('RT')
    comp_P_Rev_ecr_G = bgt.new('Ce',name='P_Rev_ecr_G',value={'k':K_P_Rev_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Rev_ecr_G)

    ## Junction 0:comp_P_Rev_ecr_G_jun
    comp_P_Rev_ecr_G_jun = bgt.new('0')
    model.add(comp_P_Rev_ecr_G_jun)

    ## Bond from comp_P_Rev_ecr_G_jun to comp_P_Rev_ecr_G
    bgt.connect(comp_P_Rev_ecr_G_jun,comp_P_Rev_ecr_G)

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

    ### Ce:Int

    ## Component Ce:comp_Int
    K_Int =  sp.symbols('K_Int')
    RT = sp.symbols('RT')
    comp_Int = bgt.new('Ce',name='Int',value={'k':K_Int,'R':RT,'T':1},library='BioChem')
    model.add(comp_Int)

    ## Junction 0:comp_Int_jun
    comp_Int_jun = bgt.new('0')
    model.add(comp_Int_jun)

    ## Bond from comp_Int_jun to comp_Int
    bgt.connect(comp_Int_jun,comp_Int)
    ### Reactions

    ### Re:I_Fwd_ecr_r0

    ## Component Re:comp_I_Fwd_ecr_r0
    kappa_I_Fwd_ecr_r0 =  sp.symbols('kappa_I_Fwd_ecr_r0')
    RT = sp.symbols('RT')
    comp_I_Fwd_ecr_r0 = bgt.new('Re',name='I_Fwd_ecr_r0',value={'r':kappa_I_Fwd_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Fwd_ecr_r0)

    ## Junction 1:comp_I_Fwd_ecr_r0_junF
    comp_I_Fwd_ecr_r0_junF = bgt.new('1')
    model.add(comp_I_Fwd_ecr_r0_junF)

    ## Bond from comp_I_Fwd_ecr_r0_junF to (comp_I_Fwd_ecr_r0,0)
    bgt.connect(comp_I_Fwd_ecr_r0_junF,(comp_I_Fwd_ecr_r0,0))

    ## Junction 1:comp_I_Fwd_ecr_r0_junR
    comp_I_Fwd_ecr_r0_junR = bgt.new('1')
    model.add(comp_I_Fwd_ecr_r0_junR)

    ## Bond from (comp_I_Fwd_ecr_r0,1) to comp_I_Fwd_ecr_r0_junR
    bgt.connect((comp_I_Fwd_ecr_r0,1),comp_I_Fwd_ecr_r0_junR)

    ### Re:I_Fwd_ecr_r1

    ## Component Re:comp_I_Fwd_ecr_r1
    kappa_I_Fwd_ecr_r1 =  sp.symbols('kappa_I_Fwd_ecr_r1')
    RT = sp.symbols('RT')
    comp_I_Fwd_ecr_r1 = bgt.new('Re',name='I_Fwd_ecr_r1',value={'r':kappa_I_Fwd_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Fwd_ecr_r1)

    ## Junction 1:comp_I_Fwd_ecr_r1_junF
    comp_I_Fwd_ecr_r1_junF = bgt.new('1')
    model.add(comp_I_Fwd_ecr_r1_junF)

    ## Bond from comp_I_Fwd_ecr_r1_junF to (comp_I_Fwd_ecr_r1,0)
    bgt.connect(comp_I_Fwd_ecr_r1_junF,(comp_I_Fwd_ecr_r1,0))

    ## Junction 1:comp_I_Fwd_ecr_r1_junR
    comp_I_Fwd_ecr_r1_junR = bgt.new('1')
    model.add(comp_I_Fwd_ecr_r1_junR)

    ## Bond from (comp_I_Fwd_ecr_r1,1) to comp_I_Fwd_ecr_r1_junR
    bgt.connect((comp_I_Fwd_ecr_r1,1),comp_I_Fwd_ecr_r1_junR)

    ### Re:I_Fwd_ecr_r2

    ## Component Re:comp_I_Fwd_ecr_r2
    kappa_I_Fwd_ecr_r2 =  sp.symbols('kappa_I_Fwd_ecr_r2')
    RT = sp.symbols('RT')
    comp_I_Fwd_ecr_r2 = bgt.new('Re',name='I_Fwd_ecr_r2',value={'r':kappa_I_Fwd_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Fwd_ecr_r2)

    ## Junction 1:comp_I_Fwd_ecr_r2_junF
    comp_I_Fwd_ecr_r2_junF = bgt.new('1')
    model.add(comp_I_Fwd_ecr_r2_junF)

    ## Bond from comp_I_Fwd_ecr_r2_junF to (comp_I_Fwd_ecr_r2,0)
    bgt.connect(comp_I_Fwd_ecr_r2_junF,(comp_I_Fwd_ecr_r2,0))

    ## Junction 1:comp_I_Fwd_ecr_r2_junR
    comp_I_Fwd_ecr_r2_junR = bgt.new('1')
    model.add(comp_I_Fwd_ecr_r2_junR)

    ## Bond from (comp_I_Fwd_ecr_r2,1) to comp_I_Fwd_ecr_r2_junR
    bgt.connect((comp_I_Fwd_ecr_r2,1),comp_I_Fwd_ecr_r2_junR)

    ### Re:I_Rev_ecr_r0

    ## Component Re:comp_I_Rev_ecr_r0
    kappa_I_Rev_ecr_r0 =  sp.symbols('kappa_I_Rev_ecr_r0')
    RT = sp.symbols('RT')
    comp_I_Rev_ecr_r0 = bgt.new('Re',name='I_Rev_ecr_r0',value={'r':kappa_I_Rev_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Rev_ecr_r0)

    ## Junction 1:comp_I_Rev_ecr_r0_junF
    comp_I_Rev_ecr_r0_junF = bgt.new('1')
    model.add(comp_I_Rev_ecr_r0_junF)

    ## Bond from comp_I_Rev_ecr_r0_junF to (comp_I_Rev_ecr_r0,0)
    bgt.connect(comp_I_Rev_ecr_r0_junF,(comp_I_Rev_ecr_r0,0))

    ## Junction 1:comp_I_Rev_ecr_r0_junR
    comp_I_Rev_ecr_r0_junR = bgt.new('1')
    model.add(comp_I_Rev_ecr_r0_junR)

    ## Bond from (comp_I_Rev_ecr_r0,1) to comp_I_Rev_ecr_r0_junR
    bgt.connect((comp_I_Rev_ecr_r0,1),comp_I_Rev_ecr_r0_junR)

    ### Re:I_Rev_ecr_r1

    ## Component Re:comp_I_Rev_ecr_r1
    kappa_I_Rev_ecr_r1 =  sp.symbols('kappa_I_Rev_ecr_r1')
    RT = sp.symbols('RT')
    comp_I_Rev_ecr_r1 = bgt.new('Re',name='I_Rev_ecr_r1',value={'r':kappa_I_Rev_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Rev_ecr_r1)

    ## Junction 1:comp_I_Rev_ecr_r1_junF
    comp_I_Rev_ecr_r1_junF = bgt.new('1')
    model.add(comp_I_Rev_ecr_r1_junF)

    ## Bond from comp_I_Rev_ecr_r1_junF to (comp_I_Rev_ecr_r1,0)
    bgt.connect(comp_I_Rev_ecr_r1_junF,(comp_I_Rev_ecr_r1,0))

    ## Junction 1:comp_I_Rev_ecr_r1_junR
    comp_I_Rev_ecr_r1_junR = bgt.new('1')
    model.add(comp_I_Rev_ecr_r1_junR)

    ## Bond from (comp_I_Rev_ecr_r1,1) to comp_I_Rev_ecr_r1_junR
    bgt.connect((comp_I_Rev_ecr_r1,1),comp_I_Rev_ecr_r1_junR)

    ### Re:I_Rev_ecr_r2

    ## Component Re:comp_I_Rev_ecr_r2
    kappa_I_Rev_ecr_r2 =  sp.symbols('kappa_I_Rev_ecr_r2')
    RT = sp.symbols('RT')
    comp_I_Rev_ecr_r2 = bgt.new('Re',name='I_Rev_ecr_r2',value={'r':kappa_I_Rev_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_I_Rev_ecr_r2)

    ## Junction 1:comp_I_Rev_ecr_r2_junF
    comp_I_Rev_ecr_r2_junF = bgt.new('1')
    model.add(comp_I_Rev_ecr_r2_junF)

    ## Bond from comp_I_Rev_ecr_r2_junF to (comp_I_Rev_ecr_r2,0)
    bgt.connect(comp_I_Rev_ecr_r2_junF,(comp_I_Rev_ecr_r2,0))

    ## Junction 1:comp_I_Rev_ecr_r2_junR
    comp_I_Rev_ecr_r2_junR = bgt.new('1')
    model.add(comp_I_Rev_ecr_r2_junR)

    ## Bond from (comp_I_Rev_ecr_r2,1) to comp_I_Rev_ecr_r2_junR
    bgt.connect((comp_I_Rev_ecr_r2,1),comp_I_Rev_ecr_r2_junR)

    ### Re:P_Fwd_ecr_r0

    ## Component Re:comp_P_Fwd_ecr_r0
    kappa_P_Fwd_ecr_r0 =  sp.symbols('kappa_P_Fwd_ecr_r0')
    RT = sp.symbols('RT')
    comp_P_Fwd_ecr_r0 = bgt.new('Re',name='P_Fwd_ecr_r0',value={'r':kappa_P_Fwd_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Fwd_ecr_r0)

    ## Junction 1:comp_P_Fwd_ecr_r0_junF
    comp_P_Fwd_ecr_r0_junF = bgt.new('1')
    model.add(comp_P_Fwd_ecr_r0_junF)

    ## Bond from comp_P_Fwd_ecr_r0_junF to (comp_P_Fwd_ecr_r0,0)
    bgt.connect(comp_P_Fwd_ecr_r0_junF,(comp_P_Fwd_ecr_r0,0))

    ## Junction 1:comp_P_Fwd_ecr_r0_junR
    comp_P_Fwd_ecr_r0_junR = bgt.new('1')
    model.add(comp_P_Fwd_ecr_r0_junR)

    ## Bond from (comp_P_Fwd_ecr_r0,1) to comp_P_Fwd_ecr_r0_junR
    bgt.connect((comp_P_Fwd_ecr_r0,1),comp_P_Fwd_ecr_r0_junR)

    ### Re:P_Fwd_ecr_r1

    ## Component Re:comp_P_Fwd_ecr_r1
    kappa_P_Fwd_ecr_r1 =  sp.symbols('kappa_P_Fwd_ecr_r1')
    RT = sp.symbols('RT')
    comp_P_Fwd_ecr_r1 = bgt.new('Re',name='P_Fwd_ecr_r1',value={'r':kappa_P_Fwd_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Fwd_ecr_r1)

    ## Junction 1:comp_P_Fwd_ecr_r1_junF
    comp_P_Fwd_ecr_r1_junF = bgt.new('1')
    model.add(comp_P_Fwd_ecr_r1_junF)

    ## Bond from comp_P_Fwd_ecr_r1_junF to (comp_P_Fwd_ecr_r1,0)
    bgt.connect(comp_P_Fwd_ecr_r1_junF,(comp_P_Fwd_ecr_r1,0))

    ## Junction 1:comp_P_Fwd_ecr_r1_junR
    comp_P_Fwd_ecr_r1_junR = bgt.new('1')
    model.add(comp_P_Fwd_ecr_r1_junR)

    ## Bond from (comp_P_Fwd_ecr_r1,1) to comp_P_Fwd_ecr_r1_junR
    bgt.connect((comp_P_Fwd_ecr_r1,1),comp_P_Fwd_ecr_r1_junR)

    ### Re:P_Fwd_ecr_r2

    ## Component Re:comp_P_Fwd_ecr_r2
    kappa_P_Fwd_ecr_r2 =  sp.symbols('kappa_P_Fwd_ecr_r2')
    RT = sp.symbols('RT')
    comp_P_Fwd_ecr_r2 = bgt.new('Re',name='P_Fwd_ecr_r2',value={'r':kappa_P_Fwd_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Fwd_ecr_r2)

    ## Junction 1:comp_P_Fwd_ecr_r2_junF
    comp_P_Fwd_ecr_r2_junF = bgt.new('1')
    model.add(comp_P_Fwd_ecr_r2_junF)

    ## Bond from comp_P_Fwd_ecr_r2_junF to (comp_P_Fwd_ecr_r2,0)
    bgt.connect(comp_P_Fwd_ecr_r2_junF,(comp_P_Fwd_ecr_r2,0))

    ## Junction 1:comp_P_Fwd_ecr_r2_junR
    comp_P_Fwd_ecr_r2_junR = bgt.new('1')
    model.add(comp_P_Fwd_ecr_r2_junR)

    ## Bond from (comp_P_Fwd_ecr_r2,1) to comp_P_Fwd_ecr_r2_junR
    bgt.connect((comp_P_Fwd_ecr_r2,1),comp_P_Fwd_ecr_r2_junR)

    ### Re:P_Rev_ecr_r0

    ## Component Re:comp_P_Rev_ecr_r0
    kappa_P_Rev_ecr_r0 =  sp.symbols('kappa_P_Rev_ecr_r0')
    RT = sp.symbols('RT')
    comp_P_Rev_ecr_r0 = bgt.new('Re',name='P_Rev_ecr_r0',value={'r':kappa_P_Rev_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Rev_ecr_r0)

    ## Junction 1:comp_P_Rev_ecr_r0_junF
    comp_P_Rev_ecr_r0_junF = bgt.new('1')
    model.add(comp_P_Rev_ecr_r0_junF)

    ## Bond from comp_P_Rev_ecr_r0_junF to (comp_P_Rev_ecr_r0,0)
    bgt.connect(comp_P_Rev_ecr_r0_junF,(comp_P_Rev_ecr_r0,0))

    ## Junction 1:comp_P_Rev_ecr_r0_junR
    comp_P_Rev_ecr_r0_junR = bgt.new('1')
    model.add(comp_P_Rev_ecr_r0_junR)

    ## Bond from (comp_P_Rev_ecr_r0,1) to comp_P_Rev_ecr_r0_junR
    bgt.connect((comp_P_Rev_ecr_r0,1),comp_P_Rev_ecr_r0_junR)

    ### Re:P_Rev_ecr_r1

    ## Component Re:comp_P_Rev_ecr_r1
    kappa_P_Rev_ecr_r1 =  sp.symbols('kappa_P_Rev_ecr_r1')
    RT = sp.symbols('RT')
    comp_P_Rev_ecr_r1 = bgt.new('Re',name='P_Rev_ecr_r1',value={'r':kappa_P_Rev_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Rev_ecr_r1)

    ## Junction 1:comp_P_Rev_ecr_r1_junF
    comp_P_Rev_ecr_r1_junF = bgt.new('1')
    model.add(comp_P_Rev_ecr_r1_junF)

    ## Bond from comp_P_Rev_ecr_r1_junF to (comp_P_Rev_ecr_r1,0)
    bgt.connect(comp_P_Rev_ecr_r1_junF,(comp_P_Rev_ecr_r1,0))

    ## Junction 1:comp_P_Rev_ecr_r1_junR
    comp_P_Rev_ecr_r1_junR = bgt.new('1')
    model.add(comp_P_Rev_ecr_r1_junR)

    ## Bond from (comp_P_Rev_ecr_r1,1) to comp_P_Rev_ecr_r1_junR
    bgt.connect((comp_P_Rev_ecr_r1,1),comp_P_Rev_ecr_r1_junR)

    ### Re:P_Rev_ecr_r2

    ## Component Re:comp_P_Rev_ecr_r2
    kappa_P_Rev_ecr_r2 =  sp.symbols('kappa_P_Rev_ecr_r2')
    RT = sp.symbols('RT')
    comp_P_Rev_ecr_r2 = bgt.new('Re',name='P_Rev_ecr_r2',value={'r':kappa_P_Rev_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_P_Rev_ecr_r2)

    ## Junction 1:comp_P_Rev_ecr_r2_junF
    comp_P_Rev_ecr_r2_junF = bgt.new('1')
    model.add(comp_P_Rev_ecr_r2_junF)

    ## Bond from comp_P_Rev_ecr_r2_junF to (comp_P_Rev_ecr_r2,0)
    bgt.connect(comp_P_Rev_ecr_r2_junF,(comp_P_Rev_ecr_r2,0))

    ## Junction 1:comp_P_Rev_ecr_r2_junR
    comp_P_Rev_ecr_r2_junR = bgt.new('1')
    model.add(comp_P_Rev_ecr_r2_junR)

    ## Bond from (comp_P_Rev_ecr_r2,1) to comp_P_Rev_ecr_r2_junR
    bgt.connect((comp_P_Rev_ecr_r2,1),comp_P_Rev_ecr_r2_junR)
    ### Connections

    ### Ce:I_Fwd_ecr_C to Re:I_Fwd_ecr_r2

    ## Bond from comp_I_Fwd_ecr_C_jun to comp_I_Fwd_ecr_r2_junF
    bgt.connect(comp_I_Fwd_ecr_C_jun,comp_I_Fwd_ecr_r2_junF)

    ### Ce:I_Fwd_ecr_E to Re:I_Fwd_ecr_r0

    ## Bond from comp_I_Fwd_ecr_E_jun to comp_I_Fwd_ecr_r0_junF
    bgt.connect(comp_I_Fwd_ecr_E_jun,comp_I_Fwd_ecr_r0_junF)

    ### Ce:I_Fwd_ecr_E to Re:I_Fwd_ecr_r1

    ## Bond from comp_I_Fwd_ecr_E_jun to comp_I_Fwd_ecr_r1_junF
    bgt.connect(comp_I_Fwd_ecr_E_jun,comp_I_Fwd_ecr_r1_junF)

    ### Ce:I_Fwd_ecr_F to Re:I_Fwd_ecr_r1

    ## Bond from comp_I_Fwd_ecr_F_jun to comp_I_Fwd_ecr_r1_junF
    bgt.connect(comp_I_Fwd_ecr_F_jun,comp_I_Fwd_ecr_r1_junF)

    ### Ce:I_Rev_ecr_C to Re:I_Rev_ecr_r2

    ## Bond from comp_I_Rev_ecr_C_jun to comp_I_Rev_ecr_r2_junF
    bgt.connect(comp_I_Rev_ecr_C_jun,comp_I_Rev_ecr_r2_junF)

    ### Ce:I_Rev_ecr_E to Re:I_Rev_ecr_r0

    ## Bond from comp_I_Rev_ecr_E_jun to comp_I_Rev_ecr_r0_junF
    bgt.connect(comp_I_Rev_ecr_E_jun,comp_I_Rev_ecr_r0_junF)

    ### Ce:I_Rev_ecr_E to Re:I_Rev_ecr_r1

    ## Bond from comp_I_Rev_ecr_E_jun to comp_I_Rev_ecr_r1_junF
    bgt.connect(comp_I_Rev_ecr_E_jun,comp_I_Rev_ecr_r1_junF)

    ### Ce:I_Rev_ecr_F to Re:I_Rev_ecr_r1

    ## Bond from comp_I_Rev_ecr_F_jun to comp_I_Rev_ecr_r1_junF
    bgt.connect(comp_I_Rev_ecr_F_jun,comp_I_Rev_ecr_r1_junF)

    ### Ce:P_Fwd_ecr_C to Re:P_Fwd_ecr_r2

    ## Bond from comp_P_Fwd_ecr_C_jun to comp_P_Fwd_ecr_r2_junF
    bgt.connect(comp_P_Fwd_ecr_C_jun,comp_P_Fwd_ecr_r2_junF)

    ### Ce:P_Fwd_ecr_E to Re:P_Fwd_ecr_r0

    ## Bond from comp_P_Fwd_ecr_E_jun to comp_P_Fwd_ecr_r0_junF
    bgt.connect(comp_P_Fwd_ecr_E_jun,comp_P_Fwd_ecr_r0_junF)

    ### Ce:P_Fwd_ecr_E to Re:P_Fwd_ecr_r1

    ## Bond from comp_P_Fwd_ecr_E_jun to comp_P_Fwd_ecr_r1_junF
    bgt.connect(comp_P_Fwd_ecr_E_jun,comp_P_Fwd_ecr_r1_junF)

    ### Ce:P_Fwd_ecr_F to Re:P_Fwd_ecr_r1

    ## Bond from comp_P_Fwd_ecr_F_jun to comp_P_Fwd_ecr_r1_junF
    bgt.connect(comp_P_Fwd_ecr_F_jun,comp_P_Fwd_ecr_r1_junF)

    ### Ce:P_Rev_ecr_C to Re:P_Rev_ecr_r2

    ## Bond from comp_P_Rev_ecr_C_jun to comp_P_Rev_ecr_r2_junF
    bgt.connect(comp_P_Rev_ecr_C_jun,comp_P_Rev_ecr_r2_junF)

    ### Ce:P_Rev_ecr_E to Re:P_Rev_ecr_r0

    ## Bond from comp_P_Rev_ecr_E_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_P_Rev_ecr_E_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:P_Rev_ecr_E to Re:P_Rev_ecr_r1

    ## Bond from comp_P_Rev_ecr_E_jun to comp_P_Rev_ecr_r1_junF
    bgt.connect(comp_P_Rev_ecr_E_jun,comp_P_Rev_ecr_r1_junF)

    ### Ce:P_Rev_ecr_F to Re:P_Rev_ecr_r1

    ## Bond from comp_P_Rev_ecr_F_jun to comp_P_Rev_ecr_r1_junF
    bgt.connect(comp_P_Rev_ecr_F_jun,comp_P_Rev_ecr_r1_junF)

    ### Ce:A to Re:I_Fwd_ecr_r1

    ## Bond from comp_A_jun to comp_I_Fwd_ecr_r1_junF
    bgt.connect(comp_A_jun,comp_I_Fwd_ecr_r1_junF)

    ### Ce:A to Re:P_Fwd_ecr_r1

    ## Bond from comp_A_jun to comp_P_Fwd_ecr_r1_junF
    bgt.connect(comp_A_jun,comp_P_Fwd_ecr_r1_junF)

    ### Ce:Act to Re:I_Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_I_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_I_Rev_ecr_r0_junF)

    ### Ce:Act to Re:I_Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_I_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_I_Rev_ecr_r0_junF)

    ### Ce:Act to Re:I_Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_I_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_I_Rev_ecr_r0_junF)

    ### Ce:Act to Re:I_Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_I_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_I_Rev_ecr_r0_junF)

    ### Ce:Act to Re:P_Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Act to Re:P_Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Act to Re:P_Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Act to Re:P_Rev_ecr_r0

    ## Bond from comp_Act_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Act_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:B to Re:P_Rev_ecr_r1

    ## Bond from comp_B_jun to comp_P_Rev_ecr_r1_junF
    bgt.connect(comp_B_jun,comp_P_Rev_ecr_r1_junF)

    ### Ce:Inh to Re:I_Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_I_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_I_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:I_Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_I_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_I_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:I_Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_I_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_I_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:I_Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_I_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_I_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:P_Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_P_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_P_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:P_Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_P_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_P_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:P_Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_P_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_P_Fwd_ecr_r0_junF)

    ### Ce:Inh to Re:P_Fwd_ecr_r0

    ## Bond from comp_Inh_jun to comp_P_Fwd_ecr_r0_junF
    bgt.connect(comp_Inh_jun,comp_P_Fwd_ecr_r0_junF)

    ### Ce:Int to Re:I_Rev_ecr_r1

    ## Bond from comp_Int_jun to comp_I_Rev_ecr_r1_junF
    bgt.connect(comp_Int_jun,comp_I_Rev_ecr_r1_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Ce:Int to Re:P_Rev_ecr_r0

    ## Bond from comp_Int_jun to comp_P_Rev_ecr_r0_junF
    bgt.connect(comp_Int_jun,comp_P_Rev_ecr_r0_junF)

    ### Re:I_Fwd_ecr_r1 to Ce:I_Fwd_ecr_C

    ## Bond from comp_I_Fwd_ecr_r1_junR to comp_I_Fwd_ecr_C_jun
    bgt.connect(comp_I_Fwd_ecr_r1_junR,comp_I_Fwd_ecr_C_jun)

    ### Re:I_Fwd_ecr_r2 to Ce:I_Fwd_ecr_E

    ## Bond from comp_I_Fwd_ecr_r2_junR to comp_I_Fwd_ecr_E_jun
    bgt.connect(comp_I_Fwd_ecr_r2_junR,comp_I_Fwd_ecr_E_jun)

    ### Re:I_Fwd_ecr_r0 to Ce:I_Fwd_ecr_E0

    ## Bond from comp_I_Fwd_ecr_r0_junR to comp_I_Fwd_ecr_E0_jun
    bgt.connect(comp_I_Fwd_ecr_r0_junR,comp_I_Fwd_ecr_E0_jun)

    ### Re:I_Fwd_ecr_r2 to Ce:I_Fwd_ecr_G

    ## Bond from comp_I_Fwd_ecr_r2_junR to comp_I_Fwd_ecr_G_jun
    bgt.connect(comp_I_Fwd_ecr_r2_junR,comp_I_Fwd_ecr_G_jun)

    ### Re:I_Rev_ecr_r1 to Ce:I_Rev_ecr_C

    ## Bond from comp_I_Rev_ecr_r1_junR to comp_I_Rev_ecr_C_jun
    bgt.connect(comp_I_Rev_ecr_r1_junR,comp_I_Rev_ecr_C_jun)

    ### Re:I_Rev_ecr_r2 to Ce:I_Rev_ecr_E

    ## Bond from comp_I_Rev_ecr_r2_junR to comp_I_Rev_ecr_E_jun
    bgt.connect(comp_I_Rev_ecr_r2_junR,comp_I_Rev_ecr_E_jun)

    ### Re:I_Rev_ecr_r0 to Ce:I_Rev_ecr_E0

    ## Bond from comp_I_Rev_ecr_r0_junR to comp_I_Rev_ecr_E0_jun
    bgt.connect(comp_I_Rev_ecr_r0_junR,comp_I_Rev_ecr_E0_jun)

    ### Re:I_Rev_ecr_r2 to Ce:I_Rev_ecr_G

    ## Bond from comp_I_Rev_ecr_r2_junR to comp_I_Rev_ecr_G_jun
    bgt.connect(comp_I_Rev_ecr_r2_junR,comp_I_Rev_ecr_G_jun)

    ### Re:P_Fwd_ecr_r1 to Ce:P_Fwd_ecr_C

    ## Bond from comp_P_Fwd_ecr_r1_junR to comp_P_Fwd_ecr_C_jun
    bgt.connect(comp_P_Fwd_ecr_r1_junR,comp_P_Fwd_ecr_C_jun)

    ### Re:P_Fwd_ecr_r2 to Ce:P_Fwd_ecr_E

    ## Bond from comp_P_Fwd_ecr_r2_junR to comp_P_Fwd_ecr_E_jun
    bgt.connect(comp_P_Fwd_ecr_r2_junR,comp_P_Fwd_ecr_E_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:P_Fwd_ecr_E0

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_P_Fwd_ecr_E0_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_P_Fwd_ecr_E0_jun)

    ### Re:P_Fwd_ecr_r2 to Ce:P_Fwd_ecr_G

    ## Bond from comp_P_Fwd_ecr_r2_junR to comp_P_Fwd_ecr_G_jun
    bgt.connect(comp_P_Fwd_ecr_r2_junR,comp_P_Fwd_ecr_G_jun)

    ### Re:P_Rev_ecr_r1 to Ce:P_Rev_ecr_C

    ## Bond from comp_P_Rev_ecr_r1_junR to comp_P_Rev_ecr_C_jun
    bgt.connect(comp_P_Rev_ecr_r1_junR,comp_P_Rev_ecr_C_jun)

    ### Re:P_Rev_ecr_r2 to Ce:P_Rev_ecr_E

    ## Bond from comp_P_Rev_ecr_r2_junR to comp_P_Rev_ecr_E_jun
    bgt.connect(comp_P_Rev_ecr_r2_junR,comp_P_Rev_ecr_E_jun)

    ### Re:P_Rev_ecr_r0 to Ce:P_Rev_ecr_E0

    ## Bond from comp_P_Rev_ecr_r0_junR to comp_P_Rev_ecr_E0_jun
    bgt.connect(comp_P_Rev_ecr_r0_junR,comp_P_Rev_ecr_E0_jun)

    ### Re:P_Rev_ecr_r2 to Ce:P_Rev_ecr_G

    ## Bond from comp_P_Rev_ecr_r2_junR to comp_P_Rev_ecr_G_jun
    bgt.connect(comp_P_Rev_ecr_r2_junR,comp_P_Rev_ecr_G_jun)

    ### Re:I_Rev_ecr_r2 to Ce:A

    ## Bond from comp_I_Rev_ecr_r2_junR to comp_A_jun
    bgt.connect(comp_I_Rev_ecr_r2_junR,comp_A_jun)

    ### Re:P_Rev_ecr_r2 to Ce:A

    ## Bond from comp_P_Rev_ecr_r2_junR to comp_A_jun
    bgt.connect(comp_P_Rev_ecr_r2_junR,comp_A_jun)

    ### Re:I_Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_I_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_I_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:I_Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_I_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_I_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:I_Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_I_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_I_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:I_Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_I_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_I_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Act

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Act_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Act_jun)

    ### Re:P_Fwd_ecr_r2 to Ce:B

    ## Bond from comp_P_Fwd_ecr_r2_junR to comp_B_jun
    bgt.connect(comp_P_Fwd_ecr_r2_junR,comp_B_jun)

    ### Re:I_Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_I_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_I_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:I_Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_I_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_I_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:I_Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_I_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_I_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:I_Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_I_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_I_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:P_Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_P_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_P_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:P_Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_P_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_P_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:P_Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_P_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_P_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:P_Rev_ecr_r0 to Ce:Inh

    ## Bond from comp_P_Rev_ecr_r0_junR to comp_Inh_jun
    bgt.connect(comp_P_Rev_ecr_r0_junR,comp_Inh_jun)

    ### Re:I_Fwd_ecr_r2 to Ce:Int

    ## Bond from comp_I_Fwd_ecr_r2_junR to comp_Int_jun
    bgt.connect(comp_I_Fwd_ecr_r2_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    ### Re:P_Fwd_ecr_r0 to Ce:Int

    ## Bond from comp_P_Fwd_ecr_r0_junR to comp_Int_jun
    bgt.connect(comp_P_Fwd_ecr_r0_junR,comp_Int_jun)

    return model
