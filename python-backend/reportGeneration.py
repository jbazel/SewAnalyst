
def generateReport(PeSeverity, DwfSeverity, FftSeverity, OverallSeverity, PeGraph, DwfGraph):


    #Idea to do this:
    ## Data generation (will probs come from adam)
    ## Create the struct for the pdf (Snippets of graphs and text?? etc)
    ## Create the pdf report using fpdf
    from PIL import Image
    from fpdf import FPDF

    #Deciding values and paragraph
    def PEParagraph(PeSeverity):
        if PeSeverity == "none":
            paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as "none". This means that it was correctly reported and is not a point for concern. '
        elif PeSeverity == "mild":
            paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as "mild". This means there was a slight difference between the reported PE and the actual forecasted one. This may be due company trying to avoid the extra funding they would need to inject in STWs maintenance and upgrade in order to be sufficient and safe for the environment. The other possibility is that they have not properly considered things like tourist population which impacts PE. '
        elif PeSeverity == "severe":
            paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as "severe". This means there was a high difference between the reported PE and the actual forecasted one. This could insinuate the company is trying to minimise the maintenance cost for the STWs and as well may be hiding insufficient appropriate infrastructures for their respective true populations. This is a red flag, and it would be suggested to look further into the company as to whether they are being honest and they are just struggling to update their figures quick enough and accordingly or if they are lacking honesty and are trying to cut cost in an unethical manner. '
        else: 
            paragraph = 'There was an error with the PE data analysis please retry it and make sure your pe data is proper'
        return paragraph

    def DWFParagraph(DwfSeverity):
        if DwfSeverity == "none":
            paragraph = 'DWF value reported and the one calculated were deemed to be the same and thus of severity "none". Meaning the company is calculating DWF accurately and with the proper figures.'
        elif DwfSeverity == "mild":
            paragraph = 'DWF value reported and the one calculated were not the same and the severity of this difference was determined as "mild". Due to a change in 2012, there is a lot more leeway about the calculations of this therefore could explain the mild difference reported. As well numbers may have been rounded up and therefore vary the final value slightly or it was that a company was slightly over a threshold and wish to stay under, so they do not have to increase expenses on their STWs.'
        elif DwfSeverity == "severe":
            paragraph = 'DWF value reported and the one calculated were not the same and the severity of this difference was determined as "severe". This raises an important warning as often this means the company is changing values in order to avoid certain requirements that comes with higher DWF which would mean an increase in cost for STW maintenance. There is a possibility the wrong data or something was forgotten during the calculations, but this is highly unlikely.'
        else: 
            paragraph = 'There was an error with the DWF data analysis please retry it and make sure your pe data is proper'
        return paragraph

    def FFTParagraph(FftSeverity):
        if FftSeverity == "none":
            paragraph = 'FFT value reported and the one calculated were deemed to be the same and thus of severity "none". Meaning the company is calculating FFT accurately and with the proper figures.'
        elif FftSeverity == "mild":
            paragraph = 'FFT value reported and the one calculated were not the same and the severity of this difference was determined as "mild". Numbers and values used in its calculations may have been rounded up and therefore vary the final value slightly. As well there are two different ways to calculate this and therefore the other equation may have been used in which values vary and it is dependent on PE which if flagged earlier may be the issue. Alternatively, it was that a company was slightly over a threshold and wish to stay under, so they do not have to increase expenses on their STWs.'
        elif FftSeverity == "severe":
            paragraph = 'FFT value reported and the one calculated were not the same and the severity of this difference was determined as "severe". Numbers and values used in its calculations may have been rounded up and therefore vary the final value slightly. As well there are two different ways to calculate this and therefore the other equation may have been used in which values vary and it is dependent on PE which if flagged earlier may be the issue. Alternatively, this raises an important warning about the company changing values in order to avoid certain requirements that comes with higher FFT which would mean an increase in cost for STW maintenance. There is a possibility the wrong data or something was forgotten during the calculations, but this is highly unlikely. As well, the common agreement is that FFT is around 3 times DWF however many companies disagree and say it is around 2 times only and this is where a lot of the differences come from.'
        else: 
            paragraph = 'There was an error with the FFT data analysis please retry it and make sure your pe data is proper'
        return paragraph

    def CompAnParagraph(OverallSeverity):
        if OverallSeverity == "none":
            paragraph = 'The overall difference severity was "none". This means the company has not been flagged for any of the data it has reported and therefore it may be trusted.'
        elif OverallSeverity == "mild":
            paragraph = 'The overall difference severity was "mild". Some data values were flagged, or they were all averagely flagged for being mild differences meaning that some areas of data the company sent in did not match up with what was calculated or forecasted. This may just be miscalculations and a mistake by the company or it is an issue and they are trying to stay below the threshold to cut cost however this can be mildly detrimental to the environment and river ecosystems.'
        elif OverallSeverity == "severe":
            paragraph = 'The overall difference severity was "severe". This means that the company has consistently misreported the data and values. This is highly unlikely to be a mistake and is more likely to raise a red flag on the company suggesting they are severely trying to cut cost and investment into their STWs however this results in highly negative impacts on the environment around it.'
        else: 
            paragraph = 'There was an error with the overall company data analysis please retry it and make sure your pe data is proper'
        return paragraph

    PEPara = PEParagraph(PeSeverity)
    DWFPara = DWFParagraph(DwfSeverity)
    FFTPara = FFTParagraph(FftSeverity)
    CompAna = CompAnParagraph(OverallSeverity)
    title = 'STW Analysis Report'
    intro = 'The analysis of the data input has been conducted. The analysis will provide answers on: 1. Asses the accuracy and correctness of the company given PE for individual STWs 2. Verify that the company accurately calculated and reported their proper DWF for the according STWs 3. Verify that the company accurately calculated and reported the proper FFT for the according STWs 4. Qualitatively assure companies are ensuring provision of adequate sewage treatment capacity at water companies STWs  '
    conc = f'Overall to summarise the analysis of the data found: \n\
                PE: {PeSeverity} \n\
                DWF: {DwfSeverity} \n\
                FFT:{FftSeverity} \n\
                Company Analysis: {OverallSeverity}' 

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
            self.cell(w, 9, title, 0, 1, 'C', 0)
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
            self.cell(0, 6, 'Section %d : %s' %(num, title), 0, 1, 'L', 1)
            self.ln(4)

            #Body Format
            self.set_font('Times', '', 12)
            self.multi_cell(0, 5, txt)
            self.ln()
        
        def ImageSet(self, img):
            #Set up the image so it fits on the page
            iMage = Image.open(img)
            width, height = iMage.size

            width, height = float(width * 0.264583), float(height * 0.264583)
            pdfSize = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
            if width < height:
                orientation = 'P' 
            else:
                orientation = 'L'

            
            if width < pdfSize[orientation]['w']:
                width = width 
            else:
                width = pdfSize[orientation]['w']
            if height < pdfSize[orientation]['h']:
                height = height
            else:
                height = pdfSize[orientation]['h']
            
            self.image(img, w=width,h=height)
            self.ln()

        def print_section(self, num, title, txt, img):
            self.titleAndText(num, title, txt)
            if img != '0':
                self.ImageSet(img)

        
    pdf = PDF()

    pdf.add_page()
    pdf.print_section(0, 'Introduction', intro, '0')
    pdf.print_section(1, 'Population Equivalence', PEPara, PeGraph)
    pdf.print_section(2, 'Dry Weather Flow ', DWFPara, DwfGraph)
    pdf.print_section(3, 'Flow to Full Treatment', FFTPara, '0')
    pdf.print_section(4, 'Company Analysis', CompAna, '0')
    pdf.print_section(5, 'Conclusion', conc, '0')
        
    pdf.output('./Data_Report.pdf', 'F')


# if __name__ == "__main__":
#     generateReport("mild", "none", "severe", "mild", "PE_plot.png", "DWF_plot.png")
#     #It goes to which ever directory this was executed in so in this case C:\Users\margu>