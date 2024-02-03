import os

x = "ATGCGCC"
path="C:\\Users\\nafis\\PycharmProjects\\BioInformatics project"
for i in range(len(x)):
    os.chdir(path)
    Newfolders=(f"{x[i]}{i+1}")
    os.mkdir(Newfolders)
    path2=path+'\\'+Newfolders
    os.chdir(path2)
    for j in range(0,1):
        n=open(f'{x[i].lower()}.txt','w')
        for k in range(i+1):
            n.write(f'{x[i].lower()}')


