'use strict';

var questionsController = angular.module('Questions.controllers', []);

questionsController.controller('QuestionListCtrl', ['$scope', 'QuestionService',
    function ($scope, Questions) {
        $scope.getQuestions = function() {
            var promise = QuestionService.getQuestions();
            promise.then(
                function(data) {
                    $scope.questions = data.results;
                },
                function(error) {
                    console.log('Error: ', error);
                }
            );
        };
    }
])
