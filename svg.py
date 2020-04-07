import svgwrite
from svgwrite import cm , mm
from svgwrite.shapes import Rect


FONT_SIZE = 200
ROUNDNESS = 80
COLOR = 'white'
def generateSVG(name):
	XDIM = len(name) * FONT_SIZE/1.3
	YDIM = FONT_SIZE 
	dwg = svgwrite.Drawing('temp'  + '.svg', 
		(XDIM, YDIM),
		debug=True)
	
	dwg.add(
		dwg.rect(
			insert=(0*cm, 0*cm), 
			size=(XDIM-1,YDIM-1),
			stroke=COLOR, 
			stroke_width=30,
			rx = ROUNDNESS,
			ry =ROUNDNESS,
			fill_opacity = 0
		)
	)
	paragraph = dwg.add(dwg.g(font_size=FONT_SIZE ))
	paragraph.add(
		dwg.text(
			name, 
			(XDIM//2, YDIM // 2 + FONT_SIZE // 2 - 30),
			font_family = 'Chalkboard',
			fill = COLOR,
			text_anchor = 'middle',
		)
	)
	dwg.save()

	
	# return dwg.tostring()



from cairosvg import svg2png
import os

def generate(text) : 
	generateSVG(text.strip())
	text = text.strip()
	print('text = ' , text)
	with open('temp.svg') as f :
		string  = ''.join(f.readlines()[1:])
	svg2png(bytestring=string,write_to=os.path.join('png',text.replace(" ","_") + '.png'))



def build ():
	with open('__string__.py') as f :
		for text in f.readlines():
			generate(text)


def add (word):
	with open("__string__.py","a") as f :
		f.write(word + "\n")

from git import Repo
def deploy():
	print('github: file change triggered')
	if True:
		repo = Repo('')
		print('\tgithub: get repo')
		repo.git.add('-A')
		print('\tgithub: add git')
		repo.index.commit('dummy')
		print('\tgithub: commit repo')
		origin = repo.remote(name='origin')
		print('\tgithub: get remote')
		origin.push()
		print('\tgithub: push remote')

import sys


if len(sys.argv) > 1:
	add (sys.argv[1])

import time
prev = ''
if True :
	# with open('__string__.py') as f :
	# 	now = f.read()
	# if now != prev :
	# 	prev = now
	# 	build()
	# 	deploy()

	build()
	deploy()
	time.sleep(3)