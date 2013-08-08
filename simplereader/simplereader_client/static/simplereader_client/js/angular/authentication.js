var app = angular.module('angSimpleReader', []);

function AuthenticationController($scope) {
    $scope.signupFieldHidden = true;

    $scope.logIn = function()
    {
    };

    $scope.signUp = function()
    {
        $scope.signupFieldHidden = false;
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