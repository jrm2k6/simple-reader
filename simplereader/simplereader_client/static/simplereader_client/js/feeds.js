
var currentfeedUrl;
function retrieveFeed(_feedUrl)
{
  currentfeedUrl = _feedUrl;
  loadFeed();
}

function loadFeed()
{
    var feed = new google.feeds.Feed(currentfeedUrl);
    feed.setNumEntries(100);
    feed.includeHistoricalEntries();
    feed.load(function(result) {
        if (!result.error) {
            var container = document.getElementById("feed");
            for (var i = 0; i < result.feed.entries.length; i++) {
                var entry = result.feed.entries[i];
                var div = document.createElement("div");
                div.appendChild(document.createTextNode(entry.title));
                div.appendChild(document.createTextNode(entry.link));
                container.appendChild(div);
            }
        }
    });
}