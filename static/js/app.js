'use strict';

angular.module('Questions', [
    'ngRoute',
    'Questions.controllers',
    'Questions.services',
    'Questions.directives'
])
    .config(['$routeProvider', '$locationProvider', '$httpProvider', function ($routeProvider, $locationProvider, $httpProvider) {
        $routeProvider.
            when('/questions/:questionId', {
                templateUrl: '/static/templates/question_detail.html'
            }).
            when('/questions', {
                templateUrl: '/static/templates/question_list.html'
            }).
            otherwise({
                redirectTo: '/questions'
            });

    }]);
