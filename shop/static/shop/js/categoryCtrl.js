myApp.controller('categoryCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.test = 'test 123';
    $scope.list = [];
    $scope.name = '';
    $scope.success = false;

    //Function init, get all categories from database
    $scope.init = function () {
        $http({
            method: 'GET',
            url: 'get_categories'
        }).then(function successCallback(response) {
            angular.forEach(response.data, function (value, key) {
                $scope.list.push({'key': value.pk, 'name': value.fields.name});
            });
        }, function errorCallback(response) {
        });
    };

    //When submit the form (add, edit)
    $scope.CategoryForm = function () {
        if ($scope.name) {
            $http({
                method: 'POST',
                data: {'name': $scope.name},
                url: 'category/add'
            }).then(function successCallback(response) {
                $scope.success = true;
                $scope.list.push({'key': response.data.id, 'name': response.data.name});
            }, function errorCallback(response) {
            });
        }
    };

    //When delete the category
    $scope.deleteCategory = function (key) {
        $http({
            method: 'POST',
            data: {'id': key},
            url: 'category/delete'
        }).then(function successCallback(response) {
            angular.forEach($scope.list, function (value, index) {
                if (value.key == key) {
                    $scope.list.splice(index, 1);
                }
            });
        }, function errorCallback(response) {

        });
    };

}]);