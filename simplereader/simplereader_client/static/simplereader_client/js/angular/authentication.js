var app = angular.module('angSimpleReader', []);

function AuthenticationController($scope, $http) {
    $scope.signupFieldHidden = true;
    $scope.creationDone = false;

    $scope.logIn = function() {
    };

    $scope.signUp = function() {
        $scope.signupFieldHidden = false;
    };

    $scope.createAccount = function(_email, _password) {
        $http({
            url: 'http://localhost:8000/api/newuser/',
            method: 'POST',
            data: JSON.stringify({first_name: "", last_name: "", email: _email, password: _password}),
            headers: {'Content-Type': 'application/json'},
	     }).
	    success(function(data, status) {  $scope.showConfirmationMessage(true);}).
	    error(function(data, status) { $scope.showConfirmationMessage(false);})
    };

    $scope.showConfirmationMessage = function(isASuccess) {
        $scope.creationDone = true;
        $scope.userCreatedSuccess = isASuccess? "Woohoo, your user have been created!" : "Oops, something happened, please, try again!";
        $scope.classMessage = isASuccess? "alert-success" :"alert-error";
    };           




}


angular.module('angSimpleReader', []).directive('validPasswordC', function () {
    return {
        require: 'ngModel',
        link: function (scope, elm, attrs, ctrl) {
            ctrl.$parsers.unshift(function (viewValue, $scope) {
                var noMatch = viewValue != scope.signUpForm.passwordUser.$viewValue
                ctrl.$setValidity('noMatch', !noMatch)
            })
        }
    }
})
