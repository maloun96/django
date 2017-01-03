myApp.controller('categoryCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.test = 'test 123';
    $scope.list = [];
    $scope.name = '';
    $scope.category_id = '';
    $scope.success = false;

    //Function init, get all categories from database
    $scope.init = function () {
        $http({
            method: 'GET',
            url: 'categories/all'
        }).then(function successCallback(response) {
            angular.forEach(response.data, function (value, key) {
                $scope.list.push({'key': value.pk, 'name': value.fields.name});
            });
        }, function errorCallback(response) {
        });
    };

    //When submit the form (add, edit)
    $scope.CategoryForm = function () {
        //If isset category_id than it is edit
        if ($scope.category_id != '') {
            $scope.saveEditCategory();
        } else {
            $scope.SaveAddCategory();
        }
    };

    $scope.SaveAddCategory = function () {
        if ($scope.name) {
            $http({
                method: 'POST',
                data: {'name': $scope.name},
                url: 'categories/add'
            }).then(function successCallback(response) {
                $scope.success = true;
                $scope.list.push({'key': response.data.id, 'name': response.data.name});
            }, function errorCallback(response) {
            });
        }
    };

    $scope.resetForm = function () {
        $scope.name = '';
        $scope.category_id = '';
    };

    $scope.saveEditCategory = function () {
        if ($scope.name) {
            $http({
                method: 'POST',
                data: {'name': $scope.name, 'id': $scope.category_id},
                url: 'categories/edit'
            }).then(function successCallback(response) {
                angular.forEach($scope.list, function (value, index) {
                    if (value.key == $scope.category_id) {
                        $scope.list[index].name = $scope.name;
                    }
                });

                $scope.name = '';
                $scope.category_id = '';
                $scope.success = true;

            }, function errorCallback(response) {
            });
        }
    };

    //On click edit button
    $scope.editCategory = function (key) {
        angular.forEach($scope.list, function (value, index) {
            if (value.key == key) {
                $scope.name = value.name;
                $scope.category_id = value.key;
            }
        });
        $('.category_form input[name="name"]').focus();
    };

    //When delete the category
    $scope.deleteCategory = function (key) {
        $http({
            method: 'POST',
            data: {'id': key},
            url: 'categories/delete'
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