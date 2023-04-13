import pyshorteners
shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short("https://www.amazon.in/HP-i3-1115G4-Micro-Edge-Anti-Glare-15s-fq2673TU/dp/B0B4N6JVMW?ref_=Oct_DLandingS_D_2c2d3a50_60&th=1")
print(x)