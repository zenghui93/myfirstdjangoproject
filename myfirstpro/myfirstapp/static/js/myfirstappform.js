  (function(){
            'use strict';
            var myApp = angular.module('myfirstapp.demo', []);
                myApp.controller('MyfirstappController',
                ['$scope','$http', MyfirstappController]);



            function MyfirstappController($scope, $http){
                 console.log('In main Control');


                 $scope.data=[];
                 $scope.category_sets=[];
                 $http.get('/myfirstapp/categories').then(function(response){
                     $scope.category_sets = response.data;

                   });
                 $http.get('/myfirstapp/lists').then(function(response){
                     $scope.data = response.data;

                   });







                   };



 }());