import pandas as pd
from fpdf import FPDF


df = pd.read_csv("articles.csv")
print(df)

class Buy():
    def __init__(self,id):
        self.id = id
        self.item_name = df.loc[df["id"]==self.id, "name"].squeeze()
        self.item_price = df.loc[df["id"]==self.id, "price"].squeeze()
    
    def available(self):
        avail = df.loc[df["id"]==self.id, "in stock"].squeeze()
        if avail == 0:
            return False
        else:
            stock = df.loc[df["id"]==self.id, "in stock"]
            stock = stock - 1
            df.loc[df["id"] == self.id, "in stock"] = stock
            df.to_csv("articles.csv", index=False)
            return True
    


class PrintPdf():
    def __init__(self,buy_object):
        self.buy = buy_object
        
        
    def printin(self):
        
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.1", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.buy.item_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.buy.item_price}", ln=1)

        return pdf.output("receipt.pdf")
        


item_id = int(input("enter id of item: "))
buy = Buy(item_id)

if buy.available():
    printpdf = PrintPdf(buy)
    printpdf.printin()
    print("hello")
else:
    print("unabalilbe")
    




# from fpdf import FPDF






# pdf = FPDF(orientation="P", unit="mm", format="A4")
# pdf.add_page()

# pdf.set_font(family="Times", size=16, style="B")
# pdf.cell(w=50, h=8, txt=f"Receipt nr.1", ln=1)

# pdf.set_font(family="Times", size=16, style="B")
# pdf.cell(w=50, h=8, txt=f"Article: Laptop Sven", ln=1)

# pdf.set_font(family="Times", size=16, style="B")
# pdf.cell(w=50, h=8, txt=f"Price: 999", ln=1)

# pdf.output("receipt.pdf")
