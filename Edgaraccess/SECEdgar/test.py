import time
from mapping import get_cik
from crawler import SecCrawler
from config import DEFAULT_DATA_PATH

def test():
    t1 = time.time()
    # file containig company name and corresponding cik codes
    seccrawler = SecCrawler()

    company_code_list = list()   # company code list
    cik_list = list()            # cik code list
    date_list = list()           # pror date list
    count_list = list()



    print "Enter the company name?"
    comp11 = raw_input()
    cik11 = get_cik(comp11)
    print "Enter the date in format YYYYMMDD?"
    date11 = raw_input()
    company_code_list.append(comp11)
    cik_list.append(cik11)
    date_list.append(date11)
    count_list.append("2")

    # call different  API from the crawler
    for i in range(len(cik_list)):
        seccrawler.filing_10Q(str(company_code_list[i]), str(cik_list[i]),
            str(date_list[i]), str(count_list[i]))
        seccrawler.filing_10K(str(company_code_list[i]), str(cik_list[i]),
            str(date_list[i]), str(count_list[i]))
        # seccrawler.filing_8K(str(company_code_list[i]), str(cik_list[i]),
        #     str(date_list[i]), str(count_list[i]))

    t2 = time.time()
    print ("Total Time taken: "),
    print (t2 - t1)

if __name__ == '__main__':
    print "Path of the directory where data will be saved: " + DEFAULT_DATA_PATH
    test()
