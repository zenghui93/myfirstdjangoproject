(function(){
       'use strict';


       angular.module('myfirstapp.demo')
           .directive('myRecord', myRecordDirective);

        function myRecordDirective(){
            return {

                restrict: 'E',
                templateUrl: '/static/html/myThing.html'


            };

        }








    })();






