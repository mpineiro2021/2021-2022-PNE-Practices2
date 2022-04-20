import jinja2 as j
from urllib.parse import parse_qs, urlparse
HTML_FOLDER = "./html/"
SEQUENCES_LIST = ["AAAAA","CGGGTA","TTTTTA","AAACTTTAAG","AAATTCG"]
GENES_LIST =
def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents
try:
    url_path = urlparse(self.path)
    path = url_path.path
    arguments = parse_
    print("The old path was", self.path)
    print("The n ew path is",url_path.path)

    if self.path == "/":
        contents = read_html_file("index.html").render(context={"n_sequeces": len(SEQUENCES_LIST),"genes": GENES_LIST})
    elif path == "/ping":
        contents = read_html_file(path[1:]+ ".html").render()
    elif path == "/get":
        n_sequence = int(arguments["n_sequence"])
        sequence = SEQUENCES_LIST[n_sequences]
        contents = read_html_file("index.html").render(context={"n_sequence":n_sequence,"sequence": sequence})
    elif path == "/gene":
        gene_name = arguments["gene_name"][0]
        sequence = Path("./sequence/"+gene_name+".txt")
        contents = read_html_file("index.html").render(context={"gene_name": gene_name, "sequence": sequence})
