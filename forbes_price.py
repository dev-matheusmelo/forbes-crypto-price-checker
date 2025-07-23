import requests
import sys 


if __name__ == "__main__":
    url_btc = "https://www.forbes.com/digital-assets/assets/bitcoin-btc/"

    def get_price(url,price_size):
        if(str(url).find("forbes.com") != -1):
            crypto_pair_name = str(url).replace("forbes.com/digital-assets/assets/","")
            crypto_pair_name = crypto_pair_name.replace("http://","")
            crypto_pair_name = crypto_pair_name.replace("https://","")
            crypto_pair_name = crypto_pair_name.replace("www.","")
            crypto_pair_name = crypto_pair_name.replace("/","")
            html_doc = requests.get(url)
            if(html_doc.status_code == 200):
                string_to_find = "price\":"
                start_index = html_doc.text.find(string_to_find) + len(string_to_find) + 2
                end_index = start_index + int(price_size)
                price = html_doc.text[start_index:end_index]
                print(crypto_pair_name + " current price is: $" + price)
            else:
                print("cant request")
                print(html_doc.status_code)

        
    if(len(sys.argv) > 1):
        print("args:" + str(len(sys.argv)))
        arg_url = ""
        arg_size = ""
        for args in sys.argv:
            if(args != sys.argv[0]):
                if(len(args) > 10):
                    arg_url = args
                else:
                    arg_size = args
            if(arg_url != "" and arg_size != ""):
                get_price(arg_url,arg_size)
                arg_url = ""
                arg_size = ""
                
    else:
        get_price(url_btc, 3)
        