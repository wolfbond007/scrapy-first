
## 指令
```
scrapy                                      # 查看指令
scrapy startproject ali_first               # 创建爬虫项目
scrapy genspider -l                         # 查看爬虫模板
scrapy genspider -t basic fst aliwx.com.cn  # 按模板创建文件
scrapy crawl fst                            # 执行爬虫文件
scrapy list                                 #查看有哪些爬虫
```

## 爬虫模板
```
scrapy genspider -l # 查看爬虫模板
basic  # 基础模板
crawl  # 通用模板
csvfeed # csv格式数据爬虫模板
xmlfeed # xml格式数据爬虫模板
```

## 按模板创建文件
```
scrapy genspider -t basic fst aliwx.com.cn
# basic 模式
# fst 新建文件名
# aliwx.com.cn 爬虫目标域名 
```