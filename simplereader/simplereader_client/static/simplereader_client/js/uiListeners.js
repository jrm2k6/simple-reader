function initJQueryListeners()
{
    $('#feedButton').click(function()
    {
        retrieveFeed("https://news.ycombinator.com/rss");
    });
}