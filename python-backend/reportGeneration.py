
def generateReport(data="", figures=""):


    #Idea to do this:
    ## Data generation (will probs come from adam)
    ## Create the struct for the pdf (Snippets of graphs and text?? etc)
    ## Create the pdf report using fpdf

    from fpdf import FPDF

    #Deciding values and paragraph
    def PEParagraph(PeSeverity):
        if PeSeverity == "none":
            paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as none. *Paragraph continuing: what this means* '
        elif PeSeverity == "mild":
            paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as mild. *Paragraph continuing: what this means* '
        elif PeSeverity == "severe":
            paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as severe. *Paragraph continuing: what this means* '
        else: 
            paragraph = 'There was an error with the PE data analysis please retry it and make sure your pe data is proper'
        return paragraph

    def DWFParagraph(DwfSeverity):
        if DwfSeverity == "none":
            paragraph = 'DWF value reported and the one calculated were deemed to be the same and there were no issues reported. *Paragraph continuing: what this means* '
        
        elif DwfSeverity == "mild":
            paragraph = 'DWF value reported and the one calculated were not the same however the difference was deemed to be minimal. *Paragraph continuing: what this means* '
        elif DwfSeverity == "severe":
            paragraph = 'DWF value reported and the one calculated were not the same the difference was deemed to be severe. *Paragraph continuing: what this means*'
        else: 
            paragraph = 'There was an error with the DWF data analysis please retry it and make sure your pe data is proper'
        return paragraph

    def FFTParagraph(FftSeverity):
        if FftSeverity == "none":
            paragraph = 'FFT value reported and the one calculated were deemed to be the same and there were no issues reported. *Paragraph continuing: what this means* '
        elif FftSeverity == "mild":
            paragraph = 'FFT value reported and the one calculated were not the same however the difference was deemed to be minimal. *Paragraph continuing: what this means*'
        elif FftSeverity == "severe":
            paragraph = 'FFT value reported and the one calculated were not the same the difference was deemed to be severe. *Paragraph continuing: what this means* '
        else: 
            paragraph = 'There was an error with the FFT data analysis please retry it and make sure your pe data is proper'
        return paragraph

    def CompAnParagraph(OverallSeverity):
        if OverallSeverity == "none":
            paragraph = 'The overall difference severity was none. *Paragraph continuing: what this means*'
        elif OverallSeverity == "mild":
            paragraph = 'The overall difference severity was mild. *Paragraph continuing: what this means*'
        elif OverallSeverity == "severe":
            paragraph = 'The overall difference severity was severe. *Paragraph continuing: what this means*'
        else: 
            paragraph = 'There was an error with the overall company data analysis please retry it and make sure your pe data is proper'
        return paragraph

    PeSeverity = "mild"
    DwfSeverity = "none"
    FftSeverity = "severe"
    OverallSeverity = "mild"

    PEPara = PEParagraph(PeSeverity)
    DWFPara = DWFParagraph(DwfSeverity)
    FFTPara = FFTParagraph(FftSeverity)
    CompAna = CompAnParagraph(OverallSeverity)
    title = 'STW Analysis Report'
    intro = 'The analysis of the data input has been conducted. The analysis will provide answers on: 1. Asses the accuracy and correctness of the company given PE for individual STWs 2. Verify that the company accurately calculated and reported their proper DWF for the according STWs 3. Verify that the company accurately calculated and reported the proper FFT for the according STWs 4. Qualitatively assure companies are ensuring provision of adequate sewage treatment capacity at water companies STWs  '
    conc = 'Overall to summarise the analysis of the data found: PE: *select correct* none, mild, severe DWF: *select correct* not same, same FFT: *select correct* not same, same Company Analysis: *select correct* none, mild, severe'

    #Creating the pdf
    class PDF(FPDF):
        def __init__(self):
            super().__init__()
            self.WIDTH = 210
            self.HEIGHT = 297
            
        def header(self):
            #Title
            self.set_font('Arial', 'B', 15)
            w = self.get_string_width(title) + 6
            self.set_x((210 - w) / 2)
            self.cell(w, 9, title, 0, 1, 'C', 1)
            self.ln(10)
            
        def footer(self):
            # Page numbers in the footer
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(128)
            self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


        def titleAndText(self, num, title, txt):
            #Text Format
            self.set_font('Arial', '', 12)
            self.set_fill_color(200, 220, 255)
            self.cell(0, 6, 'Chapter %d : %s' % (num, title), 0, 1, 'L', 1)
            self.ln(4)

            #Body Format
            self.set_font('Times', '', 12)
            self.multi_cell(0, 5, txt)
            self.ln()
        
        def print_section(self, num, title, txt):
            self.titleAndText(num, title, txt)

        
    pdf = PDF()

    pdf.add_page()
    pdf.print_section(0, 'Introduction', intro)
    pdf.print_section(1, 'Population Equivalence', PEPara)
    pdf.print_section(2, 'Dry Weather Flow ', DWFPara)
    pdf.print_section(3, 'Flow to Full Treatment', FFTPara)
    pdf.print_section(4, 'Company Analysis', CompAna)
    pdf.print_section(5, 'Conclusion', conc)
        
    pdf.output('Data Report.pdf', 'F')

generateReport()
    #It goes to which ever directory this was executed in so in this case C:\Users\margu>