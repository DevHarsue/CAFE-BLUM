from fpdf import FPDF
import os

class CierrePDF(FPDF):
    def __init__(self, fecha_cierre, total_dolares,total_bs,total_cop):
        super().__init__()
        self.fecha_cierre = fecha_cierre
        self.total_dolares = round(float(total_dolares),2)
        self.total_bs = round(float(total_bs),2)
        self.total_cop = round(float(total_cop),2)
        
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_logo()
        self.add_title()
        self.add_invoice_info()
        self.add_table()
        self.add_footer()

    def add_logo(self):
        logo_path = 'images/logo.png'
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 8, 33)
        else:
            print(f"Error: No se encontró el archivo {logo_path}")

    def add_title(self):
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'FACTURA', 0, 1, 'C')
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'CAFE BLUM', 0, 1, 'C')
        self.cell(0,10,'Barrio obrero, calle 10 entre carreras 17-18',0,1,'C')

    def add_invoice_info(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Contacto: 0414-1754290', 0, 1, 'C')
        self.cell(0, 10, f'Cierre del {self.fecha_cierre}', 0, 1, 'C')


    def add_table(self):
        self.set_font('Arial', 'B', 12)
        self.cell(75, 10, 'Divisa', 1)
        self.cell(115, 10, 'Total', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        
        self.cell(150, 10, 'DOLARES', 1)
        self.cell(40, 10, f"{self.total_dolares}$", 1)
        self.ln()
        self.cell(150, 10, 'BOLIVARES', 1)
        self.cell(40, 10, f"{self.total_bs}$", 1)
        self.ln()
        self.cell(150, 10, 'COP', 1)
        self.cell(40, 10, f"{self.total_cop}$", 1)
        self.ln()
    def add_footer(self):
        self.set_y(250)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'FIN DEL CIERRE', 0, 1, 'C')