"use strict";

angular.module('angSimpleReader.directives', [])
.directive('addFeedModal', function(){
    return {
      restrict: 'A',
      replace: true,
      scope: {},
      template: '<div>'+
                  '<a href="#" ng-click="toggle()">Add new feed</a>'+
                  '<div ng-show="opened">' +
                  '<form>'+
                  '<fieldset>'+
                  '<input type="text" placeholder="URL of your feed…"><br />'+
                  '<button type="submit" class="btn disabled">Submit</button>'+
                  '</fieldset>'+
                  '</form>' +
                  '</div>' +
                '</div>',
      link: function(scope, elm, attr){
        scope.opened = false;
        
        scope.toggle = function(){
          scope.opened = !scope.opened;
        }
      }
    }
  });