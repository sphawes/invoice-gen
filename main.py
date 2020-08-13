from fpdf import FPDF

print("Welcome to the SPH Invoice generator! Here come the questions:")
reason = input("Invoice Title> ")
filename = input("Exported Filename> ")
company = input("Company> ")
contact = input("Contact> ")
contact_email = input("Contact Email> ")
date = input("Date> ")
notes = input("Notes> ")

num_of_items = int(input("Ok, how many items?> "))

items = []

i=0
while i < num_of_items:
    item = []
    item.append(input("Item #" + str(i+1) + " title> "))
    item.append(input("Item #" + str(i+1) + " description> "))
    item.append(input("Item #" + str(i+1) + " quantity> "))
    item.append(input("Item #" + str(i+1) + " price> "))
    item.append(float(item[2]) * float(item[3]))
    items.append(item)
    i = i + 1

print(items)

total = 0
for j in items:
    total = total + j[4]
    j[4] = "$" + str(j[4])
    j[3] = "$" + str(j[3])

total = round(total, 2)

print("Cool, generating the invoice...")

table_column_widths = [40,90,20,20,20]

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(True, 0)
pdf.add_page()

#header
pdf.set_font("Arial", size=28)
pdf.set_fill_color(230,190,30)
pdf.rect(0, 0, 220, 30, "F")

pdf.set_fill_color(200,160,0)
pdf.rect(150,0,80,30,"F")

pdf.cell(20, 10, 'INVOICE', 0, 25)
pdf.set_font("Arial", size=12)
pdf.cell(20, 10, reason)

pdf.set_xy(150,5)
pdf.cell(60,10,"Amount Due (USD)",0,0,'C')
pdf.set_font("Arial", size=20)
pdf.set_xy(150,9)
pdf.cell(60,20,"$" + str(total),0,0,'C')

#bill to and date
pdf.set_xy(5,35)
pdf.set_font("Arial", size=12)
pdf.cell(0,5,company,0)
pdf.set_xy(5,40)
pdf.cell(0,5,contact,0)
pdf.set_xy(5,45)
pdf.cell(0,5,contact_email,0)

pdf.set_xy(150, 35)
pdf.cell(0,5,"Invoice Date:",0)
pdf.set_xy(150, 40)
pdf.cell(0,5,date,0)

#generating table of items
pdf.set_xy(10,55)
pdf.cell(40,10,"Item",0,ln=0,fill=True)
pdf.cell(90,10,"Description",0,ln=0,fill=True)
pdf.cell(20,10,"Quantity",0,ln=0,fill=True)
pdf.cell(20,10,"Price",0,ln=0,fill=True)
pdf.cell(20,10,"Amount",0,ln=0,fill=True)

pdf.set_font("Arial", size=8)
col_width = pdf.w / 4.5
row_height = pdf.font_size + 5
pdf.set_xy(10, 70)
x_pos = 10
y_pos = 70
i = 0
for row in items:
    for item in row:
        pdf.multi_cell(table_column_widths[i], row_height, txt=str(item), border="LTR")
        x_pos = x_pos + table_column_widths[i]
        i = i + 1
        pdf.set_xy(x_pos, y_pos)
    y_pos = y_pos + row_height*2
    x_pos = 10
    i=0
    pdf.set_xy(x_pos, y_pos)

pdf.set_font("Arial", size=10)
pdf.cell(170,10,"Total",0,ln=0,fill=True)
pdf.cell(20,10,"$" + str(total),1,ln=0,align='C',fill=True)

#notes
pdf.set_fill_color(220,220,220)
pdf.rect(0,230,300,20,"F")

pdf.set_text_color(255,255,255)
pdf.set_xy(1,231)
pdf.cell(0,6,'NOTES')

pdf.set_text_color(0,0,0)
pdf.set_font("Arial",size=10)
pdf.set_xy(6,238)
pdf.multi_cell(0,5,notes)

#footer
pdf.set_fill_color(230,190,30)
pdf.rect(0,250,300,50,"F")
pdf.set_font("Arial",size=12)
pdf.set_xy(8,258)
pdf.cell(0,5,'Stephen Hawes',0,2)
pdf.cell(0,5,'458 Broadway',0,2)
pdf.cell(0,5,'Floor 3',0,2)
pdf.cell(0,5,'Somerville, MA 02145',0,2)

pdf.cell(0,5,'sphawes@gmail.com',0,2)
pdf.cell(0,5,'860-754-7121',0,2)

#output
pdf.output(filename + ".pdf")

print("Done! PDF exported to this directory.")