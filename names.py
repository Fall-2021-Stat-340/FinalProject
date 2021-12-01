code = ["AG.LND.ARBL.HA.PC", "EN.URB.MCTY", "NE.IMP.GNFS.ZS", "NY.GSR.NFCY.CD", "NE.TRD.GNFS.ZS", "SP.POP.TOTL", "TG.VAL.TOTL.GD.ZS", "NY.TAX.NIND.CN", "EN.POP.DNST", "FI.RES.TOTL.CD", "SP.POP.65UP.TO.ZS"]

name = ["Arable land (hectares per person)", "Population in urban agglomerations of more than 1 million", "Imports of goods and services (% of GDP)", "Net income from abroad (current US$)", "Trade (% of GDP)", "Population, total", "Merchandise trade (% of GDP)", "Net taxes on products (current LCU)", "Population density (people per sq. km of land area)", "Total reserves (includes gold, current US$)", "Population ages 65 and above (% of total)"]

print("| Code | Name |")
print("|-|-|")
for (c, n) in zip(code, name):
    print("|", c, " | ", n, "|")