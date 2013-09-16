"use strict";

angular.module('angSimpleReader', ['angSimpleReader.directives'])
    .controller('FeedController', function($scope) {
        $scope.addFieldModalShown = false;
        
        $scope.addNewFeed = function() {
            var text = $scope.formAddFeedText;
            $scope.formAddFeedText = '';
        };
    })