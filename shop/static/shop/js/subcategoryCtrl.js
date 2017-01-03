myApp.controller('subcategoryCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.list = [];
    $scope.categories = [];
    $scope.name = '';
    $scope.subcategory_id = '';
    $scope.category = '';
    $scope.success = false;

    //Function init, get all categories from database
    $scope.init = function () {
        $http({
            method: 'GET',
            url: 'subcategories/all'
        }).then(function successCallback(response) {
            angular.forEach(response.data, function (value, key) {
                $scope.list.push(value);
            });
            //Get categories
            $scope.getCategories();
        }, function errorCallback(response) {
            console.log(response);
        });
    };

    $scope.getCategories = function () {
        $http({
            method: 'GET',
            url: 'categories/all'
        }).then(function successCallback(response) {
            angular.forEach(response.data, function (value, key) {
                $scope.categories.push({'key': value.pk, 'name': value.fields.name});
            });
        }, function errorCallback(response) {
        });
    };

    //When submit the form (add, edit)
    $scope.subCategoryForm = function () {
        if ($scope.subcategory_id == '')
            $scope.SaveAddSubcategory();
        else
            $scope.SaveEditSubcategory();
    };

    $scope.SaveAddSubcategory = function () {
        if ($scope.name) {
            $http({
                method: 'POST',
                data: {'name': $scope.name, 'category': $scope.category},
                url: 'subcategories/add'
            }).then(function successCallback(response) {
                $scope.success = true;
                $scope.list.push(response.data.obj);
            }, function errorCallback(response) {
            });
        }
    };

    $scope.SaveEditSubcategory = function () {
        if ($scope.name) {
            $http({
                method: 'POST',
                data: {'name': $scope.name, 'category_id': $scope.category, 'subcategory_id': $scope.subcategory_id},
                url: 'subcategories/edit'
            }).then(function successCallback(response) {
                angular.forEach($scope.list, function (value, index) {
                    if (value.subcategory_id == $scope.subcategory_id) {
                        $scope.list[index].subcategory_name = response.data.subcategory_name;
                        $scope.list[index].subcategory_id = response.data.subcategory_id;
                        $scope.list[index].category_name = response.data.category_name;
                        $scope.list[index].category_id = response.data.category_id;
                    }
                });
                $scope.name = '';
                $scope.category = '';
                $scope.success = true;

            }, function errorCallback(response) {
            });
        }
    };

    //On click edit button
    $scope.editsubCategory = function (key) {
        angular.forEach($scope.list, function (value, index) {
            if (value.subcategory_id == key) {
                $scope.name = value.subcategory_name;
                $scope.category = value.category_id;
                $('.subcategory_form input[name="name"]').focus();
                $scope.subcategory_id = value.subcategory_id;
            }
        });
        $('.category_form input[name="name"]').focus();
    };

    $scope.resetForm = function () {
        $scope.name = '';
        $scope.category = '';
        $scope.subcategory_id = '';
    };

    // //When delete the category
    $scope.deletesubCategory = function (key) {
        $http({
            method: 'POST',
            data: {'id': key},
            url: 'subcategories/delete'
        }).then(function successCallback(response) {
            angular.forEach($scope.list, function (value, index) {
                if (value.subcategory_id == key) {
                    $scope.list.splice(index, 1);
                }
            });
        }, function errorCallback(response) {

        });
    };

}]);