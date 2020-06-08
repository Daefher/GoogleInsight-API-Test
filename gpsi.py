import requests 
from retrieveurl import retrieveURLs

class gspi_info(object):

    def __init__(self):
        self.urlsfile = retrieveURLs("pageSpeedList.txt")
        self.content = self.urlsfile.getURL()


    def get_full_request(self):
        final_output = []
        for url in self.content:
            elem = []
            x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}'
            y = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile'
            r = requests.get(x)
            r2 = requests.get(y)
            output = r.json()
            outputM = r2.json()
            try:
                URLid = output['id']
                URLstring =  str(URLid)
                elem.append(URLstring)
                URLFCP = output['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
                FCP = f'First Contentful Paint ~ {str(URLFCP)}'
                FCPstring = str(URLFCP)
                elem.append(FCPstring)
                URLfi = output['lighthouseResult']['audits']['interactive']['displayValue']
                FI = f'First Interactive ~ {str(URLfi)}'
                ffstring =  str(URLfi)
                elem.append(ffstring)
                Performance = output['lighthouseResult']['categories']['performance']['score']
                performanceStrng = str(Performance*100)
                elem.append(performanceStrng)
                Performance_mobile = outputM['lighthouseResult']['categories']['performance']['score']
                performance_mobileStrng = str(Performance_mobile*100)
                elem.append(performance_mobileStrng)
            except KeyError:
                return (f'<KeyError> One or more keys cant be found with url {url}.')            
            final_output.append(elem)
        return final_output