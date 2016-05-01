'''
Having a fixed format
slide 1 : title , subtitle
slide 2 : intro
slide 3 : major points
slide 3.1 : more points
slide 3.2: with images
slide 4: conclusion
slide 5 : references
'''
from pptx import Presentation
from pptx.util import Inches
import csv
import functionsGoHere


row=[]
with open('content.csv', 'rb') as csvfile:
	spamreader= csv.reader(csvfile, delimiter=',')
	for row in spamreader:

		title_csv=row[0]
		subtitle_csv=row[1]
		introduction_csv=row[2]
		points_csv=row[3].split('/')
		conclusion_csv=row[4]
		references_csv=row[5].split('/')
		

#---slide 1 ---- Starts
prs = Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]
title_name=title_csv#CSV
subtitle_name=subtitle_csv#CSV
title.text = title_name
subtitle.text = subtitle_name

# img_path = 'img1.jpg'
# blank_slide_layout = prs.slide_layouts[6]
# slide = prs.slides.add_slide(blank_slide_layout)
# left = top = Inches(1)
# pic = slide.shapes.add_picture(img_path, left, top)
# left = Inches(5)
# height = Inches(5.5)
# pic = slide.shapes.add_picture(img_path, left, top, height=height)

#slide 2-------- Introduction
introduction_slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(introduction_slide_layout)
slide_title= slide.placeholders[0]
slide_title_name ="Introduction"
slide_title.text = slide_title_name

shapes = slide.shapes

body_shape = shapes.placeholders[1]
tf = body_shape.text_frame

p= tf.add_paragraph()
p.text = introduction_csv#DATA

#slide 3-------- Major points
heading_slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(heading_slide_layout)
slide_title= slide.placeholders[0]
slide_title_name ="zzz"
slide_title.text = slide_title_name

shapes = slide.shapes

body_shape = shapes.placeholders[1]
tf = body_shape.text_frame

# <in a loop>

for i in range(0,5):
	

	p = tf.add_paragraph()
	p.text = points_csv[i]#DATA


#slide 3.1-------- More points If needed
if len(points_csv) > 5:

	heading_slide_layout = prs.slide_layouts[1]
	slide = prs.slides.add_slide(heading_slide_layout)
	slide_title= slide.placeholders[0]
	slide_title_name ="zzz"
	slide_title.text = slide_title_name

	shapes = slide.shapes

	body_shape = shapes.placeholders[1]
	tf = body_shape.text_frame

	# <in a loop>

	for i in range(5,len(points_csv)):
	

		p = tf.add_paragraph()
		p.text = points_csv[i]#DATA

#slide 3.2-------- More point with images
heading_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(heading_slide_layout)
img_path = 'img1.jpg'
left = top =Inches(1)
height = Inches(5.5)
pic = slide.shapes.add_picture(img_path, left, top, height=height)

#slide 4-------- Conclusion
heading_slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(heading_slide_layout)
slide_title= slide.placeholders[0]
slide_title_name ="Conclusion"
slide_title.text = slide_title_name

shapes = slide.shapes

body_shape = shapes.placeholders[1]
tf = body_shape.text_frame

p = tf.add_paragraph()
p.text = conclusion_csv #DATA

#slide 5--------References
heading_slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(heading_slide_layout)
slide_title= slide.placeholders[0]
slide_title_name ="References"
slide_title.text = slide_title_name

shapes = slide.shapes

body_shape = shapes.placeholders[1]
tf = body_shape.text_frame

for i in range(0,len(references_csv)):
	

		p = tf.add_paragraph()
		p.text = references_csv[i]#DATA

##slide ends

prs.save(title_csv+'.pptx')
# setPPTReadyButton(1)
