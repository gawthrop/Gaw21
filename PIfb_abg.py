import BondGraphTools as bgt
import sympy as sp

def model():
    """ Acausal bond graph PIfb.py
    Created by stoichBondGraph at Wed Jan 27 12:36:09 2021

    Usage:
    import PIfb; model = PIfb.model()
    """

    model = bgt.new(name="PIfb")
    ### Species

    ### Ce:D

    ## Component Ce:comp_D
    K_D =  sp.symbols('K_D')
    RT = sp.symbols('RT')
    comp_D = bgt.new('Ce',name='D',value={'k':K_D,'R':RT,'T':1},library='BioChem')
    model.add(comp_D)

    ## Junction 0:comp_D_jun
    comp_D_jun = bgt.new('0')
    model.add(comp_D_jun)

    ## Bond from comp_D_jun to comp_D
    bgt.connect(comp_D_jun,comp_D)

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

    ### Ce:P0

    ## Component Ce:comp_P0
    K_P0 =  sp.symbols('K_P0')
    RT = sp.symbols('RT')
    comp_P0 = bgt.new('Ce',name='P0',value={'k':K_P0,'R':RT,'T':1},library='BioChem')
    model.add(comp_P0)

    ## Junction 0:comp_P0_jun
    comp_P0_jun = bgt.new('0')
    model.add(comp_P0_jun)

    ## Bond from comp_P0_jun to comp_P0
    bgt.connect(comp_P0_jun,comp_P0)

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

    ### Ce:con_I_Fwd_ecr_C

    ## Component Ce:comp_con_I_Fwd_ecr_C
    K_con_I_Fwd_ecr_C =  sp.symbols('K_con_I_Fwd_ecr_C')
    RT = sp.symbols('RT')
    comp_con_I_Fwd_ecr_C = bgt.new('Ce',name='con_I_Fwd_ecr_C',value={'k':K_con_I_Fwd_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Fwd_ecr_C)

    ## Junction 0:comp_con_I_Fwd_ecr_C_jun
    comp_con_I_Fwd_ecr_C_jun = bgt.new('0')
    model.add(comp_con_I_Fwd_ecr_C_jun)

    ## Bond from comp_con_I_Fwd_ecr_C_jun to comp_con_I_Fwd_ecr_C
    bgt.connect(comp_con_I_Fwd_ecr_C_jun,comp_con_I_Fwd_ecr_C)

    ### Ce:con_I_Fwd_ecr_E

    ## Component Ce:comp_con_I_Fwd_ecr_E
    K_con_I_Fwd_ecr_E =  sp.symbols('K_con_I_Fwd_ecr_E')
    RT = sp.symbols('RT')
    comp_con_I_Fwd_ecr_E = bgt.new('Ce',name='con_I_Fwd_ecr_E',value={'k':K_con_I_Fwd_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Fwd_ecr_E)

    ## Junction 0:comp_con_I_Fwd_ecr_E_jun
    comp_con_I_Fwd_ecr_E_jun = bgt.new('0')
    model.add(comp_con_I_Fwd_ecr_E_jun)

    ## Bond from comp_con_I_Fwd_ecr_E_jun to comp_con_I_Fwd_ecr_E
    bgt.connect(comp_con_I_Fwd_ecr_E_jun,comp_con_I_Fwd_ecr_E)

    ### Ce:con_I_Fwd_ecr_E0

    ## Component Ce:comp_con_I_Fwd_ecr_E0
    K_con_I_Fwd_ecr_E0 =  sp.symbols('K_con_I_Fwd_ecr_E0')
    RT = sp.symbols('RT')
    comp_con_I_Fwd_ecr_E0 = bgt.new('Ce',name='con_I_Fwd_ecr_E0',value={'k':K_con_I_Fwd_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Fwd_ecr_E0)

    ## Junction 0:comp_con_I_Fwd_ecr_E0_jun
    comp_con_I_Fwd_ecr_E0_jun = bgt.new('0')
    model.add(comp_con_I_Fwd_ecr_E0_jun)

    ## Bond from comp_con_I_Fwd_ecr_E0_jun to comp_con_I_Fwd_ecr_E0
    bgt.connect(comp_con_I_Fwd_ecr_E0_jun,comp_con_I_Fwd_ecr_E0)

    ### Ce:con_I_Fwd_ecr_F

    ## Component Ce:comp_con_I_Fwd_ecr_F
    K_con_I_Fwd_ecr_F =  sp.symbols('K_con_I_Fwd_ecr_F')
    RT = sp.symbols('RT')
    comp_con_I_Fwd_ecr_F = bgt.new('Ce',name='con_I_Fwd_ecr_F',value={'k':K_con_I_Fwd_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Fwd_ecr_F)

    ## Junction 0:comp_con_I_Fwd_ecr_F_jun
    comp_con_I_Fwd_ecr_F_jun = bgt.new('0')
    model.add(comp_con_I_Fwd_ecr_F_jun)

    ## Bond from comp_con_I_Fwd_ecr_F_jun to comp_con_I_Fwd_ecr_F
    bgt.connect(comp_con_I_Fwd_ecr_F_jun,comp_con_I_Fwd_ecr_F)

    ### Ce:con_I_Fwd_ecr_G

    ## Component Ce:comp_con_I_Fwd_ecr_G
    K_con_I_Fwd_ecr_G =  sp.symbols('K_con_I_Fwd_ecr_G')
    RT = sp.symbols('RT')
    comp_con_I_Fwd_ecr_G = bgt.new('Ce',name='con_I_Fwd_ecr_G',value={'k':K_con_I_Fwd_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Fwd_ecr_G)

    ## Junction 0:comp_con_I_Fwd_ecr_G_jun
    comp_con_I_Fwd_ecr_G_jun = bgt.new('0')
    model.add(comp_con_I_Fwd_ecr_G_jun)

    ## Bond from comp_con_I_Fwd_ecr_G_jun to comp_con_I_Fwd_ecr_G
    bgt.connect(comp_con_I_Fwd_ecr_G_jun,comp_con_I_Fwd_ecr_G)

    ### Ce:con_I_Rev_ecr_C

    ## Component Ce:comp_con_I_Rev_ecr_C
    K_con_I_Rev_ecr_C =  sp.symbols('K_con_I_Rev_ecr_C')
    RT = sp.symbols('RT')
    comp_con_I_Rev_ecr_C = bgt.new('Ce',name='con_I_Rev_ecr_C',value={'k':K_con_I_Rev_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Rev_ecr_C)

    ## Junction 0:comp_con_I_Rev_ecr_C_jun
    comp_con_I_Rev_ecr_C_jun = bgt.new('0')
    model.add(comp_con_I_Rev_ecr_C_jun)

    ## Bond from comp_con_I_Rev_ecr_C_jun to comp_con_I_Rev_ecr_C
    bgt.connect(comp_con_I_Rev_ecr_C_jun,comp_con_I_Rev_ecr_C)

    ### Ce:con_I_Rev_ecr_E

    ## Component Ce:comp_con_I_Rev_ecr_E
    K_con_I_Rev_ecr_E =  sp.symbols('K_con_I_Rev_ecr_E')
    RT = sp.symbols('RT')
    comp_con_I_Rev_ecr_E = bgt.new('Ce',name='con_I_Rev_ecr_E',value={'k':K_con_I_Rev_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Rev_ecr_E)

    ## Junction 0:comp_con_I_Rev_ecr_E_jun
    comp_con_I_Rev_ecr_E_jun = bgt.new('0')
    model.add(comp_con_I_Rev_ecr_E_jun)

    ## Bond from comp_con_I_Rev_ecr_E_jun to comp_con_I_Rev_ecr_E
    bgt.connect(comp_con_I_Rev_ecr_E_jun,comp_con_I_Rev_ecr_E)

    ### Ce:con_I_Rev_ecr_E0

    ## Component Ce:comp_con_I_Rev_ecr_E0
    K_con_I_Rev_ecr_E0 =  sp.symbols('K_con_I_Rev_ecr_E0')
    RT = sp.symbols('RT')
    comp_con_I_Rev_ecr_E0 = bgt.new('Ce',name='con_I_Rev_ecr_E0',value={'k':K_con_I_Rev_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Rev_ecr_E0)

    ## Junction 0:comp_con_I_Rev_ecr_E0_jun
    comp_con_I_Rev_ecr_E0_jun = bgt.new('0')
    model.add(comp_con_I_Rev_ecr_E0_jun)

    ## Bond from comp_con_I_Rev_ecr_E0_jun to comp_con_I_Rev_ecr_E0
    bgt.connect(comp_con_I_Rev_ecr_E0_jun,comp_con_I_Rev_ecr_E0)

    ### Ce:con_I_Rev_ecr_F

    ## Component Ce:comp_con_I_Rev_ecr_F
    K_con_I_Rev_ecr_F =  sp.symbols('K_con_I_Rev_ecr_F')
    RT = sp.symbols('RT')
    comp_con_I_Rev_ecr_F = bgt.new('Ce',name='con_I_Rev_ecr_F',value={'k':K_con_I_Rev_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Rev_ecr_F)

    ## Junction 0:comp_con_I_Rev_ecr_F_jun
    comp_con_I_Rev_ecr_F_jun = bgt.new('0')
    model.add(comp_con_I_Rev_ecr_F_jun)

    ## Bond from comp_con_I_Rev_ecr_F_jun to comp_con_I_Rev_ecr_F
    bgt.connect(comp_con_I_Rev_ecr_F_jun,comp_con_I_Rev_ecr_F)

    ### Ce:con_I_Rev_ecr_G

    ## Component Ce:comp_con_I_Rev_ecr_G
    K_con_I_Rev_ecr_G =  sp.symbols('K_con_I_Rev_ecr_G')
    RT = sp.symbols('RT')
    comp_con_I_Rev_ecr_G = bgt.new('Ce',name='con_I_Rev_ecr_G',value={'k':K_con_I_Rev_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Rev_ecr_G)

    ## Junction 0:comp_con_I_Rev_ecr_G_jun
    comp_con_I_Rev_ecr_G_jun = bgt.new('0')
    model.add(comp_con_I_Rev_ecr_G_jun)

    ## Bond from comp_con_I_Rev_ecr_G_jun to comp_con_I_Rev_ecr_G
    bgt.connect(comp_con_I_Rev_ecr_G_jun,comp_con_I_Rev_ecr_G)

    ### Ce:con_P_Fwd_ecr_C

    ## Component Ce:comp_con_P_Fwd_ecr_C
    K_con_P_Fwd_ecr_C =  sp.symbols('K_con_P_Fwd_ecr_C')
    RT = sp.symbols('RT')
    comp_con_P_Fwd_ecr_C = bgt.new('Ce',name='con_P_Fwd_ecr_C',value={'k':K_con_P_Fwd_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Fwd_ecr_C)

    ## Junction 0:comp_con_P_Fwd_ecr_C_jun
    comp_con_P_Fwd_ecr_C_jun = bgt.new('0')
    model.add(comp_con_P_Fwd_ecr_C_jun)

    ## Bond from comp_con_P_Fwd_ecr_C_jun to comp_con_P_Fwd_ecr_C
    bgt.connect(comp_con_P_Fwd_ecr_C_jun,comp_con_P_Fwd_ecr_C)

    ### Ce:con_P_Fwd_ecr_E

    ## Component Ce:comp_con_P_Fwd_ecr_E
    K_con_P_Fwd_ecr_E =  sp.symbols('K_con_P_Fwd_ecr_E')
    RT = sp.symbols('RT')
    comp_con_P_Fwd_ecr_E = bgt.new('Ce',name='con_P_Fwd_ecr_E',value={'k':K_con_P_Fwd_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Fwd_ecr_E)

    ## Junction 0:comp_con_P_Fwd_ecr_E_jun
    comp_con_P_Fwd_ecr_E_jun = bgt.new('0')
    model.add(comp_con_P_Fwd_ecr_E_jun)

    ## Bond from comp_con_P_Fwd_ecr_E_jun to comp_con_P_Fwd_ecr_E
    bgt.connect(comp_con_P_Fwd_ecr_E_jun,comp_con_P_Fwd_ecr_E)

    ### Ce:con_P_Fwd_ecr_E0

    ## Component Ce:comp_con_P_Fwd_ecr_E0
    K_con_P_Fwd_ecr_E0 =  sp.symbols('K_con_P_Fwd_ecr_E0')
    RT = sp.symbols('RT')
    comp_con_P_Fwd_ecr_E0 = bgt.new('Ce',name='con_P_Fwd_ecr_E0',value={'k':K_con_P_Fwd_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Fwd_ecr_E0)

    ## Junction 0:comp_con_P_Fwd_ecr_E0_jun
    comp_con_P_Fwd_ecr_E0_jun = bgt.new('0')
    model.add(comp_con_P_Fwd_ecr_E0_jun)

    ## Bond from comp_con_P_Fwd_ecr_E0_jun to comp_con_P_Fwd_ecr_E0
    bgt.connect(comp_con_P_Fwd_ecr_E0_jun,comp_con_P_Fwd_ecr_E0)

    ### Ce:con_P_Fwd_ecr_F

    ## Component Ce:comp_con_P_Fwd_ecr_F
    K_con_P_Fwd_ecr_F =  sp.symbols('K_con_P_Fwd_ecr_F')
    RT = sp.symbols('RT')
    comp_con_P_Fwd_ecr_F = bgt.new('Ce',name='con_P_Fwd_ecr_F',value={'k':K_con_P_Fwd_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Fwd_ecr_F)

    ## Junction 0:comp_con_P_Fwd_ecr_F_jun
    comp_con_P_Fwd_ecr_F_jun = bgt.new('0')
    model.add(comp_con_P_Fwd_ecr_F_jun)

    ## Bond from comp_con_P_Fwd_ecr_F_jun to comp_con_P_Fwd_ecr_F
    bgt.connect(comp_con_P_Fwd_ecr_F_jun,comp_con_P_Fwd_ecr_F)

    ### Ce:con_P_Fwd_ecr_G

    ## Component Ce:comp_con_P_Fwd_ecr_G
    K_con_P_Fwd_ecr_G =  sp.symbols('K_con_P_Fwd_ecr_G')
    RT = sp.symbols('RT')
    comp_con_P_Fwd_ecr_G = bgt.new('Ce',name='con_P_Fwd_ecr_G',value={'k':K_con_P_Fwd_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Fwd_ecr_G)

    ## Junction 0:comp_con_P_Fwd_ecr_G_jun
    comp_con_P_Fwd_ecr_G_jun = bgt.new('0')
    model.add(comp_con_P_Fwd_ecr_G_jun)

    ## Bond from comp_con_P_Fwd_ecr_G_jun to comp_con_P_Fwd_ecr_G
    bgt.connect(comp_con_P_Fwd_ecr_G_jun,comp_con_P_Fwd_ecr_G)

    ### Ce:con_P_Rev_ecr_C

    ## Component Ce:comp_con_P_Rev_ecr_C
    K_con_P_Rev_ecr_C =  sp.symbols('K_con_P_Rev_ecr_C')
    RT = sp.symbols('RT')
    comp_con_P_Rev_ecr_C = bgt.new('Ce',name='con_P_Rev_ecr_C',value={'k':K_con_P_Rev_ecr_C,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Rev_ecr_C)

    ## Junction 0:comp_con_P_Rev_ecr_C_jun
    comp_con_P_Rev_ecr_C_jun = bgt.new('0')
    model.add(comp_con_P_Rev_ecr_C_jun)

    ## Bond from comp_con_P_Rev_ecr_C_jun to comp_con_P_Rev_ecr_C
    bgt.connect(comp_con_P_Rev_ecr_C_jun,comp_con_P_Rev_ecr_C)

    ### Ce:con_P_Rev_ecr_E

    ## Component Ce:comp_con_P_Rev_ecr_E
    K_con_P_Rev_ecr_E =  sp.symbols('K_con_P_Rev_ecr_E')
    RT = sp.symbols('RT')
    comp_con_P_Rev_ecr_E = bgt.new('Ce',name='con_P_Rev_ecr_E',value={'k':K_con_P_Rev_ecr_E,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Rev_ecr_E)

    ## Junction 0:comp_con_P_Rev_ecr_E_jun
    comp_con_P_Rev_ecr_E_jun = bgt.new('0')
    model.add(comp_con_P_Rev_ecr_E_jun)

    ## Bond from comp_con_P_Rev_ecr_E_jun to comp_con_P_Rev_ecr_E
    bgt.connect(comp_con_P_Rev_ecr_E_jun,comp_con_P_Rev_ecr_E)

    ### Ce:con_P_Rev_ecr_E0

    ## Component Ce:comp_con_P_Rev_ecr_E0
    K_con_P_Rev_ecr_E0 =  sp.symbols('K_con_P_Rev_ecr_E0')
    RT = sp.symbols('RT')
    comp_con_P_Rev_ecr_E0 = bgt.new('Ce',name='con_P_Rev_ecr_E0',value={'k':K_con_P_Rev_ecr_E0,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Rev_ecr_E0)

    ## Junction 0:comp_con_P_Rev_ecr_E0_jun
    comp_con_P_Rev_ecr_E0_jun = bgt.new('0')
    model.add(comp_con_P_Rev_ecr_E0_jun)

    ## Bond from comp_con_P_Rev_ecr_E0_jun to comp_con_P_Rev_ecr_E0
    bgt.connect(comp_con_P_Rev_ecr_E0_jun,comp_con_P_Rev_ecr_E0)

    ### Ce:con_P_Rev_ecr_F

    ## Component Ce:comp_con_P_Rev_ecr_F
    K_con_P_Rev_ecr_F =  sp.symbols('K_con_P_Rev_ecr_F')
    RT = sp.symbols('RT')
    comp_con_P_Rev_ecr_F = bgt.new('Ce',name='con_P_Rev_ecr_F',value={'k':K_con_P_Rev_ecr_F,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Rev_ecr_F)

    ## Junction 0:comp_con_P_Rev_ecr_F_jun
    comp_con_P_Rev_ecr_F_jun = bgt.new('0')
    model.add(comp_con_P_Rev_ecr_F_jun)

    ## Bond from comp_con_P_Rev_ecr_F_jun to comp_con_P_Rev_ecr_F
    bgt.connect(comp_con_P_Rev_ecr_F_jun,comp_con_P_Rev_ecr_F)

    ### Ce:con_P_Rev_ecr_G

    ## Component Ce:comp_con_P_Rev_ecr_G
    K_con_P_Rev_ecr_G =  sp.symbols('K_con_P_Rev_ecr_G')
    RT = sp.symbols('RT')
    comp_con_P_Rev_ecr_G = bgt.new('Ce',name='con_P_Rev_ecr_G',value={'k':K_con_P_Rev_ecr_G,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Rev_ecr_G)

    ## Junction 0:comp_con_P_Rev_ecr_G_jun
    comp_con_P_Rev_ecr_G_jun = bgt.new('0')
    model.add(comp_con_P_Rev_ecr_G_jun)

    ## Bond from comp_con_P_Rev_ecr_G_jun to comp_con_P_Rev_ecr_G
    bgt.connect(comp_con_P_Rev_ecr_G_jun,comp_con_P_Rev_ecr_G)

    ### Ce:con_A

    ## Component Ce:comp_con_A
    K_con_A =  sp.symbols('K_con_A')
    RT = sp.symbols('RT')
    comp_con_A = bgt.new('Ce',name='con_A',value={'k':K_con_A,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_A)

    ## Junction 0:comp_con_A_jun
    comp_con_A_jun = bgt.new('0')
    model.add(comp_con_A_jun)

    ## Bond from comp_con_A_jun to comp_con_A
    bgt.connect(comp_con_A_jun,comp_con_A)

    ### Ce:con_Int

    ## Component Ce:comp_con_Int
    K_con_Int =  sp.symbols('K_con_Int')
    RT = sp.symbols('RT')
    comp_con_Int = bgt.new('Ce',name='con_Int',value={'k':K_con_Int,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_Int)

    ## Junction 0:comp_con_Int_jun
    comp_con_Int_jun = bgt.new('0')
    model.add(comp_con_Int_jun)

    ## Bond from comp_con_Int_jun to comp_con_Int
    bgt.connect(comp_con_Int_jun,comp_con_Int)

    ### Ce:sys_I1

    ## Component Ce:comp_sys_I1
    K_sys_I1 =  sp.symbols('K_sys_I1')
    RT = sp.symbols('RT')
    comp_sys_I1 = bgt.new('Ce',name='sys_I1',value={'k':K_sys_I1,'R':RT,'T':1},library='BioChem')
    model.add(comp_sys_I1)

    ## Junction 0:comp_sys_I1_jun
    comp_sys_I1_jun = bgt.new('0')
    model.add(comp_sys_I1_jun)

    ## Bond from comp_sys_I1_jun to comp_sys_I1
    bgt.connect(comp_sys_I1_jun,comp_sys_I1)

    ### Ce:sys_I2

    ## Component Ce:comp_sys_I2
    K_sys_I2 =  sp.symbols('K_sys_I2')
    RT = sp.symbols('RT')
    comp_sys_I2 = bgt.new('Ce',name='sys_I2',value={'k':K_sys_I2,'R':RT,'T':1},library='BioChem')
    model.add(comp_sys_I2)

    ## Junction 0:comp_sys_I2_jun
    comp_sys_I2_jun = bgt.new('0')
    model.add(comp_sys_I2_jun)

    ## Bond from comp_sys_I2_jun to comp_sys_I2
    bgt.connect(comp_sys_I2_jun,comp_sys_I2)
    ### Reactions

    ### Re:con_I_Fwd_ecr_r0

    ## Component Re:comp_con_I_Fwd_ecr_r0
    kappa_con_I_Fwd_ecr_r0 =  sp.symbols('kappa_con_I_Fwd_ecr_r0')
    RT = sp.symbols('RT')
    comp_con_I_Fwd_ecr_r0 = bgt.new('Re',name='con_I_Fwd_ecr_r0',value={'r':kappa_con_I_Fwd_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Fwd_ecr_r0)

    ## Junction 1:comp_con_I_Fwd_ecr_r0_junF
    comp_con_I_Fwd_ecr_r0_junF = bgt.new('1')
    model.add(comp_con_I_Fwd_ecr_r0_junF)

    ## Bond from comp_con_I_Fwd_ecr_r0_junF to (comp_con_I_Fwd_ecr_r0,0)
    bgt.connect(comp_con_I_Fwd_ecr_r0_junF,(comp_con_I_Fwd_ecr_r0,0))

    ## Junction 1:comp_con_I_Fwd_ecr_r0_junR
    comp_con_I_Fwd_ecr_r0_junR = bgt.new('1')
    model.add(comp_con_I_Fwd_ecr_r0_junR)

    ## Bond from (comp_con_I_Fwd_ecr_r0,1) to comp_con_I_Fwd_ecr_r0_junR
    bgt.connect((comp_con_I_Fwd_ecr_r0,1),comp_con_I_Fwd_ecr_r0_junR)

    ### Re:con_I_Fwd_ecr_r1

    ## Component Re:comp_con_I_Fwd_ecr_r1
    kappa_con_I_Fwd_ecr_r1 =  sp.symbols('kappa_con_I_Fwd_ecr_r1')
    RT = sp.symbols('RT')
    comp_con_I_Fwd_ecr_r1 = bgt.new('Re',name='con_I_Fwd_ecr_r1',value={'r':kappa_con_I_Fwd_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Fwd_ecr_r1)

    ## Junction 1:comp_con_I_Fwd_ecr_r1_junF
    comp_con_I_Fwd_ecr_r1_junF = bgt.new('1')
    model.add(comp_con_I_Fwd_ecr_r1_junF)

    ## Bond from comp_con_I_Fwd_ecr_r1_junF to (comp_con_I_Fwd_ecr_r1,0)
    bgt.connect(comp_con_I_Fwd_ecr_r1_junF,(comp_con_I_Fwd_ecr_r1,0))

    ## Junction 1:comp_con_I_Fwd_ecr_r1_junR
    comp_con_I_Fwd_ecr_r1_junR = bgt.new('1')
    model.add(comp_con_I_Fwd_ecr_r1_junR)

    ## Bond from (comp_con_I_Fwd_ecr_r1,1) to comp_con_I_Fwd_ecr_r1_junR
    bgt.connect((comp_con_I_Fwd_ecr_r1,1),comp_con_I_Fwd_ecr_r1_junR)

    ### Re:con_I_Fwd_ecr_r2

    ## Component Re:comp_con_I_Fwd_ecr_r2
    kappa_con_I_Fwd_ecr_r2 =  sp.symbols('kappa_con_I_Fwd_ecr_r2')
    RT = sp.symbols('RT')
    comp_con_I_Fwd_ecr_r2 = bgt.new('Re',name='con_I_Fwd_ecr_r2',value={'r':kappa_con_I_Fwd_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Fwd_ecr_r2)

    ## Junction 1:comp_con_I_Fwd_ecr_r2_junF
    comp_con_I_Fwd_ecr_r2_junF = bgt.new('1')
    model.add(comp_con_I_Fwd_ecr_r2_junF)

    ## Bond from comp_con_I_Fwd_ecr_r2_junF to (comp_con_I_Fwd_ecr_r2,0)
    bgt.connect(comp_con_I_Fwd_ecr_r2_junF,(comp_con_I_Fwd_ecr_r2,0))

    ## Junction 1:comp_con_I_Fwd_ecr_r2_junR
    comp_con_I_Fwd_ecr_r2_junR = bgt.new('1')
    model.add(comp_con_I_Fwd_ecr_r2_junR)

    ## Bond from (comp_con_I_Fwd_ecr_r2,1) to comp_con_I_Fwd_ecr_r2_junR
    bgt.connect((comp_con_I_Fwd_ecr_r2,1),comp_con_I_Fwd_ecr_r2_junR)

    ### Re:con_I_Rev_ecr_r0

    ## Component Re:comp_con_I_Rev_ecr_r0
    kappa_con_I_Rev_ecr_r0 =  sp.symbols('kappa_con_I_Rev_ecr_r0')
    RT = sp.symbols('RT')
    comp_con_I_Rev_ecr_r0 = bgt.new('Re',name='con_I_Rev_ecr_r0',value={'r':kappa_con_I_Rev_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Rev_ecr_r0)

    ## Junction 1:comp_con_I_Rev_ecr_r0_junF
    comp_con_I_Rev_ecr_r0_junF = bgt.new('1')
    model.add(comp_con_I_Rev_ecr_r0_junF)

    ## Bond from comp_con_I_Rev_ecr_r0_junF to (comp_con_I_Rev_ecr_r0,0)
    bgt.connect(comp_con_I_Rev_ecr_r0_junF,(comp_con_I_Rev_ecr_r0,0))

    ## Junction 1:comp_con_I_Rev_ecr_r0_junR
    comp_con_I_Rev_ecr_r0_junR = bgt.new('1')
    model.add(comp_con_I_Rev_ecr_r0_junR)

    ## Bond from (comp_con_I_Rev_ecr_r0,1) to comp_con_I_Rev_ecr_r0_junR
    bgt.connect((comp_con_I_Rev_ecr_r0,1),comp_con_I_Rev_ecr_r0_junR)

    ### Re:con_I_Rev_ecr_r1

    ## Component Re:comp_con_I_Rev_ecr_r1
    kappa_con_I_Rev_ecr_r1 =  sp.symbols('kappa_con_I_Rev_ecr_r1')
    RT = sp.symbols('RT')
    comp_con_I_Rev_ecr_r1 = bgt.new('Re',name='con_I_Rev_ecr_r1',value={'r':kappa_con_I_Rev_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Rev_ecr_r1)

    ## Junction 1:comp_con_I_Rev_ecr_r1_junF
    comp_con_I_Rev_ecr_r1_junF = bgt.new('1')
    model.add(comp_con_I_Rev_ecr_r1_junF)

    ## Bond from comp_con_I_Rev_ecr_r1_junF to (comp_con_I_Rev_ecr_r1,0)
    bgt.connect(comp_con_I_Rev_ecr_r1_junF,(comp_con_I_Rev_ecr_r1,0))

    ## Junction 1:comp_con_I_Rev_ecr_r1_junR
    comp_con_I_Rev_ecr_r1_junR = bgt.new('1')
    model.add(comp_con_I_Rev_ecr_r1_junR)

    ## Bond from (comp_con_I_Rev_ecr_r1,1) to comp_con_I_Rev_ecr_r1_junR
    bgt.connect((comp_con_I_Rev_ecr_r1,1),comp_con_I_Rev_ecr_r1_junR)

    ### Re:con_I_Rev_ecr_r2

    ## Component Re:comp_con_I_Rev_ecr_r2
    kappa_con_I_Rev_ecr_r2 =  sp.symbols('kappa_con_I_Rev_ecr_r2')
    RT = sp.symbols('RT')
    comp_con_I_Rev_ecr_r2 = bgt.new('Re',name='con_I_Rev_ecr_r2',value={'r':kappa_con_I_Rev_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_I_Rev_ecr_r2)

    ## Junction 1:comp_con_I_Rev_ecr_r2_junF
    comp_con_I_Rev_ecr_r2_junF = bgt.new('1')
    model.add(comp_con_I_Rev_ecr_r2_junF)

    ## Bond from comp_con_I_Rev_ecr_r2_junF to (comp_con_I_Rev_ecr_r2,0)
    bgt.connect(comp_con_I_Rev_ecr_r2_junF,(comp_con_I_Rev_ecr_r2,0))

    ## Junction 1:comp_con_I_Rev_ecr_r2_junR
    comp_con_I_Rev_ecr_r2_junR = bgt.new('1')
    model.add(comp_con_I_Rev_ecr_r2_junR)

    ## Bond from (comp_con_I_Rev_ecr_r2,1) to comp_con_I_Rev_ecr_r2_junR
    bgt.connect((comp_con_I_Rev_ecr_r2,1),comp_con_I_Rev_ecr_r2_junR)

    ### Re:con_P_Fwd_ecr_r0

    ## Component Re:comp_con_P_Fwd_ecr_r0
    kappa_con_P_Fwd_ecr_r0 =  sp.symbols('kappa_con_P_Fwd_ecr_r0')
    RT = sp.symbols('RT')
    comp_con_P_Fwd_ecr_r0 = bgt.new('Re',name='con_P_Fwd_ecr_r0',value={'r':kappa_con_P_Fwd_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Fwd_ecr_r0)

    ## Junction 1:comp_con_P_Fwd_ecr_r0_junF
    comp_con_P_Fwd_ecr_r0_junF = bgt.new('1')
    model.add(comp_con_P_Fwd_ecr_r0_junF)

    ## Bond from comp_con_P_Fwd_ecr_r0_junF to (comp_con_P_Fwd_ecr_r0,0)
    bgt.connect(comp_con_P_Fwd_ecr_r0_junF,(comp_con_P_Fwd_ecr_r0,0))

    ## Junction 1:comp_con_P_Fwd_ecr_r0_junR
    comp_con_P_Fwd_ecr_r0_junR = bgt.new('1')
    model.add(comp_con_P_Fwd_ecr_r0_junR)

    ## Bond from (comp_con_P_Fwd_ecr_r0,1) to comp_con_P_Fwd_ecr_r0_junR
    bgt.connect((comp_con_P_Fwd_ecr_r0,1),comp_con_P_Fwd_ecr_r0_junR)

    ### Re:con_P_Fwd_ecr_r1

    ## Component Re:comp_con_P_Fwd_ecr_r1
    kappa_con_P_Fwd_ecr_r1 =  sp.symbols('kappa_con_P_Fwd_ecr_r1')
    RT = sp.symbols('RT')
    comp_con_P_Fwd_ecr_r1 = bgt.new('Re',name='con_P_Fwd_ecr_r1',value={'r':kappa_con_P_Fwd_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Fwd_ecr_r1)

    ## Junction 1:comp_con_P_Fwd_ecr_r1_junF
    comp_con_P_Fwd_ecr_r1_junF = bgt.new('1')
    model.add(comp_con_P_Fwd_ecr_r1_junF)

    ## Bond from comp_con_P_Fwd_ecr_r1_junF to (comp_con_P_Fwd_ecr_r1,0)
    bgt.connect(comp_con_P_Fwd_ecr_r1_junF,(comp_con_P_Fwd_ecr_r1,0))

    ## Junction 1:comp_con_P_Fwd_ecr_r1_junR
    comp_con_P_Fwd_ecr_r1_junR = bgt.new('1')
    model.add(comp_con_P_Fwd_ecr_r1_junR)

    ## Bond from (comp_con_P_Fwd_ecr_r1,1) to comp_con_P_Fwd_ecr_r1_junR
    bgt.connect((comp_con_P_Fwd_ecr_r1,1),comp_con_P_Fwd_ecr_r1_junR)

    ### Re:con_P_Fwd_ecr_r2

    ## Component Re:comp_con_P_Fwd_ecr_r2
    kappa_con_P_Fwd_ecr_r2 =  sp.symbols('kappa_con_P_Fwd_ecr_r2')
    RT = sp.symbols('RT')
    comp_con_P_Fwd_ecr_r2 = bgt.new('Re',name='con_P_Fwd_ecr_r2',value={'r':kappa_con_P_Fwd_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Fwd_ecr_r2)

    ## Junction 1:comp_con_P_Fwd_ecr_r2_junF
    comp_con_P_Fwd_ecr_r2_junF = bgt.new('1')
    model.add(comp_con_P_Fwd_ecr_r2_junF)

    ## Bond from comp_con_P_Fwd_ecr_r2_junF to (comp_con_P_Fwd_ecr_r2,0)
    bgt.connect(comp_con_P_Fwd_ecr_r2_junF,(comp_con_P_Fwd_ecr_r2,0))

    ## Junction 1:comp_con_P_Fwd_ecr_r2_junR
    comp_con_P_Fwd_ecr_r2_junR = bgt.new('1')
    model.add(comp_con_P_Fwd_ecr_r2_junR)

    ## Bond from (comp_con_P_Fwd_ecr_r2,1) to comp_con_P_Fwd_ecr_r2_junR
    bgt.connect((comp_con_P_Fwd_ecr_r2,1),comp_con_P_Fwd_ecr_r2_junR)

    ### Re:con_P_Rev_ecr_r0

    ## Component Re:comp_con_P_Rev_ecr_r0
    kappa_con_P_Rev_ecr_r0 =  sp.symbols('kappa_con_P_Rev_ecr_r0')
    RT = sp.symbols('RT')
    comp_con_P_Rev_ecr_r0 = bgt.new('Re',name='con_P_Rev_ecr_r0',value={'r':kappa_con_P_Rev_ecr_r0,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Rev_ecr_r0)

    ## Junction 1:comp_con_P_Rev_ecr_r0_junF
    comp_con_P_Rev_ecr_r0_junF = bgt.new('1')
    model.add(comp_con_P_Rev_ecr_r0_junF)

    ## Bond from comp_con_P_Rev_ecr_r0_junF to (comp_con_P_Rev_ecr_r0,0)
    bgt.connect(comp_con_P_Rev_ecr_r0_junF,(comp_con_P_Rev_ecr_r0,0))

    ## Junction 1:comp_con_P_Rev_ecr_r0_junR
    comp_con_P_Rev_ecr_r0_junR = bgt.new('1')
    model.add(comp_con_P_Rev_ecr_r0_junR)

    ## Bond from (comp_con_P_Rev_ecr_r0,1) to comp_con_P_Rev_ecr_r0_junR
    bgt.connect((comp_con_P_Rev_ecr_r0,1),comp_con_P_Rev_ecr_r0_junR)

    ### Re:con_P_Rev_ecr_r1

    ## Component Re:comp_con_P_Rev_ecr_r1
    kappa_con_P_Rev_ecr_r1 =  sp.symbols('kappa_con_P_Rev_ecr_r1')
    RT = sp.symbols('RT')
    comp_con_P_Rev_ecr_r1 = bgt.new('Re',name='con_P_Rev_ecr_r1',value={'r':kappa_con_P_Rev_ecr_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Rev_ecr_r1)

    ## Junction 1:comp_con_P_Rev_ecr_r1_junF
    comp_con_P_Rev_ecr_r1_junF = bgt.new('1')
    model.add(comp_con_P_Rev_ecr_r1_junF)

    ## Bond from comp_con_P_Rev_ecr_r1_junF to (comp_con_P_Rev_ecr_r1,0)
    bgt.connect(comp_con_P_Rev_ecr_r1_junF,(comp_con_P_Rev_ecr_r1,0))

    ## Junction 1:comp_con_P_Rev_ecr_r1_junR
    comp_con_P_Rev_ecr_r1_junR = bgt.new('1')
    model.add(comp_con_P_Rev_ecr_r1_junR)

    ## Bond from (comp_con_P_Rev_ecr_r1,1) to comp_con_P_Rev_ecr_r1_junR
    bgt.connect((comp_con_P_Rev_ecr_r1,1),comp_con_P_Rev_ecr_r1_junR)

    ### Re:con_P_Rev_ecr_r2

    ## Component Re:comp_con_P_Rev_ecr_r2
    kappa_con_P_Rev_ecr_r2 =  sp.symbols('kappa_con_P_Rev_ecr_r2')
    RT = sp.symbols('RT')
    comp_con_P_Rev_ecr_r2 = bgt.new('Re',name='con_P_Rev_ecr_r2',value={'r':kappa_con_P_Rev_ecr_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_con_P_Rev_ecr_r2)

    ## Junction 1:comp_con_P_Rev_ecr_r2_junF
    comp_con_P_Rev_ecr_r2_junF = bgt.new('1')
    model.add(comp_con_P_Rev_ecr_r2_junF)

    ## Bond from comp_con_P_Rev_ecr_r2_junF to (comp_con_P_Rev_ecr_r2,0)
    bgt.connect(comp_con_P_Rev_ecr_r2_junF,(comp_con_P_Rev_ecr_r2,0))

    ## Junction 1:comp_con_P_Rev_ecr_r2_junR
    comp_con_P_Rev_ecr_r2_junR = bgt.new('1')
    model.add(comp_con_P_Rev_ecr_r2_junR)

    ## Bond from (comp_con_P_Rev_ecr_r2,1) to comp_con_P_Rev_ecr_r2_junR
    bgt.connect((comp_con_P_Rev_ecr_r2,1),comp_con_P_Rev_ecr_r2_junR)

    ### Re:sys_r1

    ## Component Re:comp_sys_r1
    kappa_sys_r1 =  sp.symbols('kappa_sys_r1')
    RT = sp.symbols('RT')
    comp_sys_r1 = bgt.new('Re',name='sys_r1',value={'r':kappa_sys_r1,'R':RT,'T':1},library='BioChem')
    model.add(comp_sys_r1)

    ## Junction 1:comp_sys_r1_junF
    comp_sys_r1_junF = bgt.new('1')
    model.add(comp_sys_r1_junF)

    ## Bond from comp_sys_r1_junF to (comp_sys_r1,0)
    bgt.connect(comp_sys_r1_junF,(comp_sys_r1,0))

    ## Junction 1:comp_sys_r1_junR
    comp_sys_r1_junR = bgt.new('1')
    model.add(comp_sys_r1_junR)

    ## Bond from (comp_sys_r1,1) to comp_sys_r1_junR
    bgt.connect((comp_sys_r1,1),comp_sys_r1_junR)

    ### Re:sys_r2

    ## Component Re:comp_sys_r2
    kappa_sys_r2 =  sp.symbols('kappa_sys_r2')
    RT = sp.symbols('RT')
    comp_sys_r2 = bgt.new('Re',name='sys_r2',value={'r':kappa_sys_r2,'R':RT,'T':1},library='BioChem')
    model.add(comp_sys_r2)

    ## Junction 1:comp_sys_r2_junF
    comp_sys_r2_junF = bgt.new('1')
    model.add(comp_sys_r2_junF)

    ## Bond from comp_sys_r2_junF to (comp_sys_r2,0)
    bgt.connect(comp_sys_r2_junF,(comp_sys_r2,0))

    ## Junction 1:comp_sys_r2_junR
    comp_sys_r2_junR = bgt.new('1')
    model.add(comp_sys_r2_junR)

    ## Bond from (comp_sys_r2,1) to comp_sys_r2_junR
    bgt.connect((comp_sys_r2,1),comp_sys_r2_junR)

    ### Re:sys_r3

    ## Component Re:comp_sys_r3
    kappa_sys_r3 =  sp.symbols('kappa_sys_r3')
    RT = sp.symbols('RT')
    comp_sys_r3 = bgt.new('Re',name='sys_r3',value={'r':kappa_sys_r3,'R':RT,'T':1},library='BioChem')
    model.add(comp_sys_r3)

    ## Junction 1:comp_sys_r3_junF
    comp_sys_r3_junF = bgt.new('1')
    model.add(comp_sys_r3_junF)

    ## Bond from comp_sys_r3_junF to (comp_sys_r3,0)
    bgt.connect(comp_sys_r3_junF,(comp_sys_r3,0))

    ## Junction 1:comp_sys_r3_junR
    comp_sys_r3_junR = bgt.new('1')
    model.add(comp_sys_r3_junR)

    ## Bond from (comp_sys_r3,1) to comp_sys_r3_junR
    bgt.connect((comp_sys_r3,1),comp_sys_r3_junR)

    ### Re:rd

    ## Component Re:comp_rd
    kappa_rd =  sp.symbols('kappa_rd')
    RT = sp.symbols('RT')
    comp_rd = bgt.new('Re',name='rd',value={'r':kappa_rd,'R':RT,'T':1},library='BioChem')
    model.add(comp_rd)

    ## Junction 1:comp_rd_junF
    comp_rd_junF = bgt.new('1')
    model.add(comp_rd_junF)

    ## Bond from comp_rd_junF to (comp_rd,0)
    bgt.connect(comp_rd_junF,(comp_rd,0))

    ## Junction 1:comp_rd_junR
    comp_rd_junR = bgt.new('1')
    model.add(comp_rd_junR)

    ## Bond from (comp_rd,1) to comp_rd_junR
    bgt.connect((comp_rd,1),comp_rd_junR)
    ### Connections

    ### Ce:P to Re:con_I_Fwd_ecr_r0

    ## Bond from comp_P_jun to comp_con_I_Fwd_ecr_r0_junF
    bgt.connect(comp_P_jun,comp_con_I_Fwd_ecr_r0_junF)

    ### Ce:P to Re:con_I_Fwd_ecr_r0

    ## Bond from comp_P_jun to comp_con_I_Fwd_ecr_r0_junF
    bgt.connect(comp_P_jun,comp_con_I_Fwd_ecr_r0_junF)

    ### Ce:P to Re:con_I_Fwd_ecr_r0

    ## Bond from comp_P_jun to comp_con_I_Fwd_ecr_r0_junF
    bgt.connect(comp_P_jun,comp_con_I_Fwd_ecr_r0_junF)

    ### Ce:P to Re:con_I_Fwd_ecr_r0

    ## Bond from comp_P_jun to comp_con_I_Fwd_ecr_r0_junF
    bgt.connect(comp_P_jun,comp_con_I_Fwd_ecr_r0_junF)

    ### Ce:P to Re:con_P_Fwd_ecr_r0

    ## Bond from comp_P_jun to comp_con_P_Fwd_ecr_r0_junF
    bgt.connect(comp_P_jun,comp_con_P_Fwd_ecr_r0_junF)

    ### Ce:P to Re:con_P_Fwd_ecr_r0

    ## Bond from comp_P_jun to comp_con_P_Fwd_ecr_r0_junF
    bgt.connect(comp_P_jun,comp_con_P_Fwd_ecr_r0_junF)

    ### Ce:P to Re:con_P_Fwd_ecr_r0

    ## Bond from comp_P_jun to comp_con_P_Fwd_ecr_r0_junF
    bgt.connect(comp_P_jun,comp_con_P_Fwd_ecr_r0_junF)

    ### Ce:P to Re:con_P_Fwd_ecr_r0

    ## Bond from comp_P_jun to comp_con_P_Fwd_ecr_r0_junF
    bgt.connect(comp_P_jun,comp_con_P_Fwd_ecr_r0_junF)

    ### Ce:P to Re:rd

    ## Bond from comp_P_jun to comp_rd_junF
    bgt.connect(comp_P_jun,comp_rd_junF)

    ### Ce:P0 to Re:con_I_Rev_ecr_r0

    ## Bond from comp_P0_jun to comp_con_I_Rev_ecr_r0_junF
    bgt.connect(comp_P0_jun,comp_con_I_Rev_ecr_r0_junF)

    ### Ce:P0 to Re:con_I_Rev_ecr_r0

    ## Bond from comp_P0_jun to comp_con_I_Rev_ecr_r0_junF
    bgt.connect(comp_P0_jun,comp_con_I_Rev_ecr_r0_junF)

    ### Ce:P0 to Re:con_I_Rev_ecr_r0

    ## Bond from comp_P0_jun to comp_con_I_Rev_ecr_r0_junF
    bgt.connect(comp_P0_jun,comp_con_I_Rev_ecr_r0_junF)

    ### Ce:P0 to Re:con_I_Rev_ecr_r0

    ## Bond from comp_P0_jun to comp_con_I_Rev_ecr_r0_junF
    bgt.connect(comp_P0_jun,comp_con_I_Rev_ecr_r0_junF)

    ### Ce:P0 to Re:con_P_Rev_ecr_r0

    ## Bond from comp_P0_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_P0_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:P0 to Re:con_P_Rev_ecr_r0

    ## Bond from comp_P0_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_P0_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:P0 to Re:con_P_Rev_ecr_r0

    ## Bond from comp_P0_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_P0_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:P0 to Re:con_P_Rev_ecr_r0

    ## Bond from comp_P0_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_P0_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:S to Re:con_P_Rev_ecr_r1

    ## Bond from comp_S_jun to comp_con_P_Rev_ecr_r1_junF
    bgt.connect(comp_S_jun,comp_con_P_Rev_ecr_r1_junF)

    ### Ce:S to Re:sys_r1

    ## Bond from comp_S_jun to comp_sys_r1_junF
    bgt.connect(comp_S_jun,comp_sys_r1_junF)

    ### Ce:con_I_Fwd_ecr_C to Re:con_I_Fwd_ecr_r2

    ## Bond from comp_con_I_Fwd_ecr_C_jun to comp_con_I_Fwd_ecr_r2_junF
    bgt.connect(comp_con_I_Fwd_ecr_C_jun,comp_con_I_Fwd_ecr_r2_junF)

    ### Ce:con_I_Fwd_ecr_E to Re:con_I_Fwd_ecr_r0

    ## Bond from comp_con_I_Fwd_ecr_E_jun to comp_con_I_Fwd_ecr_r0_junF
    bgt.connect(comp_con_I_Fwd_ecr_E_jun,comp_con_I_Fwd_ecr_r0_junF)

    ### Ce:con_I_Fwd_ecr_E to Re:con_I_Fwd_ecr_r1

    ## Bond from comp_con_I_Fwd_ecr_E_jun to comp_con_I_Fwd_ecr_r1_junF
    bgt.connect(comp_con_I_Fwd_ecr_E_jun,comp_con_I_Fwd_ecr_r1_junF)

    ### Ce:con_I_Fwd_ecr_F to Re:con_I_Fwd_ecr_r1

    ## Bond from comp_con_I_Fwd_ecr_F_jun to comp_con_I_Fwd_ecr_r1_junF
    bgt.connect(comp_con_I_Fwd_ecr_F_jun,comp_con_I_Fwd_ecr_r1_junF)

    ### Ce:con_I_Rev_ecr_C to Re:con_I_Rev_ecr_r2

    ## Bond from comp_con_I_Rev_ecr_C_jun to comp_con_I_Rev_ecr_r2_junF
    bgt.connect(comp_con_I_Rev_ecr_C_jun,comp_con_I_Rev_ecr_r2_junF)

    ### Ce:con_I_Rev_ecr_E to Re:con_I_Rev_ecr_r0

    ## Bond from comp_con_I_Rev_ecr_E_jun to comp_con_I_Rev_ecr_r0_junF
    bgt.connect(comp_con_I_Rev_ecr_E_jun,comp_con_I_Rev_ecr_r0_junF)

    ### Ce:con_I_Rev_ecr_E to Re:con_I_Rev_ecr_r1

    ## Bond from comp_con_I_Rev_ecr_E_jun to comp_con_I_Rev_ecr_r1_junF
    bgt.connect(comp_con_I_Rev_ecr_E_jun,comp_con_I_Rev_ecr_r1_junF)

    ### Ce:con_I_Rev_ecr_F to Re:con_I_Rev_ecr_r1

    ## Bond from comp_con_I_Rev_ecr_F_jun to comp_con_I_Rev_ecr_r1_junF
    bgt.connect(comp_con_I_Rev_ecr_F_jun,comp_con_I_Rev_ecr_r1_junF)

    ### Ce:con_P_Fwd_ecr_C to Re:con_P_Fwd_ecr_r2

    ## Bond from comp_con_P_Fwd_ecr_C_jun to comp_con_P_Fwd_ecr_r2_junF
    bgt.connect(comp_con_P_Fwd_ecr_C_jun,comp_con_P_Fwd_ecr_r2_junF)

    ### Ce:con_P_Fwd_ecr_E to Re:con_P_Fwd_ecr_r0

    ## Bond from comp_con_P_Fwd_ecr_E_jun to comp_con_P_Fwd_ecr_r0_junF
    bgt.connect(comp_con_P_Fwd_ecr_E_jun,comp_con_P_Fwd_ecr_r0_junF)

    ### Ce:con_P_Fwd_ecr_E to Re:con_P_Fwd_ecr_r1

    ## Bond from comp_con_P_Fwd_ecr_E_jun to comp_con_P_Fwd_ecr_r1_junF
    bgt.connect(comp_con_P_Fwd_ecr_E_jun,comp_con_P_Fwd_ecr_r1_junF)

    ### Ce:con_P_Fwd_ecr_F to Re:con_P_Fwd_ecr_r1

    ## Bond from comp_con_P_Fwd_ecr_F_jun to comp_con_P_Fwd_ecr_r1_junF
    bgt.connect(comp_con_P_Fwd_ecr_F_jun,comp_con_P_Fwd_ecr_r1_junF)

    ### Ce:con_P_Rev_ecr_C to Re:con_P_Rev_ecr_r2

    ## Bond from comp_con_P_Rev_ecr_C_jun to comp_con_P_Rev_ecr_r2_junF
    bgt.connect(comp_con_P_Rev_ecr_C_jun,comp_con_P_Rev_ecr_r2_junF)

    ### Ce:con_P_Rev_ecr_E to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_P_Rev_ecr_E_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_P_Rev_ecr_E_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_P_Rev_ecr_E to Re:con_P_Rev_ecr_r1

    ## Bond from comp_con_P_Rev_ecr_E_jun to comp_con_P_Rev_ecr_r1_junF
    bgt.connect(comp_con_P_Rev_ecr_E_jun,comp_con_P_Rev_ecr_r1_junF)

    ### Ce:con_P_Rev_ecr_F to Re:con_P_Rev_ecr_r1

    ## Bond from comp_con_P_Rev_ecr_F_jun to comp_con_P_Rev_ecr_r1_junF
    bgt.connect(comp_con_P_Rev_ecr_F_jun,comp_con_P_Rev_ecr_r1_junF)

    ### Ce:con_A to Re:con_I_Fwd_ecr_r1

    ## Bond from comp_con_A_jun to comp_con_I_Fwd_ecr_r1_junF
    bgt.connect(comp_con_A_jun,comp_con_I_Fwd_ecr_r1_junF)

    ### Ce:con_A to Re:con_P_Fwd_ecr_r1

    ## Bond from comp_con_A_jun to comp_con_P_Fwd_ecr_r1_junF
    bgt.connect(comp_con_A_jun,comp_con_P_Fwd_ecr_r1_junF)

    ### Ce:con_Int to Re:con_I_Rev_ecr_r1

    ## Bond from comp_con_Int_jun to comp_con_I_Rev_ecr_r1_junF
    bgt.connect(comp_con_Int_jun,comp_con_I_Rev_ecr_r1_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:con_Int to Re:con_P_Rev_ecr_r0

    ## Bond from comp_con_Int_jun to comp_con_P_Rev_ecr_r0_junF
    bgt.connect(comp_con_Int_jun,comp_con_P_Rev_ecr_r0_junF)

    ### Ce:sys_I1 to Re:sys_r2

    ## Bond from comp_sys_I1_jun to comp_sys_r2_junF
    bgt.connect(comp_sys_I1_jun,comp_sys_r2_junF)

    ### Ce:sys_I2 to Re:sys_r3

    ## Bond from comp_sys_I2_jun to comp_sys_r3_junF
    bgt.connect(comp_sys_I2_jun,comp_sys_r3_junF)

    ### Re:rd to Ce:D

    ## Bond from comp_rd_junR to comp_D_jun
    bgt.connect(comp_rd_junR,comp_D_jun)

    ### Re:con_I_Rev_ecr_r0 to Ce:P

    ## Bond from comp_con_I_Rev_ecr_r0_junR to comp_P_jun
    bgt.connect(comp_con_I_Rev_ecr_r0_junR,comp_P_jun)

    ### Re:con_I_Rev_ecr_r0 to Ce:P

    ## Bond from comp_con_I_Rev_ecr_r0_junR to comp_P_jun
    bgt.connect(comp_con_I_Rev_ecr_r0_junR,comp_P_jun)

    ### Re:con_I_Rev_ecr_r0 to Ce:P

    ## Bond from comp_con_I_Rev_ecr_r0_junR to comp_P_jun
    bgt.connect(comp_con_I_Rev_ecr_r0_junR,comp_P_jun)

    ### Re:con_I_Rev_ecr_r0 to Ce:P

    ## Bond from comp_con_I_Rev_ecr_r0_junR to comp_P_jun
    bgt.connect(comp_con_I_Rev_ecr_r0_junR,comp_P_jun)

    ### Re:con_P_Rev_ecr_r0 to Ce:P

    ## Bond from comp_con_P_Rev_ecr_r0_junR to comp_P_jun
    bgt.connect(comp_con_P_Rev_ecr_r0_junR,comp_P_jun)

    ### Re:con_P_Rev_ecr_r0 to Ce:P

    ## Bond from comp_con_P_Rev_ecr_r0_junR to comp_P_jun
    bgt.connect(comp_con_P_Rev_ecr_r0_junR,comp_P_jun)

    ### Re:con_P_Rev_ecr_r0 to Ce:P

    ## Bond from comp_con_P_Rev_ecr_r0_junR to comp_P_jun
    bgt.connect(comp_con_P_Rev_ecr_r0_junR,comp_P_jun)

    ### Re:con_P_Rev_ecr_r0 to Ce:P

    ## Bond from comp_con_P_Rev_ecr_r0_junR to comp_P_jun
    bgt.connect(comp_con_P_Rev_ecr_r0_junR,comp_P_jun)

    ### Re:sys_r3 to Ce:P

    ## Bond from comp_sys_r3_junR to comp_P_jun
    bgt.connect(comp_sys_r3_junR,comp_P_jun)

    ### Re:con_I_Fwd_ecr_r0 to Ce:P0

    ## Bond from comp_con_I_Fwd_ecr_r0_junR to comp_P0_jun
    bgt.connect(comp_con_I_Fwd_ecr_r0_junR,comp_P0_jun)

    ### Re:con_I_Fwd_ecr_r0 to Ce:P0

    ## Bond from comp_con_I_Fwd_ecr_r0_junR to comp_P0_jun
    bgt.connect(comp_con_I_Fwd_ecr_r0_junR,comp_P0_jun)

    ### Re:con_I_Fwd_ecr_r0 to Ce:P0

    ## Bond from comp_con_I_Fwd_ecr_r0_junR to comp_P0_jun
    bgt.connect(comp_con_I_Fwd_ecr_r0_junR,comp_P0_jun)

    ### Re:con_I_Fwd_ecr_r0 to Ce:P0

    ## Bond from comp_con_I_Fwd_ecr_r0_junR to comp_P0_jun
    bgt.connect(comp_con_I_Fwd_ecr_r0_junR,comp_P0_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:P0

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_P0_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_P0_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:P0

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_P0_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_P0_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:P0

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_P0_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_P0_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:P0

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_P0_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_P0_jun)

    ### Re:con_P_Fwd_ecr_r2 to Ce:S

    ## Bond from comp_con_P_Fwd_ecr_r2_junR to comp_S_jun
    bgt.connect(comp_con_P_Fwd_ecr_r2_junR,comp_S_jun)

    ### Re:con_I_Fwd_ecr_r1 to Ce:con_I_Fwd_ecr_C

    ## Bond from comp_con_I_Fwd_ecr_r1_junR to comp_con_I_Fwd_ecr_C_jun
    bgt.connect(comp_con_I_Fwd_ecr_r1_junR,comp_con_I_Fwd_ecr_C_jun)

    ### Re:con_I_Fwd_ecr_r2 to Ce:con_I_Fwd_ecr_E

    ## Bond from comp_con_I_Fwd_ecr_r2_junR to comp_con_I_Fwd_ecr_E_jun
    bgt.connect(comp_con_I_Fwd_ecr_r2_junR,comp_con_I_Fwd_ecr_E_jun)

    ### Re:con_I_Fwd_ecr_r0 to Ce:con_I_Fwd_ecr_E0

    ## Bond from comp_con_I_Fwd_ecr_r0_junR to comp_con_I_Fwd_ecr_E0_jun
    bgt.connect(comp_con_I_Fwd_ecr_r0_junR,comp_con_I_Fwd_ecr_E0_jun)

    ### Re:con_I_Fwd_ecr_r2 to Ce:con_I_Fwd_ecr_G

    ## Bond from comp_con_I_Fwd_ecr_r2_junR to comp_con_I_Fwd_ecr_G_jun
    bgt.connect(comp_con_I_Fwd_ecr_r2_junR,comp_con_I_Fwd_ecr_G_jun)

    ### Re:con_I_Rev_ecr_r1 to Ce:con_I_Rev_ecr_C

    ## Bond from comp_con_I_Rev_ecr_r1_junR to comp_con_I_Rev_ecr_C_jun
    bgt.connect(comp_con_I_Rev_ecr_r1_junR,comp_con_I_Rev_ecr_C_jun)

    ### Re:con_I_Rev_ecr_r2 to Ce:con_I_Rev_ecr_E

    ## Bond from comp_con_I_Rev_ecr_r2_junR to comp_con_I_Rev_ecr_E_jun
    bgt.connect(comp_con_I_Rev_ecr_r2_junR,comp_con_I_Rev_ecr_E_jun)

    ### Re:con_I_Rev_ecr_r0 to Ce:con_I_Rev_ecr_E0

    ## Bond from comp_con_I_Rev_ecr_r0_junR to comp_con_I_Rev_ecr_E0_jun
    bgt.connect(comp_con_I_Rev_ecr_r0_junR,comp_con_I_Rev_ecr_E0_jun)

    ### Re:con_I_Rev_ecr_r2 to Ce:con_I_Rev_ecr_G

    ## Bond from comp_con_I_Rev_ecr_r2_junR to comp_con_I_Rev_ecr_G_jun
    bgt.connect(comp_con_I_Rev_ecr_r2_junR,comp_con_I_Rev_ecr_G_jun)

    ### Re:con_P_Fwd_ecr_r1 to Ce:con_P_Fwd_ecr_C

    ## Bond from comp_con_P_Fwd_ecr_r1_junR to comp_con_P_Fwd_ecr_C_jun
    bgt.connect(comp_con_P_Fwd_ecr_r1_junR,comp_con_P_Fwd_ecr_C_jun)

    ### Re:con_P_Fwd_ecr_r2 to Ce:con_P_Fwd_ecr_E

    ## Bond from comp_con_P_Fwd_ecr_r2_junR to comp_con_P_Fwd_ecr_E_jun
    bgt.connect(comp_con_P_Fwd_ecr_r2_junR,comp_con_P_Fwd_ecr_E_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_P_Fwd_ecr_E0

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_P_Fwd_ecr_E0_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_P_Fwd_ecr_E0_jun)

    ### Re:con_P_Fwd_ecr_r2 to Ce:con_P_Fwd_ecr_G

    ## Bond from comp_con_P_Fwd_ecr_r2_junR to comp_con_P_Fwd_ecr_G_jun
    bgt.connect(comp_con_P_Fwd_ecr_r2_junR,comp_con_P_Fwd_ecr_G_jun)

    ### Re:con_P_Rev_ecr_r1 to Ce:con_P_Rev_ecr_C

    ## Bond from comp_con_P_Rev_ecr_r1_junR to comp_con_P_Rev_ecr_C_jun
    bgt.connect(comp_con_P_Rev_ecr_r1_junR,comp_con_P_Rev_ecr_C_jun)

    ### Re:con_P_Rev_ecr_r2 to Ce:con_P_Rev_ecr_E

    ## Bond from comp_con_P_Rev_ecr_r2_junR to comp_con_P_Rev_ecr_E_jun
    bgt.connect(comp_con_P_Rev_ecr_r2_junR,comp_con_P_Rev_ecr_E_jun)

    ### Re:con_P_Rev_ecr_r0 to Ce:con_P_Rev_ecr_E0

    ## Bond from comp_con_P_Rev_ecr_r0_junR to comp_con_P_Rev_ecr_E0_jun
    bgt.connect(comp_con_P_Rev_ecr_r0_junR,comp_con_P_Rev_ecr_E0_jun)

    ### Re:con_P_Rev_ecr_r2 to Ce:con_P_Rev_ecr_G

    ## Bond from comp_con_P_Rev_ecr_r2_junR to comp_con_P_Rev_ecr_G_jun
    bgt.connect(comp_con_P_Rev_ecr_r2_junR,comp_con_P_Rev_ecr_G_jun)

    ### Re:con_I_Rev_ecr_r2 to Ce:con_A

    ## Bond from comp_con_I_Rev_ecr_r2_junR to comp_con_A_jun
    bgt.connect(comp_con_I_Rev_ecr_r2_junR,comp_con_A_jun)

    ### Re:con_P_Rev_ecr_r2 to Ce:con_A

    ## Bond from comp_con_P_Rev_ecr_r2_junR to comp_con_A_jun
    bgt.connect(comp_con_P_Rev_ecr_r2_junR,comp_con_A_jun)

    ### Re:con_I_Fwd_ecr_r2 to Ce:con_Int

    ## Bond from comp_con_I_Fwd_ecr_r2_junR to comp_con_Int_jun
    bgt.connect(comp_con_I_Fwd_ecr_r2_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:con_P_Fwd_ecr_r0 to Ce:con_Int

    ## Bond from comp_con_P_Fwd_ecr_r0_junR to comp_con_Int_jun
    bgt.connect(comp_con_P_Fwd_ecr_r0_junR,comp_con_Int_jun)

    ### Re:sys_r1 to Ce:sys_I1

    ## Bond from comp_sys_r1_junR to comp_sys_I1_jun
    bgt.connect(comp_sys_r1_junR,comp_sys_I1_jun)

    ### Re:sys_r2 to Ce:sys_I2

    ## Bond from comp_sys_r2_junR to comp_sys_I2_jun
    bgt.connect(comp_sys_r2_junR,comp_sys_I2_jun)

    return model
