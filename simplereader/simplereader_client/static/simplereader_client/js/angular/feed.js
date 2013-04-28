function FeedController($scope)
{
    $scope.addNewFeed = function()
    {
        var text = $scope.formAddFeedText;
        $scope.formAddFeedText = '';
    };
}