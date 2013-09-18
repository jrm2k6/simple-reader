"use strict";

angular.module('angSimpleReader.directives', [])
.directive('addFeedModal', function(){
    return {
      restrict: 'A',
      replace: true,
      template: '<div>'+
                  '<a href="#" ng-click="toggle()">Add new feed</a>'+
                  '<div ng-show="opened">' +
                  '<form>'+
                  '<fieldset>'+
                  '<input type="text" placeholder="URL of your feed…" ng-model="newFeedUrl"><br />'+
                  '<button type="submit" class="btn" ng-click="addNewFeed()">Submit</button>'+
                  '</fieldset>'+
                  '</form>' +
                  '</div>' +
                '</div>',
      scope: {
        addNewFeed: "&",
        newFeedUrl: "="
      },
      link: function(scope, elm, attr){
        scope.opened = false;
        
        scope.toggle = function(){
          scope.opened = !scope.opened;
        }
      }
    }
  });