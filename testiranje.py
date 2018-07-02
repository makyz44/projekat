import os
import random
import time
import funkcije
import kombinacije

def heuristika2():
    nazkolone=[kombinacije.nazkombd[:], kombinacije.nazkombg[:], kombinacije.nazkombsp1[:], kombinacije.nazkombsp2[:], kombinacije.nazkombun1[:], kombinacije.nazkombun2[:], kombinacije.nazkombs[:]]
    reznazkolone=[kombinacije.reznazkombd[:], kombinacije.reznazkombg[:], kombinacije.reznazkombsp1[:], kombinacije.reznazkombsp2[:], kombinacije.reznazkombun1[:], kombinacije.reznazkombun2[:], kombinacije.reznazkombs[:]]
    vredkolone=[kombinacije.vredkombd[:], kombinacije.vredkombg[:], kombinacije.vredkombsp1[:], kombinacije.vredkombsp2[:], kombinacije.vredkombun1[:], kombinacije.vredkombun2[:], kombinacije.vredkombs[:]]
    rezvredkolone=[kombinacije.rezvredkombd[:], kombinacije.rezvredkombg[:], kombinacije.rezvredkombsp1[:], kombinacije.rezvredkombsp2[:], kombinacije.rezvredkombun1[:], kombinacije.rezvredkombun2[:], kombinacije.rezvredkombs[:]]

    brojpoteza=65
    brojac=0
    while brojac<brojpoteza:
        nizkombinacije = []
        nizkombinacijes=[]
        nizverovatnoce = []
        nizverovatnoces=[]
        refver=0
        refvers=0
        z=0
        z1=0
        zs=0
        x=funkcije.prvobacanje()
        for i in range(len(nazkolone)-1):
            if len(nazkolone[i])==0:
                l="*"
            else:
                l=nazkolone[i][0]
            nz=funkcije.najpogodnijiniz(x, l)
            nizkombinacije.append(nz)
            ver=funkcije.vrv(x, nz)
            nizverovatnoce.append(ver)
            if ver>refver:
                 refver=ver
                 z=i
        if funkcije.vrv(x, nizkombinacije[z]) == 1:
            vredkolone[z][0]=funkcije.bodovi(x, nazkolone[z][0])
            rezvredkolone[z].append(vredkolone[z].pop(0))
            reznazkolone[z].append(nazkolone[z].pop(0))
        else:
                n1=funkcije.zamena(x, nizkombinacije[z])
                for i in range(len(nazkolone)-1):
                    if len(nazkolone[i])==0:
                        l="*"
                    else:
                        l=nazkolone[i][0]
                    nz=funkcije.najpogodnijiniz(n1, l)
                    nizkombinacije.append(nz)
                    ver=funkcije.vrv(n1, nz)
                    nizverovatnoce.append(ver)
                    if ver>refver:
                        refver=ver
                        z=i
                if funkcije.vrv(n1, nizkombinacije[z]) == 1:
                    vredkolone[z][0]=funkcije.bodovi(n1, nazkolone[z][0])
                    rezvredkolone[z].append(vredkolone[z].pop(0))
                    reznazkolone[z].append(nazkolone[z].pop(0))###############
                else:
                        n2=funkcije.zamena(n1, nizkombinacije[z])
                        for i in range(len(nazkolone)-1):
                            if len(nazkolone[i])==0:
                                l="*"
                            else:
                                l=nazkolone[i][0]
                        nz=funkcije.najpogodnijiniz(n2, l)
                        nizkombinacije.append(nz)
                        ver=funkcije.vrv(n2, nz)
                        nizverovatnoce.append(ver)
                        if ver>refver:
                            refver=ver
                            z=i
                        if funkcije.vrv(n2, nizkombinacije[z]) == 1:
                            vredkolone[z][0]=funkcije.bodovi(n2, nazkolone[z][0])
                            rezvredkolone[z].append(vredkolone[z].pop(0))
                            reznazkolone[z].append(nazkolone[z].pop(0))###############
                        else:
                                for i in range(len(nazkolone[6])):
                                    if len(nazkolone[6])==0:
                                        m="*"
                                    else:
                                        m=nazkolone[6][i]
                                    nzs=funkcije.najpogodnijiniz(n2, m)
                                    nizkombinacijes.append(nzs)
                                    vers=funkcije.vrv(n2, nzs)
                                    nizverovatnoces.append(vers)
                                    if vers>refvers:
                                            refvers=vers
                                            zs=i
                                if funkcije.vrv(n2, nizkombinacijes[zs]) == 1:
                                    vredkolone[6][zs]=funkcije.bodovi(n2, nazkolone[6][zs])
                                    rezvredkolone[6].append(vredkolone[6].pop(zs))
                                    reznazkolone[6].append(nazkolone[6].pop(zs))
                                else:
                                    if len(vredkolone[z])!=0 or len(nazkolone[z])!=0:
                                        vredkolone[z][0]=funkcije.bodovi(n2, vredkolone[z][0])
                                        rezvredkolone[z].append(vredkolone[z].pop(0))
                                        reznazkolone[z].append(nazkolone[z].pop(0))
                                    else:
                                        continue
            
        brojac=brojac+1

    brojbodova0=funkcije.suma(rezvredkolone[0])-rezvredkolone[0][6]-rezvredkolone[0][7]+rezvredkolone[0][6]-rezvredkolone[0][7]
    brojbodova1=funkcije.suma(rezvredkolone[1])-(rezvredkolone[1][5]+rezvredkolone[1][6])+(rezvredkolone[1][6]-rezvredkolone[1][5])
    brojbodova34=funkcije.suma(rezvredkolone[2])+funkcije.suma(rezvredkolone[3])-(rezvredkolone[2][0]+rezvredkolone[3][0])+(rezvredkolone[2][0]-rezvredkolone[3][0])
    brojbodova56=funkcije.suma(rezvredkolone[4])+funkcije.suma(rezvredkolone[5])-(rezvredkolone[4][6]+rezvredkolone[5][5])+(rezvredkolone[4][6]-rezvredkolone[5][5])
    brojbodovaslobodne=funkcije.suma(rezvredkolone[6])-(rezvredkolone[6][6]+rezvredkolone[6][7])+(rezvredkolone[6][6]-rezvredkolone[6][7])
    bonus1=0
    bonus11=0
    bonus22=0
    bonus33=0
    bonus44=0
    bonus1=0
    for i in range(6):
        bonus1=bonus1+rezvredkolone[0][i]
    if bonus1>=60:
        bonus11=30
    bonus2=0
    for i in range(7, 13):
        bonus2=bonus2+rezvredkolone[1][i]
    if bonus2>=60:
        bonus22=30
    bonus3=0
    for i in range(1, 7):
        bonus3=bonus3+rezvredkolone[2][i]
    if bonus3>=60:
        bonus33=30
    bonus4=0
    for i in range(6):
        bonus4=bonus4+rezvredkolone[5][i]
    if bonus4>=60:
        bonus44=30
    ukupnobodova=brojbodova0+brojbodova1+brojbodova34+brojbodova56+brojbodovaslobodne+bonus11+bonus22+bonus33+bonus44
    return ukupnobodova


def randheuristika():
    nazkolone=[kombinacije.nazkombd[:], kombinacije.nazkombg[:], kombinacije.nazkombsp1[:], kombinacije.nazkombsp2[:], kombinacije.nazkombun1[:], kombinacije.nazkombun2[:], kombinacije.nazkombs[:]]
    reznazkolone=[kombinacije.reznazkombd[:], kombinacije.reznazkombg[:], kombinacije.reznazkombsp1[:], kombinacije.reznazkombsp2[:], kombinacije.reznazkombun1[:], kombinacije.reznazkombun2[:], kombinacije.reznazkombs[:]]
    vredkolone=[kombinacije.vredkombd[:], kombinacije.vredkombg[:], kombinacije.vredkombsp1[:], kombinacije.vredkombsp2[:], kombinacije.vredkombun1[:], kombinacije.vredkombun2[:], kombinacije.vredkombs[:]]
    rezvredkolone=[kombinacije.rezvredkombd[:], kombinacije.rezvredkombg[:], kombinacije.rezvredkombsp1[:], kombinacije.rezvredkombsp2[:], kombinacije.rezvredkombun1[:], kombinacije.rezvredkombun2[:], kombinacije.rezvredkombs[:]]

    brojpoteza=65
    brojac=0
    brojac2=0
    k=12
    while brojac<brojpoteza:
        x=funkcije.prvobacanje()
        ind=random.randint(1, 2)
        index=[]
        if ind==1 and brojac2<52:
            z=random.randint(0, 5)
            while len(nazkolone[z])==0:
                z=random.randint(0, 5)
            vredkolone[z][0]=funkcije.bodovi(x, nazkolone[z][0])
            rezvredkolone[z].append(vredkolone[z].pop(0))
            reznazkolone[z].append(nazkolone[z].pop(0))
            brojac2=brojac2+1 ######################################
        elif ind==2 and len(nazkolone[6])!=0:
                m=random.randint(0, k)
                vredkolone[6][m]=funkcije.bodovi(x, nazkolone[6][m])
                rezvredkolone[6].append(vredkolone[6].pop(m))
                reznazkolone[6].append(nazkolone[6].pop(m))
                k=k-1
        else:
            continue
        brojac=brojac+1

    brojbodova0=funkcije.suma(rezvredkolone[0])-rezvredkolone[0][6]-rezvredkolone[0][7]+rezvredkolone[0][6]-rezvredkolone[0][7]
    brojbodova1=funkcije.suma(rezvredkolone[1])-(rezvredkolone[1][5]+rezvredkolone[1][6])+(rezvredkolone[1][6]-rezvredkolone[1][5])
    brojbodova34=funkcije.suma(rezvredkolone[2])+funkcije.suma(rezvredkolone[3])-(rezvredkolone[2][0]+rezvredkolone[3][0])+(rezvredkolone[2][0]-rezvredkolone[3][0])
    brojbodova56=funkcije.suma(rezvredkolone[4])+funkcije.suma(rezvredkolone[5])-(rezvredkolone[4][6]+rezvredkolone[5][5])+(rezvredkolone[4][6]-rezvredkolone[5][5])
    brojbodovaslobodne=funkcije.suma(rezvredkolone[6])-(rezvredkolone[6][6]+rezvredkolone[6][7])+(rezvredkolone[6][6]-rezvredkolone[6][7])
    bonus1=0
    bonus11=0
    bonus22=0
    bonus33=0
    bonus44=0
    bonus1=0
    for i in range(6):
        bonus1=bonus1+rezvredkolone[0][i]
    if bonus1>=60:
        bonus11=30
    bonus2=0
    for i in range(7, 13):
        bonus2=bonus2+rezvredkolone[1][i]
    if bonus2>=60:
        bonus22=30
    bonus3=0
    for i in range(1, 7):
        bonus3=bonus3+rezvredkolone[2][i]
    if bonus3>=60:
        bonus33=30
    bonus4=0
    for i in range(6):
        bonus4=bonus4+rezvredkolone[5][i]
    if bonus4>=60:
        bonus44=30
    ukupnobodova=brojbodova0+brojbodova1+brojbodova34+brojbodova56+brojbodovaslobodne+bonus11+bonus22+bonus33+bonus44
    return ukupnobodova

def heuristika1():
    nazkolone=[kombinacije.nazkombd[:], kombinacije.nazkombg[:], kombinacije.nazkombsp1[:], kombinacije.nazkombsp2[:], kombinacije.nazkombun1[:], kombinacije.nazkombun2[:], kombinacije.nazkombs[:]]
    reznazkolone=[kombinacije.reznazkombd[:], kombinacije.reznazkombg[:], kombinacije.reznazkombsp1[:], kombinacije.reznazkombsp2[:], kombinacije.reznazkombun1[:], kombinacije.reznazkombun2[:], kombinacije.reznazkombs[:]]
    vredkolone=[kombinacije.vredkombd[:], kombinacije.vredkombg[:], kombinacije.vredkombsp1[:], kombinacije.vredkombsp2[:], kombinacije.vredkombun1[:], kombinacije.vredkombun2[:], kombinacije.vredkombs[:]]
    rezvredkolone=[kombinacije.rezvredkombd[:], kombinacije.rezvredkombg[:], kombinacije.rezvredkombsp1[:], kombinacije.rezvredkombsp2[:], kombinacije.rezvredkombun1[:], kombinacije.rezvredkombun2[:], kombinacije.rezvredkombs[:]]

    brojpoteza=65
    brojac=0
    while brojac<brojpoteza:
        nizkombinacije = []
        nizkombinacijes=[]
        nizverovatnoce = []
        nizverovatnoces=[]
        refver=0
        refvers=0
        z=0
        z1=0
        zs=0
        x=funkcije.prvobacanje()
        for i in range(len(nazkolone)-1):
            if len(nazkolone[i])==0:
              l="*"
            else:
                l=nazkolone[i][0]
            nz=funkcije.najpogodnijiniz(x, l)
            nizkombinacije.append(nz)
            ver=funkcije.vrv(x, nz)
            nizverovatnoce.append(ver)
            if ver>refver:
                refver=ver
                z=i
        if funkcije.vrv(x, nizkombinacije[z]) == 1:
            vredkolone[z][0]=funkcije.bodovi(x, nazkolone[z][0])
            rezvredkolone[z].append(vredkolone[z].pop(0))
            reznazkolone[z].append(nazkolone[z].pop(0))
        else:
            n1=funkcije.zamena(x, nizkombinacije[z])
            if funkcije.vrv(n1, nizkombinacije[z]) == 1:
               vredkolone[z][0]=funkcije.bodovi(n1, nazkolone[z][0])
               rezvredkolone[z].append(vredkolone[z].pop(0))
               reznazkolone[z].append(nazkolone[z].pop(0))
            else:
                n2=funkcije.zamena(n1, nizkombinacije[z])
                if funkcije.vrv(n2, nizkombinacije[z]) == 1:
                    vredkolone[z][0]=funkcije.bodovi(n2, nazkolone[z][0])
                    rezvredkolone[z].append(vredkolone[z].pop(0))
                    reznazkolone[z].append(nazkolone[z].pop(0))     
                else:
                    for i in range(len(nazkolone[6])):
                        if len(nazkolone[6])==0:
                            m="*"
                        else:
                            m=nazkolone[6][i]
                        nzs=funkcije.najpogodnijiniz(n2, m)
                        nizkombinacijes.append(nzs)
                        vers=funkcije.vrv(n2, nzs)
                        nizverovatnoces.append(vers)
                        if vers>refvers:
                            refvers=vers
                            zs=i
                    if funkcije.vrv(n2, nizkombinacijes[zs]) == 1:
                        vredkolone[6][zs]=funkcije.bodovi(n2, nazkolone[6][zs])
                        rezvredkolone[6].append(vredkolone[6].pop(zs))
                        reznazkolone[6].append(nazkolone[6].pop(zs))
                    else:
                        if len(vredkolone[z])!=0 or len(nazkolone[z])!=0:
                            vredkolone[z][0]=funkcije.bodovi(n2, vredkolone[z][0])
                            rezvredkolone[z].append(vredkolone[z].pop(0))
                            reznazkolone[z].append(nazkolone[z].pop(0))
                        else:
                            continue
        brojac=brojac+1

    brojbodova0=funkcije.suma(rezvredkolone[0])-rezvredkolone[0][6]-rezvredkolone[0][7]+rezvredkolone[0][6]-rezvredkolone[0][7]
    brojbodova1=funkcije.suma(rezvredkolone[1])-(rezvredkolone[1][5]+rezvredkolone[1][6])+(rezvredkolone[1][6]-rezvredkolone[1][5])
    brojbodova34=funkcije.suma(rezvredkolone[2])+funkcije.suma(rezvredkolone[3])-(rezvredkolone[2][0]+rezvredkolone[3][0])+(rezvredkolone[2][0]-rezvredkolone[3][0])
    brojbodova56=funkcije.suma(rezvredkolone[4])+funkcije.suma(rezvredkolone[5])-(rezvredkolone[4][6]+rezvredkolone[5][5])+(rezvredkolone[4][6]-rezvredkolone[5][5])
    brojbodovaslobodne=funkcije.suma(rezvredkolone[6])-(rezvredkolone[6][6]+rezvredkolone[6][7])+(rezvredkolone[6][6]-rezvredkolone[6][7])
    bonus11=0
    bonus22=0
    bonus33=0
    bonus44=0
    bonus1=0
    for i in range(6):
        bonus1=bonus1+rezvredkolone[0][i]
    if bonus1>=60:
        bonus11=30
    bonus2=0
    for i in range(7, 13):
        bonus2=bonus2+rezvredkolone[1][i]
    if bonus2>=60:
        bonus22=30
    bonus3=0
    for i in range(1, 7):
        bonus3=bonus3+rezvredkolone[2][i]
    if bonus3>=60:
        bonus33=30
    bonus4=0
    for i in range(6):
        bonus4=bonus4+rezvredkolone[5][i]
    if bonus4>=60:
        bonus44=30
    ukupnobodova=brojbodova0+brojbodova1+brojbodova34+brojbodova56+brojbodovaslobodne+bonus11+bonus22+bonus33+bonus44
    return ukupnobodova


nh1=[]
nh2=[]
nhr=[]
for i in range(100):
    nh1.append(heuristika1())
    nh2.append(heuristika2())
    nhr.append(randheuristika())
bh1=funkcije.suma(nh1)/100
bh2=funkcije.suma(nh2)/100
bhr=funkcije.suma(nhr)/100
print(bh1)
print(bh2)
print(bhr)
