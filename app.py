


# laca = 'ADD1G78'
# pctExcesso = 12.37
# codRadar= 'r2'
# veiculoEspecial = False

# print("Placa   -Pct   -Radar")
# if(veiculoEspecial== False):
#     print(placa +'\t'+ str(pctExcesso) +'\t'+  codRadar+'\n')
# else:
#     print('foste moleque')


registroVeiculo = [
    ["r1", "BEE4R22", 70.00,  60,  "comum"],
    ["r1", "DKR5Y21", 67.00,  60,  "especial"],
    ["r1", "ABX4I22", 60.00,  60,  "comum"],
    ["r1", "ABT8I78", 67.01,  60,  "comum"],
    ["r2", "VXX0f74", 56.90,  80,  "comum"],
    ["r2", "AKR7T45", 87.00,  80,  "comum"],
    ["r2", "ADD1G78", 89.90,  80,  "comum"],
    ["r2", "CFG3J77", 73.89,  80,  "comum"],
    ["r3", "ERR3J79", 73.89,  100, "comum"],
    ["r3", "ERP1J22", 65.89,  100, "comum"],
    ["r3", "BNG9J99", 110.89, 100, "especial"],
    ["r3", "ABT8I78", 110.98, 100, "comum"]
]
#print(registroVeiculo[0][2])

# for elemento in registroVeiculo:
#     if(elemento[4] == "comum" ):
#         pctExcesso = (float(elemento[2]) - float(elemento[3])) / float(elemento[3]) * 100
#         print(f"Placa: {elemento[1]}, Porcentagem de Excesso: {pctExcesso:.2f}%")
# print("\n")

# print(registroVeiculo.__len__())
# print(type(registroVeiculo))



for i in range(0,len(registroVeiculo)):
 velApurada = registroVeiculo[i][2]
 velPermitida= registroVeiculo[i][3]
 placa = registroVeiculo[i][1]
codRadar = registroVeiculo[i][0]
tipoveiculo = registroVeiculo[i][4]
pctExcessos = (float(velApurada[2]) - float(velPermitida[3])) / float(velPermitida[3]) * 100

if(tipoveiculo[i][4] == "comum" ) and\
    (pctExcessos > 0) :
    #       ((velPermitida<= 100 )) and (velApurada>(velPermitida+7))    
    print(f"{placa}  -  {pctExcessos :.2f}  -  {codRadar}")
#pctExcesso = (float(registroVeiculo[0][2]) - float(registroVeiculo[0][3]))/float(registroVeiculo[0][3]) * 100

#print("PLACA   -PCT   -RADAR")
#if(registroVeiculo[0][4] == "comum"):
#    print(f"{registroVeiculo[0][1]} - {pctExcesso:.2}  -  {registroVeiculo[0][0]}")
