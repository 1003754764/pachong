# -*- coding: utf-8 -*-

# Scrapy settings for xiangmu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiangmu'

SPIDER_MODULES = ['xiangmu.spiders']
NEWSPIDER_MODULE = 'xiangmu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xiangmu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#   'Cookie':'_ga=GA1.2.1172916609.1534171309; user_trace_token=20180813224154-05c0b19b-9f07-11e8-a37b-5254005c3644; LGUID=20180813224154-05c0bb05-9f07-11e8-a37b-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; _qddaz=QD.x5j6w2.cdvnhi.jlgnb78u; JSESSIONID=ABAAABAAADEAAFI01B4C4774B054FEBA6316E8B56C79E27; _gid=GA1.2.895817303.1535638221; TG-TRACK-CODE=index_navigation; _gat=1; LGSID=20180830225613-d6ec0eee-ac64-11e8-b30a-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dxc4t6ZqmDIRgKyPm-4BYzy-nS18-QT6eZimkvZks5MO_qJq470p5BGiKsNFGG5Lc%26wd%3D%26eqid%3De6a2ff8100022758000000035b880588; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fgongsi%2F147.html; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535638223,1535638994,1535639103,1535640972; X_HTTP_TOKEN=469e501fb06daab7cbdeb7774e600139; SEARCH_ID=a2ed8b5f605f47a29c8f3e3f81a68139; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535641489; LGRID=20180830230451-0b3d789a-ac66-11e8-b30a-5254005c3644',
#   # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xiangmu.middlewares.XiangmuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xiangmu.middlewares.XiangmuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xiangmu.pipelines.MysqlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
