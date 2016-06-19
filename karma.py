import praw
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='gzeinieh', api_key='bnrb5u3b30')


user_agent = "yourappname:version (by /u/your reddit user name)"

r = praw.Reddit(user_agent=user_agent)

# user_name = "pepsi_next"
# rank = 1

# user_name = "Libertatea"
# rank = 10

# user_name = "ibleeedorange"
# rank = 3

user_name = "GallowBoob"
rank = 2

user = r.get_redditor(user_name)

########### comment karma

thing_limit = 10
gen = user.get_comments(limit=thing_limit)

karma_by_subreddit1 = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit1[subreddit] = (karma_by_subreddit1.get(subreddit, 0)
                                     + thing.score)

labels1 = list(karma_by_subreddit1.keys())
values1 = list(karma_by_subreddit1.values())

########### link Karma

thing_limit = 10
gen = user.get_submitted(limit=thing_limit)

karma_by_subreddit2 = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit2[subreddit] = (karma_by_subreddit2.get(subreddit, 0)
                                     + thing.score)


labels2 = list(karma_by_subreddit2.keys())
values2 = list(karma_by_subreddit2.values())

title = "Reddit karma by Subreddit for %s, #%s on Reddit Leaderboard" % (user_name, rank)

fig = {
  "data": [
    {
      "values": values1,
      "labels": labels1,
      "domain": {"x": [0, .48]},
      "name": "Comment",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    {
      "values": values2,
      "labels": labels2,
      "text":"Link",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "Link Karma",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":title ,
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Comment",
                "x": 0.17,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Link",
                "x": 0.802,
                "y": 0.5
            }
        ]
    }
}
py.plot(fig)
py.image.save_as(fig, filename="plots/karma" + user_name + ".png")
