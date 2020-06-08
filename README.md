
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

## 使用
第一步: 创建爬虫文件
第二步: 编辑item, 添加属性
第三步: 在爬虫文件中进行数据处理 为属性赋值(爬虫文件是第一步创建的，再/spiders文件夹下)
第四步: 再pipelines文件中进行爬后处理 (如保存到文件 或 写入到数据库)