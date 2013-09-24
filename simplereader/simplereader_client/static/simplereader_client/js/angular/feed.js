"use strict";

angular.module('angSimpleReader', ['angSimpleReader.directives'])
    .controller('FeedController', function($scope, $http) {
    	$scope.newFeedUrl;
        $scope.newFeedTitle;
        $scope.newFeedCategory;
        $scope.addFieldModalShown = false;
        
        $scope.addNewFeed = function() {
            $http.get("/api/me/?format=json").then(function(response) {
                $scope.userEmail = response.data.objects[0].email;
                
                $http.post("/api/addfeed/", 
                { "email_user" : $scope.userEmail, "url" : $scope.newFeedUrl,
                "category" : $scope.newFeedCategory, "title" : $scope.newFeedTitle })
                    .success(function(data, status, headers, config) {
                        $scope.data = data;
                    }).error(function(data, status, headers, config) {
                        $scope.status = status;
                    });
                });
        };
    })