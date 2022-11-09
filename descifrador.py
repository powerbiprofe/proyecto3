diccionario = {'hysrphc':'a',
               'ttcigip':'b',
               'cmeozmn':'c',
               'looefqh':'d',
               'xcemwrj':'e',
               'yjlnzdw':'f',
               'vwbqqtr':'g',
               'rapqfld':'h',
               'houlchi':'i',
               'erdehxi':'j',
               'wjlnlsm':'k',
               'epdwkxq':'l',
               'zcyglpx':'m',
               'tcjssjk':'n',
               'gykgkjw':'o',
               'twbqdih':'p',
               'atrwzpc':'q',
               'qqebimb':'r',
               'qgsmxyk':'s',
               'yqsooez':'t',
               'bctabnl':'u',
               'ugmfbhj':'v',
               'jqpnofo':'w',
               'dctzpyw':'x',
               'lnkzhdk':'y',
               'bofxibv':'z' }

'''entrada = "%xcemwrj%%cmeozmn%%rapqfld%%gykgkjw% %gykgkjw%%yjlnzdw%%yjlnzdw%"

for d in diccionario.keys():
    entrada = entrada.replace('%' + d + '%', diccionario[d])

print (entrada)'''

entrada = ""


with open("bichoCifrado.bat", mode = "r") as f_entrada:
    entrada = f_entrada.read() 

for d in diccionario.keys():
    entrada = entrada.replace('%' + d + '%', diccionario[d])

with open("bichoDescifrado.bat", mode = "w") as f_salida:
    f_salida.write(entrada)

