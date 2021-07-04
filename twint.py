import twint

c = twint.Config()
c.Search = "#SouthChinaSea"
c.Since = "2020-01-01"
# c.Until = "2021-06-30"
c.Verified = True
c.Index_tweets = "scs"
c.Elasticsearch = "http://localhost:9200"

twint.run.Search(c)