myApp.controller('productCtrl', ['$scope', '$http', function ($scope, $http) {

    $scope.modal_image = function(image_url){
        $('.modal-body img').attr('src', image_url);
        $('.image_pop_up').trigger('click');
    }
}]);