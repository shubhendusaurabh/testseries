'use strict';

var questionsController = angular.module('Questions.controllers', []);

questionsController.controller('QuestionCtrl', ['$scope', '$routeParams', 'QuestionService',
    function ($scope, $routeParams, QuestionService) {
        QuestionService.getAllQuestions().then(function (questions) {
            $scope.questions = questions;
            console.log(questions);
        });
    }
]);

questionsController.controller('QuestionDetailCtrl', ['$scope', '$routeParams', 'QuestionService',
    function ($scope, $routeParams, QuestionService) {
        $scope.questionId = $routeParams.questionId;
        QuestionService.getQuestionById($scope.questionId).then(function (question) {
            $scope.question = question;
            console.log(question);
        });
    }
]);

questionsController.controller('navigationController', ['$scope', '$location', 'QuestionService',
    function ($scope, $location, QuestionService) {
        $scope.next = function(questionId) {

        }
    }
])
