import glob
import os

frags_files = glob.glob('S1_frags/*.mol2')
frags_keys = [os.path.basename(frag).replace('.mol2','') for frag in frags_files]

for i,frag in enumerate(frags_files):
    f_in = open(frag,'r')
    f_out = open('fragment_S1.mdb/'+frags_keys[i]+'.mol2','w')
    count_H = 1
    for line in f_in:
        if 'Du' in line:
            if count_H <= 9:
                line = line.replace('Du','H'+str(count_H),1)
            else:
                line = line.replace('Du ','H'+str(count_H),1)
            line = line.replace('Du   ','H.spc',1)
            count_H+=1
            f_out.write(line)
        else:
            f_out.write(line)
    f_in.close()
    f_out.close()
