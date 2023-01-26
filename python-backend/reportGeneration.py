
def generateReport(data, figures):
    #Idea to do this:
## Data generation (will probs come from adam)
## Create the struct for the pdf (Snippets of graphs and text?? etc)
## Create the pdf report using fpdf



from fpdf import FPDF

#Deciding values and paragraph
def PEParagraph(PeSeverity):
    paragraph = '' 
    if PeSeverity == "none":
        paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as “none”. *Paragraph continuing: what this means* '
    
    elif PeSeverity == "mild":
        paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as “mild”. *Paragraph continuing: what this means* '
    elif PeSeverity == "severe":
        paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as “severe”. *Paragraph continuing: what this means* '
    else: 
        paragraph = 'There was an error with the PE data analysis please retry it and make sure your pe data is proper'
    return paragraph

def DWFParagraph(DwfSeverity):
    paragraph = '' 
    if DwfSeverity == "none":
        paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as “none”. *Paragraph continuing: what this means* '
    
    elif DwfSeverity == "mild":
        paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as “mild”. *Paragraph continuing: what this means* '
    elif DwfSeverity == "severe":
        paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as “severe”. *Paragraph continuing: what this means* '
    else: 
        paragraph = 'There was an error with the PE data analysis please retry it and make sure your pe data is proper'
    return paragraph

def FFTParagraph(FftSeverity):
    paragraph = '' 
    if FftSeverity == "none":
        paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as “none”. *Paragraph continuing: what this means* '
    
    elif FftSeverity == "mild":
        paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as “mild”. *Paragraph continuing: what this means* '
    elif FftSeverity == "severe":
        paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as “severe”. *Paragraph continuing: what this means* '
    else: 
        paragraph = 'There was an error with the PE data analysis please retry it and make sure your pe data is proper'
    return paragraph

def CompAnParagraph(OverallSeverity):
    paragraph = '' 
    if OverallSeverity == "none":
        paragraph = 'The overall difference severity was none. *Paragraph continuing: what this means*  '
    elif OverallSeverity == "mild":
        paragraph = 'The overall difference severity was mild. *Paragraph continuing: what this means*'
    elif OverallSeverity == "severe":
        paragraph = 'The overall difference severity was severe. *Paragraph continuing: what this means*'
    else: 
        paragraph = 'There was an error with the overall company data analysis please retry it and make sure your pe data is proper'
    return paragraph


#Creating the pdf
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        
    def header(self):
        # Custom logo and positioning
        # Create an `assets` folder and put any wide and short image inside
        # Name the image `logo.png`
        self.image('assets/logo.jpg', 10, 8, 33)
        self.set_font('Times New Roman', 'B', 11)
        self.cell(self.WIDTH - 80)
        self.cell(60, 1, 'STW Analysis Report', 0, 0, 'R')
        self.ln(20)
        
    def footer(self):
        # Page numbers in the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def page_body(self):
        self.set_font('Arial', '', 14)
        self.write(5, 'Hello')
        # Determine how many plots there are per page and set positions
        # and margins accordingly
        # if len(images) == 3:
        #     self.image(images[0], 15, 25, self.WIDTH - 30)
        #     self.image(images[1], 15, self.WIDTH / 2 + 5, self.WIDTH - 30)
        #     self.image(images[2], 15, self.WIDTH / 2 + 90, self.WIDTH - 30)
        # elif len(images) == 2:
        #     self.image(images[0], 15, 25, self.WIDTH - 30)
        #     self.image(images[1], 15, self.WIDTH / 2 + 5, self.WIDTH - 30)
        # else:
        #     self.image(images[0], 15, 25, self.WIDTH - 30)
        
    def print_page(self):
        # Generates the report
        self.add_page()
        self.page_body()
    
pdf = PDF()

pdf.print_page()
    
pdf.output('Data Report.pdf', 'F')

#It goes to which ever directory this was executed in so in this case C:\Users\margu>