import setuptools

setuptools.setup(
	name='pySIC',
	version='0.0.2',
	description='A tool that crops images and extract text from them for giving PDFs and HOCRs',
	license='MIT',
	packages=["pySIC"],
	author='Davide Risaliti',
	author_email='davdag24@gmail.com',
	keywords=['image','ocr','deskew'],
	url='https://github.com/DavDag/image_to_hOCR',
	install_requires=[
	'opencv-python',
	'numpy',
	'scipy',
	'pytesseract',
	'reportlab',
	'hocr-tools'
	]
)
