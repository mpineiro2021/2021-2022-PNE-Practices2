import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from Sequence import Seq
import http.client
import functions
GENES = {'FRAT1' : "ENSG00000165879", 'ADA' : 'ENSG00000196839','FXN' : 'ENSG00000165060','RNU6_269P' : 'ENSG00000212379','MIR633' : 'ENSG00000207552' ,'TTTY4C' : 'ENSG00000228296','RBMY2YP' : 'ENSG00000227633','FGFR3' : 'ENSG00000068078','KDR' : 'ENSG00000128052','ANK2' : 'ENSG00000145362'}







def read_html_file(filename):
    contents = Path( HTML_FOLDER + filename).read_text()#./html/ping.html
    contents = j.Template(contents)#crea una plantilla de ese nombre
    return contents

SERVER = 'rest.ensembl.org'
HTML_FOLDER = "./html/"
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)# a la función urlparse se le pasa el path
        path = url_path.path #endpoint
        arguments = parse_qs(url_path.query)#parameters
        print(path, arguments)
        contents = ""

        if path == "/":
            contents = read_html_file("index.html").render(context={'genes': GENES})

        elif path == "/listSpecies":
            try:
                if len(arguments) == 0: #seria el limite que va :/listSpecies/limite

                    limit = None
                    ensembl_endpoint = "/info/species"
                    answer = functions.info_server(ensembl_endpoint)

                    n_species = len(answer['species'])

                    list_dict_species = answer['species']

                    names = []
                    for s in list_dict_species:
                        names.append(s['display_name'])
                    contents = read_html_file("list_species.html").\
                        render(context={'n_species': n_species,'limit':limit, 'names': names})

                elif len(arguments) == 1: #seria el limite que va :/listSpecies/limite

                    limit = int(arguments['limit'][0])
                    ensembl_endpoint = "/info/species"
                    answer = functions.info_server(ensembl_endpoint)
                    n_species = len(answer['species'])
                    list_dict_species = answer['species']
                    names = []
                    for s in list_dict_species:
                        names.append(s['display_name'])
                    contents = read_html_file("list_species.html").\
                        render(context={'n_species': n_species,'limit':limit, 'names': names})
            except (KeyError, ValueError):
                context = "Introduce an integer number for the limit"
                contents = read_html_file("error.html").render(context={'context':context})






        elif path == "/karyotype":
            try:
                species = arguments['species'][0]
                ensembl_endpoint = "/info/assembly/" + species
                answer = functions.info_server(ensembl_endpoint)
                print(answer)
                k_list = answer['karyotype']
                print(k_list)
                contents = read_html_file(path[1:] + ".html"). \
                        render(context={"karyo_list": k_list})
            except (KeyError, ValueError):
                context = "Not available Karyotype, select other specie"
                contents = read_html_file("error.html").render(context={'context':context})


        elif path == "/chromosomeLength":
            try:
                species = arguments['species'][0]
                length = int(arguments['length'][0])
                ensembl_endpoint = "/info/assembly/" + species
                answer = functions.info_server(ensembl_endpoint)
                print(answer)
                dict_list = answer['top_level_region']
                chromosome_name = []

                if length < 0:
                    context = "Introduce a positive number"
                    contents = read_html_file("error.html").render(context={'context': context})
                else:
                    for d in dict_list:
                        try:
                            if int(d['length']) >= length:
                                if d['coord_system'] == 'chromosome':
                                    chromosome_name.append(d['name'])
                        except KeyError:
                            pass
                if len(chromosome_name) == 0:
                    context = "Introduce a lower number"
                    contents = read_html_file("error.html").render(context={'context': context})
                else:
                    contents = read_html_file("chromosome_length.html"). \
                            render(context={"chromosome_name": chromosome_name, "length":length})
            except KeyError:
                context = "Not available chromosome length, select other species or chromosomes"
                contents = read_html_file("error.html").render(context={'context':context})
            except ValueError:
                context = "Introduce a number, not an string!!!"
                contents = read_html_file("error.html").render(context={'context':context})


        elif path == "/geneSeq":
            try:
                gene = arguments['gene'][0]
                id = GENES[gene]
                ensembl_endpoint = '/sequence/id/' + id
                answer = functions.info_server(ensembl_endpoint)
                gene_sequence = answer['seq']
                contents = read_html_file("gene_seq.html"). \
                   render(context={"gene_sequence": gene_sequence, "gene": gene})
            except ValueError:
                context = "Select another gene"
                contents = read_html_file("error.html").render(context={'context':context})

        elif path == "/geneInfo":
            try:
                gene = (arguments['gene'][0])
                id = GENES[gene]
                ensembl_endpoint = '/sequence/id/' + id
                answer = functions.info_server(ensembl_endpoint)
                information = (answer['desc']).split(":")
                print (information)
                start = information[3]
                end = information[4]
                name = information[1]
                length = int(end) - int(start)
                contents = read_html_file("gene_info.html"). \
                       render(context={"start": start, "gene": gene, "end":end, "name":name, "length":length, "id":id})
            except (ValueError, IndexError, KeyError):
                context = "Not available information for that gene, select another one"
                contents = read_html_file("error.html").render(context={'context':context})


        elif path == "/geneCalc":
            try:
                gene = (arguments['gene'][0])
                id = GENES[gene]
                ensembl_endpoint = '/sequence/id/' + id
                answer = functions.info_server(ensembl_endpoint)
                gene_sequence = answer['seq']
                seq = Seq(gene_sequence)
                calc = seq.percentage_length()

                contents = read_html_file("gene_calc.html"). \
                    render(context={ "gene": gene, "calc":calc})
            except (ValueError, IndexError, KeyError):
                context = "Not available calculations for that gene, select another one"
                contents = read_html_file("error.html").render(context={'context':context})

        elif path == "/geneList":

            try:
                if len(arguments) == 3:
                    chromosome = (arguments['chromosome'][0])
                    start = (arguments['start'][0])
                    end = (arguments['end'][0])
                    ensembl_endpoint = f'/phenotype/region/homo_sapiens/{chromosome}:{start}-{end}'
                    answer = functions.info_server(ensembl_endpoint)
                    print(answer)
                    gene_list = []
                    for dictionary in answer:
                        dict_list = dictionary['phenotype_associations']
                        for i in dict_list:
                            try:
                                gene_list.append( i['attributes']['associated_gene'])
                            except KeyError:
                                pass
                    if len(gene_list) == 0:
                        context = "Introduce different parameters"
                        contents = read_html_file("error.html").render(context={'context':context})
                    else:
                        contents = read_html_file("gene_list.html"). \
                            render(context={ "gene_list":gene_list, 'chromosome':chromosome})


                else:
                    context = "Introduce 3 parameters"
                    contents = read_html_file("error.html").render(context={'context':context})
            except Exception:
                context = "Resource Not available, introduce different integer parameters"
                contents = read_html_file("error.html").render(context={'context':context})

        else:
            context = 'Invalid path, choose a different one'
            contents = read_html_file("error.html").render(context={'context':context})


        # Generating the response message

        self.send_response(200)  # -- Status line: OK!
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()