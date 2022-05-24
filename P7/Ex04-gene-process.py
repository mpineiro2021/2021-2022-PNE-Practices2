import http.client
import json
from Sequence import Seq



GENES = {'FRAT1' : "ENSG00000165879", 'ADA' : 'ENSG00000196839','FXN' : 'ENSG00000165060','RNU6_269P' : 'ENSG00000212379','MIR633' : 'ENSG00000207552' ,'TTTY4C' : 'ENSG00000228296','RBMY2YP' : 'ENSG00000227633','FGFR3' : 'ENSG00000068078','KDR' : 'ENSG00000128052','ANK2' : 'ENSG00000145362'}
SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id'
gene = input('Write the gene name: ').upper()
try:
    PARAMS = '/' + GENES[gene] + f"?content-type=application/json"
    URL = SERVER + ENDPOINT + PARAMS


    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMS)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")



    data = r1.read().decode("utf-8")
    data = json.loads(data)

    print(data)#para saber las keys de la info que queremos

    print(f"Gene: {gene}")
    print(f"Description: {data['desc']}")
    print(Seq(data['seq']).info())

except KeyError:
    print("Incorrect gene!!!")

