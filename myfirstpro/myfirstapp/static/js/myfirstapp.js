




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

                 $scope.login = function(){
                        $http.post('/auth_api/login/',
                        {username: 'zenghuihuang', password: 'asdf1234'});



                  };







                   };



 }());



/** myfirstapp.js ORIGINAL VERSION
     (function(){
            'use strict';
            var myApp = angular.module('myfirstapp.demo', []);
                myApp.controller('MyfirstappController',
                ['$scope', '$http', MyfirstappController]);

            function MyfirstappController($scope, $http){

                 $scope.data=[];
                 $http.get('/myfirstapp/lists').then(function(response){
                     $scope.data = response.data;

                   });


             }
      }());
*/


/**
   *This is my row data( Demo Data)
        (function()
        {
            'use strict';
            angular.module('myfirstapp.demo', [])
                .controller('MyfirstappController',
                ['$scope', MyfirstappController]);

            function MyfirstappController($scope)
            {

                 $scope.data =
                 [
                               {
                               name: ' Things That I have Started',
                               categories:
                               [
                                               {
                                               name: ' Learning',
                                               records : [

                                                              {
                                                                   title: ' I have to learn Django',
                                                                   description: ' I need to learn everyday'
                                                              },
                                                              {
                                                                   title: ' I have to learn English',
                                                                   description: ' I would like to be able to speak very well'
                                                              },


                                                              ]

                                               },
                                               {
                                               name: ' Personal Project',
                                               records : [
                                                              {
                                                                   title: ' My Personal Project A',
                                                                   description: ' This is My Personal Project A'
                                                              },
                                                              {
                                                                    title: ' My Personal Project B',
                                                                    description: ' This is My Personal Project B'
                                                              },
                                                              ]
                                               },
                               ]
                               },
                               {
                               name: ' Things That I would like to do',
                               categories :
                               [
                                               {
                                               name: ' Learning',
                                               records : [

                                                              {
                                                                   title: ' I have to learn Django',
                                                                   description: ' I need to learn everyday'
                                                              },
                                                              {
                                                                   title: ' I have to learn English',
                                                                   description: ' I would like to be able to speak very well'
                                                              },


                                                              ]

                                               },
                                               {
                                               name: ' Personal Project',
                                               records : [
                                                              {
                                                                   title: ' My Personal Project A',
                                                                   description: ' This is My Personal Project A'
                                                              },
                                                              {
                                                                    title: ' My Personal Project B',
                                                                    description: ' This is My Personal Project B'
                                                              },
                                                              ]
                                               },
                               ]
                               },
                               {
                               name: 'Things That I have done',
                               categories :
                               [
                                               {
                                               name: ' Learning',
                                               records : [

                                                              {
                                                                   title: ' I have to learn Django',
                                                                   description: ' I need to learn everyday'
                                                              },
                                                              {
                                                                   title: ' I have to learn English',
                                                                   description: ' I would like to be able to speak very well'
                                                              },


                                                              ]

                                               },
                                               {
                                               name: ' Personal Project',
                                               records : [
                                                              {
                                                                   title: ' My Personal Project A',
                                                                   description: ' This is My Personal Project A'
                                                              },
                                                              {
                                                                    title: ' My Personal Project B',
                                                                    description: ' This is My Personal Project B'
                                                              },
                                                              ]
                                               },
                               ]
                               }
                 ]
            }


        }());

*/


