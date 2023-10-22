from fpdf import FPDF 
import glob as g

pdf = FPDF(orientation="portrait",format="a4")
filename = g.glob('*.txt')

print(filename)

for f in filename:
    name = f.capitalize()
    # name = name.split('.')[0]
    # print(name)
    pdf.add_page()
    pdf.set_font(family='Times', size=20, style='BIU')  
    pdf.cell(align='L', w=0, h=12, txt=name.split('.')[0])
    # print(f)
    pdf.ln(30)

    with open(file=f) as file:
        text = file.readline()
    pdf.set_font(family='Times', size=12)     
    pdf.multi_cell(align='L', w=200, h=12, border= 1, txt=text)
        
        
    
pdf.output("mod.pdf")


