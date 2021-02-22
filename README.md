# Generator of random or customized memes - via Web Application or CLI.

### Overview
This project allows to create memes, either randomly with predefined images and quotes or customized with user input.
The memes can be generated via web application or via CLI.

### Instructions
Before starting the meme generator, please follow these instructions:
- Install dependencies by running: pip install -r requirements.txt
- Install the pdftotext CLI from: https://www.xpdfreader.com/download.html

### Web Application
In order to start the web application, run the follwing command:
	python app.py
The application is accessible at: http://127.0.0.1:5000/

In the web application, the user can generate randon meme by clicking on "random". The generated memes are saved 
in the folder "static" until a restart of the application occurs.
The user has also the possibility to create its own customized meme by clicking on "Creator" and providing an image url, quote (optional) and author (optional).
The created meme is saved in the folder "static" until a restart of the application occurs.

### CLI
The user can start the meme generator by running the following command:
	python meme.py
	
If no information is given, a random meme will be generated and saved in the folder "tmp".

The user has the possibility to customize a meme by giving the image (--path), the quote (--body) and the author (--author).
Note that if only quote and author are given, a random image will be used. If a quote is given, an author is also needed.

Here an example of generating a customized meme:
	python meme.py --path ./_data/photos/pics/Download_1.jpg --body HelloWorld! --author Python

### Project scaffolding

|-- README.md
|-- requirements.txt
|-- meme.py			# To start the meme generator via CLI
|-- app.py			# To start the meme generator on web app
|-- tmp				# Folder for memes generated via CLI
|-- static			# Folder for memes generated via web app
|-- templates
|	|-- base.html
|	|-- meme.html
|	|-- meme_form.html
|-- fonts			# Folder with fonts for body and author
|	|-- LilitaOne-Regular.ttf 
|	|-- SANTO___.ttf
|-- _data
|	|-- photos
|	|	|-- pics	# pictures for random meme generator
|	|-- Quotes		# quotes and authors for random meme generator
|	|	|-- QuotesCSV.csv
|	|	|-- QuotesDOCX.docx
|	|	|-- QuotesPDF.pdf
|	|	|-- QuotesTXT.txt
|	|-- SimpleLines
|		|-- SimpleLines.csv
|		|-- SimpleLines.docx
|		|-- SimpleLines.pdf
|		|-- SimpleLines.txt
|-- MemeEngine
|	|--__init__.py
|	|-- MemeGenerator.py	# generate the meme
|-- QuoteEngine
	|-- __init__.py
	|-- CSVIngestor.py		# Strategy object for csv files - inherits from IngestInterface
	|-- DocxIngestor.py		# Strategy object for docx files - inherits from IngestInterface
	|-- PDFIngestor.py		# Strategy object for pdf files - inherits from IngestInterface
	|-- TextIngestor.py		# Strategy object for txt files - inherits from IngestInterface
	|-- IngestInterface.py	# Abstract Base Class
	|-- Ingestor.py			# Realization of the IngestInterface ABC class
	|-- QuoteModel.py		# QuoteModel object with body and author attributes