import pdftables_api
import glob
c = pdftables_api.Client('insert-apikey-here')


f= glob.glob("*.pdf")
print(f)

for i in f:
	c.xlsx(i, i+"out")

f = glob.glob("*.xlsx")
print(f)