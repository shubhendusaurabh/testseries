'use strict';

var questionsController = angular.module('Questions.controllers', []);

questionsController.controller('QuesionListCtrl', ['$scope', 'QuestionService',
    function ($scope, QuestionService) {
        $scope.questions = [];
        $scope.getQuestions = function() {
            var promise = QuestionService.getQuestions();
            promise.then(
                function(data) {
                    $scope.questions = data.data.results;
                    console.log(data.data.results);
                },
                function(error) {
                    console.log('Error: ', error);
                }
            );
        }();
        //$scope.getQuestions();
    }
])
