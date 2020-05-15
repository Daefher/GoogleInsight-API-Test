""" Simple script to see data from PSI for a lot of pages at the time 


API URL https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=


"""

import requests

with open("pageSpeedList.txt") as pageSpeedListURL:
    dump_file_name = 'pages-result.csv'
    dump_file = open(dump_file_name,'w')
    content = pageSpeedListURL.readlines()
    content = [line.rstrip('\n') for line in content]
    overallscore = 0
    overallscoreM = 0

    column_title = "URL, First Contentful Paint, First Interactive , Performance DeskTop, Performance Mobile \n"
    dump_file.write(column_title)

    for url in content:
        #&strategy=mobile if you want to do mobile version
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}'
        y = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile'        
        print(f'Requesting desktop {x}...')
        print(f'Requesting mobile {y}...')
        r = requests.get(x)
        r2 = requests.get(y)
        output = r.json()
        outputM = r2.json()

        try:
            #Parameter to display
            URLid = output['id']
            URLstring =  str(URLid)
            URLFCP = output['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
            FCP = f'First Contentful Paint ~ {str(URLFCP)}'
            FCPstring = str(URLFCP)
            URLfi = output['lighthouseResult']['audits']['interactive']['displayValue']
            FI = f'First Interactive ~ {str(URLfi)}'
            ffstring =  str(URLfi)
            Performance = output['lighthouseResult']['categories']['performance']['score']
            performanceStrng = str(Performance*100)
            Performance_mobile = outputM['lighthouseResult']['categories']['performance']['score']
            performance_mobileStrng = str(Performance_mobile*100)
            overallscore += (Performance)
            overallscoreM += Performance_mobile

        except KeyError:
            print(f'<KeyError> One or more keys cant be found with url {url}.')

        try: 
            row =  f'{URLstring},{FCPstring},{ffstring},{performanceStrng},{performance_mobileStrng}\n'
            dump_file.write(row)
        except NameError:
            dump_file.write(f'<KeyError> & <NameError> Failing because of nonexistant Key ~ {url}.' + '\n')

        try:
            print(URLid)
            print(URLFCP)
            print(URLfi)            
        except NameError:
            print(f'<NameError>')

    overallscore = str((overallscore / len(content) * 100))
    overallscoreM = str((overallscoreM / len(content) * 100))
    finalrow = f" ,  , OverallScore , {overallscore}, {overallscoreM} \n"
    dump_file.write(finalrow)    
    dump_file.write('something')
    dump_file.close()