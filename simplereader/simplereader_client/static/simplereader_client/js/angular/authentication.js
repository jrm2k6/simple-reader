function AuthenticationController($scope)
{
    $scope.signupFieldHidden = true;

    $scope.logIn = function()
    {
    };

    $scope.signUp = function()
    {
        $scope.signupFieldHidden = false;
    };
}