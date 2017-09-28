# -*- coding: utf-8 -*-

# Scrapy settings for jd project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd'

SPIDER_MODULES = ['jd.spiders']
NEWSPIDER_MODULE = 'jd.spiders'

# HEADER={":authority":"so.m.jd.com",
# ":method":"POST",
# ":path:/ware/searchList.action":"scheme:https",
# "accept":"application/json",
# "accept-encoding":"gzip, deflate, br",
# "accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
# "content-length":"42",
# "content-type":"application/x-www-form-urlencoded",
# "origin":"https://so.m.jd.com",
# "referer":"https://so.m.jd.com/ware/search.action?keyword=%E6%89%8B%E6%9C%BA",
# "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
# "x-requested-with":"XMLHttpRequest"}
#
# cookies={"JAMCookie":"true", "__jdv":"122270672|www.google.com.ph|-|referral|-|1506329677955","ipLoc-djd":"1-72-2799-0"," user-key":"a1448ccc-a329-4d96-97d9-656c1f85acdf","cn":"0","mt_xid":"V2_52007VwMXWlVaUFseTB5cDWAHEVpdX1BTGk4pVVVnAkcHWwtOWhhBHEAANwEUTg5dV1wDSRAOUWQHEVBcX1dYL0oYXAN7AhpOXl9DWhZCG1wOYgIiUG1YYlodTxtZBWcCFmJdXVRd"," 3AB9D23F7A4B3C9B":"6CLCPRXBUQEET3PTFXMTI6TG7D4DZEJMBQY2YTXHL3UO57CWVIDDIF7ETCBCBZDT4QKLBNK2UYTRR4H6PQ66IB6H7I"," mobilev":"html5"," USER_FLAG_CHECK":"49a3e45417041b0649607d60230cff1f"," recommendShow":"show"," __jda":"122270672.1499330046196529163846.1499330046.1506421903.1506424050.13"," __jdb":"122270672.8.1499330046196529163846|13.1506424050"," __jdc":"122270672"," abtest":"20170926202040330_94"," sid":"0fb4ebe82351285df75b22199b79a6c8"," M_Identification":"d9b448bc66667fb6_4162cd15299c38949570fd74a14fffb1"," M_Identification_abtest":"20170926195052190_65232904"," mba_muid":"1499330046196529163846"," mba_sid":"15064265970608257097713659909.4","M_Identification":"d9b448bc66667fb6_4162cd15299c38949570fd74a14fffb1"," __jdu":"1499330046196529163846"}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jd (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY =False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jd.middlewares.JdSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jd.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jd.pipelines.JdPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
