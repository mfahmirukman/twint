import twint

c = twint.Config()
c.Search = "#SouthChinaSea"
c.Since = "2021-01-01"
c.Until = "2021-06-30"
c.Verified = True
c.Index_tweets = "scs2"
c.Elasticsearch = "http://localhost:9200"

twint.run.Search(c)