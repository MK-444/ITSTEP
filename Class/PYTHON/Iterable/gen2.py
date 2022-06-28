seznam = [1, 2, 3, 4, 5]

novy_seznam = [i * i for i in seznam]

#druhe mocniny pomoci cyklu 
novy_seznam  = []
for i in seznam:
    novy_seznam.append(i * i)
    
#druhe mocniny pomoci list complrehension 
novy_seznam2 = [i * i  for i in seznam]

#druhe mocniny pomoci generator expression 
novy_seznam2 = (i * i for i in seznam)

    