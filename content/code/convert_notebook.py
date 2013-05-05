import os
import sys

try:
    nbconvert = sys.argv[1]
    notebook = sys.argv[2]
except:
    print "usage: python convert_notebook.py  /path/to/nbconvert.py  /path/to/notebook_file.ipynb"
    sys.exit(-1)

# convert notebook
os.system('%s -f blogger-html %s' % (nbconvert, notebook))

# get out filenames
outfile_root = os.path.splitext(notebook)[0]
body_file = outfile_root + '.html'
header_file = outfile_root + '_header.html'


# read the files
body = open(body_file).read()
header = open(header_file).read()


# replace the highlight tags
body = body.replace('class="highlight"', 'class="highlight-ipynb"')
header = header.replace('highlight', 'highlight-ipynb')


# specify <pre> tags
body = body.replace('<pre', '<pre class="ipynb"')
header = header.replace('html, body', '\n'.join(('pre.ipynb {',
                                                 '  color: black;',
                                                 '  background: #f7f7f7;',
                                                 '  border: 0;',
                                                 '  box-shadow: none;',
                                                 '  margin-bottom: 0;',
                                                 '  padding: 0;'
                                                 '}\n',
                                                 'html, body')))


# create a special div for notebook
body = '<div class="ipynb">\n\n' + body + "\n\n</div>"
header = header.replace('body {', 'div.ipynb {')


# specialize headers
header = header.replace('html, body,',
                        '\n'.join((('h1.ipynb h2.ipynb h3.ipynb '
                                    'h4.ipynb h5.ipynb h6.ipynb {'),
                                   'h1.ipynb h2.ipynb ... {',
                                   '  margin: 0;',
                                   '  padding: 0;',
                                   '  border: 0;',
                                   '  font-size: 100%;',
                                   '  font: inherit;',
                                   '  vertical-align: baseline;',
                                   '}\n',
                                   'html, body,')))
for h in '123456':
    body = body.replace('<h%s' % h, '<h%s class="ipynb"' % h)


# comment out document-level formatting
header = header.replace('html, body,',
                        '/*html, body,*/')
header = header.replace('h1, h2, h3, h4, h5, h6,',
                        '/*h1, h2, h3, h4, h5, h6,*/')

#----------------------------------------------------------------------
# Write the results to file
open(body_file, 'w').write(body)
open(header_file, 'w').write(header)
