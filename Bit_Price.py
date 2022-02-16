import requests
import bs4

def bitParice():
    # f = open('C:/a.txt', 'w+')
    page = requests.get('https://coinmarketcap.com/')
    html = bs4.BeautifulSoup(page.text,'lxml')
    # print(html)
    total = ""
    for a in html.find_all(["tr"]):
        # print(a)
        if a.find_all(["td"]):
            bitcoin_info = ""
            for b in a.find_all(["td"]):
                if b.text == "":
                    break
                bitcoin_info = bitcoin_info+"\n"+"<td>"+b.text+"</td>"
            total = total+"<tr>"+bitcoin_info+"</tr>"
    html = """<td></td><!DOCTYPE html>
                                               <html lang="en">
                                               <head>
                                                   <meta charset="UTF-8">
                                                   <title>bit price</title>
                                               </head>
                                               <body>
                                                <h1 style="color: goldenrod">"Bit Price"</h1>
                                                   <table align="center"bgcolor="#ffebcd"border="1" cellpadding="4" callspacing="4" height="200" weight="800" rules="all" title="Top 100 Cryptocurrencies by Market Capitalization">
                                                       <tr> <th>rank</th>
                                                       <th  style="color:black ">name</th>
                                                            <th>price</th>
                                                            <th>change</th>
                                                            <th>m.cap</th>
                                                            <th>supply</th>
                                                            <th>volume</th>
                                                       </tr>

                                                        {bitcoin_info}

                                                   </table>
                                               </body>

                                             </html>""".format(bitcoin_info=total)
    print(total)
    return html
bitParice()





