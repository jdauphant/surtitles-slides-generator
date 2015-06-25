#!/usr/bin/env python

from __future__ import unicode_literals
import sys

if len(sys.argv) != 3:
    raise ValueError('usage: '+sys.argv[0]+' input-text ouput.pdf')

input_file=sys.argv[1]
ouput_pdf_file=sys.argv[2]
height = 210
width = 280
text_height = 40
text_width = width - 10
font_size = 60
max_per_cent_text_size = 0.90

from fpdf import FPDF

class PDF(FPDF):
	def new_slide(self,text):
		self.add_page()
		self.set_fill_color(0,0,0)
		self.rect(0,0,width,height,'F')
		self.set_font('DejaVuSans-Bold', '', font_size)
		string_width = self.get_string_width(text)
		if string_width > width*max_per_cent_text_size:
			new_font_size = int((float(width*max_per_cent_text_size) / float(string_width)) * float(font_size))
			self.set_font('DejaVuSans-Bold', '', new_font_size)
		self.set_text_color(255,255,255)
		self.cell(0,height/2-text_height/2)
		self.ln()
		self.cell(0, 0, text, align = 'C')

pdf = PDF('L','mm',(height,width))
pdf.add_font('DejaVuSans-Bold', '', 'DejaVuSans-Bold.ttf', uni=True)
import codecs
with open(input_file) as f:
    for line in f:
		pdf.new_slide(line.rstrip())
pdf.output(ouput_pdf_file, 'F')