'use strict';

angular.module('Questions', [
    'ngRoute',
    'Questions.controllers',
    'Questions.services'
])
    .config(['$routeProvider', '$locationProvider', '$httpProvider', function ($routeProvider, $locationProvider, $httpProvider) {
        $routeProvider.
            when('/question/:questionId', {
                templateUrl: '/static/templates/question-detail.html',
                controller: 'QuestionDetailCtrl'
            }).
            when('/questions', {
                templateUrl: '/static/templates/question_list.html',
                controller: 'QuesionListCtrl'
            }).
            otherwise({
                redirectTo: '/questions'
            });



    }]);
