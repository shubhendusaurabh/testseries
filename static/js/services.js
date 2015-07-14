'use strict';

var questionsService = angular.module('Questions.services', []);

questionsService.factory('QuestionService', ['$http', '$q',
    function ($http, $q) {
        function getQuestions() {
            return $http.get('/api/questions/');
        }

        function getQuestion(id) {
            return $http.get('/api/questions/' + id);
        }

        return {
            getQuestions: getQuestions,
            getQuestion: getQuestion
        }
    }
]);
