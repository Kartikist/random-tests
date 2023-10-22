from fpdf import FPDF 
import glob as g

pdf = FPDF(orientation="portrait",format="a4")
filename = g.glob('*.txt')

print(filename)

for f in filename:
    name = f.capitalize()
    
    pdf.add_page()
    pdf.set_font(family='Times', size=20, style='BIU')  
    pdf.cell(w=0, h=12, txt=name.split('.')[0])
    # print(f)
    pdf.ln(30)

    with open(file=f) as file:
        text = file.read()
    pdf.set_font(family='Times', size=12)     
    pdf.multi_cell(w=0, h=12, txt=text)
        
        
    
pdf.output("mod.pdf")


