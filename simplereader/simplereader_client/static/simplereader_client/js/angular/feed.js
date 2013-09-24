"use strict";

angular.module('angSimpleReader', ['angSimpleReader.directives'])
    .controller('FeedController', function($scope, $http) {
    	$scope.newFeedUrl;
        $scope.newFeedName;
        $scope.newFeedCategory;
        $scope.addFieldModalShown = false;
        
        $scope.addNewFeed = function() {
            console.log($scope.newFeedUrl);

            $http.post("/api/addfeed/", 
                {"email_user" : "jeremy.dagorn@gmail.com", "url" : "www.jeremydagorn.com",
                "category" : "test", "title" : "Testify"})
            .success(function(data, status, headers, config) {
                $scope.data = data;
            }).error(function(data, status, headers, config) {
                $scope.status = status;
            });
        };
    })