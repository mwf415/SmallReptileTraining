import url_managerMy,out_put_my,html_downloader_me,html_parser_me
class SpiderMain(object):
    def __init__(self):
        self.urls = url_managerMy.URLManager()
        self.output = out_put_my.HtmlOutPut()
        self.down_load = html_downloader_me.HtmlDownLoader()
        self.parser = html_parser_me.HtmlParser()

    def crow(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
                }
                html_content = self.down_load.downLoad(new_url, retry_count=2, headers=headers)
                new_urls ,new_datas = self.parser.parse(new_url, html_content, "utf-8")
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_datas)
                if count> 20:
                    break
                count = count+1
            except Exception as e:
                print("craw failed!\n" + str(e))
        self.output.output()
if __name__ == "__main__":
    rootUrl = "https://baike.baidu.com/item/%E7%8B%97/85474#hotspotmining"
    #rootUrl = sys.argv[1] # 获取命令行参数
    #count_limit = int(sys.argv[2])

    objSpider = SpiderMain()
    objSpider.crow(rootUrl)